def mix_up(lst):
    a,b = lst
    return b[:2] + a[2:], a[:2] + b[2:]
print mix_up(raw_input('enter 2 words separated by a space: ').split())