

# test/my_frame_test.py

import unittest

from my_lambdata.my_frames import MyFrame

class TestMyFrame(unittest.TestCase):

    def test_add_state_names(self):
        my_frame = MyFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
        # test to make sure this test was setup properly
        self.assertTrue("name" not in my_frame.columns.tolist())

        my_frame.add_state_names() # directly invoke the code we wish to test
        #print(my_frame.head())
        #breakpoint()

        # assert there exists a name column
        self.assertTrue("name" in my_frame.columns.tolist())

        # assert there are string values in the "name" col
        self.assertTrue(isinstance(my_frame["name"][0], str))

        # assert specific corresponding values in for example the first row
        self.assertEqual(my_frame["abbrev"][0], "CT")
        self.assertEqual(my_frame["name"][0], "Connecticut")

if __name__ == '__main__':
    unittest.main()
