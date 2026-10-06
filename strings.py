#Строки
sample = "Тестовый Тестовый тест для теста"


def analyze_text(text):
    cout = 0
    currentw = ''
    maxleng = 0
    maxword = ''
    letter = {}

    for i in text+' ':
        if i != ' ':
            currentw += i
            char = i.lower()
            letter[char] = letter.get(char, 0) + 1
        elif (i == " " and currentw != ''):
            cout+=1

            coutltr =  len(currentw)

            if (maxleng < coutltr):
                maxword = currentw
                maxleng = coutltr
            elif (maxleng == coutltr):
                maxword += "и " + currentw
            
            currentw = ''
    
    print(f'''
    1. Количество слов в тексте: {cout} 
    2. Самое длинное слово: {maxword}
    3. Частота символов: {letter}
    ''')


        



analyze_text(sample)