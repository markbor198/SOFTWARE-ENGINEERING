from unittest import main, TestCase
from Maximum import maximum

class MyUnitTests (TestCase):
    def test_1(self):
        self.assertEqual(maximum(3,5,7), 7)
        
if __name__ == "__main__":
    main()
