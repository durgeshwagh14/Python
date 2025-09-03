import random
import datetime

start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2020, 12, 31)

random_dates = [start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days)) for _ in range(10)]

print(random_dates)
