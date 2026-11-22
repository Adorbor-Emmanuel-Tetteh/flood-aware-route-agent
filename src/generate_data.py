import argparse
import json
import random
from pathlib import Path
from typing import Any


def generate_flood_network(
    rows: int = 6,
    cols: int = 6,
    seed: int = 42,
    closure_ratio: float = 0.2,
) -> dict[str, Any]:
    """Generate a deterministic (seeded) synthetic grid road network with flood closures."""
    if rows < 2 or cols < 2:
        raise ValueError("rows and cols must both be at least 2.")
    if not 0.0 <= closure_ratio < 1.0:
        raise ValueError("closure_ratio must be between 0.0 and 0.99.")

    rng = random.Random(seed)
    nodes: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []

    for r in range(rows):
        for c in range(cols):
            node_id = f"N_{r}_{c}"
            nodes.append({"id": node_id, "row": r, "col": c})

    def add_road(u: str, v: str, idx: int) -> None:
        edges.append(
            {
                "id": f"E_{idx}",
                "source": u,
                "target": v,
                "base_travel_time": round(rng.uniform(1.0, 3.0), 2),
                "status": "open",
                "closure_type": None,
                "flood_severity": 0.0,
            }
        )

    edge_idx = 0
    for r in range(rows):
        for c in range(cols):
            u = f"N_{r}_{c}"
            if c + 1 < cols:
                add_road(u, f"N_{r}_{c + 1}", edge_idx)
                edge_idx += 1
            if r + 1 < rows:
                add_road(u, f"N_{r + 1}_{c}", edge_idx)
                edge_idx += 1

    closure_types = ["fixed_from_start", "random", "found_on_arrival"]
    num_closed = int(len(edges) * closure_ratio)
    closed_indices = set(rng.sample(range(len(edges)), k=num_closed))

    for idx in closed_indices:
        edges[idx]["status"] = "closed"
        edges[idx]["closure_type"] = rng.choice(closure_types)
        edges[idx]["flood_severity"] = round(rng.uniform(0.5, 1.0), 2)

    return {
        "metadata": {
            "data_origin": "SYNTHETIC_SIMULATED_ONLY",
            "human_subjects": False,
            "seed": seed,
            "grid_size": {"rows": rows, "cols": cols},
            "node_count": len(nodes),
            "edge_count": len(edges),
            "closed_edge_count": num_closed,
        },
        "start_node": "N_0_0",
        "goal_node": f"N_{rows - 1}_{cols - 1}",
        "nodes": nodes,
        "edges": edges,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate synthetic seeded flood-road network data."
    )
    parser.add_argument("--rows", type=int, default=6, help="Number of grid rows")
    parser.add_argument("--cols", type=int, default=6, help="Number of grid columns")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument(
        "--closure-ratio",
        type=float,
        default=0.2,
        help="Fraction of edges marked closed/flooded (0.0 to 0.99)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/sample_network_seed42.json"),
        help="Output JSON file path",
    )
    args = parser.parse_args()

    dataset = generate_flood_network(
        rows=args.rows,
        cols=args.cols,
        seed=args.seed,
        closure_ratio=args.closure_ratio,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(dataset, indent=2), encoding="utf-8")
    print(f"Saved synthetic dataset to {args.output}")


if __name__ == "__main__":
    main()
