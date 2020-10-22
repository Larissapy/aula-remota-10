def remove(list):
    l = []
    for i in list:
        if i not in l:
            l.append(i)
    l.sort()
    return l

def main():
    anos = {}
    lista = []
    for c in range(1, 1001):
            ano = int(input())
            anos["ano"] = ano
            lista.append(ano)
    listas = remove(lista)

    for c in listas:
        n = lista.count(c)
        print(f'{c}: {n}')

if __name__ == '__main__':
    main()