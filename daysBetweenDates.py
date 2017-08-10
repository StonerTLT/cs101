# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

def is_leap_year(year):
    """Returns True if the year is leap year. Otherwise, returns False"""
    if year%4 ==0 and year%100 != 0:
        return True
    if year%400 == 0:
        return True
    return False

def nextDay(year, month, day):
    """Return the next day after (year, month, day)"""
    if month != 2:
        if day < 30:
            return year, month, day + 1
        if day == 30:
            if month == 4 or month == 6 or month == 9 or month == 11:
                return year, month + 1, 1
            else:
                return year, month , day + 1
        else:
            if month == 12:
                return year + 1, 1, 1
            else:
                return year, month + 1, 1
    if month == 2:
        if day < 28:
            return year, month, day + 1
        if day == 28:
            if is_leap_year(year):
                return year, month, day + 1
            else:
                return year, month + 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

print daysBetweenDates(2012, 1, 1, 2012, 2, 28)
print daysBetweenDates(2012, 1, 1, 2012, 3, 1)
print daysBetweenDates(2011, 6, 30, 2012, 6, 30)
print daysBetweenDates(2011, 1, 1, 2012, 8, 8)
print daysBetweenDates(1900, 1, 1, 1999, 12, 31)

def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"


test()