from calendar import weekday
from datetime import date
from datetime import timedelta as delta


def main():
    start = date.today()
    length = 365
    list_holidays(start, length)


def list_holidays(start, length):
    date = start + delta(days=i)
    date_list = []
    for d in range(length):
        date_list.append(f"{date} is {is_working(date)}")

    date_list = sorted(list(set(date_list)))
    with open("Scripts/working_days.txt", "w") as f:
        for i in date_list:
            f.write(f"{i}\n")


def is_working(date):
    day = weekday(date.year, date.month, date.day)

    # Check for weekends
    if day == 5:
        return f"{date} a Saturday"
    if day == 6:
        return f"{date} a Sunday"

    # Check for winter closure.
    if date in ["12-26", "12-27", "12-28", "12-29", "12-30", "12-31"]:
        return f"{date} during Winter Break"

    # Check for date-defined holidays
    holidays = {
        "01-01": "New Year's Day",
        "03-31": "Cesar Chavez Day",
        "06-19": "Juneteenth",
        "07-04": "Independence Day",
        "11-11": "Veteran's Day",
        "12-25": "Christmas",
    }
    if date in holidays:
        return holidays[date]

    # Thanksgiving (fourth Thursday in Nov)
    if day == 3:
        if date in ["11-22", "11-23", "11-24", "11-25", "11-26", "11-27", "11-28"]:
            return "Thanksgiving Day"

    # Check for 'Sunday observed on Monday' holidays:
    if day == 7:
        mondays = {
            "01-02": "New Year Day (observed)",
            "04-01": "Cesar Chavez Day (observed)",
            "06-20": "Juneteenth (observed)",
            "07-05": "Independence Day (observed)",
            "11-12": "Veteran's Day (observed)",
        }
        if date in mondays:
            return mondays[date]

        # Check for 'Monday' holidays:
        if date in ["01-15", "01-16", "01-17", "01-18", "01-19", "01-20", "01-21"]:
            return "Martin Luther King Jr. Day"  # MLK (third Monday in Jan)

        if date in ["02-15", "02-16", "02-17", "02-18", "02-19", "02-20", "02-21"]:
            return "President's Day"  # Presidents (third Monday in Feb)

        if date in ["05-25", "05-26", "05-27", "05-28", "05-29", "05-30", "05-31"]:
            return "Memorial Day"  # Memorial (last Monday in May)

        if date in ["09-01", "09-02", "09-03", "09-04", "09-05", "09-06", "09-07"]:
            return "Labor Day"  # Labor (first Monday in Sep)

        if date in ["11-23", "11-24", "11-25", "11-26", "11-27", "11-28", "11-29"]:
            return "the Day After Thanksgiving"

    # Check for 'Saturday observed on Friday' holidays:
    if day == 4:
        fridays = {
            "03-30": "Cesar Chavez Day (observed)",
            "06-18": "Juneteenth (observed)",
            "07-03": "Independence Day (observed)",
            "11-10": "Veteran's Day (observed)",
            "12-24": "Christmas Day (observed)",
        }
        if date in fridays:
            return fridays[date]

    return "a Business Day"


if __name__ == "__main__":
    main()
