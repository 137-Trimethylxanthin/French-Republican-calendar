import PySimpleGUI as sg
from time import sleep
import datetime
import sys
import subprocess
import pkg_resources

required = {'pysimplegui'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed


if missing:
    python = sys.executable
    subprocess.check_call(
        [python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)


def romanNummeral(num):
    res = ""
    table = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    for cap, roman in table:
        d, m = divmod(num, cap)
        res += roman * d
        num = m

    return res


def revulutionsDays():
    day = ['Primidi', 'Duodi', 'Tridi', 'Quartidi', 'Quintidi',
           'Sextidi', 'Septidi', 'Octidi', 'Nonidi', 'Decadi']
    today = datetime.date.today()
    creationDay = datetime.date(1789, 7, 15)
    delta = today - creationDay
    foo = str(delta.days)[-1]

    return day[int(foo)]


def revulutionsYears():
    today = datetime.date.today()
    creationDay = datetime.date(1789, 7, 15)
    delta = today - creationDay
    foo = delta.days // 365
    return foo


def revulutionsTime():
    getTime = datetime.datetime.now().time()
    timeDeRevulution = int(
        (getTime.hour * 3600 + getTime.minute * 60 + getTime.second)//0.864)
    hour = str(timeDeRevulution).zfill(5)[0]
    minute1 = str(timeDeRevulution).zfill(5)[1]
    minute2 = str(timeDeRevulution).zfill(5)[2]
    sec1 = str(timeDeRevulution).zfill(5)[3]
    sec2 = str(timeDeRevulution).zfill(5)[4]
    return hour, minute1, minute2, sec1, sec2


def revulutionsMonths():
    year = datetime.date.today().year
    today = datetime.date.today()
    month = ['Vendémiaire', 'Brumaire', 'Frimaire', 'Nivôse', 'Pluviôse', 'Ventôse',
             'Germinal', 'Floréal', 'Prairial', 'Messidor', 'Thermidor', 'Fructidor']

    start = datetime.date(year, 9, 22)
    end = datetime.date(year, 10, 21)
    if start <= today <= end:
        monthRay = 0

    start = datetime.date(year, 10, 22)
    end = datetime.date(year, 11, 20)
    if start <= today <= end:
        monthRay = 1

    start = datetime.date(year, 11, 21)
    end = datetime.date(year, 12, 20)
    if start <= today <= end:
        monthRay = 2

    start = datetime.date(year, 12, 21)
    end = datetime.date(year, 1, 19)
    if start <= today <= end:
        monthRay = 3

    start = datetime.date(year, 1, 20)
    end = datetime.date(year, 2, 18)
    if start <= today <= end:
        monthRay = 4

    start = datetime.date(year, 2, 19)
    end = datetime.date(year, 3, 20)
    if start <= today <= end:
        monthRay = 5

    start = datetime.date(year, 3, 21)
    end = datetime.date(year, 4, 19)
    if start <= today <= end:
        monthRay = 6

    start = datetime.date(year, 4, 20)
    end = datetime.date(year, 5, 19)
    if start <= today <= end:
        monthRay = 7

    start = datetime.date(year, 5, 20)
    end = datetime.date(year, 6, 18)
    if start <= today <= end:
        monthRay = 8

    start = datetime.date(year, 6, 19)
    end = datetime.date(year, 7, 18)
    if start <= today <= end:
        monthRay = 9

    start = datetime.date(year, 7, 19)
    end = datetime.date(year, 8, 17)
    if start <= today <= end:
        monthRay = 10

    start = datetime.date(year, 8, 18)
    end = datetime.date(year, 9, 16)
    if start <= today <= end:
        monthRay = 11

    return month[monthRay]


#


# ask what do do:

def asking():
    print(' ')
    print(' ')
    print('cli or gui?')
    print('please typ it out or the type out the fist letter of you choice')
    ask = input('input: ')
    print(f'you selected {ask}')
    sleep(1)

    # print terminal:
    if ask.lower() == 'cli' or ask.lower() == 'c':
        hour, minute1, minute2, sec1, sec2 = revulutionsTime()
        days = revulutionsDays()
        months = revulutionsMonths()
        roman = romanNummeral(revulutionsYears())
        years = revulutionsYears()
        print(' ')
        print(' ')
        print(
            f'the day is: {days}  this month is: {months}    {roman}|{years}  years of freedom', sep='')
        print(f'{hour}:{minute1}{minute2}:{sec1}{sec2}')
        print(' ')
        print(' ')
        exit()

    # GUI here:
    if ask.lower() == 'gui' or ask.lower() == 'g':

        sg.theme('DarkAmber')

        layout = [[sg.Text('Revolution', expand_y=True)],
                  [sg.Text('the day is: '), sg.Text('', key='_day_')],
                  [sg.Text('this month is: '), sg.Text('', key='_month_')],
                  [sg.Text('years of freedom: '), sg.Text('', key='_year_')],
                  [sg.Text('Time: ', expand_y=True), sg.Text(
                      '', key='_time_', expand_y=True)],
                  [(sg.Quit())]
                  ]

        # Create the window object
        window = sg.Window('Revolution', size=(500, 300),
                           element_justification='center').Layout(layout)

        def getTime():
            hour, minute1, minute2, sec1, sec2 = revulutionsTime()
            return f'{hour}:{minute1}{minute2}:{sec1}{sec2}'

        def getDay():
            days = revulutionsDays()
            return f'{days}'

        def getMonth():
            months = revulutionsMonths()
            return f'{months}'

        def getYear():
            roman = romanNummeral(revulutionsYears())
            years = revulutionsYears()
            return f'{roman}|{years}'

        def main(gui_obj):
            # Event loop
            while True:
                event, values = gui_obj.Read(timeout=10)

                # Exits program cleanly if user clicks "X" or "Quit" buttons
                if event in (None, 'Quit'):
                    break

                # Update '_time_' key value with return value of getTime()
                gui_obj.FindElement('_time_').Update(getTime())
                gui_obj.FindElement('_day_').Update(getDay())
                gui_obj.FindElement('_month_').Update(getMonth())
                gui_obj.FindElement('_year_').Update(getYear())

        if __name__ == '__main__':
            main(window)
    else:
        print('error wrong input pease try again')
        sleep(1)
        asking()


asking()
