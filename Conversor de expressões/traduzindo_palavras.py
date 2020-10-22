text_speak_dictionary = {
    "rs" : "risos",
    "tmb" : "também"
}

print("Dicionário =", text_speak_dictionary)

print('\nrs =', text_speak_dictionary['rs'])

key = input('\nO que você gostaria de converter? : ')
print(key , '=', text_speak_dictionary[key])