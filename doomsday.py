def set_century(year):
    start_days = (2, 0, 5, 3)
    c = year / 100
    x = c % 4

    return start_days[x]


def set_year(year):
    y = year % 100
    y12 = y / 12
    yr = y % 12
    yr4 = yr / 4

    return (y12 + yr + yr4) % 7


def set_month(month, year):
    if month % 2:
        if month == 1:
            if year % 4 == 0:
                mday = 4
            else:
                mday = 3
        else:
            if month in (9, 11):
                mday = month - 4
            else:
                mday = month + 4
    else:
        if month == 2:
            if year % 4 == 0:
                mday = 29
            else:
                mday = 28
        else:
            mday = month

    return mday


def day_offset(month, day, year):
    mday = set_month(month, year)
    offset = (day - mday) % 7

    return offset


def calc_dow(month, day, year):
    days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday')
    c = set_century(year)
    y = set_year(year)
    m = day_offset(month, day, year)
    dow = days[(c + y + m) % 7]

    return dow
