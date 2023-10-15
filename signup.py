from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)

#database connection
def connect_database():
    if emailEntry.get()=='' or usernameEntry=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please Accept Terms & Conditions')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='AngryBird19')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issus, Please Try Again')
            return
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary_key not null, email varchar(50),username varchar(100),password varchar(20)'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))

        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Error','Username Already exists')

        else:
            query='insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is successful')
            clear()
            signup_window.destroy()
            import login


#function call
def login_page():
    signup_window.destroy()
    import login

signup_window=Tk()
signup_window.title('signup Page')
signup_window.resizable(0,0)

background=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=200,y=80)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('glazier',23,'bold'),bg='white',fg='brown4')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('glazier',13,'bold'),bg='white',fg='brown4')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))
emailEntry=Entry(frame,width=30,font=('glazier',15,'bold'),fg='white',bg='brown4')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',font=('glazier',13,'bold'),bg='white',fg='brown4')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
usernameEntry=Entry(frame,width=30,font=('glazier',15,'bold'),fg='white',bg='brown4')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('glazier',13,'bold'),bg='white',fg='brown4')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
passwordEntry=Entry(frame,width=30,font=('glazier',15,'bold'),fg='white',bg='brown4')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmLabel=Label(frame,text='Confirm Password',font=('glazier',13,'bold'),bg='white',fg='brown4')
confirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
confirmEntry=Entry(frame,width=30,font=('glazier',15,'bold'),fg='white',bg='brown4')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)
check=IntVar()
termsconditions=Checkbutton(frame,text='I agree to the Terms & conditions',font=('glazier',10,'bold'),fg='brown4',bg='white',activebackground='white',activeforeground='brown4',cursor='hand2',variable=check)
termsconditions.grid(row=9,column=0,sticky='w',pady=10,padx=15)

signupButton=Button(frame,text='Signup',font=('glazier',14,'bold'),bd=0,bg='brown4',fg='white',activebackground='brown4',activeforeground='white',width=15,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alreadyaccount=Label(frame,text="Don't have an account?",font=('glazier',9,'bold'),bg='white',fg='brown4')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)
loginButton=Button(frame,text='Log in',font=('glazier',9,'bold'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=login_page)
loginButton.place(x=170,y=425)


signup_window.mainloop()