from tkinter import *
 
def Shuvam1():
       

    #Input   
    
    def I_n():
        tp=Tk()
        
        
        e110=Label(tp,text='Enter the SRN:').grid()
        EX_SRN=Entry(tp,width=20)
        EX_SRN.grid()
        
        e122=Label(tp,text='Enter the Name:').grid()
        EX_N=Entry(tp,width=20)
        EX_N.grid()
    
        e133=Label(tp,text='Enter the Physics marks:').grid()
        EX_M1=Entry(tp,width=20)
        EX_M1.grid()
        
        e144=Label(tp,text='Enter the Maths marks:').grid()
        EX_M3=Entry(tp,width=20)
        EX_M3.grid()
    
        e155=Label(tp,text='Enter the CS marks:').grid()
        EX_M2=Entry(tp,width=20)
        EX_M2.grid()
    
        e177=Label(tp,text='Enter the attendance out of 100 days::').grid()
        EX_A=Entry(tp,width=20)
        EX_A.grid()
        
        #ar=str()
        
        def WT(n): #Func to write to a txt file.
            file = open("Marks.txt", 'a') #a=append text
            if file: #to check if file opened for reading succes or not.
                file.write('\n') 
                file.write(n) #The data thats passed for writing after input taken
                file.close()
                return 1
            else: 
                file.close()
                return 0 #failed to open.
        
        def ABC():
            
                   
            a1=EX_SRN.get()
            a2=EX_N.get()
            a3=int(EX_A.get())
            a4=int(EX_M1.get())
            a5=int(EX_M2.get())
            a6=int(EX_M3.get())
            a7=(a4+a5+a6)*100/300   
            ar=str(a1+','+a2+','+str(a3)+','+str(a4)+','+str(a5)+','+str(a6)+','+str(a7)+','+'|')
            
            q=WT(ar)
            if q==0:
                print('File Open ERROR !')
            else:
                print('File Successfully Updated.') 
        
        bt=Button(tp,text='Submit',command=ABC).grid()
        #return ar
    
    I_n()
    

def Shuvam2(): #modify
    f=open("Marks.txt",'r')
    l=f.read()
    f.close()#optional
    ao=l.split() 
    top=Tk()
    #print('Data Available: \n',ao)
    
    e881=Label(top,text='Enter the srn:').grid()
    e11=Entry(top,width=20)
    e11.grid()
    
    e121=Label(top,text='Enter the Name to be updated:').grid()
    e22=Entry(top,width=20)
    e22.grid()
    
    e131=Label(top,text='Enter the Physics marks:').grid()
    e33=Entry(top,width=20)
    e33.grid()
    
    e141=Label(top,text='Enter the Maths marks:').grid()
    e44=Entry(top,width=20)
    e44.grid()
    
    e151=Label(top,text='Enter the CS marks:').grid()
    e55=Entry(top,width=20)
    e55.grid()
    
        
    e171=Label(top,text='Enter the attendance:').grid()
    e77=Entry(top,width=20)
    e77.grid()
      
    

    i=0
    w=[]

    for i in range(len(ao)):
        w.append(list(ao[i].split(',')))
        i+=1    
               
    
    Nm=0
    M1=0
    M2=0
    M3=0
    p=0
    srn=0
    Ag=0
    def disp():
        #print('Updated contents:\n',w)
        f=open("Marks.txt",'w')
        for i in w:
            for j in i:
            
                if j ==i[7]:
                
                    print(j,end='\n',file=f)
                else:
                
                    print(j,end=',',file=f)
    def func(srn,Nm,M1,M2,M3,p,Ag):
        for j in w:
            
            if srn == j[0]:
                
                j[1]=Nm
                
                j[2]=p
                j[3]=M1
                j[4]=M2
                j[5]=M3
                j[6]=Ag
        disp()
    def abc():
        nonlocal Nm
        nonlocal M1
        nonlocal M2
        nonlocal M3
        nonlocal p
        nonlocal srn
        nonlocal Ag
        srn=e11.get()
        
        Nm=e22.get()
        M1=e33.get()
        
        M2=e44.get()
        M3=e55.get()
        p=e77.get()
        
        Ag=((int(M1)+int(M2)+int(M3))/300)*100 
        func(srn,Nm,M1,M2,M3,p,Ag)   
    
    bt=Button(top,text='Submit',command=abc)
    bt.grid()
    
 


    
    f.close()


#Admin interface

def admin():
    
    c=dict()
    root=Tk()
    f=open("Marks.txt","r")
    
    def convert():
        l=list()
        
        nonlocal c
        for a in f:
            a=a.strip('\n') #removes \n
            
            b=a.split(',') #splits based on comma into list 
            
            c[b[0]]=(b[1],b[2],b[3],b[4],b[5],b[6]) #creates dictionary
            
        
        return c

    a=convert()
    key=0
    def search():
        e1=Label(root,text="Enter SRN : ").grid()
        k=Entry(root,width=50)
        k.grid()
        nonlocal key
        nonlocal a
        def s():
            h=k.get() 
            
            for j in list(a.keys()):
                if j==h:
                    l=Label(root,text='*'*25).grid()
                    lb=Label(root,text='SRN : '+j).grid()
                    lb1=Label(root,text="Name : "+a[j][0]).grid()
                    lb2=Label(root,text="Attendance : "+a[j][1]).grid()
                    lb3=Label(root,text="Physics marks : "+a[j][2]).grid()
                    lb4=Label(root,text="Math marks : "+a[j][3]).grid()
                    lb5=Label(root,text="Computer science marks : "+a[j][4]).grid()
                    lb6=Label(root,text="Average : "+a[j][5]).grid()
                    key=1
            if key==0:
                lb=Label(root,text="SRN doesn't exist :(").grid()
        bt=Button(root,text="Submit",command = s).grid()

    def r(): #reads from file as req.
        b=convert()
        l=Label(root,text='*'*25).grid()
        for i in a.keys():
            
            lb=Label(root,text='SRN : '+i).grid()
            lb1=Label(root,text="Name : "+b[i][0]).grid()
            lb2=Label(root,text="Attendance : "+b[i][1]).grid()
            lb3=Label(root,text="Physics marks : "+b[i][2]).grid()
            lb4=Label(root,text="Computer science marks : "+b[i][3]).grid()
            lb5=Label(root,text="Math marks : "+b[i][4]).grid()
            lb6=Label(root,text="Average : "+b[i][5]).grid()
            
        return 

    def all_children (window) :
        _list = window.winfo_children()
    
        for item in _list :
            if item.winfo_children() :
                _list.extend(item.winfo_children())

        return _list
  
    def clr():
        widget_list = all_children(root)
        for item in widget_list:
            item.grid_forget()
        
  
    def apage():
        bt1=Button(root,text='View all students data',command=r).grid(row=0,column=0)
        bt2=Button(root,text='Search for a particular student',command=search).grid(row=1,column=0)
        bt3=Button(root,text='Modify record',command=Shuvam2).grid()
        b4=Button(root,text='Insert',command=Shuvam1).grid()
        button=Button(root,text='Exit',command=root.destroy).grid()

    root.title("Admin-Interface")
    def authen():
        lb1=Label(root,text='Enter password : ').grid() #make change here 

        p="password"
        e1=Entry(root,width=20)
        e1.grid(row=0,column=1) 
        def m():
            password=e1.get()
            if password==p: 
                lb2=Label(root,text="Correct password!").grid()
                clr()
                apage()
            else :
                lb2=Label(root,text="Incorrect password!").grid()
        bt1 = Button(root, text = 'Submit', command = m).grid(row=1,column=1)
    authen()
    root.mainloop()
  
#student interface
def studentinterface():
    import matplotlib.pyplot as plt
    import pyqrcode 
    import png 
    import qrcode
    from pyqrcode import QRCode 
    
    root=Tk()
    f=open("Marks.txt","r")
    c=dict()
    a=''
    e=Label(root,text='Enter SRN : ').grid()
    e1=Entry(root,width=20)
    e1.grid(row=0,column=1)

    def convert(): #extract data from file and return dict 
        l=list()
        for a in f:
            a=a.strip('\n') #removes \n
            b=a.split(',') #splits based on comma into list 
            
            c[b[0]]=(b[1],b[2],b[3],b[4],b[5],b[6]) #creates dictionary
            l.append(c)
        return c

    def graph():
        global a 
        l=convert()
        names=a
        
        def stdgraph(names,l): #name here is ref to SRN
            for i in l.keys():
                if i==names:
                    subs=["COMPUTER","PHYSICS","MATHS"]
                    subsm=[]#to add marks of phy,cs,math
                    subsm.append(float(l[i][2]))
                    subsm.append(float(l[i][3]))
                    subsm.append(float(l[i][4]))
                    
                    plt.bar(subs,subsm[3::-1]) #for x and y axes resp.
                    plt.title(names)
                    plt.xlabel("SUBJECTS")
                    plt.ylabel('MARKS')
                    plt.show()
        stdgraph(names,l)
    
    def piechart():
        l=convert()
        global a
        names=a
        for i in l.keys():
            if i==names:
                pieLabels = 'Present' , 'Absent' 
                piel=[] #attendance values
                piel.append(int(l[i][1]))   #pres.
                piel.append(100-int(l[i][1])) #ab.
                figureObject, axesObject = plt.subplots()
                
                axesObject.pie(piel,labels=pieLabels,autopct='%1.1f%%',shadow=True,startangle=0) #autopct=to view % of share in pie
                # Aspect ratio - equal means pie is a circle
                axesObject.axis('equal')
                
                plt.show()
                

    def qrcode():
        l=convert()
        global a 
        names=a
        for i  in l.keys():
            if i==names:
                s = ("NAME: "+l[i][0]+" ,ATTENDANCE: "+l[i][1]+ " ,SRN: "+i+' ,Maths: '+l[i][4]+' ,PHYSICS: '+l[i][2]+' ,CS: '+l[i][3])
                # we write into the qr code as a string of data, thats the standard way
        url = pyqrcode.create(s)
         
        url.png('myqr.png', scale = 6) 

    def sd(srn): #function that shows student details
        a=convert()
        lb1=Label(root,text='Name : '+a[srn][0]).grid()
        lb2=Label(root,text='SRN : '+srn).grid()
        lb3=Label(root,text='Attendance : '+a[srn][1]).grid()
        lb4=Label(root,text='Math marks : '+a[srn][2]).grid()
        lb5=Label(root,text='Physics marks : '+a[srn][3]).grid()
        lb6=Label(root,text='Computer science marks : '+a[srn][4]).grid()
        lb7=Label(root,text='Average : '+a[srn][5]).grid()
        #buttons :
        b1=Button(root,text='Graph',command=graph).grid()
        b2=Button(root,text='Pie chart',command=piechart).grid()
        b3=Button(root,text='QR Code',command=qrcode).grid()
        button=Button(root,text='Exit',command=root.destroy).grid()

    def all_children (window) :
        _list = window.winfo_children()

        for item in _list :
            if item.winfo_children() :
                _list.extend(item.winfo_children())

        return _list

    def m(): #function to verify SRN 
        srn=e1.get()
        key=0
        xx=convert()
        for i in xx.keys():
            if srn==i: #checks srn
                key=1
                widget_list = all_children(root) #code to clear screen 
                for item in widget_list:
                    item.grid_forget()
                global a
                a=srn 
                sd(srn) #returns srn
        if key==0:
            lb=Label(root,text='Invalid SRN! Please try again').grid()
    bt1 = Button(root, text = 'Submit', command = m).grid(row=1,column=1)
    root.mainloop()
    f.close()
   
def Shuvam3():# Main tk interface
    
    top=Tk()
    top.title("Student ReportCard Management ")
    label = Label(text="Welcome Dear User!")
    label.grid()
    
    label0 = Label(
    text="Student ReportCard Management Project (2020-2021) \n Done by:\n 1.Shuvam Bose\n2.Siddarth S \n3.Siddhant Pathak",
    foreground="White",  # Set the text color to white
    background="Purple" , # Set the background color to black
    width=0, height=18
    )
    label0.grid()
    
    
    label1 = Label(text="Click the right button for their info available:",
    foreground='Red',
    background='White'
    
    )
    label1.grid()
    
    button0= Button(top,
    text="ADMIN",width=8,
    height=1,
    bg="Red",
    fg="White",command=admin)
    button0.grid()
      

    button1=Button(top,
    text="Student",
    
    width=8,
    height=1,
    bg="Green",
    fg="White",
    command=studentinterface#change this name to ()
    )
    
    top.geometry("290x370")
    button1.grid()
    top.mainloop()
    
   
Shuvam3()   #because this is the very first part to be executed.
#'''    



















