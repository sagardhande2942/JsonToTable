import pathlib

from json_to_table import table_parser


def test_parse_table():

  file_path = pathlib.Path("/Users/sagardhande/Desktop/Project/trad/json_to_table/sample/sample1.json")
  table = table_parser.parse_table(file_path)
  output_file = file_path.parent / "output.html"
  output_file.write_text(table.to_html())

if __name__ == "__main__":
  test_parse_table()
