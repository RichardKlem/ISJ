#!/usr/bin/env python3


def first_with_given_key(iterable, key=lambda x: x):
    """
    Funkce aplikuje klíč na položky objektu iterable a vybírá (generuje) pouze ty, jejichž klíč se
        dosud nevyskytl.
    :param iterable: povinný parametr iterable, odpovídající předanému iterovatelnému objektu (může
        být i nekonečný)
    :param key: nepovinný parametr key, odpovídající funkci, která při volání na položce objektu
        iterable vrátí hodnotu klíče, s defaultní hodnotou identické funkce (tedy vrácení přímo
        položky, na které je funkce zavolána)
    :return: generuje polozky, jejichz klic se jeste nevyskytl, cini tak pomoci yield
    """

    iter_key_values = []

    for iter_obj in iterable:
        if key(iter_obj) not in iter_key_values:
            iter_key_values.append(key(iter_obj))
            yield iter_obj
