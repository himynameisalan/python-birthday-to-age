from datetime import date
from datetime import datetime
import pandas as pd


def calculateAge(birthday):
    if birthday == '':
        return -1

    birthday = datetime.strptime(birthday, '%Y-%m-%d')
    today = date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    return age


users = pd.DataFrame(['', '2005-01-01', '2010-12-31'], columns=['birthday'])

users['age'] = users.apply(lambda row: calculateAge(row['birthday']), axis=1)

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120]
labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-99', '100+']
users['age_range'] = pd.cut(users.age, bins, labels=labels, include_lowest=True)

print(users)
