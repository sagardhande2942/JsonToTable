"""Parser module for the project."""

import json
import pathlib

from jsoncomment import JsonComment

from .table import Table
from .text_field import TextField

types_mapping = {
  "string": str,
  "boolean": bool,
  "float": float
}

def parse_table(file_path: pathlib.Path) -> Table:
  json_parser = JsonComment(json)
  data = json_parser.loads(file_path.read_text())
  table = Table()
  for row, data in data.items():
    rows = []
    for column, value in data.items():
      if column not in table: 
        table.add_column(column, types_mapping[value["type"]])
      rows.append(value["value"])
    table.add_rows(rows)
  return table
