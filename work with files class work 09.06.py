def readFromFile(fileName):
    with open(fileName) as fileHandler:
        data=fileHandler.read()
        print(data)

def replaceTextInfile(fileName,originalText,newText):
    with open(fileName) as fileHandler:
        data=fileHandler.read()
        data=data.replace(originalText,newText)


    with open(fileName,"w") as fileHandler:
        fileHandler.write(data)
def wordCounter(fileName):
    nWord=0
    with open(fileName) as fileHandler:
        data=fileHandler.read()
        lines=data.split()
        for word in lines:
            if not word.isnumeric():
                nWord+=1
        return nWord


# readFromFile("data/test.txt")
# print("after replaceTextInFile")
# replaceTextInfile("data/test.txt", "Python", "C++")
# readFromFile("data/test.txt")
# print(wordCounter("data/test.txt"))

def removePunctuation(myStr, marks):
    resultStr=" "
    for char in myStr:
      if char not in marks:
        resultStr+=char
    return resultStr

punctSymbols="""!"£$%^&*()_+?><=-``"""
text = "C++ is a high-le""!$^vel, interpreted,"
text=removePunctuation(text,marks)

# Python Core
#
# Practical Assignments
# Файли
# Частина 1
# Рівень 1
# Завдання 1
# Напишіть програму, яка створює текстовий файл output.txt і записує в нього рядок "Hello, world!".
# Завдання 2
# Напишіть програму, яка відкриває файл output.txt, читає його вміст і виводить у консоль.
# Рівень 2
# Завдання 3
# Напишіть програму, яка копіює вміст файлу data.txt у новий файл backup.txt.
# Завдання 4
# Напишіть програму, яка підраховує кількість рядків у файлі data.txt і виводить результат.
# Рівень 3
# Завдання 5
# with open("output.txt", "w", encoding="utf-8") as f:
#     f.write("Hello, world!")
#
# print("file created")