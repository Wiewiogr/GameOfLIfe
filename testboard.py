import unittest
import board

class TestBoardClass(unittest.TestCase):

    def testBoardShouldRasiseExceptionWhenInitWithLivingGreaterThanSize(self):
        testBoard = board.Board(10,100)
        self.assertRaises(Exception)

    def testAmountOfCells(self):
        testBoard = board.Board(10,20)
        self.assertEqual(20,testBoard.numberOfCells)

if __name__ == "__main__":
    unittest.main(verbosity=2)
