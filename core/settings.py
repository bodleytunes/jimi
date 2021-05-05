import json
from pathlib import Path
from os import environ
import os



with open(str(Path("data/settings.json"))) as f:
  config = json.load(f)

# Over-ride via environment vars
if os.getenv("JIMI_DB") is not None:
  config['mongodb']['hosts'][0] = os.getenv("JIMI_DB")


