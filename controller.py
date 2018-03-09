import sys

class Controller():
    def exit(self):
        return(0)

    def format_data(self):
        return("12:12:12, 1, 2, 3, 4")

    def display_data(self):
        str_value = self.format_data()
        print (str_value)

    def get_sensor_value(self):
        return 79


def main(argv):
    controller = Controller()
    controller.display_data()


if __name__ == '__main__':
    main(sys.argv)