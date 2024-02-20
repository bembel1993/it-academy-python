sentence = 'Найти самое длинное слово в введенном предложении, но учтите, что в предложении есть знаки препинания.'

most_long = ''
for x in sentence.split():
    if len(x) > len(most_long):
        most_long = x
print(most_long)

# sentence = str(input("Введите предложение:\n "))

# sentence = sentence.translate(str.maketrans('', '', string.punctuation))
# sharedWord = sentence.split()
# mostlong = []
#
# for x in range(len(sharedWord)):
#     for y in range(x+1, len(sharedWord)):
#         if len(sharedWord[x]) > len(sharedWord[y]):
#             temp = sharedWord[x]
#             sharedWord[x] = sharedWord[y]
#             sharedWord[y] = temp
#             mostlong = sharedWord[y]
#
# print(sharedWord)
# print("Самое длинное слово: " + mostlong)
