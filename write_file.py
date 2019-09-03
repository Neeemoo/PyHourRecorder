import os

k
class WriteFile:
    file_location = 'C:/Users/' + os.getlogin() + '/.PyHourRecorder'

    time_work_start = []
    time_lunch_start = []
    time_lunch_end = []
    time_work_end = []
    Day_of_week = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
    Date_dd_mm_yyyy = [dd.mm.yyyy, dd + 1, mm, yyyy, dd + 2, mm, yyyy, dd + 3, mm, yyyy, dd + 4, mm, yyyy, dd + 5, mm, yyyy, dd + 6, mm, yyyy, dd + 7, mm, yyyy, dd + 8, mm, yyyy, dd + 9, mm, yyyy, dd + 10, mm, yyyy]

    first_file_print = "+-----------------------------------+ \n" \
                       "| Start:  | " + Day[0] + ", " + Date[0] + " | " + time_work_start[0] + " | \n" \
                       "| Mittag: | --------------- | " + time_lunch_start[0] + " | \n" \
                       "| M-Ende: | --------------- | " + time_lunch_ende[0] + " | \n" \
                       "| Ende:   | --------------- | " + time_work_ende[0] + " | \n" \
                       "+-----------------------------------+ "

    def validate_date(self):
        yyyy = 1111
        mm = 1
        dd = 1
        if mm == 1 or 3 or 5 or 7:
            if dd > 31:
                mm += 1
                dd - 31

        elif mm == 8 or 10 or 12:
            if dd > 31:
                mm += 1
                dd - 31

            if mm == 12:
                if dd > 31:
                    mm = 1
                    dd - 31

        elif mm == 4 or 6 or 9 or 11:
            if dd > 30:
                mm += 1
                dd - 30

        elif mm == 2:
            if dd > 29 and yyyy == isinstance(yyyy / 4, int):
                mm += 1
                dd - 29

            if dd > 28 and yyyy == isinstance(yyyy / 4, float):
                mm += 1
                dd - 28

        if dd < 10:
            dd = "0" + dd

        if mm < 10:
            mm = "0" + mm

    def write_txt(self):
        txt = open(self.file_location + '/hours.txt', "w+")
        txt.close()

    def first_write(self):
        first_txt = open(self.file_location + '/hours.txt', "w+")
        first_txt.write(self.first_file_print)
