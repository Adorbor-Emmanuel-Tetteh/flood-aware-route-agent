"""Input checks and safe failure.

Owner: Cindy. Starter file, fill in the TODOs.
"""

MAX_STEPS = 200  # step limit so the agent can never loop forever (team can change it)


def validate_request(network, start, goal):
    """Raise ValueError with a clear message if the request is not valid."""
    # TODO: reject a start or goal that is not a junction on the map
    # TODO: reject start == goal if the team decides it is not allowed
    # TODO: handle a missing or empty network
    raise NotImplementedError("validate_request is not written yet")


def no_route_message():
    """Text shown when no route exists. Must say it is a simulation."""
    raise NotImplementedError("no_route_message is not written yet")
