import numpy as np


class PizzaBot:

    def __init__(self):
        self.WAY_DICT = {'move_north': 'N',
                         'move_south': 'S',
                         'move_east': 'E',
                         'move_west': 'W',
                         'drop_pizza': 'D'}

    def get_x_y_distance(self, point_1, point_2):

        """
        Returns x and y difference between two points

        Parameters:
            point_1 (list): List with pizza delivery point coordinates.
            point_2 (list): List with pizza delivery point coordinates.

        Returns:
             (int, int): tuple with int difference between x coordinates and y coordinates of two points.
        """

        return point_2[0] - point_1[0], point_2[1] - point_1[1]

    def sort_points(self, points):

        """
        Returns the points of pizza delivery coordinates in sorted order.

        Algorithm of sorting starts from finding the closest point to (0,0) and
        sequentially builds the shortest path between last found point and the remaining ones.

         Parameters:
            nodes (np.array): 2D numpy array with pizza delivery points.

        Returns:
             (np.array): 2D numpy array with pizza delivery points in sorted way.
        """

        points_way = []
        nodes_len = len(points)
        point = [0, 0]
        while len(points_way) != nodes_len:
            dist_array = np.sum(abs(points - point), axis=1)
            clos_node = np.argmin(dist_array)
            point = points[clos_node]
            points_way.append(point)
            points = np.delete(points, clos_node, 0)

        return np.array(points_way)

    def deliver_pizza(self, matrix, points):
        """
            Returns all way between all pizza delivery points

            Parameters:
                path (np.array): List with pizza delivery point coordinates.

            Returns:
                all_way (str): String of instructions for getting Pizzabot to all locations and delivering.
            """

        path = self.sort_points(points)
        path = np.insert(path, 0, [0, 0], axis=0)
        all_way = ""
        for i in range(len(path) - 1):
            point_1 = path[i]
            point_2 = path[i + 1]
            dist_x, dist_y = self.get_x_y_distance(point_1, point_2)
            if dist_x < 0:
                key_x = 'move_west'
            else:
                key_x = 'move_east'

            if dist_y < 0:
                key_y = 'move_south'
            else:
                key_y = 'move_north'

            x_path = self.WAY_DICT.get(key_x)
            y_path = self.WAY_DICT.get(key_y)

            all_way = all_way + (abs(dist_x) * x_path)
            all_way = all_way + (abs(dist_y) * y_path)
            all_way = all_way + (self.WAY_DICT.get('drop_pizza'))

        return all_way
