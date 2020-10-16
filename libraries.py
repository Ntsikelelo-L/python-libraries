from datetime import date
from datetime import time
from datetime import datetime, timedelta

#timedelta

x=datetime(2020, 10, 16, 11, 58, 59)

for i in range(10):
    print(x)
    x=x +timedelta(days=14)

