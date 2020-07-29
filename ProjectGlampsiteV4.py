# Initialise Tkinter
from tkinter import *
from tkinter import ttk
from tkcalendar import *
import csv
# from datetime import *


# Window dimensions
root = Tk()
root.geometry('1000x500')
root.resizable(False, False)


# Error Window

def create():
    # noinspection PyGlobalUndefined
    global error
    error = Tk()
    error.geometry('185x150')
    error.resizable(False, False)
    error.title('Error')


# Tab control
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Calendar")
tabControl.pack(expand=1, fill="both")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="People")
tabControl.pack(expand=1, fill="both")

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text="Site")
tabControl.pack(expand=1, fill="both")

tab4 = ttk.Frame(tabControl)

tab1canvas = Canvas(tab1, bg='Light Blue', width=1000, height=500)
tab1canvas.place(x=0, y=0)

tab2canvas = Canvas(tab2, bg='Light Blue', width=1000, height=500)
tab2canvas.place(x=0, y=0)

tab3canvas = Canvas(tab3, bg='Light Blue', width=1000, height=500)
tab3canvas.place(x=0, y=0)


# Site Tab Variables
kaurion = 0
oakon = 0
willowon = 0
oakselected = False
willowselected = False
kauriselected = False
site = 'Not Chosen'


# Entry Tab variables
nameentry = ''
numberentry = ''


# Random Variables
foodoption = True
paid1 = True
everythinglist = []


# Calendar Tab Variables
errorlabel = Label(tab1, font=('Courier', 20, 'bold'), text='', bg='Light Blue', fg='Black')


# input class
# noinspection PyMethodMayBeStatic
class order(object):
    def __init__(self, name, date, date2, site1, number, food, paid):
        self.name = name
        self.date = date
        self.date2 = date2
        self.site1 = site1
        self.number = number
        self.food = food
        self.paid1 = paid


# writing Function
def writeb1():
    global nameentry
    global numberentry
    with open('orders.csv', mode='a') as data:
        data_writer = csv.writer(data, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        data_writer.writerow([nameentry.get(), calen.get_date(), calen2.get_date(), site,
                             numberentry.get(), foodoption, paid1])


# Reading function
def readb1():
    with open('orders.csv', 'rt')as f:
        data = csv.reader(f)
        for row in data:
            everythinglist.append(order(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        for row in everythinglist:
            print(row.food)


# Tab Changing functions
def tab1change():
    tabControl.select(tab1)


def tab2change():
    tabControl.select(tab2)


def tab3change():
    tabControl.select(tab3)
    tabControl.add(tab4, text="Details")
    tabControl.pack(expand=1, fill="both")


def tab4change():
    tabControl.add(tab4, text="Details")
    tabControl.pack(expand=1, fill="both")
    tab4canvas = Canvas(tab4, bg='Light Blue', width=1000, height=500)
    tab4canvas.place(x=0, y=0)
    tabControl.select(tab4)
    createtab4()


# ============================================== Calendar Tab ==========================================================

calendar = Label(tab1, text='Dates', font=('Courier', 20, 'bold'), bg='Light Blue', fg='black')
calendar.place(x=450, y=150)

to = Label(tab1, text='To:', font='Courier', bg='Light Blue', fg='black')
to.place(x=475, y=196)

calen = DateEntry(tab1, dateformat=3, font=('Courier', 12), width=12, background='Dodger Blue', foreground='Black',
                  borderwidth=4, Calendar=2020)
calen.place(x=325, y=200)

calen2 = DateEntry(tab1, dateformat=3, font=('Courier', 12), width=12, background='Dodger Blue', foreground='Black',
                   borderwidth=4, Calendar=2020)
calen2.place(x=525, y=200)

calnext = Button(tab1, text='Next', font=('Courier', 15), command=tab2change, bg='Dodger Blue', fg='Black', width=15)
calnext.place(x=750, y=400)

calentest = DateEntry(tab1, dateformat=3, font=('Courier', 12), width=12, background='Dodger Blue', foreground='Black',
                      borderwidth=4, Calendar=2020)

todaydate = Label(tab1, font=('Courier', 16), text="Today's Date: " + str(calentest.get_date()), bg='light blue')
todaydate.place(x=650, y=50)


# ==================================================== Details Tab ========================================================

def createtab4():
    global nameentry
    global numberentry
    
    i = 10
    nameentry = Entry(tab4, width=20, font=('Courier', 15))
    nameentry.insert(0, 'Name')
    nameentry.place(x=50, y=i*5)

    numberentry = Entry(tab4, width=20, font=('Courier', 15))
    numberentry.insert(0, 'Phone Number')
    numberentry.place(x=50, y=i*8.5)

    emailentry = Entry(tab4, width=20, font=('Courier', 15))
    emailentry.insert(0, 'Email')
    emailentry.place(x=50, y=i*12)

    cardnumentry = Entry(tab4, width=20, font=('Courier', 15))
    cardnumentry.insert(0, 'Card Number')
    cardnumentry.place(x=500, y=i*5)

    expireentry = Entry(tab4, width=20, font=('Courier', 15))
    expireentry.insert(0, 'Expire Date')
    expireentry.place(x=500, y=i*8.5)

    cardnameentry = Entry(tab4, width=20, font=('Courier', 15))
    cardnameentry.insert(0, 'Name On Card')
    cardnameentry.place(x=500, y=i*12)

    cvventry = Entry(tab4, width=20, font=('Courier', 15))
    cvventry.insert(0, 'CCV')
    cvventry.place(x=500, y=i*15.5)

    nameback = Button(tab4, text='Back', font=('Courier', 15), command=tab2change, bg='Dodger Blue', fg='Black', width=15)
    nameback.place(x=50, y=400)

    calwrite = Button(tab4, text='Write', font=('Courier', 15), command=writeb1, bg='Dodger Blue', fg='Black', width=15)
    calwrite.place(x=750, y=400)

    calread = Button(tab4, text='Read', font=('Courier', 15), command=readb1, bg='Dodger Blue', fg='Black', width=15)
    calread.place(x=750, y=350)


# ==================================================== Site Tab ========================================================

def oakfun():
    global oakselect
    global willowselect
    global kauriselect
    global oakselected
    global willowselected
    global kauriselected
    global site
    oakselected = True
    willowselected = False
    kauriselected = False
    site = 'Oak'
    oakselect.configure(bg='Red')
    willowselect.configure(bg='Dodger Blue')
    kauriselect.configure(bg='Dodger Blue')


def willowfun():
    global oakselect
    global willowselect
    global kauriselect
    global oakselected
    global willowselected
    global kauriselected
    global site
    oakselected = False
    willowselected = True
    kauriselected = False
    site = 'Willow'
    oakselect.configure(bg='Dodger Blue')
    willowselect.configure(bg='Red')
    kauriselect.configure(bg='Dodger Blue')


def kaurifun():
    global oakselect
    global willowselect
    global kauriselect
    global oakselected
    global willowselected
    global kauriselected
    global site
    oakselected = False
    willowselected = False
    kauriselected = True
    site = 'Kauri'
    oakselect.configure(bg='Dodger Blue')
    willowselect.configure(bg='Dodger Blue')
    kauriselect.configure(bg='Red')


oakselect = Button(tab3, text='The Oak', font=('Courier', 15), bg='Dodger Blue', command=oakfun, activebackground='Dodger Blue',
                   width=10, height=3)
oakselect.place(x=100, y=100)

willowselect = Button(tab3, text='The Willow', font=('Courier', 15), bg='Dodger Blue', command=willowfun, activebackground='Dodger Blue',
                      width=10, height=3)
willowselect.place(x=300, y=100)

kauriselect = Button(tab3, text='The Kauri', font=('Courier', 15), bg='Dodger Blue', command=kaurifun, activebackground='Dodger Blue',
                     width=10, height=3)
kauriselect.place(x=500, y=100)

tab3next = Button(tab3, text='Next', font=('Courier', 15), command=tab4change, bg='Dodger Blue', fg='Black', width=15)
tab3next.place(x=750, y=400)

calback = Button(tab3, text='Back', font=('Courier', 15), command=tab1change, bg='Dodger Blue', fg='Black', width=15)
calback.place(x=50, y=400)


# ================================================= People Tab =========================================================

adultlabel = Label(tab2, text='Adults: ', font=('Courier', 20), bg='light blue')
adultlabel.place(x=225, y=150)

childlabel = Label(tab2, text='Children: ', font=('Courier', 20), bg='light blue')
childlabel.place(x=192, y=225)

adultentry = Spinbox(tab2, from_=1, to=5, font=('Courier', 20))
adultentry.place(x=350, y=150)

childentry = Spinbox(tab2, from_=0, to=5, font=('Courier', 20))
childentry.place(x=350, y=225)

# Running Mainlooo
root.mainloop()

'''
Notes


getting calendar date
calen.get_date()


getting today's date
today = date.today()
print(today)
'''