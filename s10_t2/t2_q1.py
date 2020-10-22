def texto():
    frase = input().strip().upper()
    letra = {}
    for p in ' .,;:?!\t\n()-_':
        frase = frase.replace(p, "")
    for l in frase:
        if l in 'ÁÀÂÃ':
            l = 'A'
        elif l in 'ÉÊÈ':
            l = 'E'
        elif l in 'ÎÍÌ':
            l = 'I'
        elif l in 'ÔÓÒÕ':
            l = 'O'
        elif l in 'ÚÙÛ':
            l = 'U'
        elif l == 'Ç':
            l = 'C'
        if l in letra:
            letra[l] += 1
        else:
            letra[l] = 1
    return (letra)
def main():
    desconsidere = ' .,;:?!\t\n()-_'
    matriz = []

    r = texto()

    print(r)

if __name__ == '__main__':
    main()