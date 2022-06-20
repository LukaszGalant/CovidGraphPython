import requests
import pandas as pd
import matplotlib.pylab as plt
import matplotlib.ticker as ticker
from tkcalendar import *
import tkinter

data = requests.get(f"https://api.covid19api.com/total/dayone/country/Poland").json()
df = pd.DataFrame(data)



def ShowGraph(df,lowdate,highdate):

    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

    #gdybym dodał warunki to bym zaweżał dataframe w ten sposób (jeżeli dobrze pamietam)
    #fdf = df.loc[df['Date'] >= date_low & df['Date'] <= date_high]

    #plot creation
    fig, ax = plt.subplots()
    ax.plot(df['Date'],df['Confirmed'])
    ax.xaxis_date() 


    #automatically redistribute dates in the X-axis. Without it dates are overlapping
    fig.autofmt_xdate()

    #format of Y-axis 1 000 000 --> 1 000 K
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, pos:'{:,.0f}'.format(y/1000) + ' tys'))

    plt.show()

form = tkinter.Tk()

## HEADER ##
form.title("COVID")
form.geometry("900x400")

lbl_left = tkinter.Label(form, text="Date from",bg="lightblue",highlightbackground="black", highlightthickness=1)
lbl_left.grid(row=1,column=0,sticky="nw")

lbl_right = tkinter.Label(form, text="Date to",bg="lightblue",highlightbackground="black", highlightthickness=1)
lbl_right.grid(row=1,column=1,sticky="nw")



cal = Calendar(form,selectmode = "day", year = 2020, month = 5, day = 22)
cal.grid (row=2, column=0)

cal2 = Calendar(form,selectmode = "day", year = 2020, month = 5, day = 22)
cal2.grid (row=2, column=1)

date_low = cal.get_date()
date_high = cal.get_date()

#sprawdzanie inputu
def btn_checkinput():
    
    #to be finished
    #if(date_low>date_high):
    #    print("incorrect input")
    #elif (date_high > datetime.now()):
    #    print("incorrect input")
    #else:

    ShowGraph(df,date_low,date_high)

#button
btn = tkinter.Button(form,width=30,text="Generate graph",command=btn_checkinput)
btn.grid(row=3, column = 0)


lbl_leftdown = tkinter.Label(form, text="Graph pokazuje wszystkie dane, bo nie zdążyłem dopisać warunków z datami",bg="lightblue",highlightbackground="black", highlightthickness=1)
lbl_leftdown.grid(row=4,column=0,sticky="nw")

tkinter.mainloop()


