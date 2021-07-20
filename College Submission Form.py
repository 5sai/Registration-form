from tkinter import *
import mysql.connector as mysql

'''creating a root'''

root=Tk()
root.geometry("500x500")
root.title("college student forum")



def Submit():
    fname=e_1.get()
    lname=e_2.get()
    sname=e_3.get()
    gender=e_4.get()
    email=e_5.get()
    Phone=e_6.get()
    address=e_7.get()



    if(fname=="" or lname=="" or sname=="" or gender=="" or email=="" or Phone=="" or address==""):
        print("fill form")
    else:
        conn=mysql.connect(host="localhost",user="root",password="",database="Registration form")
        cursor=conn.cursor()
        cursor.execute("insert into student values('"+ fname +"','" + lname +"','"+ sname +"','"+ gender +"','"+ email +"','"+ Phone +"','"+ address +"')")
        conn.commit()



registration=Label(root,text="Registration form",width="25",font="20",bg="yellow",fg="red")
registration.place(x=160,y=30)
Fname=Label(root,text="First name :",width="20",font="20",fg="red")
Fname.place(x=50,y=100)
Lname=Label(root,text="Last name  :",width="20",font="20",fg="red")
Lname.place(x=50,y=130)
Sname=Label(root,text="Sur name   :",width="20",font="20",fg="red")
Sname.place(x=50,y=160)
Gender=Label(root,text="Gender   :",width="20",font="20",fg="red")
Gender.place(x=50,y=190)
Email=Label(root,text="Email   :",width="20",font="20",fg="red")
Email.place(x=50,y=220)
Phone=Label(root,text="Phone number   :",width="20",font="20",fg="red")
Phone.place(x=50,y=250)
Address=Label(root,text="Address",width="20",font="20",fg="red")
Address.place(x=50,y=280)



e_1=Entry(root,width="25")
e_1.place(x=280,y=105)
e_2=Entry(root,width="25")
e_2.place(x=280,y=135)
e_3=Entry(root,width="25")
e_3.place(x=280,y=165)
e_4=Entry(root,width="25")
e_4.place(x=280,y=195)
e_5=Entry(root,width="25")
e_5.place(x=280,y=225)
e_6=Entry(root,width="25")
e_6.place(x=280,y=255)
e_7=Entry(root,width="25")
e_7.place(x=280,y=285)



Button(root, text="Submit",width="25",font="20",bg="yellow",fg="red",command=Submit).place(x=160,y=405)



root.mainloop()
