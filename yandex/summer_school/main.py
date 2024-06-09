import pandas as pd
from datetime import datetime, timedelta
import time

START = 1706745600
DT_START = datetime.fromtimestamp(START)
END = 1709251200
DT_END = datetime.fromtimestamp(END)

ID = 'id'
USER_ID = 'user_id'
TIME_START = 'timestamp'
DAYS = 'billing_period'
COST = 'billing_total_price_usd'


def day_before_feb(ts):
    dt = datetime.fromtimestamp(ts)
    if dt < DT_START:
        diff = DT_START - dt
        if diff.total_seconds() - diff.days * 24 * 60 * 60 > 0:
            return diff.days + 1
        return diff.days
    else:
        return 0


def day_after_feb_start(ts):
    # delt = timedelta(days=int(days_long))
    dt = datetime.fromtimestamp(ts)
    if DT_START < dt:
        diff = dt - DT_START
        # if diff.total_seconds() - diff.days * 24 * 60 * 60 > 0:
        #     return diff.days + 1
        return diff.days
    else:
        return 0


def process(df):
    print(list(df.keys()))

    users = dict()
    for i in range(len(df)):
        user_id = df[USER_ID][i]
        cost = df[COST][i]
        days = df[DAYS][i]
        ts = df[TIME_START][i]
        days_in_feb = min(days - day_before_feb(ts), 29 - day_after_feb_start(ts))
        print(f'{user_id}: ts - {ts} before - {day_before_feb(ts)}, day_after_feb_start - {day_after_feb_start(ts)}, days_in_feb - {days_in_feb}, cost_per_day - {cost / days}, summa - {days_in_feb * (cost / days)}')

        summa = days_in_feb * (cost / days)
        if user_id not in users.keys():
            users[user_id] = summa
        else:
            users[user_id] += summa
    print(users)
    print(sorted(users.values(), reverse=True))
    return sum(sorted(users.values(), reverse=True)[:3])



if __name__ == '__main__':
    # print(START)
    # dt = datetime.fromtimestamp(START)
    # print(dt.day)
    # test = 1709337600
    # dte = datetime.fromtimestamp(test)
    # print(dte.day)
    # print('---', day_after_feb(test))
    df = pd.read_csv("sample_1.csv")
    print(process(df))
