# Initialise Tkinter
from tkinter import *
from tkinter import ttk
from tkcalendar import *
import csv
from datetime import *


# Window dimensions
root = Tk()
root.geometry('1000x500+50+50')
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
    calendar.title('')
    errorcanvas = Canvas(calendar, bg='Light Blue', width=1000, height=500)
    errorcanvas.place(x=0, y=0)


# Calendar check function
checklist = []
oaklist = []
kaurilist = []
willowlist = []
selecteddates = []
samedate = []


# Tab control
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Calendar")
tabControl.pack(expand=1, fill="both")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="People", state='hidden')
tabControl.pack(expand=1, fill="both")

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text="Site", state='hidden')
tabControl.pack(expand=1, fill="both")

tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text="Details", state='hidden')
tabControl.pack(expand=1, fill="both")
tab4canvas = Canvas(tab4, bg='Light Blue', width=1000, height=500)
tab4canvas.place(x=0, y=0)

tab5 = ttk.Frame(tabControl)
tabControl.add(tab5, text="Search", state='hidden')
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

# Random Variables
foodoption = False
everythinglist = []
minimumdate = datetime.strptime('2020-01-01', '%Y-%m-%d').date()
maximumdate = datetime.strptime('2022-01-01', '%Y-%m-%d').date()
searchdates = []
labellist = []


# input class
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
    p = 0
    datelist = []
    with open('orders.csv', 'rt')as f:
        data = csv.reader(f)
        everythinglist.clear()
        for row in data:
            everythinglist.append(order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                        row[10]))

        if site == 'Kauri':
            for row in everythinglist:
                if row.site1 == 'Kauri':
                    n = (datetime.strptime(row.date2, '%Y-%m-%d').date() - datetime.strptime(row.date1, '%Y-%m-%d').date())
                    datelist.append(datetime.strptime(row.date1, '%Y-%m-%d').date())
                    datelist.append(datetime.strptime(row.date2, '%Y-%m-%d').date())
                    if n.days >= 2:
                        for m in range(1, n.days):
                            nextday = datetime.strptime(row.date1, '%Y-%m-%d') + timedelta(days=m)
                            datelist.append(nextday)

            for row in datelist:
                if calen.get_date() == row or calen2.get_date() == row:
                    p = 1

        if site == 'Oak':
            for row in everythinglist:
                if row.site1 == 'Oak':
                    n = (datetime.strptime(row.date2, '%Y-%m-%d').date() - datetime.strptime(row.date1, '%Y-%m-%d').date())
                    datelist.append(datetime.strptime(row.date1, '%Y-%m-%d').date())
                    datelist.append(datetime.strptime(row.date2, '%Y-%m-%d').date())
                    if n.days >= 2:
                        for m in range(1, n.days):
                            nextday = datetime.strptime(row.date1, '%Y-%m-%d') + timedelta(days=m)
                            datelist.append(nextday)

            for row in datelist:
                if calen.get_date() == row or calen2.get_date() == row:
                    p = 1

        if site == 'Willow':
            for row in everythinglist:
                if row.site1 == 'Willow':
                    n = (datetime.strptime(row.date2, '%Y-%m-%d').date() - datetime.strptime(row.date1, '%Y-%m-%d').date())
                    datelist.append(datetime.strptime(row.date1, '%Y-%m-%d').date())
                    datelist.append(datetime.strptime(row.date2, '%Y-%m-%d').date())
                    if n.days >= 2:
                        for m in range(1, n.days):
                            nextday = datetime.strptime(row.date1, '%Y-%m-%d') + timedelta(days=m)
                            datelist.append(nextday)

            for row in datelist:
                if calen.get_date() == row or calen2.get_date() == row:
                    p = 1

        if p == 0:
            with open('orders.csv', mode='a') as data:
                data_writer = csv.writer(data, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
                data_writer.writerow([nameentry.get().lower(), calen.get_date(), calen2.get_date(), site,
                                      numberentry.get(), emailentry.get(), cardnumentry.get(), expireentry.get(),
                                      cardnameentry.get(), cvventry.get(), foodoption])

        elif p == 1:
            createerror()
            errorlabel = Label(error, text='Date Selected \nUnavailable For \nSelected Site', font=('courier', 15), bg='light blue')
            errorlabel.place(x=0, y=0)
            ok = Button(error, text='ok')
            ok.place(x=0, y=50)

        else:
            createerror()
            errorlabel = Label(error, text='Please Select \nA Date', font=('courier', 15),
                               bg='light blue')
            errorlabel.place(x=0, y=0)
            ok = Button(error, text='ok')
            ok.place(x=0, y=50)


def foodchange():
    global foodoption
    if foodoption:
        foodoption = False

    else:
        foodoption = True


# Searching Function
def search():
    global searchbox
    global searchlabel
    searchdates.clear()
    everythinglist.clear()
    i = 0
    o = 1
    for ii in labellist:
        ii.destroy()
    with open('orders.csv', 'rt')as f:
        data = csv.reader(f)
        for row in data:
            everythinglist.append(order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                        row[10]))
        for row in everythinglist:
            if searchvar.get() == 'Name' and o == 1:
                if searchbox.get().lower() == str(row.name):
                    searchlabel.configure(text=(row.name.upper(), row.date1, row.date2))
                    o = 0

                else:
                    searchlabel.configure(text='Not Found')

            if searchvar.get() == 'Date':
                searchdates.clear()
                searchlabel.configure(text='')
                n = (datetime.strptime(row.date2, '%Y-%m-%d').date() - datetime.strptime(row.date1, '%Y-%m-%d').date())
                searchdates.append(row.date1)
                if n.days >= 2:
                    for m in range(1, n.days):
                        nextday = datetime.strptime(row.date1, '%Y-%m-%d').date() + timedelta(days=m)
                        searchdates.append(str(nextday))
                searchdates.append(row.date2)

                for wor in searchdates:
                    if searchbox.get() == wor:
                        o = 0
                        i = i + 35
                        label = Label(tab5, font=('', 16), text=(row.name, row.date1, 'to', row.date2, row.site1),
                                      bg='light blue')
                        labellist.append(label)
                        label.place(x=250, y=150 + i)

                    elif o == 1:
                        searchlabel.configure(text='Not Found')

            if searchvar.get() == 'Month':
                searchlabel.configure(text='')
                searchdates.clear()
                searchdates.append(datetime.strptime(row.date1, '%Y-%m-%d').date())

                for wor in searchdates:
                    if searchbox.get() == str(wor.month):
                        o = 0
                        i = i + 35
                        label = Label(tab5, font=('', 16), text=(row.name, row.date1, row.date2), bg='light blue')
                        labellist.append(label)
                        label.place(x=250, y=150 + i)

                    elif o == 1:
                        for ii in labellist:
                            ii.destroy()
                        searchlabel.configure(text='Not Found')


def sitecheck():
    everythinglist.clear()
    kaurilist.clear()
    willowlist.clear()
    oaklist.clear()
    selecteddates.clear()
    with open('orders.csv', 'rt')as f:
        data = csv.reader(f)
        for row in data:
            everythinglist.append(order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                        row[10]))

        for row in everythinglist:
            if row.site1 == 'Kauri':
                n = (datetime.strptime(row.date2, '%Y-%m-%d').date() - datetime.strptime(row.date1, '%Y-%m-%d').date())
                kaurilist.append(datetime.strptime(row.date1, '%Y-%m-%d').date())
                kaurilist.append(datetime.strptime(row.date2, '%Y-%m-%d').date())
                if n.days >= 2:
                    for m in range(1, n.days):
                        nextday = datetime.strptime(row.date1, '%Y-%m-%d').date() + timedelta(days=m)
                        kaurilist.append(nextday)

            if row.site1 == 'Willow':
                n = (datetime.strptime(row.date2, '%Y-%m-%d').date() - datetime.strptime(row.date1, '%Y-%m-%d').date())
                willowlist.append(datetime.strptime(row.date1, '%Y-%m-%d').date())
                willowlist.append(datetime.strptime(row.date2, '%Y-%m-%d').date())
                if n.days >= 2:
                    for m in range(1, n.days):
                        nextday = datetime.strptime(row.date1, '%Y-%m-%d').date() + timedelta(days=m)
                        willowlist.append(nextday)

            if row.site1 == 'Oak':
                n = (datetime.strptime(row.date2, '%Y-%m-%d').date() - datetime.strptime(row.date1, '%Y-%m-%d').date())
                oaklist.append(datetime.strptime(row.date1, '%Y-%m-%d').date())
                oaklist.append(datetime.strptime(row.date2, '%Y-%m-%d').date())
                if n.days >= 2:
                    for m in range(1, n.days):
                        nextday = datetime.strptime(row.date1, '%Y-%m-%d').date() + timedelta(days=m)
                        oaklist.append(nextday)

        n = (calen2.get_date() - calen.get_date())
        selecteddates.append(calen.get_date())
        selecteddates.append(calen2.get_date())
        if n.days >= 2:
            for m in range(1, n.days):
                nextday = calen.get_date() + timedelta(days=m)
                selecteddates.append(nextday)

        for row in kaurilist:
            for wor in selecteddates:
                print(row)
                print(wor)
                if row == wor:
                    kauriselect.configure(bg='LightBlue4', state='disabled')

        for row in oaklist:
            for wor in selecteddates:
                print(row)
                print(wor)
                if row == wor:
                    oakselect.configure(bg='LightBlue4', state='disabled')

        for row in willowlist:
            for wor in selecteddates:
                print(row)
                print(wor)
                if row == wor:
                    willowselect.configure(bg='LightBlue4', state='disabled')



def kauricalendar():
    createcalendar()
    calendar.title('Kauri')
    cal = Calendar(calendar, maxdate=maximumdate, mindate=minimumdate, weekendbackground='Green2',
                   weekendforeground='Black', normalbackground='Green2')
    with open('orders.csv', 'rt')as f:
        data = csv.reader(f)
        for row in data:
            everythinglist.append(order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                        row[10]))
        for row in everythinglist:
            if row.site1 == 'Kauri':
                n = (datetime.strptime(row.date2, '%Y-%m-%d').date() - datetime.strptime(row.date1, '%Y-%m-%d').date())
                kaurilist.append(datetime.strptime(row.date1, '%Y-%m-%d').date())
                kaurilist.append(datetime.strptime(row.date2, '%Y-%m-%d').date())
                if n.days >= 2:
                    for m in range(1, n.days):
                        nextday = datetime.strptime(row.date1, '%Y-%m-%d').date() + timedelta(days=m)
                        kaurilist.append(nextday)

        for row in kaurilist:
            cal.calevent_create(row, 'Booked', 'days')
            cal.tag_config('days', background='red')

        samedate.clear()
        selecteddates.clear()
        selecteddates.append(calen.get_date())
        selecteddates.append(calen2.get_date())
        w = calen2.get_date() - calen.get_date()
        if w.days >= 2:
            for m in range(1, w.days):
                nextday = calen.get_date() + timedelta(days=m)
                selecteddates.append(nextday)

        for row in selecteddates:
            cal.calevent_create(row, 'Selected', 'Selected')
            cal.tag_config('Selected', background='Blue')

        for row in selecteddates:
            for wor in kaurilist:
                if row == wor:
                    samedate.append(row)

        for row in samedate:
            cal.calevent_create(row, 'Overlapping Dates', 'Same')
            cal.tag_config('Same', background='Dark Orange')

    cal.place(x=0, y=0)


def willowcalendar():
    createcalendar()
    calendar.title('Willow')
    cal = Calendar(calendar, maxdate=maximumdate, mindate=minimumdate, weekendbackground='Green2',
                   weekendforeground='Black', normalbackground='Green2')
    with open('orders.csv', 'rt')as f:
        data = csv.reader(f)
        for row in data:
            everythinglist.append(order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                        row[10]))
        for row in everythinglist:
            if row.site1 == 'Willow':
                n = (datetime.strptime(row.date2, '%Y-%m-%d').date() - datetime.strptime(row.date1, '%Y-%m-%d').date())
                willowlist.append(datetime.strptime(row.date1, '%Y-%m-%d').date())
                willowlist.append(datetime.strptime(row.date2, '%Y-%m-%d').date())
                if n.days >= 2:
                    for m in range(1, n.days):
                        nextday = datetime.strptime(row.date1, '%Y-%m-%d').date() + timedelta(days=m)
                        willowlist.append(nextday)

        for row in willowlist:
            cal.calevent_create(row, 'Booked', 'days')
            cal.tag_config('days', background='red')

        samedate.clear()
        selecteddates.clear()
        selecteddates.append(calen.get_date())
        selecteddates.append(calen2.get_date())
        w = calen2.get_date() - calen.get_date()
        if w.days >= 2:
            for m in range(1, w.days):
                nextday = calen.get_date() + timedelta(days=m)
                selecteddates.append(nextday)

        for row in selecteddates:
            cal.calevent_create(row, 'Selected', 'Selected')
            cal.tag_config('Selected', background='Blue')

        for row in selecteddates:
            for wor in willowlist:
                if row == wor:
                    samedate.append(row)

        for row in samedate:
            cal.calevent_create(row, 'Overlapping Dates', 'Same')
            cal.tag_config('Same', background='Dark Orange')

    cal.place(x=0, y=0)


def oakcalendar():
    createcalendar()
    calendar.title('Oak')
    cal = Calendar(calendar, maxdate=maximumdate, mindate=minimumdate, weekendbackground='Green2',
                   weekendforeground='Black', normalbackground='Green2')
    with open('orders.csv', 'rt')as f:
        data = csv.reader(f)
        for row in data:
            everythinglist.append(order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                        row[10]))
        for row in everythinglist:
            if row.site1 == 'Oak':
                n = (datetime.strptime(row.date2, '%Y-%m-%d').date() - datetime.strptime(row.date1, '%Y-%m-%d').date())
                oaklist.append(datetime.strptime(row.date1, '%Y-%m-%d').date())
                oaklist.append(datetime.strptime(row.date2, '%Y-%m-%d').date())
                if n.days >= 2:
                    for m in range(1, n.days):
                        nextday = datetime.strptime(row.date1, '%Y-%m-%d').date() + timedelta(days=m)
                        oaklist.append(nextday)

        for row in oaklist:
            cal.calevent_create(row, 'Booked', 'days')
            cal.tag_config('days', background='red')

        samedate.clear()
        selecteddates.clear()
        selecteddates.append(calen.get_date())
        selecteddates.append(calen2.get_date())
        w = calen2.get_date() - calen.get_date()
        if w.days >= 2:
            for m in range(1, w.days):
                nextday = calen.get_date() + timedelta(days=m)
                selecteddates.append(nextday)

        for row in selecteddates:
            cal.calevent_create(row, 'Selected', 'Selected')
            cal.tag_config('Selected', background='Blue')

        for row in selecteddates:
            for wor in oaklist:
                if row == wor:
                    samedate.append(row)

        for row in samedate:
            cal.calevent_create(row, 'Overlapping Dates', 'Same')
            cal.tag_config('Same', background='Dark Orange')

    cal.place(x=0, y=0)


# Tab Changing functions
def tab1change():
    tabControl.hide(tab2)
    tabControl.hide(tab5)
    tabControl.select(tab1)


def tab2change():
    tabControl.hide(tab1)
    tabControl.hide(tab3)
    tabControl.select(tab2)


def tab3change():
    sitecheck()
    tabControl.hide(tab2)
    tabControl.hide(tab4)
    tabControl.select(tab3)


def tab4change():

    tabControl.hide(tab3)
    tabControl.hide(tab5)
    tabControl.select(tab4)


def tab5change():

    tabControl.hide(tab1)
    tabControl.select(tab5)


# ============================================== Calendar Tab ==========================================================

def calenchange(event):
    if (calen2.get_date() - calen.get_date()).days <= 0:
        calen2.set_date(calen.get_date())


def calen2change(event):
    if (calen2.get_date() - calen.get_date()).days <= 0:
        calen.set_date(calen2.get_date())


calendar = Label(tab1, text='Dates', font=('Courier', 20, 'bold'), bg='Light Blue', fg='black')
calendar.place(x=450, y=150)

to = Label(tab1, text='To:', font='Courier', bg='Light Blue', fg='black')
to.place(x=475, y=196)

calen = DateEntry(tab1, dateformat=3, font=('Courier', 12), width=12, background='Dodger Blue', foreground='Black',
                  borderwidth=4, Calendar=2020)
calen.place(x=325, y=200)
calen.bind('<<DateEntrySelected>>', calenchange)

calen2 = DateEntry(tab1, dateformat=3, font=('Courier', 12), width=12, background='Dodger Blue', foreground='Black',
                   borderwidth=4, Calendar=2020)
calen2.place(x=525, y=200)
calen2.bind('<<DateEntrySelected>>', calen2change)

calnext = Button(tab1, text='Next', font=('Courier', 15), command=tab2change, bg='Dodger Blue', fg='Black', width=15)
calnext.place(x=750, y=400)

searchb = Button(tab1, text='Search', font=('Courier', 15), command=tab5change, bg='Dodger Blue', fg='Black', width=15)
searchb.place(x=750, y=350)

calentest = DateEntry(tab1, dateformat=3, font=('Courier', 12), width=12, background='Dodger Blue', foreground='Black',
                      borderwidth=4, Calendar=2020)

todaydate = Label(tab1, font=('Courier', 16), text="Today's Date: " + str(calentest.get_date()), bg='light blue')
todaydate.place(x=650, y=50)


# ==================================================== Details Tab ========================================================

space = 10


def FN_on_nameentry_click(event):  # removes instruction text if the entry is clicked
    if nameentry.cget('fg') == 'grey':
        nameentry.delete(0, "end")  # delete all the text in the entry
        nameentry.insert(0, '')  # Insert blank for user input
        nameentry.config(fg='black')


def FN_on_name_focusout(event):  # restores the instruction text if the user shifts their focus
    if nameentry.get() == '':
        nameentry.insert(0, 'Full Name')
        nameentry.config(fg='grey')


def FN_on_numberentry_click(event):  # removes instruction text if the entry is clicked
    if numberentry.cget('fg') == 'grey':
        numberentry.delete(0, "end")  # delete all the text in the entry
        numberentry.insert(0, '')  # Insert blank for user input
        numberentry.config(fg='black')


def FN_on_number_focusout(event):  # restores the instruction text if the user shifts their focus
    if numberentry.get() == '':
        numberentry.insert(0, 'Phone Number')
        numberentry.config(fg='grey')


def FN_on_emailentry_click(event):  # removes instruction text if the entry is clicked
    if emailentry.cget('fg') == 'grey':
        emailentry.delete(0, "end")  # delete all the text in the entry
        emailentry.insert(0, '')  # Insert blank for user input
        emailentry.config(fg='black')


def FN_on_email_focusout(event):  # restores the instruction text if the user shifts their focus
    if emailentry.get() == '':
        emailentry.insert(0, 'Email')
        emailentry.config(fg='grey')


def FN_on_cardnumentry_click(event):  # removes instruction text if the entry is clicked
    if cardnumentry.cget('fg') == 'grey':
        cardnumentry.delete(0, "end")  # delete all the text in the entry
        cardnumentry.insert(0, '')  # Insert blank for user input
        cardnumentry.config(fg='black')


def FN_on_cardnum_focusout(event):  # restores the instruction text if the user shifts their focus
    if cardnumentry.get() == '':
        cardnumentry.insert(0, 'Card Number')
        cardnumentry.config(fg='grey')


def FN_on_expireentry_click(event):  # removes instruction text if the entry is clicked
    if expireentry.cget('fg') == 'grey':
        expireentry.delete(0, "end")  # delete all the text in the entry
        expireentry.insert(0, '')  # Insert blank for user input
        expireentry.config(fg='black')


def FN_on_expire_focusout(event):  # restores the instruction text if the user shifts their focus
    if expireentry.get() == '':
        expireentry.insert(0, 'Expire Date')
        expireentry.config(fg='grey')


def FN_on_cardnameentry_click(event):  # removes instruction text if the entry is clicked
    if cardnameentry.cget('fg') == 'grey':
        cardnameentry.delete(0, "end")  # delete all the text in the entry
        cardnameentry.insert(0, '')  # Insert blank for user input
        cardnameentry.config(fg='black')


def FN_on_cardname_focusout(event):  # restores the instruction text if the user shifts their focus
    if cardnameentry.get() == '':
        cardnameentry.insert(0, 'Name On Card')
        cardnameentry.config(fg='grey')


def FN_on_cvventry_click(event):  # removes instruction text if the entry is clicked
    if cvventry.cget('fg') == 'grey':
        cvventry.delete(0, "end")  # delete all the text in the entry
        cvventry.insert(0, '')  # Insert blank for user input
        cvventry.config(fg='black')


def FN_on_cvv_focusout(event):  # restores the instruction text if the user shifts their focus
    if cvventry.get() == '':
        cvventry.insert(0, 'CVV')
        cvventry.config(fg='grey')


nameentry = Entry(tab4, width=20, font=('Courier', 15))
nameentry.insert(0, 'Full Name')
nameentry.place(x=50, y=space*5)
nameentry.bind('<FocusIn>', FN_on_nameentry_click)
nameentry.bind('<FocusOut>', FN_on_name_focusout)
nameentry.config(fg='grey')


numberentry = Entry(tab4, width=20, font=('Courier', 15))
numberentry.insert(0, 'Phone Number')
numberentry.place(x=50, y=space*8.5)
numberentry.bind('<FocusIn>', FN_on_numberentry_click)
numberentry.bind('<FocusOut>', FN_on_number_focusout)
numberentry.config(fg='grey')

emailentry = Entry(tab4, width=20, font=('Courier', 15))
emailentry.insert(0, 'Email')
emailentry.place(x=50, y=space*12)
emailentry.bind('<FocusIn>', FN_on_emailentry_click)
emailentry.bind('<FocusOut>', FN_on_email_focusout)
emailentry.config(fg='grey')

cardnumentry = Entry(tab4, width=20, font=('Courier', 15))
cardnumentry.insert(0, 'Card Number')
cardnumentry.place(x=500, y=space*5)
cardnumentry.bind('<FocusIn>', FN_on_cardnumentry_click)
cardnumentry.bind('<FocusOut>', FN_on_cardnum_focusout)
cardnumentry.config(fg='grey')

expireentry = Entry(tab4, width=20, font=('Courier', 15))
expireentry.insert(0, 'Expire Date')
expireentry.place(x=500, y=space*8.5)
expireentry.bind('<FocusIn>', FN_on_expireentry_click)
expireentry.bind('<FocusOut>', FN_on_expire_focusout)
expireentry.config(fg='grey')

cardnameentry = Entry(tab4, width=20, font=('Courier', 15))
cardnameentry.insert(0, 'Name On Card')
cardnameentry.place(x=500, y=space*12)
cardnameentry.bind('<FocusIn>', FN_on_cardnameentry_click)
cardnameentry.bind('<FocusOut>', FN_on_cardname_focusout)
cardnameentry.config(fg='grey')

cvventry = Entry(tab4, width=20, font=('Courier', 15))
cvventry.insert(0, 'CCV')
cvventry.place(x=500, y=space*15.5)
cvventry.bind('<FocusIn>', FN_on_cvventry_click)
cvventry.bind('<FocusOut>', FN_on_cvv_focusout)
cvventry.config(fg='grey')

foodcheck = Checkbutton(tab4, text='Food Option', font=('Courier', 15), command=foodchange, bg='Light Blue')
foodcheck.place(x=50, y=200)

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
    if willowselect.cget('bg') != 'LightBlue4':
        willowselect.configure(bg='Dodger Blue')
    if kauriselect.cget('bg') != 'LightBlue4':
        kauriselect.configure(bg='Dodger Blue')
    oakselect.configure(bg='Medium Blue')


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
    if oakselect.cget('bg') != 'LightBlue4':
        oakselect.configure(bg='Dodger Blue')
    if kauriselect.cget('bg') != 'LightBlue4':
        kauriselect.configure(bg='Dodger Blue')
    willowselect.configure(bg='medium Blue')


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
    if willowselect.cget('bg') != 'LightBlue4':
        willowselect.configure(bg='Dodger Blue')
    if oakselect.cget('bg') != 'LightBlue4':
        oakselect.configure(bg='Dodger Blue')
    kauriselect.configure(bg='medium Blue')


oakselect = Button(tab3, text='The Oak', font=('Courier', 15), bg='Dodger Blue', command=oakfun, activebackground='Dodger Blue',
                   width=10, height=3)
oakselect.place(x=116, y=50)
kauricheck = Button(tab3, text='See Available \nTimes', font=('Courier', 10), bg='Dark Orange', command=oakcalendar, activebackground='Dark Orange',
                    width=20, height=3)
kauricheck.place(x=116, y=300)

willowselect = Button(tab3, text='The Willow', font=('Courier', 15), bg='Dodger Blue', command=willowfun, activebackground='Dodger Blue',
                      width=10, height=3)
willowselect.place(x=425, y=50)
kauricheck = Button(tab3, text='See Available \nTimes', font=('Courier', 10), bg='Dark Orange', command=willowcalendar, activebackground='Dark Orange',
                    width=20, height=3)
kauricheck.place(x=425, y=300)

kauriselect = Button(tab3, text='The Kauri', font=('Courier', 15), bg='Dodger Blue', command=kaurifun, activebackground='Dodger Blue',
                     width=10, height=3)
kauriselect.place(x=750, y=50)
kauricheck = Button(tab3, text='See Available \nTimes', font=('Courier', 10), bg='Dark Orange', command=kauricalendar, activebackground='Dark Orange',
                    width=20, height=3)
kauricheck.place(x=750, y=300)

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
searchbox.place(x=200, y=100)

searchbutton = Button(tab5, text='Search', font=('Courier', 10), command=search, bg='Dodger Blue', fg='Black', width=15)
searchbutton.place(x=450, y=100)

searchlabel = Label(tab5, text='', font=('Courier', 20), bg='light blue')
searchlabel.place(x=250, y=200)

searchvar = StringVar(tab5)
searchvar.set('Name')

searchselect = OptionMenu(tab5, searchvar, 'Name', 'Month', 'Date')
searchselect.place(x=600, y=100)

back = Button(tab5, text='Back', font=('Courier', 15), command=tab1change, bg='Dodger Blue', fg='Black', width=15)
back.place(x=50, y=30)

# Running Mainlooop
root.mainloop()
