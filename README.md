# Flood-Aware Route Agent (M2)

Milestone 2 (Proposal and Design) repository for the Flood-Aware Route Agent project.

## Data & Ethics Notice
- All road network data and flood closure scenarios in this repository are **synthetic and simulated only**.
- This project involves **no human participants** and uses no real-world personal or sensitive data.

## Repository Structure
- `src/` - Source code, including seeded synthetic road/closure data generation
- `data/` - Generated synthetic datasets (simulated)
- `tests/` - Automated checks and unit tests
- `evaluation/` - Evaluation scripts and comparison logic
- `results/` - Experiment outputs and summaries
- `docs/` - M2 design documentation and notes
- `ai_use_log.md` - Log of AI assistance and how outputs were checked

## Quick Start (PowerShell)
1. Install dependencies: `pip install -r requirements.txt`
2. Generate a seeded synthetic dataset: `python -m src.generate_data --seed 42 --output data/sample_network_seed42.json`
3. Run tests: `pytest`
