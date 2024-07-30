from calendar import monthrange, weekday
from datetime import datetime as dt
from datetime import date
from datetime import timedelta

def main():
    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") 
    today = date.today()
    start = int(dt.strftime(today, "%Y"))
    end = start + 10

    for year in range(start, end):
        holidays = Holidays(year).holidays
        with open("holidays.txt", "a") as f:
            for key, value in holidays.items():
                f.write(f"{key}:\n{weekdays[weekday(value.year, value.month, value.day)]}\n{value}\n\n")


class Holidays():
    def __init__(self, year: int) -> dict:
        self.holidays = {
            "New Year's Day": self.unless_weekend(year, 1, 1), # January 1 unless weekend
            "Martin Luther King, Jr. Day": self.xDayOf(year, 1, 0, 2), # creates a list of Mondays and returns the third (index 2)
            "President's Day": self.xDayOf(year, 2, 0, 2), # creates a list of Mondays and returns the third (index 2)
            "Cesar Chavez Day": self.unless_weekend(year, 3, 31), # March 31 unless weekend
            "Memorial Day": self.xDayOf(year, 5, 0, -1), # creates a list of Mondays and returns the last (index -1)
            "Juneteenth": self.unless_weekend(year, 6, 19), # June 19 unless weekend
            "Independence Day": self.unless_weekend(year, 7, 4), # July 4 unless weekend
            "Labor Day": self.xDayOf(year, 9, 0, 0), # creates a list of Mondays and returns the first (index 0)
            "Veteran's Day": self.unless_weekend(year, 11, 11), # November 11 unless weekend
            "Thanksgiving Day": self.xDayOf(year, 11, 3, 3), # creates a list of Thursdays and returns the fourth (index 3)
            "Day After Thanksgiving": "", # see below
            "Christmas": self.unless_weekend(year, 12, 25), # December 25 unless weekend
            "Winter Break: December 26": date(year, 12, 26),
            "Winter Break: December 27": date(year, 12, 27),
            "Winter Break: December 28": date(year, 12, 28),
            "Winter Break: December 29": date(year, 12, 29),
            "Winter Break: December 30": date(year, 12, 30),
            "Winter Break: December 31": date(year, 12, 31),
        }
        self.holidays["Day After Thanksgiving"] = self.holidays["Thanksgiving Day"] + timedelta(days=1)
   

    def unless_weekend(self, year: int, month: int, day: int):
        date_test = date(year, month, day)
        test = weekday(year, month, day)
        if test == 5:
            return date_test - timedelta(days=1)
        elif test == 6:
            return date_test + timedelta(days=1)
        else:
            return date_test


    def xDayOf(self, year: int, month: int, dayOfWeek:int, index: int):
        month_range = monthrange(year, month)[1]
        dates = [] # Create a list of Mondays for the specified month.
        for day in range(1, month_range):
            if weekday(year, month, day) == dayOfWeek:
                dates.append(date(year, month, day))
        return dates[index]


if __name__ == "__main__":
    main()
