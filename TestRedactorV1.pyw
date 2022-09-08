import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import sys

# тутутуутуууу
# пау пауу
SymbolsMax = 5
AnswerSymbolsMax = 1
EmptyEntry = 0
EndOfCycle = 0

def check():
    AnswerText1 = AnswerEntry1.get()
    AnswerTextLen1 = int(len(AnswerText1))

    AnswerText2 = AnswerEntry2.get()
    AnswerTextLen2 = int(len(AnswerText2))

    AnswerText3 = AnswerEntry3.get()
    AnswerTextLen3 = int(len(AnswerText3))

    RightAnswerText = RightAnswerEntry.get()
    RightAnswerTextLen = int(len(RightAnswerText))

    answertexts = [AnswerText1, AnswerText2, AnswerText3]
    answertextlens = [AnswerTextLen1, AnswerTextLen2, AnswerTextLen3]

    difference1 = AnswerTextLen1-SymbolsMax
    difference2 = AnswerTextLen2-SymbolsMax
    difference3 = AnswerTextLen3-SymbolsMax

    differences = [difference1, difference2, difference3]

    for i in range(0, 3):
        if answertextlens[i] > SymbolsMax:
            differences[i] = answertextlens[i]-SymbolsMax
            answer = mb.askokcancel(title='Проверка правильности', message=f'Вы превысили\nмаксимальное количество символов ({SymbolsMax}) на {differences[i]} символов!')
            detection1 = Label(MainWindow, text=f'Вы превысили\nмаксимальное количество символов ({SymbolsMax}) на {differences[i]} символов!', padx=0, pady=0, font='Helvetica 12', fg='red', justify=CENTER)
            detection1.place(x=380, y=375)
        elif answertextlens[i] == 1 and answertexts != 0 and answertexts[i] != ' ':
            detection2 = Label(MainWindow, text='    Ошибок не обнаружено.    ', padx=25, pady=10, font='Helvetica 12', fg='green', justify=CENTER)
            detection2.place(x=305, y=350)
            answer2 = mb.askokcancel(title='Проверка правильности', message='Ошибок не обнаружено.')
        elif answertextlens[i] == EmptyEntry:
            answer3 = mb.askokcancel(title='Проверка правильности', message='Текстовое поле пустое.')
            detection3 = Label(MainWindow, text='Впишите варианты ответов.', padx=25, pady=10, font='Helvetica 12', fg='red', justify=CENTER)
            detection3.place(x=90, y=350)

    if str(RightAnswerText) != '1' and str(RightAnswerText) != '2' and str(RightAnswerText) != '3':
        RightAnswerEntry.delete(0, END)
        detection2 = Label(MainWindow, text='Введите номер\nправильного варианта - цифра 1, 2 или 3.', padx=5, pady=0, font='Helvetica 12', fg='red', justify=CENTER)
        detection2.place(x=60, y=400)
    

def fileMake():
    QuestionText = QuestionEntry.get(1.0, END)
    RightAnswerVar = RightAnswerEntry.get()

    AnswerText1 = AnswerEntry1.get()
    AnswerText2 = AnswerEntry2.get()
    AnswerText3 = AnswerEntry3.get()
    answertexts = [AnswerText1, AnswerText2, AnswerText3]

    header.destroy()
    answer1.destroy()
    answer2.destroy()
    answer3.destroy()
    QuestionEntry.destroy()
    AnswerEntry1.destroy()
    AnswerEntry2.destroy()
    AnswerEntry3.destroy()
    RightAnswer.destroy()
    RightAnswerEntry.destroy()



    with open(f'C:\\temp\question123.txt', 'w') as question:
        question.write(RightAnswerVar)
        question.write(f'\n{QuestionText}')

        for a in range(0, 3):
            question.write(f'\n{answertexts[a]}')


MainWindow = tk.Tk()
MainWindow.title("Редактор тестирования")
MainWindow.geometry('800x500+500+200')

QuestionEntry = Text(MainWindow, font='Helvetica 10', width=110, height=6)
QuestionEntry.place(x=10, y=40)

header = Label(MainWindow, text='Введите вопрос:', padx=5, pady=0, font='Helvetica 12 bold')
header.place(x=10, y=10)


AnswerEntry1 = Entry(MainWindow, font='Helvetica 10', width=110)
AnswerEntry1.place(x=10, y=190)

answer1 = Label(MainWindow, text='Введите вариант 1:', padx=5, pady=0, font='Helvetica 12 bold')
answer1.place(x=10, y=160)


AnswerEntry2 = Entry(MainWindow, font='Helvetica 10', width=110)
AnswerEntry2.place(x=10, y=250)

answer2 = Label(MainWindow, text='Введите вариант 2:', padx=5, pady=0, font='Helvetica 12 bold')
answer2.place(x=10, y=220)


AnswerEntry3 = Entry(MainWindow, font='Helvetica 10', width=110)
AnswerEntry3.place(x=10, y=310)

answer3 = Label(MainWindow, text='Введите вариант 3:', padx=5, pady=0, font='Helvetica 12 bold')
answer3.place(x=10, y=280)


RightAnswerEntry = Entry(MainWindow, font='Helvetica 10', width=5)
RightAnswerEntry.place(x=330, y=470)

RightAnswer = Label(MainWindow, text='Введите номер правильного ответа:', padx=5, pady=0, font='Helvetica 12 bold')
RightAnswer.place(x=10, y=470)

button1 = Button(MainWindow, text="П Р О В Е Р И Т Ь   П Р А В И Л Ь Н О С Т Ь",    
                    background="#555",
                    foreground="#ccc",
                    padx=10,
                    pady=10,
                    font='Vendara 12',
                    justify=CENTER,
                    activebackground="#999",
                    activeforeground="#fff",
                    bd=2.5, 
                    command=fileMake)
button1.place(x=440, y=385)

button2 = Button(MainWindow, text="З А К О Н Ч И Т Ь   Р Е Д А К Т И Р О В А Н И Е",    
                    background="#555",
                    foreground="#ccc",
                    padx=10,
                    pady=10,
                    font='Vendara 12',
                    justify=CENTER,
                    activebackground="#999",
                    activeforeground="#fff",
                    bd=2.5, 
                    command=sys.exit)
button2.place(x=415, y=445)


MainWindow.mainloop()