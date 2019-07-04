#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
import tkinter


def receive_message():
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            messages_list.insert(tkinter.END, message)
        except OSError:
            break


def send_messages(event=None):
    if not receive_thread.isAlive():
        print('Connection has been closed by server')
    message = client_message.get()
    client_message.set('')
    sock.send(message.encode('utf-8'))
    if message.strip() == '/leave':
        sock.close()
        top.quit()


def on_closing():
    """Function is to be called when the window is closed"""
    client_message.set('/leave')
    send_messages()
    sock.close()


if __name__ == '__main__':
    address = ('localhost', 8800)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)

    # make window use tkinter
    top = tkinter.Tk()
    top.title('Little chat')
    top['bg'] = 'gray22'

    messages_frame = tkinter.Frame(top)

    # create scroolbar for messages_list
    scrool = tkinter.Scrollbar(messages_frame)
    scrool.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    # create messages list
    messages_list = tkinter.Listbox(messages_frame, height=20,
                                    width=50, yscrollcommand=scrool.set)
    messages_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    messages_list.pack()
    messages_frame.pack()

    # create message variable
    client_message = tkinter.StringVar()
    client_message.set('')

    # create entry field for message sending
    entry_field = tkinter.Entry(top, textvariable=client_message, width=45)
    entry_field.bind("<Return>", send_messages)
    entry_field.pack(side='left')

    # create new button for message sending
    send_button = tkinter.Button(top, text='Send', command=send_messages,
                                 width=5)
    send_button.pack(side='right')

    # call the function when the window is closed
    top.protocol('WM_DELETE_WINDOW', on_closing)

    # start recieve thread
    receive_thread = threading.Thread(target=receive_message)
    receive_thread.start()

    tkinter.mainloop()
