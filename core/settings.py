import json
from pathlib import Path
from os import environ
import os



with open(str(Path("data/settings.json"))) as f:
  config = json.load(f)




