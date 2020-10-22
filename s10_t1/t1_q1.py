cod = 100
titulo = ""

def ler():
    global titulo
    titulo = str(input()).strip()
    return titulo

while ler() != "":
    isbn = input().strip()
    autor = input().strip()
    preco = float(input())
    cod += 1
    if titulo == "":
        break
    print(f'Código: {cod}\nTítulo: {titulo}\nISBN: {isbn}\nAutor: {autor}\nPreço: {preco:.2f}')

