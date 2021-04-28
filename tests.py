import unittest
import logging

import numpy as np

from pizzabot_main import PizzaBot


class TestPizzabot(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        self.pizzabot = PizzaBot()

    def test_1(self):
        logging.info('Check path in 5x5 grid with points (1,3) (4, 4)')
        self.assertEqual(self.pizzabot.deliver_pizza('5x5', np.array([[1, 3], [4, 4]])), 'ENNNDEEEND')

    def test_2(self):
        logging.info('Check path in 5x5 grid with points (0, 0) (1, 3) (4,4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)')
        self.assertEqual(self.pizzabot.deliver_pizza('5x5', np.array(
            [[0, 0], [1, 3], [4, 4], [4, 2], [4, 2], [0, 1], [3, 2], [2, 3], [4, 1]])), 'DNDENNDEDESDEDDSDNNND')


if __name__ == "__main__":
    unittest.main()
