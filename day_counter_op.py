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

thirty = [4, 6, 9, 11]


def time_check(t):
    tzh, tzm = t[5][1:3], t[5][3:5]
    t[2] = switcher.get(t[2])
    hours = t[4].split(":")
    if t[5][0] == "+":
        return [int(t[1]) * 24 * 3600 + int(t[2]) * 30 * 24 * 3600 + int(t[3]) * 365 * 24 * 3600, int(
            hours[0]) * 3600 + int(hours[1]) * 60 + int(hours[2]) - (int(tzh) * 3600 + int(tzm) * 60)]
    else:
        return [int(t[1]) * 24 * 3600 + int(t[2]) * 30 * 24 * 3600 + int(t[3]) * 365 * 24 * 3600, int(
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
    else:
        return False


def month_to_days(month, year):
    if thirty.__contains__(month):
        return 30
    elif month == 2:
        if leap_year(year):
            return 29
        else:
            return 28
    else:
        return 31


def days_counter(date1, date2):
    day1 = int(date1[0])
    month1 = int(date1[1])
    year1 = int(date1[2])

    day2 = int(date2[0])
    month2 = int(date2[1])
    year2 = int(date2[2])
    days_count = 0

    if not month1 == month2 or not year1 == year2:
        temp = month_to_days(month1, year1)
        days_count = days_count + temp - day1
        day1 = temp
    else:
        days_count = days_count + day2 - day1
        day1 = day2
        return days_count

    while True:
        day_check = day1 == day2
        month_check = month1 == month2
        year_check = year1 == year2

        if day_check and month_check and year_check:
            break

        if day1 == 31 or day1 == 30 or day1 == 29 or day1 == 28:
            if month1 == 12:
                if year1 + 1 != year2:
                    while year1 != year2 - 1:
                        year1 = year1 + 1
                        if leap_year(year1):
                            days_count = days_count + 366
                        else:
                            days_count = days_count + 365
                else:
                    month1 = 0
                    year1 = year1 + 1
                    continue
            else:
                if month1 + 1 != month2 or year1 != year2:
                    while month1 + 1 != month2 or year1 != year2:
                        month1 = month1 + 1
                        temp = month_to_days(month1, year1)
                        days_count = days_count + temp
                        day1 = temp
                        if (month1 == 12): break
                else:
                    days_count = days_count + day2
                    day1 = day2
                    return days_count
    return days_count


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
        tc2[1] = t
    print(days_counter(t1[1:4], t2[1:4]) * 3600 * 24 + (tc2[1] - tc1[1]))
