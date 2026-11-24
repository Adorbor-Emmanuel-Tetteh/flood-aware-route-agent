"""The plan-once baseline, the re-planning agent and the oracle.

Owner: Gabriel. Starter file, fill in the TODOs.
"""

# Every function returns a dict like:
# {"outcome": "success" | "failure" | "no_route", "route": [...], "cost": 0.0,
#  "nodes_expanded": 0, "replans": 0}


def run_plan_once(network, start, goal, closed_roads, max_steps):
    """Plan once with A*, follow the route, stop at the first closed road (failure)."""
    raise NotImplementedError("run_plan_once is not written yet")


def run_replanning(network, start, goal, closed_roads, max_steps):
    """Same as plan-once, but on a closed road: mark it, then re-plan from here."""
    raise NotImplementedError("run_replanning is not written yet")


def run_oracle(network, start, goal, closed_roads):
    """Reference run: A* with every closure known from the start (the cost floor)."""
    raise NotImplementedError("run_oracle is not written yet")
