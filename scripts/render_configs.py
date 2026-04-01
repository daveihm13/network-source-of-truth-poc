import yaml
from jinja2 import Environment, FileSystemLoader
import os

# Load YAML data
with open("data/devices.yaml") as f:
    data = yaml.safe_load(f)

# Setup Jinja2
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("base_config.j2")

# Ensure output directory exists
os.makedirs("rendered", exist_ok=True)

# Render configs per device
for device in data["devices"]:
    output = template.render(**device)

    filename = f"rendered/{device['hostname']}.cfg"
    with open(filename, "w") as f:
        f.write(output)

    print(f"Rendered config for {device['hostname']}")
