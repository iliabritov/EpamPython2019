import string


def letters_range(start, stop=0, step=1, **change):
    alph = list(string.ascii_lowercase)
    for elem in change:
        alph[alph.index(elem)] = change[elem]
    if stop:
        return alph[alph.index(start):alph.index(stop):step]
    else:
        return alph[stop:alph.index(start):step]
