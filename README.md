# Network Source of Truth PoC

This project demonstrates a simple NetDevOps proof of concept that treats network configuration as code.

It uses structured YAML data as a source of truth, Jinja2 templates for configuration generation, and Python to render device-specific configs.

## Why this project exists

Modern network teams are increasingly adopting DevOps practices such as version control, templating, validation, and CI/CD. This repository is a lightweight example of how network configuration workflows can be modeled in a repeatable and scalable way.

## Current capabilities

- Stores device inventory and interface data in YAML
- Uses Jinja2 templates to generate device configurations
- Renders one config per device
- Separates source data from rendering logic

## Repository structure

```text
.
├── data/
│   └── devices.yaml
├── templates/
│   └── base_config.j2
├── scripts/
│   └── render_configs.py
├── rendered/
│   ├── core-1.cfg
│   └── edge-1.cfg
├── requirements.txt
└── README.md
