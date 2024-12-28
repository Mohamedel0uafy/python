from ttkbootstrap import *




root=tk.Tk()


ad = None
def add_charge():
    global ad
    add = Label(window,text="Autres charge",font=('Roboto',12)).grid(row=8,padx=10,sticky=W)
    ad = Entry(window,width=50,font=('Roboto',12))
    ad.grid(row=9,columnspan=5,padx=10,pady=5)
    btn.grid(row=10,columnspan=5,pady=5)
    frame.grid(row=11)
 
def calculer():
    try:
        global ad
        ad_value = float(ad.get()) if ad and ad.get().strip() else 0  
        totcharge = float(ele.get())+float(ea.get())+float(tel.get())+ad_value
        rez = float(rev.get())-totcharge
        revv = float(rev.get())
        re.delete(0,'end')
        to.delete(0,'end')
        totr.delete(0,'end')
        re.insert(0,rez)
        to.insert(0,totcharge)
        totr.insert(0,revv)
 
    except:
        messagebox.showerror("Erorr","Please enter a valid number")


root.geometry("600x400")
label=Label(root,text= "Revenuus")
label.grid(row=0 ,column=0,padx=10,sticky=W)
a=Entry(root,width=60)
a.grid(row=1 ,column=0,padx=10,sticky=W)

label=Label(root,text= "Electricite")
label.grid(row=2 ,column=0,padx=10,sticky=W)
a=Entry(root,width=60)
a.grid(row=3 ,column=0,padx=10,sticky=W)

label=Label(root,text= "Eau")
label.grid(row=4 ,column=0,padx=10,sticky=W)
a=Entry(root,width=60)
a.grid(row=5 ,column=0,padx=10,sticky=W)

label=Label(root,text= "Telephone")
label.grid(row=6 ,column=0,padx=10,sticky=W)
a=Entry(root,width=60)
a.grid(row=7 ,column=0,padx=10,sticky=W)


btn=Button(root,text="Ajouter charge",bootstyle="success",width=60).grid(row=8 ,column=0,padx=10,pady=20,sticky=W)

frame1=Frame(root)

label=Label(frame1,text= "Resultat")
label.grid(row=9 ,column=0)
a=Entry(frame1,width=20)
a.grid(row=10 ,column=0,padx=10)

label=Label(frame1,text= "Total des charges")
label.grid(row=9 ,column=1)
a=Entry(frame1,width=20)
a.grid(row=10 ,column=1)

label=Label(frame1,text= "Total des revenus")
label.grid(row=9 ,column=2)
a=Entry(frame1,width=20)
a.grid(row=10 ,column=2,padx=10)

frame1.grid(row=9 ,column=0,padx=10,pady=20)

btn1=Button(root,text="Calculer",bootstyle="success-outline-inverse",width=70).grid(row=11 ,column=0,padx=10,sticky=W)





root.mainloop()