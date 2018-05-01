import sys

class Controller():
    def __init__(self):
        self.recorded_data = []

    def exit(self):
        return(0)

    def format_data(self):
        formatted_data = ''
        for each in self.recorded_data:
            formatted_data += "{}, {}, {}, {}, {}".format(each[0], each[1], each[2], each[3], each[4]) + "\n"
        return(formatted_data)

    def display_data(self):
        str_value = self.format_data()
        print (str_value)

    def get_sensor_values(self):
        return 79,80,81,82

    def record_more_data(self, data_to_be_recorded):
        self.recorded_data.append(data_to_be_recorded)


def main(argv):
    controller = Controller()
    controller.display_data()


if __name__ == '__main__':
    main(sys.argv)
