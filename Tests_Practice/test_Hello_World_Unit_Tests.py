import unittest
from Hello_World import Greetings
class HelloWorldTestClass(unittest.TestCase):
    def test_HelloWorld(self):
        self.assertEqual(Greetings(), 'Hello World')
if __name__ == '__main__':
    unittest.main()