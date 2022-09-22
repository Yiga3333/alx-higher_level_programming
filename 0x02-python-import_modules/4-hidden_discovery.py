#!/usr/bin/python3

if_name_=="_main_":
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "_":
            print (name)
