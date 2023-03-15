import os
import json

config_path = 'config'

CONFIG = {}
for dir_entry in os.scandir(config_path):
  if dir_entry.is_file():
    with open(dir_entry.path) as setting:
      CONFIG[os.path.splitext(dir_entry.name)[0].upper()] = json.load(setting)
