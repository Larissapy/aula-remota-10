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

sentence = input('Insira uma frase para traduzir: ').lower()

word_to_translate = sentence.split()

translated_sentence = ""

for word in word_to_translate:
    if word in text_speak_dictionary:
        translated_sentence += text_speak_dictionary[word] + " "
    else:
        translated_sentence += word + " "

print('==>')
print(translated_sentence)