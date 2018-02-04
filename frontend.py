
from tkinter import *
import backend

windows=Tk()

windows.wm_title("BookStore 1.0")


def view_command():
    List1.delete(0,END)                 #it will clear the list box from index 0 to END
    for row in backend.view():
        List1.insert(END,row)  #END is an inbuilt vsriable this will help apped the List1

def search_command():
    List1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        List1.insert(END,row)

def insert_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    List1.delete(0,END)
    List1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def get_selected_row(event): #event variable is reaquired read the documentation
    global selected_tupple
    '''if len(List1.curselection())!=0:
        index=List1.curselection()[0]
        selected_tupple=List1.get(index)
    # return selected_tupple
        e1.delete(0,END) #clear the existing space
        e1.insert(END,selected_tupple[1]) #insert at the end
        e2.delete(0,END)
        e2.insert(END,selected_tupple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tupple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tupple[4])'''

    try:
        index=List1.curselection()[0]
        selected_tupple=List1.get(index)
    # return selected_tupple
        e1.delete(0,END) #clear the existing space
        e1.insert(END,selected_tupple[1]) #insert at the end
        e2.delete(0,END)
        e2.insert(END,selected_tupple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tupple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tupple[4])
    except IndexError:
        pass


def delete_command():
    # backend.delete(get_selected_row()[0])
    backend.delete(selected_tupple[0])

def upadate_command():
    backend.update(selected_tupple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get()) #the selected_tupple[0] is ID we dont need to change that, only change the rest


L1=Label(windows,text="Title")
L1.grid(row=0,column=0)

L2=Label(windows,text="Author")
L2.grid(row=0,column=2)

L3=Label(windows,text="Year")
L3.grid(row=1,column=0)

L4=Label(windows,text="ISBN")
L4.grid(row=1,column=2)

title_text=StringVar()   #we need to create a stringvar object to be able to insert string into the entry object HOWEVER we need to use a get() method along with it
e1=Entry(windows,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(windows,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(windows,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(windows,textvariable=isbn_text)
e4.grid(row=1,column=3)


List1=Listbox(windows,height=6,width=35)
List1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(windows)
sb1.grid(row=2,column=2,rowspan=6)

List1.configure(yscrollcommand=sb1.set)  #to config the Scrollbar with then listbox
sb1.configure(command=List1.yview)

List1.bind("<<ListboxSelect>>",get_selected_row)

b1=Button(windows,text="View all",width=12,command=view_command) #we dont add brackets after view_command.
b1.grid(row=2,column=3)

b2=Button(windows,text=" Search Entry ",width=12,command=search_command) #again we a making a wrapper function called search_command
b2.grid(row=3,column=3)

b3=Button(windows,text="Add Entry",width=12,command=insert_command)#same thing again
b3.grid(row=4,column=3)

b4=Button(windows,text=" Update Selected",width=12,command=upadate_command)
b4.grid(row=5,column=3)

b5=Button(windows,text="Delete Selected",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(windows,text="Close",width=12,command=windows.destroy)
b6.grid(row=7,column=3)

windows.mainloop()
