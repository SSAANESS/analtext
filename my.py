textinput= input('Введите текст: ')
textinput=textinput.lower()
punctuation=[".", ",", "!", "?"]
for sign in punctuation:
    if sign in textinput:
       textinput = textinput.replace(sign,'')

words = textinput.split()
print("Количество разных слов:",len(set(words)))
word_frequency = {}
for word in words:
    if word in word_frequency:
        word_frequency[word]+=1
    else:
        word_frequency[word]= 1


print("Частота слов:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")
