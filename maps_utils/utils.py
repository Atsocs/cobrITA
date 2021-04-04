def translate(s, traduccion):
    for o, n in traduccion.items():
        s = s.replace(o, n)
    return s
