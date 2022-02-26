
def text_to_num(s):
    i = 0
    for c in s:
        if 48 <= ord(c) <= 57:
            i += 1
        elif c == '.':
            i += 1
        else:
            break
    base = float(s[:i])
    if 'w' in s:
        return int(base * 10000)
    else:
        return int(base)
