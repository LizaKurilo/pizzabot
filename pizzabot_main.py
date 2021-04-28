import logging
import sys

from pizzabot_engine import PizzaBot
from validation_parse_module import validate_and_parse_input

if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG)

    try:
        args = sys.argv[1]
    except (SyntaxError, TypeError, NameError, IndexError):
        args = open("./txtfiles/test.txt").read()
        logging.info(f"Set input args from txtfiles/test.txt: {args}")
    #args = "5x5 (0, 0) (1, 3) (4,4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)"
    # args = '5x5 (1, 3) (4, 4)'
    matrix, points = validate_and_parse_input(args)

    pizzabot = PizzaBot()
    delivery_path = pizzabot.deliver_pizza(matrix, points)
    logging.info(delivery_path)
