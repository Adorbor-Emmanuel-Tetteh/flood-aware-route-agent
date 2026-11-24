"""A* search.

Owner: Gabriel. Starter file, fill in the TODOs.
"""

def a_star(network, start, goal, blocked_roads):
    """Find the cheapest route that avoids blocked_roads.

    Return (route, cost, nodes_expanded), or None if there is no route.
    """
    # TODO: build neighbours from the network (skip blocked roads)
    # TODO: heuristic = grid distance to the goal (never above the real cost,
    #       because every road costs at least 1)
    # TODO: use a priority queue (heapq) and count nodes expanded
    raise NotImplementedError("a_star is not written yet")
