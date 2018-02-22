#
# Smoker controller using the Raspberry Pi
#
# version .5 getting started. Create the one second run forever loop, initially print the count, and every 60 counts
# store some numbers in a SQL Lite table.
#
# sqlite portions inspired by http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
# grab the imports

import random
import sqlite3
import string
from time import sleep
import datetime
import sys
import tkinter as tk

# may want to create an init function in the future?

database_name = 'Data/SmokerData.db'
table_name = 'DataRecords'
key_name = "DateTimeStamp"
tc_1_name = "ChamberTemp"
tc_2_name = "Probe1"
tc_3_name = "Probe2"
tc_4_name = "Probe3"


exit_app = 'N'

def connect_to_the_database(database):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    return cur, conn

def create_the_smoking_log_table(cur):
# for now, hard code the table name, drop if it exists, and
# create a clean table.
# and for good mechanics, throw in a try/except when we get real.

    cur.execute('''DROP TABLE IF EXISTS {tn}'''.format(tn=table_name))
    cur.execute('''CREATE TABLE {tn} ({f0} {ft0} PRIMARY KEY)''' \
                .format(tn=table_name, f0=key_name, ft0='TEXT'))
    cur.execute("ALTER TABLE {tn} ADD COLUMN '{f1}' {ft1}" \
                .format(tn=table_name, f1=tc_1_name, ft1='INTEGER'))
    cur.execute("ALTER TABLE {tn} ADD COLUMN '{f1}' {ft1}" \
                .format(tn=table_name, f1=tc_2_name, ft1='INTEGER'))
    cur.execute("ALTER TABLE {tn} ADD COLUMN '{f1}' {ft1}" \
                .format(tn=table_name, f1=tc_3_name, ft1='INTEGER'))
    cur.execute("ALTER TABLE {tn} ADD COLUMN '{f1}' {ft1}" \
                .format(tn=table_name, f1=tc_4_name, ft1='INTEGER'))


def read_sensor_value():
    return int(random.randrange(200, 250))

def generate_data_values():
    tc_1_value = read_sensor_value()
    tc_2_value = read_sensor_value()
    tc_3_value = read_sensor_value()
    tc_4_value = read_sensor_value()
    return tc_1_value, tc_2_value, tc_3_value, tc_4_value

def stuff_it_in_the_smoke_logging_table(conn, cur, str_timestamp, tc_1_value, tc_2_value, tc_3_value, tc_4_value):
    #hey don, you might want to include OR IGNORE in the insert statement some day.
    try:
        cur.execute("INSERT INTO {tn} ({kn}, {f1}, {f2}, {f3}, {f4}) VALUES ({dts}, {tc1_value}, \
                    {tc2_value}, {tc3_value}, {tc4_value}) ". \
                    format(tn=table_name, kn=key_name, dts=str_timestamp, f1=tc_1_name, tc1_value=tc_1_value,
                           f2=tc_2_name, tc2_value=tc_2_value, f3=tc_3_name, tc3_value=tc_3_value, f4=tc_4_name,
                           tc4_value=tc_4_value))
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
    conn.commit()

def format_now_timestamp():
    timestamp = datetime.datetime.now()
    return "'"+timestamp.strftime('%Y-%m-%d %H:%M:%S')+"'"

def set_exit(self):
    exit_app = 'Y'

class App():


    def __init__(self):

        #set up some database stuff
        # Make some fresh tables using execute()
        global cur, conn
        cur, conn = connect_to_the_database(database_name)
        create_the_smoking_log_table(cur)

        # build a window with a pushbutton
        self.root = tk.Tk()
        self.exit_button = tk.Button(self.root, text="Push me to exit the program", command=set_exit(self))
        self.exit_button.pack()
        self.control_loop()
        self.root.mainloop()

    def control_loop(self):

        str_timestamp = format_now_timestamp()
        print(str_timestamp)

        tc_1_value, tc_2_value, tc_3_value, tc_4_value = generate_data_values()

        # now to stuff it in the smoke logging table
        stuff_it_in_the_smoke_logging_table(conn, cur, str_timestamp, tc_1_value, tc_2_value, tc_3_value,
                                                tc_4_value)

        # and now to do some control stuff ....

        self.root.after(60000,self.control_loop) # insert a data record once a minute

def main(argv):
    app = App()

if __name__ == '__main__':
    main(sys.argv)

# can we exit the program when the user says to?
# can we display data?
# can we acquire data?
# manual: how accurate is the data?
# nothing to do (already covered by Don's smoking practice): how to notice when sensors lose accuracy?
# can we record data?
# can we avoid overwriting previous data?
# can we continue acquiring (and displaying) data even if we can't record it?
# can we display the data in a GUI?
# can we enter values for thermocouple names via GUI?
# can we perform some very simplistic control function based on the data?
# can we enter (via GUI) needed inputs for intended control function?
# can we perform the intended control function?
# can we switch (via GUI) from automatic control to manual?
# can we switch (via GUI) from manual control to automatic?
