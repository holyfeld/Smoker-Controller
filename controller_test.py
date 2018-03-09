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

import unittest

from controller import Controller


def is_number(stringy_thingy):
    try:
        float(stringy_thingy)
        return True
    except ValueError:
        return False


class ControllerTest(unittest.TestCase):
    def test_exiting(self):
        instance = Controller()
        return_value = instance.exit()
        self.assertEqual(return_value,0)

    def test_display_data(self):
        instance = Controller()
        return_value = instance.format_data()
        self.assertEqual(return_value, "12:12:12, 1, 2, 3, 4")

    def test_does_sensor_send_value(self):
        instance = Controller()
        temperature = instance.get_sensor_value()
        self.assertIsNotNone(temperature)

    def test_is_sensor_value_valid(self):
        instance = Controller()
        temperature = instance.get_sensor_value()
        self.assertTrue(is_number(temperature))
        self.assertGreaterEqual(temperature,-250.0)
        self.assertLessEqual(temperature,1000)


if __name__ == '__main__':
    unittest.main()
