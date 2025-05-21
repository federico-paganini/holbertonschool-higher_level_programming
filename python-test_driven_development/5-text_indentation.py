#!/usr/bin/python3


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] not in (".", "?", ":"):
            print(text[i], end="")
            i += 1
        else:
            print(f"{text[i]:s}\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
