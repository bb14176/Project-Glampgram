# Initialise Tkinter
from tkinter import *
from tkinter import ttk
from tkcalendar import *
import csv
from datetime import *


# Window dimensions
root = Tk()
root.geometry('1000x500')
root.resizable(False, False)


# Error Window

def createerror():
    global error
    error = Tk()
    error.geometry('185x150')
    error.resizable(False, False)
    error.title('Error')
    errorcanvas = Canvas(error, bg='Light Blue', width=1000, height=500)
    errorcanvas.place(x=0, y=0)


def createcalendar():
    global calendar
    calendar = Tk()
    calendar.geometry('251x186')
    calendar.resizable(False, False)
    calendar.title('Kauri')
    errorcanvas = Canvas(calendar, bg='Light Blue', width=1000, height=500)
    errorcanvas.place(x=0, y=0)


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
tabControl.add(tab4, text="Details")
tabControl.pack(expand=1, fill="both")
tab4canvas = Canvas(tab4, bg='Light Blue', width=1000, height=500)
tab4canvas.place(x=0, y=0)

tab5 = ttk.Frame(tabControl)
tabControl.add(tab5, text="Search")
tabControl.pack(expand=1, fill="both")

tab1canvas = Canvas(tab1, bg='Light Blue', width=1000, height=500)
tab1canvas.place(x=0, y=0)

tab2canvas = Canvas(tab2, bg='Light Blue', width=1000, height=500)
tab2canvas.place(x=0, y=0)

tab3canvas = Canvas(tab3, bg='Light Blue', width=1000, height=500)
tab3canvas.place(x=0, y=0)

tab5canvas = Canvas(tab5, bg='Light Blue', width=1000, height=500)
tab5canvas.place(x=0, y=0)


# Site Tab Variables
kaurion = 0
oakon = 0
willowon = 0
oakselected = False
willowselected = False
kauriselected = False
site = 'Not Chosen'


# Entry Tab variables


# Random Variables
foodoption = True
everythinglist = []
neweverythinglist = []


# Calendar Tab Variables


# input class
# noinspection PyMethodMayBeStatic
class order(object):
    def __init__(self, name, date1, date2, site1, number, email, cardnumber, expirey, cardname, ccv, food):
        self.name = name
        self.date1 = date1
        self.date2 = date2
        self.site1 = site1
        self.number = number
        self.food = food
        self.email = email
        self.expirey = expirey
        self.cardname = cardname
        self.ccv = ccv
        self.cardnumber = cardnumber


# writing Function
def writeb1():
    global nameentry
    global numberentry
    global cardnumentry
    global emailentry
    global expireentry
    global cardnameentry
    global ccventry
    global neweverythinglist
    p = 1
    k = 1
    with open('orders.csv', 'rt')as f:
        data = csv.reader(f)
        for row in data:
            everythinglist.append(order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                        row[10]))

        neweverythinglist.append(everythinglist.reverse())

        for item in neweverythinglist:
            print(neweverythinglist)
            if nameentry.get().lower() == item.name:
                p = 0

        if p == 0:
            createerror()
            errorlabel = Label(error, font=('Courier', 15, 'bold'), text="ERROR\nName is \nalready in \ndatabase",
                               bg='Light Blue', fg='Black')
            errorlabel.place(x=25, y=5)

        if p == 1:
            for row in everythinglist:
                if calen.get_date() != datetime.strptime(row.date1, '%Y-%m-%d').date() and k == 1:
                    with open('orders.csv', mode='a') as data:
                        data_writer = csv.writer(data, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
                        data_writer.writerow([nameentry.get().lower(), calen.get_date(), calen2.get_date(), site,
                                             numberentry.get(), emailentry.get(), cardnumentry.get(), expireentry.get(),
                                             cardnameentry.get(), cvventry.get(), foodoption])
                    k = 0

                elif k == 1:
                    k = 0
                    createerror()
                    errorlabel.configure(text='Date is \nnot available \nfor selected \nCampsite')
                    errorlabel.place(x=0, y=0)


# Searching Function
def search():
    global searchbox
    global searchlabel
    o = 0
    with open('orders.csv', 'rt')as f:
        data = csv.reader(f)
        for row in data:
            everythinglist.append(order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                        row[10]))
        for row in everythinglist:
            if searchbox.get() == row.date1:
                searchlabel.configure(text=row.name.upper() + ' ' + row.date1 + ' ' + row.date2)
                o = 1
            if o == 0:
                if searchbox.get() != str(row.date1):
                    searchlabel.configure(text='Not Found')


def testing():
    print(type(calen.get_date()))
    daylist = []
    createcalendar()
    cal = Calendar(calendar, month=7, year=2020)
    with open('orders.csv', 'rt')as f:
        data = csv.reader(f)
        for row in data:
            everythinglist.append(order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                        row[10]))
        for row in everythinglist:
            if row.site1 == 'Kauri':
                daylist.append(datetime.strptime(row.date1, '%Y-%m-%d').date())

        for row in daylist:
            cal.calevent_create(row, 'thingo', 'days')
            cal.tag_config('days', background='red')
    cal.place(x=0, y=0)


# Tab Changing functions
def tab1change():
    tabControl.select(tab1)


def tab2change():
    tabControl.select(tab2)


def tab3change():
    tabControl.select(tab3)


def tab4change():
    tabControl.select(tab4)


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

testb = Button(tab1, text='Test', font=('Courier', 15), command=testing, bg='Dodger Blue', fg='Black', width=15)
testb.place(x=50, y=50)


# ==================================================== Details Tab ========================================================

i = 10
nameentry = Entry(tab4, width=20, font=('Courier', 15))
nameentry.insert(0, 'Full Name')
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

nameback = Button(tab4, text='Back', font=('Courier', 15), command=tab3change, bg='Dodger Blue', fg='Black', width=15)
nameback.place(x=50, y=400)

calwrite = Button(tab4, text='Order', font=('Courier', 15), command=writeb1, bg='Dodger Blue', fg='Black', width=15)
calwrite.place(x=750, y=400)


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
    oakselect.configure(bg='medium Blue')
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
    willowselect.configure(bg='medium Blue')
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
    kauriselect.configure(bg='medium Blue')


checklist = []
oaklist = []
kaurilist = []
willowlist = []
with open('orders.csv', 'rt')as jerry:
    read = csv.reader(jerry)
    for thing in read:
        checklist.append(order(thing[0], thing[1], thing[2], thing[3], thing[4], thing[5], thing[6], thing[7], thing[8],
                               thing[9], thing[10]))

    for item in checklist:
        if item.site1 == 'Kauri':
            kaurilist.append(item.date1)
            kaurilist.append(item.date2)

    for item in kaurilist:
        if calen.get_date() == kaurilist:
            print('bad')

oakselect = Button(tab3, text='The Oak', font=('Courier', 15), bg='Dodger Blue', command=oakfun, activebackground='Dodger Blue',
                   width=10, height=3)
oakselect.place(x=116, y=50)

willowselect = Button(tab3, text='The Willow', font=('Courier', 15), bg='Dodger Blue', command=willowfun, activebackground='Dodger Blue',
                      width=10, height=3)
willowselect.place(x=425, y=50)

kauriselect = Button(tab3, text='The Kauri', font=('Courier', 15), bg='Dodger Blue', command=kaurifun, activebackground='Dodger Blue',
                     width=10, height=3)
kauriselect.place(x=750, y=50)

tab3next = Button(tab3, text='Next', font=('Courier', 15), command=tab4change, bg='Dodger Blue', fg='Black', width=15)
tab3next.place(x=750, y=400)

calback = Button(tab3, text='Back', font=('Courier', 15), command=tab2change, bg='Dodger Blue', fg='Black', width=15)
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

tab2next = Button(tab2, text='Next', font=('Courier', 15), command=tab3change, bg='Dodger Blue', fg='Black', width=15)
tab2next.place(x=750, y=400)

tab2back = Button(tab2, text='Back', font=('Courier', 15), command=tab1change, bg='Dodger Blue', fg='Black', width=15)
tab2back.place(x=50, y=400)

# ================================================= Search Tab =========================================================

searchbox = Entry(tab5, width=20, font=('Courier', 15))
searchbox.place(x=250, y=100)

searchbutton = Button(tab5, text='Search', font=('Courier', 10), command=search, bg='Dodger Blue', fg='Black', width=15)
searchbutton.place(x=500, y=100)

searchlabel = Label(tab5, text='', font=('Courier', 20), bg='light blue')
searchlabel.place(x=250, y=200)

# Running Mainlooop
root.mainloop()

'''
Notes


getting calendar date
calen.get_date()


getting today's date
today = date.today()
print(today)
'''