from datetime import datetime,timedelta

once_upon_a_time = datetime(2010, 7, 1, 12, 0, 0)
delta = timedelta(days=13, hours=8,  minutes=20)

gen =(once_upon_a_time +x*delta for x in range(20))

print('\n'.join(map('{:%Y-%m-%d %H:%M:%S}'.format, gen)))