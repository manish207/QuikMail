import Tkinter as tk
from Tkinter import *
import smtplib
import base64
from tkFileDialog import askdirectory
import tkFileDialog

import mimetypes

# Import the email modules we'll need
import email
import email.mime.application


TITLE_FONT = ("Helvetica", 18, "bold")

'''filename = "H:/abc.txt"

# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64'''

MyText=''




class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
    

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, FinalPage):
            frame = F(container, self)
            self.frames[F] = frame
           
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, c):
        frame = self.frames[c]
        frame.tkraise()

    def get_page (self, page_class):
        return self.frames[page_class]


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="QuikMail",foreground = "Red", font=("Courier", 30, "bold"))
        label.pack(side="top")
        sublabel = tk.Label(self, text="Bringing you \n the fastest mailing service",
                            font=("Courier", 15))
        sublabel.pack()
        
        wallpaper = tk.PhotoImage(file='Python-logo-notext.gif')
        img = tk.Label(self, image=wallpaper)
        img.image = wallpaper
        img.pack(side="top", expand = True)

        button1 = tk.Button(self, text="Click Here to Login to your account",\
                            command=lambda: controller.show_frame(PageOne))
        button1.pack(side="bottom")


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        label = tk.Label(self, text="Personal Information", font=TITLE_FONT, foreground="blue")
        label.pack(side="top", fill="x", pady=10)
        self.optionv = tk.StringVar()
        self.optionv.set("---Select One---")
        optionm = tk.OptionMenu(self, self.optionv, "---Select One---", "@gmail.com", "@yahoo.com", "@hotmail.com")
        
        t1 = tk.Label(self, text="Email Account: ")
        self.v = tk.StringVar()
        self.v.set("")
        self.entry1 = tk.Entry(self, textvariable=self.v)

        t2 = tk.Label(self,text="\nPassword: ")
        self.pwd = tk.StringVar()
        self.pwd.set("")
        self.entry2 = tk.Entry(self, textvariable=self.pwd)
        self.entry2.config(show="*")
        
        lgbutton=tk.Button(self, text="Log In", command=self.login) 
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame(StartPage))        
        t1.pack()
        self.entry1.pack()
        optionm.pack()
        t2.pack()
        self.entry2.pack()
        lgbutton.pack()
        button.pack(side="bottom")

    def login(self):
        self.value = tk.Label(self, text="Invalid username / password", font=("Courier", 15, "bold"), foreground="red")
        self.success = tk.Label(self, text="Login was Successful \n (Click ""Continue"" to compose email)", \
                                font=("Courier", 15, "bold"), foreground="blue")
        self.cbutton = tk.Button(self, text="Continue", command=lambda: self.controller.show_frame(PageTwo))
        self.status = tk.Label(self, text="Please select your email domain", foreground="red")
 
        if self.optionv.get() == "@gmail.com":
            try:
                
                self.server = smtplib.SMTP("smtp.gmail.com", 587)
                self.server.ehlo()
                self.server.starttls()
                self.server.login(self.v.get()+self.optionv.get(), self.pwd.get())
                self.success.pack()
                self.cbutton.pack(side="bottom")
           
            except smtplib.SMTPException:
                self.value.pack()
            
            
        elif self.optionv.get() == "@yahoo.com":
            try:
                
                self.server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
                self.server.ehlo()
                self.server.starttls()
                self.server.login(self.v.get()+self.optionv.get(), self.pwd.get())
                self.success.pack()
                self.cbutton.pack(side="bottom")
           
            except smtplib.SMTPException:
                self.value.pack()

        elif self.optionv.get() == "@hotmail.com":
            try:
                
                self.server = smtplib.SMTP("smtp.live.com", 587)
                self.server.ehlo()
                self.server.starttls()
                self.server.login(self.v.get()+self.optionv.get(), self.pwd.get())
                self.success.pack()
                self.cbutton.pack(side="bottom")
           
            except smtplib.SMTPException:
                self.value.pack()

        else:
            self.status.pack()
            



class PageTwo(tk.Frame): 

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page1 = self.controller.get_page(PageOne) 
        label = tk.Label(self, text="Compose Mail", font=TITLE_FONT, foreground="green") 
        label.pack(side="top", fill="x", pady=10)
        
        self.reciever = tk.StringVar()
        self.reciever.set("")
        senderl = tk.Label(self, text="Send to: ")
        self.rmail = tk.Text(self,width=30,height=1)
        
        self.senderoption = tk.StringVar()
        self.senderoption.set("---Select One---")
        senderdomain = tk.OptionMenu(self, self.senderoption, "---Select One---", "@gmail.com", "@hotmail.com", "@yahoo.com")
        
        self.mail = tk.StringVar()
        self.mail.set("")
        #self.textw = tk.Entry(self, textvariable=self.mail)
        self.textq = tk.Text(self, width=20, height=1)
        self.textw = tk.Text(self, width=20, height=8)
        subjectl = tk.Label(self, text="Subject: ")
        bodyl = tk.Label(self, text="Message: ")
        attachment = tk.Label(self, text="Attachment: ")
        self.texta = tk.Text(self, width=20, height=1)
        

        self.bind("<Return>", lambda x: self.addchat())
    # this is the magic that makes your enter key do something

        sendbutton = tk.Button(self, text = "Send Mail", command=self.addchat)
        sendbutton = tk.Button(self, text = "Send Mail", command=self.sendmail)
        logout = tk.Button(self, text="Log Out", command = self.logout)
        """browse=tk.Button(self, text='Browse', command=self.DisplayDir(MyText))
        file1=tk.Entry(self, textvariable = MyText)
        ok=tk.Button(self, text='OK', command=window.destroy)
        """
        senderl.pack(side="top", anchor="w")
        self.rmail.pack(side="top", anchor="nw")
        #senderdomain.pack(side="top", anchor="nw")
        subjectl.pack(side="top", anchor="w")
        self.textq.pack(fill="both")
        bodyl.pack(side="top", anchor="w")
        self.textw.pack(fill="both")
        attachment.pack(side="top", anchor="w")
        self.texta.pack(fill="both")
        #self.textarea.pack(fill="both")
        #browse.pack(side="bottom")
        #file1.pack()
        logout.pack(side="bottom")
        sendbutton.pack(side="bottom")
  
        """browsebutton = Button(self, text="Browse", command=self.browsefunc)
        browsebutton.pack()

        

    def browsefunc(self):
        filename = tkFileDialog.askopenfilename()

        pathlabel = Label(self)
        pathlabel.pack()
        
        pathlabel.config(text=filename)

        

        ok.pack()

    
    def DisplayDir(self,Var):
        feedback = askdirectory()
        Var.set(feedback)"""
    
    def addchat(self):
        txt1 = self.textq.get("1.0", 'end-1c')
        print txt1
        txt = self.textw.get("1.0",'end')
        
        print txt 
        # gets everything in your textbox
        self.textw.insert('end',"\n"+txt)
        # tosses txt into textarea on a new line after the end
        self.textw.delete(0,'end') # deletes your textbox text
    
    def sendmail(self):
        msg = email.mime.Multipart.MIMEMultipart()
        sent = tk.Label(self, text="Email has been sent", foreground="blue", font = TITLE_FONT)
        unsent = tk.Label(self, text="Error in sending email\n Please check your connection"\
                          , foreground="red", font = TITLE_FONT)
        txt="\n"+self.textw.get("1.0",'end') + "\n\n--\nSent through QuikMail"
        body = email.mime.Text.MIMEText(txt)
        msg['Subject'] = self.textq.get("1.0", 'end')
        msg.attach(body)
        # PDF attachment
        for line in self.texta.get('1.0', 'end-1c').splitlines():
        # Iterate lines
            if line:
                filename=line
                fp=open(filename,'rb')
                att = email.mime.application.MIMEApplication(fp.read(),_subtype="txt")
                fp.close()
                att.add_header('Content-Disposition','attachment',filename=filename)
                msg.attach(att)
            #print('path: {}'.format(line))
            
        #filename=self.texta.get("1.0",'end-1c')
        """if filename!="":
            fp=open(filename,'rb')
            att = email.mime.application.MIMEApplication(fp.read(),_subtype="txt")
            fp.close()
            att.add_header('Content-Disposition','attachment',filename=filename)
            msg.attach(att)  """
        #if self.senderoption.get() == "@gmail.com":

        try:
            for line in self.rmail.get('1.0', 'end-1c').splitlines():
            # Iterate lines
                if line:
                    self.page1.server.sendmail(self.page1.v.get()+self.page1.optionv.get(),\
                                           line, msg.as_string())
            print("Success")
            sent.pack()
            
            
        except smtplib.SMTPRecipientsRefused :
            print("There was an error in sending the email")
            print(self.page1.v.get())
            unsent.pack()
    def logout(self):
        self.page1.server.quit()
        self.controller.show_frame(FinalPage)
"""
        elif self.senderoption.get() == "@hotmail.com":
            try: 
                self.page1.server.sendmail(self.page1.v.get()+self.page1.optionv.get(),\
                                           self.reciever.get(), txt)
                print("Success")
                sent.pack()
            except smtplib.SMTPRecipientsRefused :
                print("There was an error in sending the email")
                print(self.page1.v.get())
                unsent.pack()

        elif self.senderoption.get() == "@yahoo.com":
            try: 
                self.page1.server.sendmail(self.page1.v.get()+self.page1.optionv.get(),\
                                           self.reciever.get(), txt)
                print("Success")
                sent.pack()
            except smtplib.SMTPRecipientsRefused :
                print("There was an error in sending the email")
                print(self.page1.v.get())
                unsent.pack()
""" 
        

class FinalPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.page1 = self.controller.get_page(PageOne)
        endtitle = tk.Label(self, text = "Thank You \n For Using Our Program", foreground = "green", font=("Helvetica",25,"bold"))
        difacc = tk.Button(self, text = "Log in with another account", \
                           command = self.diffacc)
        exbutton = tk.Button(self, text = "Exit", command = self.ex)
        endtitle.pack(side="top", fill="both", expand = True)
        exbutton.pack(side="bottom")
        difacc.pack(side="bottom")

    def diffacc(self):
        self.page1.entry1.delete(0,'end')
        self.page1.entry2.delete(0,'end')
        self.page1.optionv.set("---Select One---")
        self.page1.value.pack_forget()
        self.page1.status.pack_forget()
        self.page1.success.pack_forget()
        self.page1.cbutton.pack_forget()
        self.controller.show_frame(PageOne)

    def ex(self):
        quit()
    
        
                
if __name__ == "__main__":
    app = SampleApp()
    app.title("QuikMail")
    app.geometry("400x400")
    app.mainloop()
