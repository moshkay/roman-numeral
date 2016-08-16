__author__="Davinci-Kay"
__project__="Roman Numeral Converter"

#importing modules
from tkinter import *
from tkinter import messagebox as msg
from collections import OrderedDict


app=Tk()
app.resizable(False,False)
app.geometry("400x400+450+150")
app.title("Roman Converter")

#these are functions for the creating instances of the widgets in the main prog.
def label(mas,text,bgcol,fgcol,hei,wid,ro,col,fontsize,colspan,just=None):
    """Function for the Label widget"""
    lab=Label(mas,text=text,height=hei,width=wid,bg=bgcol,fg=fgcol,padx=10,pady=10,font=("Verdana",fontsize,"bold"),justify=just)
    lab.grid(row=ro,column=col,sticky=N,columnspan=colspan,padx=4,pady=4)
def button(mas,text,bgcol,fgcol,hei,wid,ro,col,x,y,command=None):
    """Function for the Button widget"""
    but=Button(mas,text=text,bg=bgcol,fg=fgcol,height=hei,width=wid,font=("Arial black",10,"bold"),relief=FLAT,bd=4,pady=2,padx=2,command=command)
    but.grid(row=ro,column=col,padx=x,pady=y)
#end of global functions

class RomanConvert(Frame):
    """Roman class object"""

    def __init__(self,master):
        Frame.__init__(self,master)
        self.master=master
        self.mainmenu=Menu(self.master,activebackground="#ff6d00")
        self.master.config(bg="#ffe0b2",height=400,width=400,menu=self.mainmenu)

        #creating the frame for page 1 
        self.body_frame=Frame(self.master,height=400,width=400,bg="#ffe0b2")
        self.body_frame.grid()
        
        #creating a list for the labels and entries on page 1
        label_list=["Arabic: ","Roman: "]
        self.label_list=label_list
        
        #calling the methods of the class object
        self.create_header_label()
        self.create_button()
        self.create_page2()
        self.create_menu()
        
    def create_page2(self):
        #creating page 2 i.e the about frame
        self.page2=Frame(self.master,height=400,width=400,bg="#ffe0b2")
        label(self.page2,"Roman Converter Team","#ffe0b2","#ff6d00",1,20,0,1,15,1)
        names=["OMONIYI DAMILOLA A.    CSC/13/5032","AKINLOSOTU VICTOR    CSC/14/9665",\
               "OLASANMI BISOLA A.    CSC/14/0323","SALIU MOSHOOD K.    CSC/13/5049",\
               "OSAGIEDE NOSAKHARE A.    CSC/13/5034"]
        r=1

        #creating labels for the names
        for i in names:
            label(self.page2,i,"#ffe0b2","#ff6d00",1,40,r,0,10,3)
            r+=1
        #creating button for navigating backwards on the second page
        button(self.page2,"BACK","#ff6d00","#ffe0b2",1,5,6,0,2,2,self.Home)
        #end of the design of page 2


    def create_header_label(self):
        """creating header label on page 1"""
        label(self.body_frame,"ROMAN CONVERTER","#ff6d00","#ffe0b2",2,26,0,0,15,6)

        #creating the labels and entry widgets
        r=1
        self.value=IntVar()#initialising the text variable

        for i in self.label_list:#loop for creating the labels
            label(self.body_frame,i,"#ffe0b2","#ff6d00",3,5,r,1,10,1)
            r+=1

        #creating the entry
        self.entry=Entry(self.body_frame,width=20,bg="#ff6d00",fg="#ffe0b2",font=("arial",15,"bold"),bd=4,relief=SUNKEN,textvariable=self.value,justify=CENTER)
        self.entry.grid(row=1,column=2,columnspan=3,pady=5,padx=5)
        self.entry.bind("<Any-KeyRelease>",self.convert)

        #label for the output
        self.label_output=Label(self.body_frame,width=26,height=1,font=("arial black",10),bg="#ff6d00",fg="#ffe0b2",padx=5,pady=5)
        self.label_output.grid(row=2,column=2,columnspan=3)

        #copyright label
        label(self.body_frame,"©Copyright DaVinci kay, 2016.","#ffe0b2","#ff6d00",1,23,6,2,8,3)
        

    def create_button(self):
        #creating a list for the commands
        button_command=[self.Exit,self.Clear,self.about]
        button_list=["EXIT","CLEAR","ABOUT"]
        c=2;index=0

        for i in button_list:
            #creating the buttons
            button(self.body_frame,i,"#ff6d00","#ffe0b2",1,5,3,c,2,5,button_command[index])
            c+=1
            index+=1#incrementing the index


    def create_menu(self):
        """creating menu on the home page"""
        
        
        HelpMenu=Menu(self.body_frame,tearoff=0,activeforeground="#ffe0b2",activebackground="#ff6d00")
        self.mainmenu.add_cascade(label="HELP",menu=HelpMenu)
        HelpMenu.add_command(label="About Roman Converter",command=self.about)
        HelpMenu.add_separator()
        HelpMenu.add_command(label="Help",command=self.Help)


    def convert_int(self,num):
        
        """creating an instance of an ordered dict"""
        self.dic_roman=OrderedDict()
        self.dic_roman[1000]="M"
        self.dic_roman[900]="CM"
        self.dic_roman[500]="D"
        self.dic_roman[400]="CD"
        self.dic_roman[100]="C"
        self.dic_roman[90]="XC"
        self.dic_roman[50]="L"
        self.dic_roman[40]="XL"
        self.dic_roman[10]="X"
        self.dic_roman[9]="IX"
        self.dic_roman[5]="V"
        self.dic_roman[4]="IV"
        self.dic_roman[1]="I"
        
        
        #the function for the calculation
        
        def converter_int(num):
            """a recursive function"""
            
            for k in self.dic_roman.keys():
    
                    quotient,remainder=divmod(num,k)
                    if quotient>4:
                        break
                    yield self.dic_roman[k]*quotient
                    num=remainder

                    if num>0:
                        converter_int(num)
                    else:
                        break
            
        return "".join([a for a in converter_int(num)])
       


    def convert(self,event):
        """convert method"""
        try:

            val=self.value.get()
            if val>3999:
                self.label_output.config(text="WRONG INPUT")
            else:
                b=self.convert_int(val)
                self.label_output.config(text=b)
        except:
            self.label_output.config(text="ENTRY EMPTY/WRONG INPUT")
    


    def Exit(self):
        """exit method"""
        b=msg.askyesno(message="Are you sure you want to close this app?")
        if b==YES:
            app.destroy()


    def Clear(self):
        """clear method for the clear button"""
        self.value.set(0)
        self.label_output.config(text="")


    def about(self):
        """method for the about page"""
        self.body_frame.grid_remove()
        self.page2.grid()


    def Home(self):
        """method for navigating back to the home page"""
        self.body_frame.grid()
        self.page2.grid_remove()


    def Help(self):
        """method for the help menu"""
        helps=msg.showinfo(title="Help",message="enter your arabic numerals in the entry\n and see the magic")
    

RomanConvert(app)
app.mainloop()
