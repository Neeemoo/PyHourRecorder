import os


class WriteFile:
    file_location = 'C:/Users/' + os.getlogin() + '/.PyHourRecorder'
    time1 = "00:00"
    time2 = "00:00"
    time3 = "00:00"
    time4 = "00:00"
    Day = "Mon"
    Date = "00.00.0000"

    first_file_print = "+-----------------------------------+ \n" \
                       "| Start:  | " + Day + ", " + Date + " | " + time1 + " | \n" \
                       "| Mittag: | --------------- | " + time2 + " | \n" \
                       "| M-Ende: | --------------- | " + time3 + " | \n" \
                       "| Ende:   | --------------- | " + time4 + " | \n" \
                       "+-----------------------------------+"

    def write_txt(self):
        txt = open(self.file_location + '/hours.txt', "w+")
        txt.close()

    def first_write(self):
        first_txt = open(self.file_location + '/hours.txt', "w+")
        first_txt.write(self.first_file_print)
