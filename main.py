from read_file import ReadFile
from write_file import WriteFile
from main_window import MainWindow


class Main:
    rf = ReadFile()
    wf = WriteFile()

    # if dir does not exist create it
    rf.create_dir()

    # if file does not exist, create it and do the following steps
    if rf.create_txt():
        # write a basic table into the file
        wf.print_file()

    # read the file and print it into the console
    rf.read_txt()

    # wf.write_txt()
