# Данный блок печатает содержит методы цветной печати в консоль.

def out_red(text):
    print("\033[31m {}" .format(text))


def out_white(text):
    print("\033[37m {}" .format(text))


def out_blue(text):
    print("\033[34m {}" .format(text))


def out_yellow(text):
    print("\033[33m {}" .format(text))