import locale
import sys
from datetime import datetime
from pathlib import Path
from string import Template

args = sys.argv[1:]

locale.setlocale(locale.LC_TIME, "nl_NL")

dt = datetime.fromisoformat(args[1])

date = dt.strftime("%d %B %Y")
time = dt.strftime("%H:%M")

glucose_value = round(float(args[0]), 1)

variables = {
    "value": glucose_value,
    "date": date,
    "time": time,
    "workflow_url": args[2],
}

input_file = Path("template.html")
input_text = input_file.read_text()

result = Template(input_text).substitute(variables)

output_file = Path("public/index.html")
output_file.parent.mkdir(exist_ok=True)
output_file.write_text(result)
