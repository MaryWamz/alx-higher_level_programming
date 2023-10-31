#!/usr/bin/python3
# Author - Mary G

def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
