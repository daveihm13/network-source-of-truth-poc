# Network Source of Truth PoC

This project demonstrates a NetDevOps-style approach to managing network configurations using a source of truth model.

## Overview

- Device data is stored in YAML (source of truth)
- Jinja2 templates generate configurations
- Python script renders configs per device

## Structure

- `data/` → structured network data
- `templates/` → configuration templates
- `scripts/` → rendering logic
- `rendered/` → generated configs

## How to run

```bash
pip install pyyaml jinja2
python scripts/render_configs.py
