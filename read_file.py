import os


class ReadFile:
    file_location = 'C:/Users/' + os.getlogin() + '/.PyHourRecorder'

    def create_dir(self):
        if not os.path.exists(self.file_location):
            os.makedirs(self.file_location)

    def create_txt(self):
        if not os.path.exists(self.file_location + '/hours.txt'):
            create_file = open(self.file_location + '/hours.txt', "w+")
            create_file.close()
            return True

    def read_txt(self):
        read_file = open(self.file_location + '/hours.txt', "r+")
        text = read_file.read()
        print(text)
        read_file.close()
