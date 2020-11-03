# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import calendar
import datetime as dt
from IPython.display import display, HTML


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def cal():
    # find out today's date
    t = dt.datetime.today()

    # create HTML Calendar month
    caled = calendar.HTMLCalendar()
    s = caled.formatmonth(t.year, t.month)

    # display calendar without highlighting today
    with open("data.html", "w") as file:
        file.write(HTML(s).data)
    # add cell's backgroundcolor, bold and underling html tags
    # around today's date
    ss = s.replace('>%i<'%t.day, ' bgcolor="#66ff66"><b><u>%i</u></b><'%t.day)
    with open("data_hl.html", "w") as file:
        file.write(HTML(ss).data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    cal()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
