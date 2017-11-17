#
# Smoker controller using the Raspberry Pi
#
# version .5 getting started. Create the one second run forever loop, initially print the count, and every 60 counts
# store some numbers in a SQL Lite table.
#
# grab the imports

import random
import sqlite3
import string
from time import sleep
import datetime
#from flask import Flask
import sys

# may want to create an init function in the future?
#
# start with the web server
#app = Flask(__name__)

#
# may want to create an init function in the future? for now, hard code the table name, drop if it exists, and
# create a clean table.
#
# and for good mechanics, throw in a try/except when we get real.
# sqlite portions inspired by http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

table_name = 'DataRecords'
key_name = "DateTimeStamp"
tc_1_name = "ChamberTemp"
tc_2_name = "Probe1"
tc_3_name = "Probe2"
tc_4_name = "Probe3"

conn = sqlite3.connect('Data/SmokerData.db')
cur = conn.cursor()


def create_the_smoking_log_table():
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

def stuff_it_in_the_smoke_logging_table(str_timestamp, tc_1_value, tc_2_value, tc_3_value, tc_4_value):
    try:
        cur.execute("INSERT OR IGNORE INTO {tn} ({kn}, {f1}, {f2}, {f3}, {f4}) VALUES ({dts}, {tc1_value}, \
                    {tc2_value}, {tc3_value}, {tc4_value}) ". \
                    format(tn=table_name, kn=key_name, dts=str_timestamp, f1=tc_1_name, tc1_value=tc_1_value,
                           f2=tc_2_name, tc2_value=tc_2_value, f3=tc_3_name, tc3_value=tc_3_value, f4=tc_4_name,
                           tc4_value=tc_4_value))
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
    conn.commit()

# Some day, we'll create a control function. For now, we're just going to loop here until I get tired of pressing Y

def format_now_timestamp():
    timestamp = datetime.datetime.now()
    return "'"+timestamp.strftime('%Y-%m-%d %H:%M:%S')+"'"

def control_loop():
    answer = "n"
    count = 0

    while answer != "Y":
        count += 1
        print(count)
        sleep(1)    #sleep for a second
        if count == 10:
            # it's a minute later. (someday)
            # reset the timer (count)
            count = 0
            # Time to insert a data record.
            # get a formatted time for inserting into the table
            str_timestamp = format_now_timestamp()
            print(str_timestamp)

            tc_1_value, tc_2_value, tc_3_value, tc_4_value = generate_data_values()

            # now to stuff it in the smoke logging table
            stuff_it_in_the_smoke_logging_table(str_timestamp, tc_1_value, tc_2_value, tc_3_value, tc_4_value)

            # and now to do some control stuff ....

            answer = input('Ready to quit?: ')

def main(argv):
    # Make some fresh tables using execute()
    create_the_smoking_log_table()
    control_loop()

if __name__ == '__main__':
    main(sys.argv)
