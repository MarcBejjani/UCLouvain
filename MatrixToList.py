def mat_to_list(adj_mat):
    """ Convert adjacency matrix to an adjacency list representation

    Parameters:
    -----------
    adj_mat : (a square 0-1 matrix)
        Adjacency matrix (n x n) of the graph (of n nodes)


    Returns:
    --------
     adj_list: `list[list[int]]`
        The adjacency list of the graph

    """
    # TODO
    adj_list = []
    for row in adj_mat:
        to_add = []
        for idx, el in enumerate(row):
            if el == 1:
                to_add.append(idx)
        adj_list.append(to_add)
        
    return adj_list
