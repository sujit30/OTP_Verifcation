import smtplib
from random import *
from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("OTP Verification")
Label(root,text="OTP Verification using Gmail",fg="red").grid(row=0,column=1)
Label(root,text="Enter your account password: ").grid(row=1,column=0,sticky=W)
p=StringVar()
Entry(root,show="*",textvariable=p).grid(row=1,column=1,sticky=W)
Label(root,text="Enter your Gmail ID: ").grid(row=2,column=0,sticky=W)
a=StringVar()
Entry(root,textvariable=a).grid(row=2,column=1,sticky=W)
Label(root,text="Enter your OTP: ").grid(row=3,column=0,sticky=W)
b=StringVar()
Entry(root,textvariable=b).grid(row=3,column=1,sticky=W)
OTP=""
for i in range(6):
    OTP+=str(randint(0,9))
message=OTP+" is your OTP"
#print(message)

def Send():
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    em="sujitambole3006@gmail.com"
    server.login(em,p.get())
    server.sendmail(em,a.get(),message)
    server.quit()
def Submit():
    if(b.get()==OTP):
        Label(root,text="OTP Verified",fg="red").grid(row=6,column=1)
    else:
        Label(root,text="Invalid OTP",fg="red").grid(row=6,column=1)

Button(root,text="Send OTP",command=Send).grid(row=2,column=2,sticky=W)
Button(root,text="Submit",command=Submit).grid(row=5,column=1)
root.mainloop()