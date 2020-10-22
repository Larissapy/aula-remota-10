def letra_a():
    return 'aáàâã'


def letra_e():
    return 'eéê'


def letra_i():
    return 'ií'


def letra_o():
    return 'oóô'


def letra_u():
    return 'uú'

def conta_vogais(texto):
    quantos_a = 0
    quantos_e = 0
    quantos_i = 0
    quantos_o = 0
    quantos_u = 0

    for letra in texto:
        if letra in letra_a():
            quantos_a += 1
        if letra in letra_e():
            quantos_e += 1
        if letra in letra_i():
            quantos_i += 1
        if letra in letra_o():
            quantos_o += 1
        if letra in letra_u():
            quantos_u += 1

    a = {'A': quantos_a}
    e = {'E': quantos_e}
    i = {'I': quantos_i}
    o = {'O': quantos_o}
    u = {'U': quantos_u}

    return a, e, i, o, u

def main():
    txt = input().strip().lower()

    a, e, i, o, u = conta_vogais(txt)

    print('A: {}'.format(a['A']))
    print('E: {}'.format(e['E']))
    print('I: {}'.format(i['I']))
    print('O: {}'.format(o['O']))
    print('U: {}'.format(u['U']))

if __name__ == "__main__":
    main()