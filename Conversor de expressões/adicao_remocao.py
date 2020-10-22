def display_menu():
    print('trdtr de exprss')
    print('=' * 13)
    print('Menu: ')
    print(' c = coveter uma frase')
    print(' p = imprimir dicionário')
    print(' a = adicionar uma palavra')
    print(' d = remover uma palavra')
    print(' q = sair')

def convert_sentence():
    sentence = input('Insira uma frase para traduzir: ').lower()
    translated_sentence = ''

    list_of_words = sentence.split()

    for word in list_of_words:
        if word in text_speak_dictionary:
            translated_sentence += text_speak_dictionary[word] + " "
        else:
            translated_sentence += word + " "

    print('==>')
    print(translated_sentence)

def add_dictionary_item():
    txt_to_add = input('Insira a expressão a ser adicionada ao dicionário: ')
    meaning = input(') que ela significa?: ')

    text_speak_dictionary[txt_to_add] = meaning

def delete_dictionary_item():
    txt_to_delete = input('Insira a expressão a ser removida ao dicionário')

    del text_speak_dictionary[txt_to_delete]

text_speak_dictionary = {
    "rs" : "risos",
    "tmb" : "também",
    "pq" : "porque",
    "vc" : "você",
    "bjs" : "beijos",
    "ctz" : "certeza",
    "msm" : "mesmo",
    "n" : "não",
    "s" : "sim",
    "sqn" : "só que não",
    "vlw" : "valeu",
    "pfv" : "por favor",
    "obg" : "obrigado(a)",
    "sdds" : "saudades",
    "q" : "que"
}

running = True

display_menu()

while running == True:
    menu_choice = input('>_').lower()

    if menu_choice == 'c':
        convert_sentence()

    elif menu_choice == 'p':
        print(text_speak_dictionary)

    elif menu_choice == 'a':
        add_dictionary_item()

    elif menu_choice == 'd':
        delete_dictionary_item()

    elif menu_choice == 'q':
        running = False

    else:
        print('Escolha inválida!')
