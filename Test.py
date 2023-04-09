from MatrixToList import mat_to_list
from Reachable import reachable

if __name__ == "__main__":

    """
    Matrix to List test
    """
    adj_m = [[0, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0]]

    print(mat_to_list(adj_m))


    adj_m = [[1, 1, 0, 1, 0, 0],
             [0, 1, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 1, 0],
             [0, 1, 0, 0, 0, 0],
             [0, 1, 0, 1, 0, 0]]

    print(mat_to_list(adj_m))


    """
    Reachable nodes test
    """

    adj_list = [[1, 3], [2], [0], [4], [3], []]
    print(reachable(adj_list, 5))
    print(reachable(adj_list, 0))
    print(reachable(adj_list, 3))

    adj_list = [[1], [2, 3], [0], [4], [3, 5], [0]]
    print(reachable(adj_list, 5))
    print(reachable(adj_list, 0))
    print(reachable(adj_list, 4))