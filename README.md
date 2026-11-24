# Flood-Aware Route Agent

This project is a **simulation, not real navigation software**.

## Research Question
On the same simulated scenarios with hidden road closures, does an agent that re-plans when it finds a closed road complete more trips than an agent that plans only once at the start, and how much extra travel cost and search effort does re-planning need?

## Data and Ethics Notice
All maps, flood/road closures, scenarios, and evaluation results in this repository are **synthetic and simulated only**. No real-world personal data, human participants, passwords, or API keys are used.

## Team and Roles
| Member | Role / Responsibilities |
| :--- | :--- |
| Emmanuel | Repo setup & maintenance; `src/logger.py`; co-owner of `src/run_experiment.py` (with Gabriel) |
| Mimi | `src/generate_map.py`, `src/closures.py`, `src/scenarios.py`, and evaluation protocol |
| Gabriel | `src/planner.py`, `src/agent.py`, and co-owner of `src/run_experiment.py` (with Emmanuel) |
| Cindy | `src/validators.py`, `src/demo.py`, and risk/ethics/problem sections |
| Valery | `src/make_tables.py`, `src/plot_routes.py`, and literature/sources |

## Folder Structure
- `src/` — Simulation modules (`generate_map.py`, `closures.py`, `scenarios.py`, `planner.py`, `agent.py`, `validators.py`, `logger.py`, `run_experiment.py`, `demo.py`, `make_tables.py`, `plot_routes.py`)
- `tests/` — Automated `pytest` test suite
- `data/` — Synthetic data notes (`data/README.md`)
- `evaluation/` — Frozen scenario list and evaluation scripts
- `results/` — Generated tables, figures, and logs
- `docs/` — M2 proposal, architecture figure, system card, and report datasheet

## Quick Start
1. **Install dependencies:**
   ```powershell
   python -m pip install -r requirements.txt
   ```
2. **Generate synthetic map/data:**
   ```powershell
   python -m src.generate_data --seed 42 --output data/sample_network_seed42.json
   ```
3. **Run tests:**
   ```powershell
   python -m pytest
   ```
