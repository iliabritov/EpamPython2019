#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading


def receive_message():
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            print(message)
        except OSError:
            break


def send_messages(username):
    while True:
        if not receive_thread.isAlive():
            print('Connection has been closed by server')
            break
        message = input()
        sock.send(message.encode('utf-8'))
        if message.strip() == '/leave':
            sock.close()
            break


if __name__ == '__main__':
    port = 8800
    host = 'localhost'
    address = host, port

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)

    receive_thread = threading.Thread(target=receive_message)
    receive_thread.start()

    username = input('Your username: ')
    sock.send(username.encode('utf-8'))
    send_messages(username)



