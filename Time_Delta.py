switcher = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

def days_count(t1,t2):
    days = 0
    day = int(t1[1])
    month = int(t1[2])
    year = int(t1[3])
    check = True
    thirty = [4, 6, 9, 11]
    while (check):
        if day == int(t2[1]) and month == int(t2[2]) and year == int(t2[3]):
            check = False
            break
        days = days + 1
        if day == 28 or day == 30 or day == 31:
            if month == 2:
                if leap_year(year):
                    day = day + 1
                    if day == t2[1] and year == t2[3]:
                        return days
                    else:
                        days = days +1
                        day = 1
                        month = month + 1
                        continue
                else:
                    day = 1
                    month = month + 1
                    continue
            elif thirty.__contains__(month) and day == 30:
                day = 1
                month = month + 1
                continue
            elif day ==31:
                if month == 12:
                    year = year + 1
                    month = 1
                    day = 1
                    continue
                else:
                    month = month + 1
                    day = 1
                    continue
        day = day + 1
    return days

def time_check(t):
    tzh, tzm = t[5][1:3], t[5][3:5]
    t[2] = switcher.get(t[2])
    hours = t[4].split(":")
    if t[5][0] == "+":
        return [int(t[1]) * 24 * 3600 + int(t[2]) * 30 * 24 * 3600 + int(t[3]) * 365 * 24 * 3600 , int(
            hours[0]) * 3600 + int(hours[1]) * 60 + int(hours[2]) - (int(tzh) * 3600 + int(tzm) * 60)]
    else:
        return [int(t[1]) * 24 * 3600 + int(t[2]) * 30 * 24 * 3600 + int(t[3]) * 365 * 24 * 3600 , int(
            hours[0]) * 3600 + int(hours[1]) * 60 + int(hours[2]) + (int(tzh) * 3600 + int(tzm) * 60)]

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True

for _ in range(int(input())):
    t1 = input().split()
    t2 = input().split()
    tc1 = time_check(t1)
    tc2 = time_check(t2)
    t = (tc1[0] + tc1[1] - (tc2[0] + tc2[1]))
    if t > 0:
        t = t1
        t1 = t2
        t2 = t
        t = tc1[1]
        tc1[1] = tc2[1]
        tc2[1] =t
    print(days_count(t1,t2))
    print(days_count(t1, t2)*3600*24 +(tc2[1] - tc1[1]))