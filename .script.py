TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

registrants = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'password123'}
#username = input('Insert username:')
#password = input('Insert password:')
username = 'bob'
password = '123'
if registrants.get(username) == password:
    print('Welcome! You can analyze the copy.')
else:
    print('You are not registered. Please, sign up first.')
    exit()

#text_number_input = input('Enter number from 1 to 3 to analyze the texts:')
text_number_input = 2
text_number = [1, 2, 3]
text_number_input = int(text_number_input)

if text_number_input not in text_number:
    exit()


words = TEXTS[text_number_input-1].split()
wordCount = len(words)
print(wordCount)
FirstUpperWordsCount = 0
UpperWordsCount = 0
LowerWordsCount = 0
NumCount = 0
SumNum = 0
DictFrequency = {}

for word in words:
    if word[0].isupper():
        FirstUpperWordsCount += 1
    if word.isupper():
        UpperWordsCount += 1
    if word.islower():
        LowerWordsCount += 1
    if word.isnumeric():
        NumCount += 1
        SumNum += int(word)
    LengthWord = len(word)
    if LengthWord in DictFrequency:
       CurrentCount = DictFrequency.get(LengthWord)
       CurrentCount += 1
       DictFrequency.update({LengthWord:CurrentCount})
    else:
        DictFrequency.update({LengthWord:1})


print('Count of words - first letter upper:' + str(FirstUpperWordsCount))
print('Count of words - all letters upper:' + str(UpperWordsCount))
print('Count of words - all letters lower:' + str(LowerWordsCount))
print('Count of words - numeric:' + str(NumCount))
print('Sum of numbers:' + str(SumNum))
print(DictFrequency)

for item in DictFrequency:
    i = 1
    stars = ''
    while i <= DictFrequency[item]:
        stars += '*'
        i += 1
    print(str(item) + '|' + stars + '|' + str(DictFrequency[item]))