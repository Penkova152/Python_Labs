import time


def date_difference(my_date, date2=time.strftime("%d-%m-%Y", time.localtime())):

    start_time = time.mktime(time.strptime(my_date, "%d-%m-%Y"))
    end_time = time.mktime(time.strptime(date2, "%d-%m-%Y"))

    return abs(end_time - start_time)


print(date_difference("10-10-2022", "10-10-2022"))
print(date_difference("11-10-2022", "12-10-2022"))
print(date_difference("28-12-2022"))
