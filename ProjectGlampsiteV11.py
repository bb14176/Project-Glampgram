# Importing all the libraries I used
from tkinter import *
from tkinter import ttk
from tkcalendar import *
import csv
from datetime import *


# Window dimensions
root = Tk()  # initialising Tkinter
root.title('Booking4you')  # Changing the name
root.geometry('1000x500+50+50')  # Chinging the size and where it appers on the screen
root.resizable(False, False)  # Making the window not resizeable


# Error Window
def createerror():  # Function for creating a error popup
    global error
    error = Tk()  # Initialising the error window
    error.geometry('185x150')  # Changing the size
    error.resizable(False, False)  # Making the window not resizeable
    error.title('Error')  # Changing the name
    errorcanvas = Canvas(error, bg='Light Blue', width=1000, height=500)  # Putting a canvas on the window
    errorcanvas.place(x=-10, y=-10)  # placing the canvas


def createcalendar():  # Function for the calendar popups
    global calendartab
    calendartab = Tk()  # Initialising the calendar window
    calendartab.geometry('251x186')  # Changing the size
    calendartab.resizable(False, False)  # Making the window not resizeable
    calendartab.title('')  # Changing the title
    errorcanvas = Canvas(calendartab, bg='Light Blue', width=1000, height=500)  # putting a canvas on the window
    errorcanvas.place(x=0, y=0)  # placing the canvas


oaklist = []  # A list for dates in the oak site
kaurilist = []  # A list for dates in the kauri site
willowlist = []  # A list for dates in the willow site
selecteddates = []  # A list for dates selected
samedate = []  # A list for dates that were selected and already booked
feildnames = ['name', 'date1', 'date2', 'site1', 'number', 'email', 'cardnumber', 'expirey', 'cardname', 'cvv', 'food']  # Fieldnames for the csv function


# Tab control
tabControl = ttk.Notebook(root)  # Initialising a notebook system

tab1 = ttk.Frame(tabControl)  # Creating tab 1
tabControl.add(tab1, text="Calendar")  # adding the tab to the notbook and nameing it
tabControl.pack(expand=1, fill="both")  # placeing the tab on the notbook

tab3 = ttk.Frame(tabControl)  # Creating tab 3 becuase tab 2 was not needed anymore
tabControl.add(tab3, text="Site", state='hidden')  # adding the tab to the notbook, nameing it and making it hidden
tabControl.pack(expand=1, fill="both")  # placeing the tab on the notbook

tab4 = ttk.Frame(tabControl)  # Creating tab 4
tabControl.add(tab4, text="Details", state='hidden')  # adding the tab to the notbook, nameing it and making it hidden
tabControl.pack(expand=1, fill="both")  # placeing the tab on the notbook
tab4canvas = Canvas(tab4, bg='#F1A0D1', width=1000, height=500)  # Making a canvas for the tab to change the colour
tab4canvas.place(x=0, y=0)  # Placing the canvas

tab5 = ttk.Frame(tabControl)  # Creating tab 5
tabControl.add(tab5, text="Search", state='hidden')  # adding the tab to the notbook, nameing it and making it hidden
tabControl.pack(expand=1, fill="both")  # placeing the tab on the notbook

tab1canvas = Canvas(tab1, bg='#F1A0D1', width=1000, height=500)  # Making a canvas for the tab to change the colour
tab1canvas.place(x=0, y=0)  # Placing the canvas

tab3canvas = Canvas(tab3, bg='#F1A0D1', width=1000, height=500)  # Making a canvas for the tab to change the colour
tab3canvas.place(x=0, y=0)  # Placing the canvas

tab5canvas = Canvas(tab5, bg='#F1A0D1', width=1000, height=500)  # Making a canvas for the tab to change the colour
tab5canvas.place(x=0, y=0)  # Placing the canvas


# Tab Changing functions
def tab1change():  # Tab 1 select function
    tabControl.hide(tab3)  # Hiding the previous tab
    tabControl.hide(tab5)  # Hiding the previous tab
    tabControl.select(tab1)  # Selecting the tab


def tab3change():  # Tab 3 select function
    sitecheck()  # Site check funtion, see line 337
    tabControl.hide(tab1)
    tabControl.hide(tab4)
    tabControl.select(tab3)  # Selecting the tab


def tab4change():  # Tab 4 select function
    tabControl.hide(tab3)
    tabControl.hide(tab5)
    pricecheck()  # Price check function, see line 219
    tabControl.select(tab4)  # Selecting the tab


def tab5change():  # Tab 5 select function
    tabControl.hide(tab1)
    tabControl.select(tab5)  # Selecting the tab


# Site Tab Variables
oakselected = False  # If oak site is selected
willowselected = False  # If willow site is selected
kauriselected = False  # If kauri site is selected
site = 'Not Chosen'  # Making the site not chosen, used for an error prevention

# Random Variables
foodoption = False  # Initialising the food option as false
everythinglist = []  # A list for all the orders in the csv file
minimumdate = datetime.strptime('2020-01-01', '%Y-%m-%d').date()  # Setting the minimum date for the calendars
maximumdate = datetime.strptime('2022-01-01', '%Y-%m-%d').date()  # Setting the maximum date for the calendars
searchdates = []  # A list of dates used in the search function
labellist = []  # A list of labels to display multuple orders at once
price = 0  # The price the person has to pay for the site
firstclick = False  # Checking if the calendar has been ckicked once
firstdate = minimumdate  # Initialising the first date variable
seconddate = minimumdate  # Initialising the second date variable


# order class
class order(object):  # Class for my orders
    def __init__(self, name, date1, date2, site1, number, email, cardnumber, expirey, cardname, ccv, food):  # Initialising the variables
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
        self.cardnumber = cardnumber  # All above is naming the variables


# writing Function
def writeb1():  # The function for writing to the CSV file
    global nameentry
    global numberentry
    global cardnumentry
    global emailentry
    global expireentry
    global cardnameentry
    global cvventry
    global firstdate
    global seconddate

    errorcode = 0  # Setting error code to 0
    with open('orders.csv', 'rt')as f:  # Opening the file with intention read
        data = csv.reader(f)  # getting the data from the file
        everythinglist.clear()  # clearing everything in the list
        for row in data:
            everythinglist.append(order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                        row[10]))  # making a new object for every order in the CSV file and adding it to a list

        if nameentry.cget('fg') == 'grey':  # All if X == 'grey' is checking if the user has filled out the information
            errorcode = 1  # Error code 1 will make a window aksing to fill everything out

        if numberentry.cget('fg') == 'grey':
            errorcode = 1

        if cardnumentry.cget('fg') == 'grey':
            errorcode = 1

        if emailentry.cget('fg') == 'grey':
            errorcode = 1

        if expireentry.cget('fg') == 'grey':
            errorcode = 1

        if cardnameentry.cget('fg') == 'grey':
            errorcode = 1

        if cvventry.cget('fg') == 'grey':
            errorcode = 1

        if site == 'Not Chosen':  # If the user has not selected a site
            errorcode = 2  # error code 2 will make a window saying to choose a site

        if firstdate == seconddate:  # if the user has not selected a date
            errorcode = 3  # Will make window saying to choose a date

        if errorcode == 0:
            with open('orders.csv', mode='a') as data:  # opening the CSV file with intention append
                data_writer = csv.DictWriter(data, fieldnames=feildnames, lineterminator='\n')  # setting feildnames and line terminatiors for the writing function
                data_writer.writerow({'name': nameentry.get().lower(), 'date1': firstdate, 'date2': seconddate, 'site1': site,
                                      'number': numberentry.get(), 'email': emailentry.get(), 'cardnumber': cardnumentry.get(), 'expirey': expireentry.get(),
                                      'cardname': cardnameentry.get(), 'cvv': cvventry.get(), 'food': foodoption})  # appending all the values of the order onto a new line

        if errorcode == 1:
            createerror()  # Creating the error window
            errorlabel = Label(error, font=('Courier', 15), text='Please make \nsure everything \nis filled out', bg='light blue')  # Making a label stating the error
            errorlabel.place(x=0, y=5)  # placing the label
            ok = Button(error, font=('Courier', 10, 'bold'), text='OK', command=error.destroy, width=10, height=2, bg='Dodger blue',
                        activebackground='dodger blue')  # making a button to remove the popup
            ok.place(x=40, y=90)  # placing the button

        if errorcode == 2:
            createerror()
            errorlabel = Label(error, font=('Courier', 15), text='Plese Select \nA Site', bg='Light Blue')  # Making a label stating the error
            errorlabel.place(x=17, y=5)  # placing the label
            ok = Button(error, font=('Courier', 10, 'bold'), text='OK', command=error.destroy, width=10, height=2, bg='Dodger blue',
                        activebackground='dodger blue')  # making a button to remove the popup
            ok.place(x=40, y=90)  # placing the button

        if errorcode == 3:
            createerror()
            errorlabel = Label(error, font=('Courier', 15), text='Plese Select \nA Vadlid \nDate', bg='Light Blue')  # Making a label stating the error
            errorlabel.place(x=17, y=5)  # placing the label
            ok = Button(error, font=('Courier', 10, 'bold'), text='OK', command=error.destroy, width=10, height=2, bg='Dodger blue',
                        activebackground='dodger blue')  # making a button to remove the popup
            ok.place(x=40, y=90)  # placing the button


def pricecheck():  # Function for calculating the price of the stay
    global multuply
    global firstdate
    global seconddate
    global price
    multuply = (seconddate - firstdate).days  # value for mutyplying the price of the stay
    if site == 'Oak':
        if foodoption:  # if the food option is on
            price = 85  # changing the price

        else:
            price = 65  # changing the price

    if site == 'Willow':
        if foodoption:  # if the food option is on
            price = 70  # changing the price

        else:
            price = 55  # changing the price

    if site == 'Kauri':
        if foodoption:  # if the food option is on
            price = 110  # changing the price

        else:
            price = 95  # changing the price

    pricelabel.config(text='Price: $' + str(price*multuply))  # making the label diplay the correct price


def foodchange():  # Fuction for the food checkbox
    global foodoption
    if foodoption:  # if the food option is true
        foodoption = False  # Change it to false
        pricecheck()  # Check the price of the stay

    else:  # if the food option is false
        foodoption = True  # change it to true
        pricecheck()  # check the price


def search():  # Funtion for the search button
    global searchbox
    global searchlabel
    searchdates.clear()  # clearing all values in list
    everythinglist.clear()  # clearing all values in list
    i = 0  # label offset
    iii = 0  # loop stopper
    ll = 0  # label offset
    o = 1  # looping variable
    for ii in labellist:
        ii.destroy()  # destroying all labels in the list
    with open('orders.csv', 'rt')as f:
        data = csv.reader(f)
        for row in data:
            everythinglist.append(order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                        row[10]))
        for row in everythinglist:
            if searchvar.get() == 'Name' and o == 1:  # if the name option is selectedd and looping stopper
                if searchbox.get().lower() == str(row.name):  # if searchbox == anything in the CSV file
                    searchlabel.configure(text=row.name.upper() + ' | ' + row.date1 + ' | ' + row.date2 +
                                          ' | ' + row.site1 + '\n' + row.number + ' | ' + row.email + '\n' + row.cardnumber
                                          + ' | ' + row.expirey + ' | ' + row.cardname + ' | ' + row.ccv
                                          + '\nFood: ' + row.food)  # Displaying all values of the order
                    o = 0  # looping stopper

                else:  # if nothing is found
                    searchlabel.configure(text='Not Found')  # Display "Not Found"

            if searchvar.get() == 'Date':  # if date option is selected
                searchdates.clear()  # clearing all values in list
                searchlabel.configure(text='')  # configuring the sechlabel to say nothing
                n = (datetime.strptime(row.date2, '%Y-%m-%d').date() - datetime.strptime(row.date1, '%Y-%m-%d').date())  # a value for the amount of days a person has booked a campsite see line 620 for more information
                searchdates.append(row.date1)  # appending the first date to the list
                if n.days >= 2:  # if the person is staying for more than two days
                    for m in range(1, n.days):
                        nextday = datetime.strptime(row.date1, '%Y-%m-%d').date() + timedelta(days=m)  # making a value for the date inbetween first and last
                        searchdates.append(str(nextday))  # appending the date to the list as a string
                searchdates.append(row.date2)  # appending the last date to the list

                for wor in searchdates:
                    if searchbox.get() == wor:  # if the searchbox is == to any date in the list
                        o = 0  # loop stopper
                        i = i + 35  # offsetting the new label by 35 pixels
                        label = Label(tab5, font=('', 16), text=(row.name + ' | ' + row.date1 + ' | ' + row.date2 + ' | ' + row.site1),
                                      bg='#F1A0D1')  # creating a new label showing some values of an order
                        labellist.append(label)  # appending the label to a list to be destoryed later if needed
                        label.place(x=250, y=150 + i)  # placing the label on the screen with the offset

                    elif o == 1:  # if the loop stopper has not been changed
                        searchlabel.configure(text='Not Found')  # Displaying "Not Found"

            if searchvar.get() == 'Month':  # if the month option is selected
                searchlabel.configure(text='')  # making the search label say nothing
                searchdates.clear()  # Clearing all values in the list
                searchdates.append(datetime.strptime(row.date1, '%Y-%m-%d').date())  # appending the first date to a list
                iii = iii + 1  # loop stopper

                for wor in searchdates:
                    if searchbox.get() == str(wor.month):  # if the searchbox is == the month of the date
                        o = 0  # Looping stopper
                        i = i + 35  # off setting  the label by 35 pixels
                        label = Label(tab5, font=('', 16), text=(row.name + ' | ' + row.date1 + ' | ' + row.date2 + ' | ' + row.site1), bg='#F1A0D1')  # making a label displaying the values of some orders
                        labellist.append(label)  # appending the label to a list to be destoryed later if needed
                        label.place(x=30 + ll, y=150 + i)  # placing the label with all the offsets in place
                        for ii in range(0, iii):
                            if ii == 5:  # if there are 5 labels on a line
                                ll = 500  # offset the label by 500 pixels
                                i = 0  # putting the labels at the top

                    elif o == 1:  # if the loop stopper has not been changed
                        for ii in labellist:
                            ii.destroy()  # destroying all the labels
                        searchlabel.configure(text='Not Found')  # makingthe label say "Not Found"


def sitecheck():  # function to check if site is available for selected date
    global site
    global firstdate
    global seconddate
    global willownot
    global kaurinot
    global oaknot
    everythinglist.clear()  # clearing everything list
    kaurilist.clear()  # clearing the kauri list
    willowlist.clear()  # clearing the willow list
    oaklist.clear()  # clearing the oak list
    selecteddates.clear()  # clearing the list
    kauriselect.configure(bg='dodger blue', state='normal')  # setting all the buttons to normal state
    oakselect.configure(bg='dodger blue', state='normal')
    willowselect.configure(bg='dodger blue', state='normal')
    oaknot.configure(text='')  # making all unavailable labels to say nothing
    kaurinot.configure(text='')
    willownot.configure(text='')
    with open('orders.csv', 'rt')as f:
        data = csv.reader(f)
        for row in data:
            everythinglist.append(order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                        row[10]))

        for row in everythinglist:
            if row.site1 == 'Kauri':  # if the order is for the kauri site
                n = (datetime.strptime(row.date2, '%Y-%m-%d').date() - datetime.strptime(row.date1, '%Y-%m-%d').date())  # Appending all the dates linked to the kauri site
                kaurilist.append(datetime.strptime(row.date1, '%Y-%m-%d').date())
                kaurilist.append(datetime.strptime(row.date2, '%Y-%m-%d').date())
                if n.days >= 2:
                    for m in range(1, n.days):
                        nextday = datetime.strptime(row.date1, '%Y-%m-%d').date() + timedelta(days=m)
                        kaurilist.append(nextday)

            if row.site1 == 'Willow':
                n = (datetime.strptime(row.date2, '%Y-%m-%d').date() - datetime.strptime(row.date1, '%Y-%m-%d').date())  # Appending all the dates linked to the willow site
                willowlist.append(datetime.strptime(row.date1, '%Y-%m-%d').date())
                willowlist.append(datetime.strptime(row.date2, '%Y-%m-%d').date())
                if n.days >= 2:
                    for m in range(1, n.days):
                        nextday = datetime.strptime(row.date1, '%Y-%m-%d').date() + timedelta(days=m)
                        willowlist.append(nextday)

            if row.site1 == 'Oak':
                n = (datetime.strptime(row.date2, '%Y-%m-%d').date() - datetime.strptime(row.date1, '%Y-%m-%d').date())  # Appending all the dates linked to the Oak site
                oaklist.append(datetime.strptime(row.date1, '%Y-%m-%d').date())
                oaklist.append(datetime.strptime(row.date2, '%Y-%m-%d').date())
                if n.days >= 2:
                    for m in range(1, n.days):
                        nextday = datetime.strptime(row.date1, '%Y-%m-%d').date() + timedelta(days=m)
                        oaklist.append(nextday)

        n = (seconddate - firstdate)  # appending all the dates selected to a
        selecteddates.append(firstdate)
        selecteddates.append(seconddate)
        if n.days >= 2:
            for m in range(1, n.days):
                nextday = firstdate + timedelta(days=m)
                selecteddates.append(nextday)

        for row in kaurilist:
            for wor in selecteddates:
                if row == wor:  # If the dates are the same
                    kauriselect.configure(bg='orangered', state='disabled')  # disabling the kauri button
                    if site == 'Kauri':
                        site = 'Not Chosen'  # Changing the site to not chosen if the button becomes unavailable during the order

                    kaurinot.config(text='Unavailable')  # makes a label saying Unavailable
                    kaurinot.place(x=755, y=20)  # places the label

        for row in oaklist:
            for wor in selecteddates:
                if row == wor:
                    oakselect.configure(bg='orangered', state='disabled')  # disabling the oak button
                    if site == 'Oak':
                        site = 'Not Chosen'  # Changing the site to not chosen if the button becomes unavailable during the order

                    oaknot.config(text='Unavailable')  # makes a label saying Unavailable
                    oaknot.place(x=121, y=20)  # places the label

        for row in willowlist:
            for wor in selecteddates:
                if row == wor:
                    willowselect.configure(bg='orangered', state='disabled')  # disabling the oak button
                    if site == 'Willow':
                        site = 'Not Chosen'  # Changing the site to not chosen if the button becomes unavailable during the order

                    willownot.config(text='Unavailable')  # makes a label saying Unavailable
                    willownot.place(x=430, y=20)  # places the label


def kauricalendar():
    global firstdate
    global seconddate
    createcalendar()  # makes a window for the  calendar
    calendartab.title('Kauri')  # titles the window
    cal = Calendar(calendartab, selectbackground='green2', selectforeground='black', maxdate=maximumdate,
                   mindate=minimumdate, weekendbackground='Green2', weekendforeground='Black', normalbackground='Green2',
                   selectmode='none')  # Makes a calendar
    with open('orders.csv', 'rt')as f:
        data = csv.reader(f)
        for row in data:
            everythinglist.append(order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                        row[10]))
        for row in everythinglist:
            if row.site1 == 'Kauri':  # if the order is for kauri
                n = (datetime.strptime(row.date2, '%Y-%m-%d').date() - datetime.strptime(row.date1, '%Y-%m-%d').date())  # All below is making a list of all dates in the kauri site
                kaurilist.append(datetime.strptime(row.date1, '%Y-%m-%d').date())
                kaurilist.append(datetime.strptime(row.date2, '%Y-%m-%d').date())
                if n.days >= 2:
                    for m in range(1, n.days):
                        nextday = datetime.strptime(row.date1, '%Y-%m-%d').date() + timedelta(days=m)
                        kaurilist.append(nextday)

        for row in kaurilist:
            cal.calevent_create(row, 'Booked', 'days')  # Creating an event in calendar for date (row), name (booked) and tag (days)
            cal.tag_config('days', background='red')  # making all events with tag, days, red

        samedate.clear()  # Clearing list
        selecteddates.clear()  # clearing list
        selecteddates.append(firstdate)  # Appending the first selected date to the list
        selecteddates.append(seconddate)  # Appending the last selected date to the list
        w = seconddate - firstdate  # All below is appending everything inbetween
        if w.days >= 2:
            for m in range(1, w.days):
                nextday = firstdate + timedelta(days=m)
                selecteddates.append(nextday)

        for row in selecteddates:  # Looking through the new list
            cal.calevent_create(row, 'Selected', 'Selected')  # Creating events for the new list
            cal.tag_config('Selected', background='Blue')  # Makeing the events blue

        for row in selecteddates:
            for wor in kaurilist:
                if row == wor:  # If the selected dates match an ordered date
                    samedate.append(row)  # appending the date to a list

        for row in samedate:  # looking therough the new list
            cal.calevent_create(row, 'Overlapping Dates', 'Same')  # Creating events for the overlapping dates
            cal.tag_config('Same', background='Dark Orange')  # Makeing them orange

    cal.place(x=0, y=0)  # Placeing the new calendar onto the popup


def willowcalendar():
    global firstdate
    global seconddate
    createcalendar()  # makes a window for the  calendar
    calendartab.title('Willow')  # titles the window
    cal = Calendar(calendartab, selectbackground='green2', selectforeground='black', maxdate=maximumdate,
                   mindate=minimumdate, weekendbackground='Green2', weekendforeground='Black', normalbackground='Green2',
                   selectmode='none')  # Makes a calendar
    with open('orders.csv', 'rt')as f:
        data = csv.reader(f)
        for row in data:
            everythinglist.append(order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                        row[10]))
        for row in everythinglist:
            if row.site1 == 'Willow':  # if the order is for Willow
                n = (datetime.strptime(row.date2, '%Y-%m-%d').date() - datetime.strptime(row.date1, '%Y-%m-%d').date())  # All below is making a list of all dates in the willow site
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
        selecteddates.append(firstdate)
        selecteddates.append(seconddate)
        w = seconddate - firstdate
        if w.days >= 2:
            for m in range(1, w.days):
                nextday = firstdate + timedelta(days=m)
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
    global firstdate
    global seconddate
    createcalendar()  # makes a window for the  calendar
    calendartab.title('Oak')  # titles the window
    cal = Calendar(calendartab, selectbackground='green2', selectforeground='black', maxdate=maximumdate,
                   mindate=minimumdate, weekendbackground='Green2', weekendforeground='Black', normalbackground='Green2',
                   selectmode='none')  # Makes a calendar
    with open('orders.csv', 'rt')as f:
        data = csv.reader(f)
        for row in data:
            everythinglist.append(order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                        row[10]))
        for row in everythinglist:
            if row.site1 == 'Oak':  # if the order is for kauri
                n = (datetime.strptime(row.date2, '%Y-%m-%d').date() - datetime.strptime(row.date1, '%Y-%m-%d').date())  # All below is making a list of all dates in the oak site
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
        selecteddates.append(firstdate)
        selecteddates.append(seconddate)
        w = seconddate - firstdate
        if w.days >= 2:
            for m in range(1, w.days):
                nextday = firstdate + timedelta(days=m)
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


# ============================================== Calendar Tab ==========================================================


def selectfunction(event):  # Function when clicking the calendar
    if firstclick:  # If the calendar has been clicked once
        secondselectfunction()  # Run second click function

    else:  # Otherwise if it is the first click
        firstselectfunction()  # run the first click funton


def firstselectfunction():
    global firstclick
    global firstdate
    global seconddate
    calendar.calevent_remove('all')  # Removing all events to select new ones
    firstclick = True  # Making the first click true
    firstdate = calendar.selection_get()  # Setting the first date value
    calendar.calevent_create(calendar.selection_get(), 'Selected Date', 'selected')  # Creating an event on selected date
    calendar.tag_config('selected', background='#FF1212', foreground='Black')  # Colouring the event


def secondselectfunction():
    global firstclick
    global firstdate
    global seconddate
    firstclick = False  # Setting first click to false
    selecteddates.clear()  # Clearing the list
    seconddate = calendar.selection_get()  # setting second date to selected date
    n = seconddate - firstdate  # To calculate if the second date is lower than 1st. will be -ve if true
    calendar.calevent_create(seconddate, 'Selected Date', 'selected')  # Creating an even at the Second date
    calendar.tag_config('selected', background='#FF1212', foreground='black')  # Colouring the event
    if n.days < 0:  # if n is -ve
        seconddate = firstdate  # This makes the second date == first date
        firstdate = calendar.selection_get()  # this makes the first date == 2nd date
        n = seconddate - firstdate  # this recalculates the n value

    # n basically is the difference between the first and the second date and if is a -ve it means the user has seleced the second date first
    # if the difference is == or bigger than 2 then it means there will be a white space inbetween them so makes a list of them

    if n.days >= 2:
        for m in range(1, n.days):
            nextday = firstdate + timedelta(days=m)
            selecteddates.append(nextday)  # Crating the list of inbetween days

    for i in selecteddates:
        calendar.calevent_create(i, 'Selected Date', 'inbetween')  # Creating events for the days
        calendar.tag_config('inbetween', background='#FF9999', foreground='black')  # Colouring the events


dates = Label(tab1, text='Select Dates', font=('Courier', 20, 'bold'), bg='#F1A0D1', fg='black')  # Label saying "Select Dates"
dates.place(x=225, y=85)

calendar = Calendar(tab1, selectbackground='white', selectforeground='black', maxdate=maximumdate, mindate=minimumdate,
                    weekendbackground='white', weekendforeground='black', fg='dodger blue')  # Making the main calendar for selecting dates
calendar.place(x=200, y=135)
calendar.bind('<<CalendarSelected>>', selectfunction)  # Binding the calendar to the selectfunction


calnext = Button(tab1, text='Next', font=('Courier', 15), command=tab3change, bg='Dodger Blue', fg='Black', width=15,
                 activebackground='dodger blue')  # making a next button to go to the next tab
calnext.place(x=750, y=400)

searchb = Button(tab1, text='Search', font=('Courier', 15), command=tab5change, bg='Dodger Blue', fg='Black', width=15,
                 activebackground='dodger blue')  # making a button to go to the search tab
searchb.place(x=750, y=350)

todaydate = Label(tab1, font=('Courier', 16), text="Today's Date: " + str(datetime.now().date()), bg='#F1A0D1')  # Creating a label to display todays date
todaydate.place(x=650, y=50)


# ==================================================== Details Tab ========================================================

space = 10  # A variable to move the entry widgets


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


nameentry = Entry(tab4, width=20, font=('Courier', 15))  # Entry widget for name
nameentry.insert(0, 'Full Name')  # Inserting the instruction
nameentry.place(x=50, y=space*5)
nameentry.bind('<FocusIn>', FN_on_nameentry_click)  # Binds the entry to the focus in function
nameentry.bind('<FocusOut>', FN_on_name_focusout)  # Binds the entry to the focus out function
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

foodcheck = Checkbutton(tab4, text='Food Option', font=('Courier', 15), command=foodchange, bg='#F1A0D1', activebackground='#F1A0D1')
foodcheck.place(x=50, y=200)  # Makes a checkbutton for the food options

pricelabel = Label(tab4, text='Price: $' + str(price), font=('Courier', 15), bg='#F1A0D1')
pricelabel.place(x=50, y=250)  # Makes a label showing the price of the order

nameback = Button(tab4, text='Back', font=('Courier', 15), command=tab3change, bg='Dodger Blue', fg='Black', width=15,
                  activebackground='dodger blue')
nameback.place(x=50, y=400)  # makes a button to go back a tab

calwrite = Button(tab4, text='Order', font=('Courier', 15), command=writeb1, bg='Dodger Blue', fg='Black', width=15,
                  activebackground='dodger blue')
calwrite.place(x=750, y=400)  # Makes a button to write to the CSV


# ==================================================== Site Tab ========================================================

def oakfun():  # Function when oak button is clicked
    global oakselect
    global oaknot
    global willownot
    global kaurinot
    global willowselect
    global kauriselect
    global site
    site = 'Oak'  # Sets site to oak
    if willowselect.cget('bg') != 'orangered':  # If the button is not disabled
        willowselect.configure(bg='Dodger Blue')  # Colours the button to the normal colour
    if kauriselect.cget('bg') != 'orangered':  # If the button is not disabled
        kauriselect.configure(bg='Dodger Blue')  # Colours the button to the normal colour
    oakselect.configure(bg='Medium Blue')  # Sets the button the the select colour


def willowfun():  # function when willow button is clicked
    global oaknot
    global willownot
    global kaurinot
    global oakselect
    global willowselect
    global kauriselect
    global site
    site = 'Willow'  # Sets site to willow
    if oakselect.cget('bg') != 'orangered':  # If the button is not disabled
        oakselect.configure(bg='Dodger Blue')  # Colours the button to the normal colour
    if kauriselect.cget('bg') != 'orangered':  # If the button is not disabled
        kauriselect.configure(bg='Dodger Blue')  # Colours the button to the normal colour
    willowselect.configure(bg='medium Blue')  # Sets the button the the select colour


def kaurifun():
    global oaknot
    global willownot
    global kaurinot
    global oakselect
    global willowselect
    global kauriselect
    global site
    site = 'Kauri'  # Sets site to karui
    if willowselect.cget('bg') != 'orangered':  # If the button is not disabled
        willowselect.configure(bg='Dodger Blue')  # Colours the button to the normal colour
    if oakselect.cget('bg') != 'orangered':  # If the button is not disabled
        oakselect.configure(bg='Dodger Blue')  # Colours the button to the normal colour
    kauriselect.configure(bg='medium Blue')  # Sets the button the the select colour


oakselect = Button(tab3, text='The Oak', font=('Courier', 15), bg='Dodger Blue', command=oakfun, activebackground='Dodger Blue',
                   width=10, height=3)
oakselect.place(x=116, y=50)  # Button to select oak site
oakcheck = Button(tab3, text='See Available \nTimes', font=('Courier', 10), bg='Dark Orange', command=oakcalendar, activebackground='Dark Orange',
                  width=20, height=3)
oakcheck.place(x=116, y=300)  # Button to open the oak calendar

willowselect = Button(tab3, text='The Willow', font=('Courier', 15), bg='Dodger Blue', command=willowfun, activebackground='Dodger Blue',
                      width=10, height=3)
willowselect.place(x=425, y=50)  # Button to select willow site
willowcheck = Button(tab3, text='See Available \nTimes', font=('Courier', 10), bg='Dark Orange', command=willowcalendar, activebackground='Dark Orange',
                     width=20, height=3)
willowcheck.place(x=425, y=300)  # Button to open the willow calendar

kauriselect = Button(tab3, text='The Kauri', font=('Courier', 15), bg='Dodger Blue', command=kaurifun, activebackground='Dodger Blue',
                     width=10, height=3)
kauriselect.place(x=750, y=50)  # Button to select kauri site
kauricheck = Button(tab3, text='See Available \nTimes', font=('Courier', 10), bg='Dark Orange', command=kauricalendar, activebackground='Dark Orange',
                    width=20, height=3)
kauricheck.place(x=750, y=300)  # Button to open the kauri calendar

tab3next = Button(tab3, text='Next', font=('Courier', 15), command=tab4change, bg='Dodger Blue', fg='Black', width=15,
                  activebackground='dodger blue')
tab3next.place(x=750, y=400)  # Next button

calback = Button(tab3, text='Back', font=('Courier', 15), command=tab1change, bg='Dodger Blue', fg='Black', width=15,
                 activebackground='dodger blue')
calback.place(x=50, y=400)  # Back button

kaurinot = Label(tab3, text='Unavailable', font=('Courier', 12), fg='black', bg='#F1A0D1')  # Unavailable label

oaknot = Label(tab3, text='Unavailable', font=('Courier', 12), fg='black', bg='#F1A0D1')  # Unavailable label

willownot = Label(tab3, text='Unavailable', font=('Courier', 12), fg='black', bg='#F1A0D1')  # Unavailable label


# ================================================= Search Tab =========================================================

searchbox = Entry(tab5, width=20, font=('Courier', 15))
searchbox.place(x=200, y=100)  # Entry widget for search function

searchbutton = Button(tab5, text='Search', font=('Courier', 10), command=search, bg='Dodger Blue', fg='Black', width=15,
                      activebackground='dodger blue')
searchbutton.place(x=450, y=100)  # Search button


searchlabel = Label(tab5, text='', font=('Courier', 20), bg='#F1A0D1')
searchlabel.place(x=75, y=200)  # Label to display the search output

searchvar = StringVar(tab5)
searchvar.set('Name')  # variable for the option menu

searchselect = OptionMenu(tab5, searchvar, 'Name', 'Month', 'Date')
searchselect.place(x=600, y=100)  # Option menu for the search tab

back = Button(tab5, text='Back', font=('Courier', 15), command=tab1change, bg='Dodger Blue', fg='Black', width=15,
              activebackground='dodger blue')
back.place(x=50, y=30)  # back button to the calendar tab


root.mainloop()  # Running main loop
