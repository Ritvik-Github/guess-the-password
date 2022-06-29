from tkinter import *
import random

root = Tk()
root.title("Random Password Generator")
root.geometry("400x400")
student_guess_entry = Entry(root)
guessed_password = Label(root)
generated_password = Label(root, fg='white', bg='black')
array_3d = [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [
    "Conda", "Unconda", "Head", "Tail"], ["#", "!", "@", "$", "%"]]]


def new():
    password_input = student_guess_entry.get()
    guessed_password["text"] = "Guessed Password: "+password_input
    random_no_1 = random.randint(0, 9)
    random_no_2 = random.randint(0, 3)
    random_no_3 = random.randint(0, 4)
    letter_1 = (array_3d[0][0][random_no_1])
    letter_2 = (array_3d[0][1][random_no_2])
    letter_3 = (array_3d[0][2][random_no_3])
    generated_password["text"] = str(letter_1) + "" + letter_2 + "" + letter_3
    print(letter_1)
    print(letter_2)
    print(letter_3)


btn = Button(root, text="New Password", bg="black", fg="white", command=new)
btn.pack()
guessed_password.pack()
student_guess_entry.pack()
generated_password.pack()
root.mainloop()
