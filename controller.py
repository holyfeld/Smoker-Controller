import sys

class Controller():

    has_called_record_yet = False

    def exit(self):
        return(0)

    def format_data(self):
        if (self.has_called_record_yet):
            return("12:12:12, 1, 2, 3, 4\n01:23:45, 5, 6, 7, 8\n")
        else:
            return("12:12:12, 1, 2, 3, 4")

    def display_data(self):
        str_value = self.format_data()
        print (str_value)

    def get_sensor_values(self):
        return 79,80,81,82

    def record_more_data(self, data_to_be_recorded):
        self.has_called_record_yet = True


def main(argv):
    controller = Controller()
    controller.display_data()


if __name__ == '__main__':
    main(sys.argv)