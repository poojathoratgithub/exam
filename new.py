from tkinter import *
from sqlite3 import * 
from PIL import ImageTk, Image

con = connect('Tourist.db')
cur=con.cursor()
cur.execute('create table if not exists tourist1(name text,email text ,username text, password text)')



     
def Customizetour():

        def close():

                quit()

         
        def Submit():
                lbldata= Label(window)
                lbldata.place(x=150,y=200)
                lbldata.config(text="You send request Sucessfully...!!!")
                print("Ok")

        window=Tk()
        window.title("Domastic Page ")
        window.geometry('400x300')
        window.configure(bg="black")
        window.resizable(False,False)
        frame = Frame(window, width=800, height=800,bg="lightblue")
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.3)

        lblname = Label(frame, text="Enter Name ",bg="skyblue")
        txtname = Entry(frame)
        lblemail = Label(frame,text="Enter Email Id ",bg="skyblue")
        txtemail = Entry(frame)
        lblcity = Label(frame,text="Enter city name ",bg="skyblue")
        txtcity = Entry(frame)
        lblmobile=Label(frame, text="Enter Mobile no",bg="skyblue")
        txtmobile=Entry(frame,show="*")
        lbldays=Label(frame, text="Enter No of Days",bg="skyblue")
        txtdays=Entry(frame)

        btnsubmit = Button(frame,text="Submit",bg="light pink",command=Submit)
        btnquit=Button(frame,text="Quit",bg="light pink",command=close)
        lblname.grid(row=0,column=0)
        txtname.grid(row=0,column=1)
        lblemail.grid(row=1,column=0)
        txtemail.grid(row=1,column=1)

        lblmobile.grid(row=2,column=0)
        txtmobile.grid(row=2,column=1)
        lbldays.grid(row=3,column=0)
        txtdays.grid(row=3,column=1)
        lblcity.grid(row=4,column=0)
        txtcity.grid(row=4,column=1)
        btnsubmit.grid(row=8,column=0)
        btnquit.grid(row=8,column=1)


        window.mainloop()

def Domastic():

        window=Toplevel()
        window.title("Domastic Page ")
        window.geometry('400x300')
        window.configure(bg="black")
        lbl_title=Label(window,text="Domastic Tour",font=("Times new roman",20,"bold"),fg="black",anchor='center',bg="lightblue")
        lbl_title.place(x=600,y=30,height=50)
        frame3=Frame(window,width=300,height=300)
        frame3.place(x=0,y=100)
        goa = ImageTk.PhotoImage(Image.open("E:\\Python\\Mini project\\goa.jpg"))
        label2 = Label(frame3, image = goa,bg="black",)
        label2.pack()
        lbl_title1=Label(window,text="GOA",font=80,fg="Black",bg="lightblue")

        lbl_title1.place(x=250,y=120)
        lbl_title2=Label(window,text="Goa\nNorth Goa Beaches\nSouth Goa Beaches\nChapora Fort\nBom Jesus Basilica\nFort Aguada\nShanti Durga Temple\nLocal Market\nClub Cabana",font=10)

        lbl_title2.place(x=30,y=160)
        lbl_title7=Label(window,text=" 5 Days 6 Night ",fg="blue",font="15",bg="light blue")
        lbl_title7.place(x=30,y=400)
        lbl_title8=Label(window,text=" ₹ 13600/- ",fg="blue",font="15",bg="light blue")
        lbl_title8.place(x=250,y=400)
        btndetails=Button(window,text="Customize tour",font=5,bg="light blue",fg="dark blue",command=Customizetour)
        btndetails.place(x=380,y=400)
        
        
        frame4=Frame(window,width=300,height=300)
        frame4.place(x=600,y=100)
        Mumbai= ImageTk.PhotoImage(Image.open("E:\\Python\\Mini project\\mumbai.jpg"))
        label3 = Label(frame4, image = Mumbai,bg="black",)
        label3.pack()
        lbl_title3=Label(frame4,text="MUMBAI",font=80,fg="BLACK",bg="lightblue")

        lbl_title3.place(x=250,y=30)
        lbl_title4=Label(frame4,text="Elephanta Caves\nChurchgate\n Juhu beach\nMarine Drive\nHaji Ali\nMumba Devi Temple\nNehru Science Center\nEssel World",font=10)

        lbl_title4.place(x=30,y=60)
        lbl_title8=Label(frame4,text=" 6 Days 7 Night",fg="blue",font="15",bg="light blue")
        lbl_title8.place(x=30,y=300)
        lbl_title9=Label(frame4,text=" ₹ 10600/- ",fg="blue",font="15",bg="light blue")
        lbl_title9.place(x=250,y=300)
        btndetails=Button(frame4,text="Customize tour",font=5,bg="light blue",fg="darkblue",command=Customizetour)
        btndetails.place(x=400,y=300)

        frame5=Frame(window,width=300,height=300)
        frame5.place(x=0,y=450)
        Pune= ImageTk.PhotoImage(Image.open("E:\\Python\\Mini project\\nature.jpg"))
        label4 = Label(frame5, image = Pune,bg="black",)
        label4.pack()
        lbl_title5=Label(frame5,text="PUNE",font=80,fg="BLACK",bg="lightblue")

        lbl_title5.place(x=250,y=30)
        lbl_title6=Label(frame5,text="Shaniwar Wada Palace\nAga Khan Palace\nDagdusheth Halwai Temple\nVetal Tekdi\nLal Mahal\nRaja Dinkar Kelkar Museum\nExplore Parvati Hill\nPashan Lake",font=10)

        lbl_title6.place(x=30,y=90)
        lbl_title9=Label(frame5,text=" 4 Days 5 Night",fg="blue",font="15",bg="light blue")
        lbl_title9.place(x=30,y=300)
        lbl_title10=Label(frame5,text=" ₹ 8000/- ",fg="blue",font="15",bg="light blue")
        lbl_title10.place(x=250,y=300)
        btndetails=Button(frame5,text="Customize tour",font=5,bg="light blue",fg="darkblue",command=Customizetour)
        btndetails.place(x=350,y=300)

        frame6=Frame(window,width=600,height=500)
        frame6.place(x=600,y=450)
        abd= ImageTk.PhotoImage(Image.open("E:\\Python\\Mini project\\Aurangabad.jpg"))
        label5 = Label(frame6, image = abd,bg="black")
        label5.pack()
        lbl_title6=Label(frame6,text="AURANGABAD",font=80,fg="BLACK",bg="lightblue")

        lbl_title6.place(x=250,y=30)
        lbl_title7=Label(frame6,text="Bibi Ka Maqbara\nPanchakki\nHimayat Bagh\nAurangabad Caves\nSalim Ali Lake & Bird Sanctuary\nSiddharth Garden and Zoo\nKali Masjid\nShahganj Masjid",font=10)

        lbl_title7.place(x=30,y=90)
        lbl_title10=Label(frame6,text=" 4 Days 5 Night",fg="blue",font="15",bg="light blue")
        lbl_title10.place(x=30,y=300)
        lbl_title11=Label(frame6,text=" ₹ 5000/- ",fg="blue",font="15",bg="light blue")
        lbl_title11.place(x=250,y=300)
        btndetails=Button(frame6,text="Customize tour",font=5,bg="light blue",fg="darkblue",command=Customizetour)
        btndetails.place(x=350,y=300)

        frame6.mainloop()
        frame5.mainloop()
        frame4.mainloop()
        frame3.mainloop()
        window.mainloop()

def Home():
        window=Toplevel()
        window.title("Tourist Page ")
        window.geometry('800x500')
        window.configure(bg="black")
        window.resizable(False,False)
        frame = Frame(window, width=5000, height=5000)
        # frame.pack()
        frame.place(x=0,y=0,relx=0.1, rely=0.1)

        ##img = ImageTk.PhotoImage(Image.open("E:\\Python\\Mini project\\6871.jpg_wh1200.jpg"))
        img1 = ImageTk.PhotoImage(Image.open("E:\\Python\\Mini project\\kerala-tours3.jpg"))
        label = Label(frame, image = img1,bg="black",)
        label.pack()
        lbl_title=Label(window,text="WELCOME TO HOME PAGE",font=("Arial black",15,'bold'),fg="black",bg="light pink")
        lbl_title.place(x=250,y=70,height=30)
        btnMenu = Button(frame,text="Home",command="touristpage",font=80,bg="pink")
        # btnContactus=Button(frame,text="Contact us",font=100,bg="pink")
        btnMenu.place(relx=0.05,rely=0.5)
    
        btnDomastic=Button(frame,text="Domastic",font=80,bg="pink",command=Domastic)
        btnDomastic.place(relx=0.25,rely=0.5)
        btnGroup=Button(frame,text="Group tour",font=80,bg="pink")
        btnGroup.place(relx=0.5,rely=0.5)
        btnspl=Button(frame,text="Special tour",font=80,bg="pink")
        btnspl.place(relx=0.75,rely=0.5)
        frame.mainloop()



def Signup():
        
        def adddata():
                n=txtname.get()
                e=txtemail.get()
                un=txtusername.get()
                p=txtpassword.get()

                cur.execute('insert into tourist1 values(?,?,?,?)',(n,e,un,p))
                con.commit()
                
                btnsubmit = Button(frame2,text="Next",command=Home)
        
                btnsubmit.grid(row=5,column=1)
                lbldata= Label(window)
                lbldata.place(x=200,y=200)
                lbldata.config(text="YOU SIGNUP SUCCESFULLY...!!!")
                print("Ok")
        window=Tk()
        window.title("Signup Page ")
        window.geometry('600x300')
        window.configure(bg="black")
        window.resizable(False,False)
        frame2=Frame(window,bg="skyblue3",width=800,height=900)
        frame2.place(x=150,y=50)
        lbl_title=Label(window,text="WELCOME TO SIGN UP PAGE",font=10,fg="black",bg="light pink")
        lbl_title.place(x=130,y=10,height=20)
       
        lblname = Label(frame2, text="Enter Name ",bg="skyblue")
        txtname = Entry(frame2)
        lblemail = Label(frame2,text="Enter Email Id ",bg="skyblue")
        txtemail = Entry(frame2)
        lblusername = Label(frame2,text="Enter user name ",bg="skyblue")
        txtusername = Entry(frame2)
        lblpassword=Label(frame2, text="Enter password",bg="skyblue")
        txtpassword=Entry(frame2,show="*")
        btnsubmit = Button(frame2,text="Submit",command=adddata)
        lblname.grid(row=0,column=0)
        txtname.grid(row=0,column=1)
        lblemail.grid(row=1,column=0)
        txtemail.grid(row=1,column=1)

        lblusername.grid(row=2,column=0)
        txtusername.grid(row=2,column=1)
        lblpassword.grid(row=3,column=0)
        txtpassword.grid(row=3,column=1)

        btnsubmit.grid(row=5,column=0)
        
        frame2.mainloop()

def Login():

        # frame1=Frame(window,bg="skyblue3",width=200,height=200)
        # frame1.place(x=250,y=150)       
        u=txtusername.get()
        p=txtpassword.get()
        cur.execute('select * from tourist1 where username=? and password=?',(u,p))
        rs=cur.fetchall()
        if len(rs)==0:
                print("Invalid")
        else:
                Home()
        # btnLogin = Button(frame1,command=Mainmenu)
                
        # btnLogin.grid(row=0,column=1)

        frame1.mainloop()


window=Tk()
window.title("Tourist Page ")
window.geometry('800x500')
window.configure(bg="black")
window.resizable(False,False)
frame = Frame(window, width=800, height=800)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

##img = ImageTk.PhotoImage(Image.open("E:\\Python\\Mini project\\6871.jpg_wh1200.jpg"))
img1 = ImageTk.PhotoImage(Image.open("E:\\Python\\Mini project\\travel.jpg"))
label = Label(frame, image = img1,bg="black",)
label.pack()
lbl_title=Label(window,text="WELCOME TO LOGIN PAGE",font=20,fg="black",bg="light pink")
lbl_title.place(x=250,y=30,height=30)


frame1=Frame(window,bg="skyblue3",width=200,height=200)
frame1.place(x=250,y=150)

lblusername = Label(frame1,text="Enter Username :",fg="black",bg="light pink3")
txtusername = Entry(frame1)

lblpassword=Label(frame1, text="Enter Password :",fg="black",bg="light pink3")
txtpassword=Entry(frame1,show="*")
btnLogin = Button(frame1,text="Login",command=Login)
#btnLogin1 = Button(frame1,text="enter",command=Verify)
btnSignUp = Button(frame1,text="SignUp",command=Signup)

# lbldata= Label(frame1)

lblusername.grid(row=0,column=0,pady=30)
txtusername.grid(row=0,column=2,padx=5)
lblpassword.grid(row=1,column=0,pady=5)
txtpassword.grid(row=1,column=2,padx=5)

btnLogin.grid(row=2,column=0,pady=10)
btnSignUp.grid(row=2,column=2,padx=20)
# lbldata.grid(row=4,column=1)

frame1.mainloop()
window.mainloop()