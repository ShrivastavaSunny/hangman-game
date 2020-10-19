from tkinter import *
from tkinter import messagebox
root=Tk()

chances=4
chances1=3
chances2=4
chances3=4
chances4=4
count=1

def main():
    global count
    global root
    root.destroy()
    root=Tk()
    root.title("Hangman Game")
    root.geometry("900x600")
    root.configure(background="light pink")
    def clicked(alphabet):
        global chances
        global count
        if(count==1):
            flag=False
            answer="LIZARD"
            if alphabet in answer:
                if alphabet=='L':
                    btn1['text']=alphabet
                elif alphabet=='I':
                    btn2['text']=alphabet;
                elif alphabet=='Z':
                    btn3['text']=alphabet;
                elif alphabet=='A':
                    btn4['text']=alphabet;
                elif alphabet=='R':
                    btn5['text']=alphabet; 
                elif alphabet=='D':
                    btn6['text']=alphabet;
            else:
                chances=chances-1
                messagebox.showinfo("CHANCES LEFT",str(chances)+" "+"Chances Left")
                if chances<1:
                    messagebox.showinfo("Hanged","YOUR Game Is Over")
                    root.destroy()
                    exit()
            if btn1['text']=='L' and btn2['text']=='I'  and btn3['text']=='Z' and btn4['text']=='A' and btn5['text']=='R' and btn6['text']=='D':
                msg=messagebox.showinfo("Hangman Game","You Have successfully Completed Level '1'")
                #root.destroy()
                flag=True
                count+=1
                main()
        if(count==2):
            global chances1
            answer="GOAT"
            if alphabet in answer:
                if alphabet=='G':
                    btn1['text']=alphabet
                elif alphabet=='O':
                    btn2['text']=alphabet
                elif alphabet=='A':
                    btn3['text']=alphabet
                elif alphabet=='T':
                    btn4['text']=alphabet
            else:
                chances1=chances1-1;
                messagebox.showinfo(chances1)
                if chances1<1:
                    messagebox.showinfo("Hanged","YOUR Game Is Over")
                    root.destroy()
                    exit()
            if btn1['text']=='G' and btn2['text']=='O'  and btn3['text']=='A' and btn4['text']=='T':
                messagebox.showinfo("Hangman Game","You Have successfully Completed Level '2'")
                count+=1
                main()
        if(count==3):
            global chances2
            answer="TIGER"
            if alphabet in answer:
                if alphabet=='T':
                    btn1['text']=alphabet
                elif alphabet=='I':
                    btn2['text']=alphabet
                elif alphabet=='G':
                    btn3['text']=alphabet
                elif alphabet=='E':
                    btn4['text']=alphabet
                elif alphabet=='R':
                    btn5['text']=alphabet
            else:
                chances2=chances2-1;
                messagebox.showinfo(chances2)
                if chances2<0:
                    messagebox.showinfo("Hanged","YOUR Game Is Over")
                    root.destroy()
                    exit()
            if btn1['text']=='T' and btn2['text']=='I'  and btn3['text']=='G' and btn4['text']=='E' and btn5['text']=='R':
                messagebox.showinfo("Hangman Game","You Have successfully Completed Level '3'")
                count+=1
                main()
        if(count==4):
            global chances3
            answer="FISH"
            if alphabet in answer:
                if alphabet=='F':
                    btn1['text']=alphabet
                elif alphabet=='I':
                    btn2['text']=alphabet
                elif alphabet=='S':
                    btn3['text']=alphabet
                elif alphabet=='H':
                    btn4['text']=alphabet
            else:
                chances3=chances3-1;
                messagebox.showinfo(chances3)
                if chances3<0:
                    messagebox.showinfo("Hanged","YOUR Game Is Over")
                    root.destroy()
                    exit()
            if btn1['text']=='F' and btn2['text']=='I'  and btn3['text']=='S' and btn4['text']=='H':
                messagebox.showinfo("Hangman Game","You Have successfully Completed Level '4'")
                count+=1
                main()
        if(count==5):
            global chances4
            answer="PIGEON"
            if alphabet in answer:
                if alphabet=='P':
                    btn1['text']=alphabet
                elif alphabet=='I':
                    btn2['text']=alphabet
                elif alphabet=='G':
                    btn3['text']=alphabet
                elif alphabet=='E':
                    btn4['text']=alphabet
                elif alphabet=='O':
                    btn5['text']=alphabet
                elif alphabet=='N':
                    btn6['text']=alphabet
            else:
                chances4=chances4-1;
                messagebox.showinfo(chances4)
                if chances4<0:
                    messagebox.showinfo("Hanged","YOUR Game Is Over")
                    root.destroy()
                    exit()
            if btn1['text']=='P' and btn2['text']=='I'  and btn3['text']=='G' and btn4['text']=='E' and btn5['text']=='O' and btn6['text']=='N':
                messagebox.showinfo("Hangman Game","You Have successfully Completed Level '5'")
   
                root.destroy()
                exit()
    label_1=Label(text="!!!!!!!!!!!!!!Welcome To Hangman Game!!!!!!!!!!",font=("bold",15),fg="white",bg="black")
    label_1.place(relx=0.7,rely=0.10,anchor=E)
    label_2=Label(text="!!!!!Type Your Guessed Word!!!!!",font=("bold",15),fg="white",bg="black")
    label_2.place(relx=0.80,rely=0.45,anchor=E)
    #Botton for taking input
    btn1=Button(text=" ",bg="white",fg="black",width=3,height=1)
    btn1.place(relx=0.5,rely=0.25,anchor=E)
    btn2=Button(text=" ",bg="white",fg="black",width=3,height=1)
    btn2.place(relx=0.55,rely=0.25,anchor=E)
    btn3=Button(text=" ",bg="white",fg="black",width=3,height=1)
    btn3.place(relx=0.60,rely=0.25,anchor=E)
    btn4=Button(text=" ",bg="white",fg="black",width=3,height=1)
    btn4.place(relx=0.65,rely=0.25,anchor=E)
    btn5=Button(text=" ",bg="white",fg="black",width=3,height=1)
    btn5.place(relx=0.70,rely=0.25,ancho=E)
    btn6=Button(text=" ",bg="white",fg="black",width=3,height=1)
    btn6.place(relx=0.75,rely=0.25,anchor=E)
    btn7=Button(text=" ",bg="white",fg="black",width=3,height=1)
    btn7.place(relx=0.80,rely=0.25,anchor=E)
    btn8=Button(text=" ",bg="white",fg="black",width=3,height=1)
    btn8.place(relx=0.85,rely=0.25,anchor=E)
    btn9=Button(text="A",bg="blue",fg="white",width=3,height=1,activebackground='silver',command=lambda: clicked('A'))
    btn9.place(relx=0.2,rely=0.6,anchor=W)
    btn10=Button(text="B",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('B'))
    btn10.place(relx=0.27,rely=0.6,anchor=W)
    btn11=Button(text="C",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('C'))
    btn11.place(relx=0.34,rely=0.6,anchor=W)
    btn12=Button(text="D",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('D'))
    btn12.place(relx=0.41,rely=0.6,anchor=W)
    btn13=Button(text="E",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('E'))
    btn13.place(relx=0.48,rely=0.6,anchor=W)
    btn14=Button(text="F",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('F'))
    btn14.place(relx=0.55,rely=0.6,anchor=W)
    btn15=Button(text="G",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('G'))
    btn15.place(relx=0.62,rely=0.6,anchor=W)
    btn16=Button(text="H",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('H'))
    btn16.place(relx=0.2,rely=0.68,anchor=W)
    btn17=Button(text="I",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('I'))
    btn17.place(relx=0.27,rely=0.68,anchor=W)
    btn18=Button(text="J",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('J'))
    btn18.place(relx=0.34,rely=0.68,anchor=W)
    btn19=Button(text="K",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('K'))
    btn19.place(relx=0.41,rely=0.68,anchor=W)
    btn20=Button(text="L",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('L'))
    btn20.place(relx=0.48,rely=0.68,anchor=W)
    btn21=Button(text="M",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('M'))
    btn21.place(relx=0.55,rely=0.68,anchor=W)
    btn22=Button(text="N",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('N'))
    btn22.place(relx=0.62,rely=0.68,anchor=W)
    btn23=Button(text="O",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('O'))
    btn23.place(relx=0.2,rely=0.76,anchor=W)
    btn24=Button(text="P",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('P'))
    btn24.place(relx=0.27,rely=0.76,anchor=W)
    btn25=Button(text="Q",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('Q'))
    btn25.place(relx=0.34,rely=0.76,anchor=W)
    btn26=Button(text="R",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('R'))
    btn26.place(relx=0.41,rely=0.76,anchor=W)
    btn27=Button(text="S",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('S'))
    btn27.place(relx=0.48,rely=0.76,anchor=W)
    btn28=Button(text="T",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('T'))
    btn28.place(relx=0.55,rely=0.76,anchor=W)
    btn29=Button(text="U",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('U'))
    btn29.place(relx=0.62,rely=0.76,anchor=W)
    btn30=Button(text="V",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('V'))
    btn30.place(relx=0.27,rely=0.84,anchor=W)
    btn31=Button(text="W",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('W'))
    btn31.place(relx=0.34,rely=0.84,anchor=W)
    btn32=Button(text="X",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('X'))
    btn32.place(relx=0.41,rely=0.84,anchor=W)
    btn33=Button(text="Y",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('Y'))
    btn33.place(relx=0.48,rely=0.84,anchor=W)
    btn34=Button(text="Z",bg="blue",fg="white",width=3,height=1,command=lambda: clicked('Z'))
    btn34.place(relx=0.55,rely=0.84,anchor=W)
    if(count==1):
        x=PhotoImage(file=("lizard1.gif"))
        frame1=Frame(root)
        frame1.configure(background="light pink")
        button=Button(frame1,image=x)
        button.grid(pady=110,padx=20)
        frame1.grid()
        
        root.mainloop()
    elif(count==2):
        x=PhotoImage(file=("goat.gif"))
        frame2=Frame(root)
        frame2.configure(background="light pink")
        button=Button(frame2,image=x)
        button.grid(pady=110,padx=20)
        frame2.grid()
        root.mainloop()

    elif(count==3):
        x=PhotoImage(file=("tiger1.gif"))
        frame3=Frame(root)
        frame3.configure(background="light pink")
        button=Button(frame3,image=x)
        button.grid(pady=110,padx=20)
        frame3.grid()
        root.mainloop()

    elif(count==4):
        x=PhotoImage(file=("fish.gif"))
        frame4=Frame(root)
        frame4.configure(background="light pink")
        button=Button(frame4,image=x)
        button.grid(pady=90,padx=5)
        frame4.grid()
        root.mainloop()

    elif(count==5):
        x=PhotoImage(file=("pigeon.gif"))
        frame4=Frame(root)
        frame4.configure(background="light pink")
        button=Button(frame4,image=x)
        button.grid(pady=90,padx=5)
        frame4.grid()
        root.mainloop()
main()





root.mainloop()
