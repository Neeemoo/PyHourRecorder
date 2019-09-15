import os
import sys


class WriteFile:
    file_location = 'C:/Users/' + os.getlogin() + '/.PyHourRecorder'
    yyyy = 1111
    mm = 1
    dd = 1

    time_work_start = '00:00'
    time_lunch_start = '00:00'
    time_lunch_end = '00:00'
    time_work_end = '00:00'
    different_week_days = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
    date = dd, '.', mm, '.', yyyy
    std_balance = '00:00'
    day_of_week = different_week_days[0]

    hours_worked = '00:00'
    hours_daily_goal = '00:00'
    std_balance_today = '00:00'
    std_balance_total = '00:00'


    def write_txt(self):
        txt = open(self.file_location + '/hours.txt', "w+")
        txt.close()

    def first_write(self):
        first_txt = open(self.file_location + '/hours.txt', "w+")
        first_txt.write(self.first_file_print)

    def print_file(self):

        file_print = "+-----------------------------------+ \n" \
                     "| Start:  | --------------- | " + self.time_work_start + " | \n" \
                     "| Mittag: | --------------- | " + self.time_lunch_start + " | \n" \
                     "| M-Ende: | --------------- | " + self.time_lunch_end + " | \n" \
                     "| Ende:   | --------------- | " + self.time_work_end + " | \n" \
                     "+-----------------------------------+ \n" \
                     "| Ziel Stunden:   | ------- | " + self.hours_daily_goal + " | \n" \
                     "| Arbeits Stunden:| ------- | " + self.hours_worked + " | \n" \
                     "| Heutige-bilanz: | ------- | " + self.std_balance_today + " | \n" \
                     "| Totale-bilanz:  | ------- | " + self.std_balance_total + " | \n" \
                     "+-----------------------------------+"

        hour_txt = open(self.file_location + '/hours.txt', "w+")
        hour_txt.write(str(file_print))


















    def validate_date(self):
        if self.mm == 1 or 3 or 5 or 7:
            if self.dd > 31:
                self.mm += 1
                self.dd - 31

        elif self.mm == 8 or 10 or 12:
            if self.dd > 31:
                self.mm += 1
                self.dd - 31

            if self.mm == 12:
                if self.dd > 31:
                    self.mm = 1
                    self.dd - 31

        elif self.mm == 4 or 6 or 9 or 11:
            if self.dd > 30:
                self.mm += 1
                self.dd - 30

        elif self.mm == 2:
            if self.dd > 29 and self.yyyy == isinstance(self.yyyy / 4, int):
                self.mm += 1
                self.dd - 29

            if self.dd > 28 and self.yyyy == isinstance(self.yyyy / 4, float):
                self.mm += 1
                self.dd - 28

        if self.dd < 10:
            self.dd = "0" + self.dd

        if self.mm < 10:
            self.mm = "0" + self.mm

        if self.dd == 0:
            self.dd = 1

        return [dd, mm, yyyy]

