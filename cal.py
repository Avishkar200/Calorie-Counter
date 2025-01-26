from tkinter import *

root=Tk()
root.geometry("1060x600")
root.title("Calorie Counter")
root.resizable(False,False)

def Reset():
    entry_eggs.delete(0,END)
    entry_rice.delete(0,END)
    entry_lentils.delete(0,END)
    entry_chapati.delete(0,END)
    entry_oil.delete(0,END)
    entry_paneer.delete(0,END)
    entry_milk.delete(0,END)
    entry_fruit.delete(0,END)
    entry_chicken.delete(0,END)
    

def Total():
    try:a1=int(Eggs.get())
    except: a1=0

    try:a2=int(rice.get())
    except: a2=0

    try:a3=int(lentils.get())
    except: a3=0

    try:a4=int(chapati.get())
    except: a4=0

    try:a5=int(oil.get())
    except: a5=0

    try:a6=int(paneer.get())
    except: a6=0

    try:a7=int(milk.get())
    except: a7=0

    try:a8=int(fruit.get())
    except: a8=0

    try:a9=int(chicken.get())
    except: a9=0

    #calorie of each
    c1=69*a1
    c2=1.4*a2
    c3=1.2*a3
    c4=130*a4
    c5=120*a5
    c6=2.8*a6
    c7=0.64*a7
    c8=60*a8
    c9=3*a9

    lbl_total=Label(f2,font=('aria',20,'bold'),text="Total_calorie",width=25,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_calorie,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    total_calorie=c1+c2+c3+c4+c5+c6+c7+c8+c9 
    string_calorie="Calorie:",str('%.2f' %total_calorie)
    Total_calorie.set(string_calorie)



Label(text="Calorie Counter",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()


#MENU CARD
f=Frame(root,bg="yellow",highlightbackground="black", highlightthickness=1 ,width=300 ,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="yellow").place(x=80,y=0)

Label(f,font=("Lucia Calligraphy",15,'bold'),text="Eggs.......69cal/egg",fg="black",bg="yellow").place(x=10,y=80)
Label(f,font=("Lucia Calligraphy",15,'bold'),text="rice.......1.4cal/gm",fg="black",bg="yellow").place(x=10,y=110)
Label(f,font=("Lucia Calligraphy",15,'bold'),text="lentils.......1.2cal/gm",fg="black",bg="yellow").place(x=10,y=140)
Label(f,font=("Lucia Calligraphy",15,'bold'),text="Chapati.......130cal/piece",fg="black",bg="yellow").place(x=10,y=170)
Label(f,font=("Lucia Calligraphy",15,'bold'),text="oil.......120cal/spoon",fg="black",bg="yellow").place(x=10,y=200)
Label(f,font=("Lucia Calligraphy",15,'bold'),text="Paneer.......2.8cal/gm",fg="black",bg="yellow").place(x=10,y=230)
Label(f,font=("Lucia Calligraphy",15,'bold'),text="milk.......0.64cal/ml",fg="black",bg="yellow").place(x=10,y=260)
Label(f,font=("Lucia Calligraphy",15,'bold'),text="Any fruit.......60cal/fruit",fg="black",bg="yellow").place(x=10,y=290)
Label(f,font=("Lucia Calligraphy",15,'bold'),text="chicken.......3cal/gm",fg="black",bg="yellow").place(x=10,y=320)

f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=350,height=370)
f2.place(x=690,y=118)

Total_calorie=Label(f2,text="Total Calorie",font=('calibri',20),bg="lightyellow")
Total_calorie.place(x=120,y=10)

#Entries

f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

Eggs=StringVar()
rice=StringVar()
lentils=StringVar()
chapati=StringVar()
oil=StringVar()
paneer=StringVar()
milk=StringVar()
fruit=StringVar()
chicken=StringVar()
Total_calorie=StringVar()

#Label

lbl_Eggs=Label(f1,font=("aria",20,"bold"),text="Eggs",width=12,fg="blue4")
lbl_rice=Label(f1,font=("aria",20,"bold"),text="Rice",width=12,fg="blue4")
lbl_lentils=Label(f1,font=("aria",20,"bold"),text="lentils",width=12,fg="blue4")
lbl_chapati=Label(f1,font=("aria",20,"bold"),text="Chapati",width=12,fg="blue4")
lbl_oil=Label(f1,font=("aria",20,"bold"),text="Oil",width=12,fg="blue4")
lbl_paneer=Label(f1,font=("aria",20,"bold"),text="Paneer",width=12,fg="blue4")
lbl_milk=Label(f1,font=("aria",20,"bold"),text="Milk",width=12,fg="blue4")
lbl_fruit=Label(f1,font=("aria",20,"bold"),text="Fruits",width=12,fg="blue4")
lbl_chicken=Label(f1,font=("aria",20,"bold"),text="Chicken",width=12,fg="blue4")
lbl_Eggs.grid(row=1,column=0)
lbl_rice.grid(row=2,column=0)
lbl_lentils.grid(row=3,column=0)
lbl_chapati.grid(row=4,column=0)
lbl_oil.grid(row=5,column=0)
lbl_paneer.grid(row=6,column=0)
lbl_milk.grid(row=7,column=0)
lbl_fruit.grid(row=8,column=0)
lbl_chicken.grid(row=9,column=0)


#Entry

entry_eggs=Entry(f1,font=("aria",20,'bold'),textvariable=Eggs,bd=6,width=8,bg="yellow")
entry_rice=Entry(f1,font=("aria",20,'bold'),textvariable=rice,bd=6,width=8,bg="yellow")
entry_lentils=Entry(f1,font=("aria",20,'bold'),textvariable=lentils,bd=6,width=8,bg="yellow")
entry_chapati=Entry(f1,font=("aria",20,'bold'),textvariable=chapati,bd=6,width=8,bg="yellow")
entry_oil=Entry(f1,font=("aria",20,'bold'),textvariable=oil,bd=6,width=8,bg="yellow")
entry_paneer=Entry(f1,font=("aria",20,'bold'),textvariable=paneer,bd=6,width=8,bg="yellow")
entry_milk=Entry(f1,font=("aria",20,'bold'),textvariable=milk,bd=6,width=8,bg="yellow")
entry_fruit=Entry(f1,font=("aria",20,'bold'),textvariable=fruit,bd=6,width=8,bg="yellow")
entry_chicken=Entry(f1,font=("aria",20,'bold'),textvariable=chicken,bd=6,width=8,bg="yellow")

entry_eggs.grid(row=1,column=1)
entry_rice.grid(row=2,column=1)
entry_lentils.grid(row=3,column=1)
entry_chapati.grid(row=4,column=1)
entry_oil.grid(row=5,column=1)
entry_paneer.grid(row=6,column=1)
entry_milk.grid(row=7,column=1)
entry_fruit.grid(row=8,column=1)
entry_chicken.grid(row=9,column=1)

#Buttons

btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,"bold"),width=10,text="Reset",command=Reset)
btn_reset.grid(row=10,column=0)

btn_total=Button(f1,bd=5,bg="lightblue",fg="black",font=("ariel",16,"bold"),width=10,text="Total",command=Total)
btn_total.grid(row=10,column=1)


root.mainloop()