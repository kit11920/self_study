
DEBUG = False

MONTHS = {
    'January': 0,
    'February': 1,
    'March': 2,
    'April': 3,
    'May': 4,
    'June': 5,
    'July': 6,
    'August': 7,
    'September': 8,
    'October': 9,
    'November': 10,
    'December': 11
}

DAY_OF_WEEK = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
}

def main():
    n = int(input())
    year = int(input())
    leap_year = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    count_dm = [0] * 13
    for i in [1, 3, 5, 7, 8, 10, 12]:
        count_dm[i] = 31
    for i in [4, 6, 9, 11]:
        count_dm[i] = 30
    count_dm[2] = 29 if leap_year else 28
    if DEBUG:
        print(f'count_dm: {count_dm}')

    # номер дня начала каждого месяца начиная с 0
    for i in range(1, 13):
        count_dm[i] += count_dm[i - 1]
    del count_dm[-1]
    if DEBUG:
        print(f'count_dm: {count_dm}')

    holidays = list() # номер дня недели по клаcике без сдвига шде пн = 0 вт = 1
    for i in range(n):
        day, month = input().split()
        day, month = int(day), MONTHS[month]
        holidays.append((count_dm[month] + day - 1) % 7)

    frst_day = DAY_OF_WEEK[input()]
    for i in range(n):
        holidays[i] = (holidays[i] + frst_day) % 7
    if DEBUG:
        print(f'holidays: {holidays}')

    holidays_days = [0] * 7
    for i in range(7):
        holidays_days[i] = holidays.count(i)
    if DEBUG:
        print('holidays_days:', holidays_days)

    # кол-во дней отдыха
    choose_this = [0] * 7
    for i in range(7):
        if i == frst_day or (i == (frst_day + 1) % 7 and leap_year):
            choose_this[i] = 53 + n - holidays_days[i]
        else:
            choose_this[i] = 52 + n - holidays_days[i]
    if DEBUG:
        print(f'choose_this: {choose_this}')
    mmin = min(choose_this)
    mmax = max(choose_this)
    lasy_day, worky_day = '', ''
    for k, v in DAY_OF_WEEK.items():
        if choose_this[v] == mmax:
            lasy_day = k
        if choose_this[v] == mmin:
            worky_day = k

    print(lasy_day, worky_day)





main()
