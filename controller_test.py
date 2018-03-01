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

import unittest
import subprocess
# import controller

class Controller():
    def exit(self):
        return(0)

    def display_data(self):
        return("12:12:12, 1, 2, 3, 4")

class ControllerTest(unittest.TestCase):
    def test_exiting(self):
        instance = Controller()
        return_value = instance.exit()
        self.assertEqual(0, return_value) # is this the right order for a good red-test error message?
        # subprocess.check_call(["ls", "-l", "schmonz"])
#        self.fail("next idea was: extract Controller to separate program, run, check happy and unhappy exit paths")

    def test_display_data(self):
        # garbage time. Do we need to destroy the objects we create?
        instance = Controller()
        return_value = instance.display_data()
        self.assertEqual("12:12:12, 1, 2, 3, 4", return_value)

if __name__ == '__main__':
    unittest.main()
