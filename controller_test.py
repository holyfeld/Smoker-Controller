# Start here next time
# can we record data?
#   1. defer writing until later.
#   2. write test, invent a method for inserting data
#   3. build data structure probably an array of dictionary
#   4.
# can we acquire data from real source?
# manual: how accurate is the data?
# nothing to do (already covered by Don's smoking practice): how to notice when sensors lose accuracy?
# can we record data to somewhere persistant?
# can we avoid overwriting previous data?
# can we continue acquiring (and displaying) data even if we can't record it?
# can we display the data in a GUI?
# can we enter values for thermocouple names via GUI?
# can we perform some very simplistic control function based on the data?
# can we enter (via GUI) needed inputs for intended control function?
# can we perform the intended control function?
# can we switch (via GUI) from automatic control to manual?
# can we switch (via GUI) from manual control to automatic?

import unittest

from controller import Controller


def is_number(stringy_thingy):
    try:
        float(stringy_thingy)
        return True
    except ValueError:
        return False


class ControllerTest(unittest.TestCase):
    def assert_sensor_value_is_valid(self, sensor_value):
        self.assertTrue(is_number(sensor_value))
        self.assertGreaterEqual(sensor_value, -250.0)
        self.assertLessEqual(sensor_value, 1000)

    def test_exiting(self):
        instance = Controller()
        return_value = instance.exit()
        self.assertEqual(return_value,0)

    def test_record_and_display_some_data(self):
        instance = Controller()
        instance.record_more_data(["12:12:12", 1, 2, 3, 4])
        self.assertEqual(instance.format_data(), "12:12:12, 1, 2, 3, 4\n")

    def test_does_sensor_send_values(self):
        instance = Controller()
        tc1, tc2, tc3, tc4 = instance.get_sensor_values()
        self.assertIsNotNone(tc1)
        self.assertIsNotNone(tc2)
        self.assertIsNotNone(tc3)
        self.assertIsNotNone(tc4)

    def test_is_sensor_value_valid(self):
        instance = Controller()
        tc1, tc2, tc3, tc4 = instance.get_sensor_values()
        self.assert_sensor_value_is_valid(tc1)
        self.assert_sensor_value_is_valid(tc2)
        self.assert_sensor_value_is_valid(tc3)
        self.assert_sensor_value_is_valid(tc4)

    def test_record_more_data(self):
        instance = Controller()
        instance.record_more_data(["12:12:12", 1, 2, 3, 4])
        self.assertEqual(instance.format_data(), "12:12:12, 1, 2, 3, 4\n")
        instance.record_more_data(["01:23:45", 5, 6, 7, 8])
        self.assertEqual(instance.format_data(), "12:12:12, 1, 2, 3, 4\n01:23:45, 5, 6, 7, 8\n")


if __name__ == '__main__':
    unittest.main()
