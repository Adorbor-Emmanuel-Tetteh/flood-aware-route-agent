"""Checks on the generated road network (replaces the 4 placeholder tests)."""
import pytest
from src.generate_data import generate_flood_network


def test_seeded_network_is_reproducible():
    a = generate_flood_network(rows=5, cols=5, seed=7, closure_ratio=0.2)
    b = generate_flood_network(rows=5, cols=5, seed=7, closure_ratio=0.2)
    assert a == b


def test_dimensions_and_every_junction_reachable_on_base_grid():
    rows, cols = 4, 6
    net = generate_flood_network(rows=rows, cols=cols, seed=1, closure_ratio=0.0)
    assert net["metadata"]["node_count"] == rows * cols
    assert net["metadata"]["edge_count"] == rows * (cols - 1) + cols * (rows - 1)
    # walk the grid ignoring closures: with ratio 0 every junction must be reachable
    adj = {n["id"]: [] for n in net["nodes"]}
    for e in net["edges"]:
        adj[e["source"]].append(e["target"])
        adj[e["target"]].append(e["source"])
    seen, stack = set(), [net["start_node"]]
    while stack:
        cur = stack.pop()
        if cur in seen:
            continue
        seen.add(cur)
        stack.extend(adj[cur])
    assert len(seen) == rows * cols


def test_closed_edge_count_matches_ratio_and_status_values():
    net = generate_flood_network(rows=6, cols=6, seed=3, closure_ratio=0.25)
    closed = [e for e in net["edges"] if e["status"] == "closed"]
    assert len(closed) == net["metadata"]["closed_edge_count"]
    assert len(closed) == int(len(net["edges"]) * 0.25)
    assert all(e["status"] in ("open", "closed") for e in net["edges"])


def test_data_is_labelled_synthetic():
    net = generate_flood_network(seed=5)
    assert net["metadata"]["data_origin"] == "SYNTHETIC_SIMULATED_ONLY"
    assert net["metadata"]["human_subjects"] is False


def test_every_road_costs_at_least_one():
    # grid-distance heuristic stays admissible only if no road is cheaper than 1
    net = generate_flood_network(seed=11)
    assert all(e["base_travel_time"] >= 1.0 for e in net["edges"])


def test_bad_inputs_are_rejected():
    with pytest.raises(ValueError):
        generate_flood_network(rows=1, cols=5)
    with pytest.raises(ValueError):
        generate_flood_network(closure_ratio=1.0)
