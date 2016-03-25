# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015' 
# Calendar reference
calendar = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}  # not a leap year

year_start_string = date_start[6: 10]
year_start = int(year_start_string)
year_stop_string = date_stop[6: 10]
year_stop = int(year_stop_string)

month_start_string = date_start[0: 2]
month_start = int(month_start_string)
month_stop_string = date_stop[0: 2]
month_stop = int(month_stop_string)

day_start_string = date_start[3: 5]
day_start = int(day_start_string)
day_stop_string = date_stop[3: 5]
day_stop = int(day_stop_string)

start_date = (day_start, month_start, year_start)                   # European dates are just mathematically nicer
stop_date = (day_stop, month_stop, year_stop)
y0 = year_start
y1 = year_stop
m0 = month_start
m1 = month_stop
d0 = day_start
d1 = day_stop

day_counter = 0
run = True

while run:
    while m0 <= 12 and run:
        while d0 < calendar[m0] and run:
            d0 += 1
            day_counter += 1
            if d0 == d1 and m0 == m1 and y0 == y1:
                run = False
        d0 = 0
        m0 += 1
    m0 = 1
    y0 += 1

print(day_counter)


####b)  
date_start = '12312013'  
date_stop = '05282015'  
# Calendar reference
calendar = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

year_start_string = date_start[4: 8]
year_start = int(year_start_string)
year_stop_string = date_stop[4: 8]
year_stop = int(year_stop_string)

month_start_string = date_start[0: 2]
month_start = int(month_start_string)
month_stop_string = date_stop[0: 2]
month_stop = int(month_stop_string)

day_start_string = date_start[2: 4]
day_start = int(day_start_string)
day_stop_string = date_stop[2: 4]
day_stop = int(day_stop_string)

start_date = (day_start, month_start, year_start)
stop_date = (day_stop, month_stop, year_stop)
y0 = year_start
y1 = year_stop
m0 = month_start
m1 = month_stop
d0 = day_start
d1 = day_stop


day_counter = 0
run = True
while run:
    while m0 <= 12 and run:
        while d0 < calendar[m0] and run:
            d0 += 1
            day_counter += 1
            if d0 == d1 and m0 == m1 and y0 == y1:
                run = False
        d0 = 0
        m0 += 1
    m0 = 1
    y0 += 1

print(day_counter)


####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
# Calendar reference
calendar = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# Month to number reference
month_number = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
                'Nov': 11, 'Dec': 12}

year_start_string = date_start[7: 11]
year_start = int(year_start_string)
year_stop_string = date_stop[7: 11]
year_stop = int(year_stop_string)

month_start_string = date_start[3: 6]
month_start = month_number[month_start_string]
month_stop_string = date_stop[3: 6]
month_stop = month_number[month_stop_string]

day_start_string = date_start[0: 2]
day_start = int(day_start_string)
day_stop_string = date_stop[0: 2]
day_stop = int(day_stop_string)

start_date = (day_start, month_start, year_start)
stop_date = (day_stop, month_stop, year_stop)
y0 = year_start
y1 = year_stop
m0 = month_start
m1 = month_stop
d0 = day_start
d1 = day_stop

day_counter = 0
run = True

while run:
    while m0 <= 12 and run:
        while d0 < calendar[m0] and run:
            d0 += 1
            day_counter += 1
            if d0 == d1 and m0 == m1 and y0 == y1:
                run = False
        d0 = 0
        m0 += 1
    m0 = 1
    if y0 % 4 == 0:                         # Leap year
        day_counter += 1
    y0 += 1


print(day_counter)
