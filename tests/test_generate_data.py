from src.generate_data import generate_flood_network


def test_same_seed_produces_identical_network() -> None:
    net_1 = generate_flood_network(rows=5, cols=5, seed=99, closure_ratio=0.25)
    net_2 = generate_flood_network(rows=5, cols=5, seed=99, closure_ratio=0.25)
    assert net_1 == net_2
    assert net_1["metadata"]["data_origin"] == "SYNTHETIC_SIMULATED_ONLY"
    assert net_1["metadata"]["human_subjects"] is False


def test_different_seeds_produce_different_closures() -> None:
    net_1 = generate_flood_network(rows=5, cols=5, seed=10, closure_ratio=0.3)
    net_2 = generate_flood_network(rows=5, cols=5, seed=20, closure_ratio=0.3)
    assert net_1["edges"] != net_2["edges"]
