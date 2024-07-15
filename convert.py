import sys
from datetime import datetime
from pathlib import Path
from string import Template

args = sys.argv[1:]

months = [
    "januari",
    "februari",
    "maart",
    "april",
    "mei",
    "juni",
    "juli",
    "augustus",
    "september",
    "oktober",
    "november",
    "december",
]

dt = datetime.fromisoformat(args[1])

date = f"{dt.day} {months[dt.month-1]} {dt.year}"

time = dt.strftime("%H:%M")

glucose_value = round(float(args[0]), 1)

variables = {
    "value": glucose_value,
    "date": date,
    "time": time,
    "workflow_url": f"https://github.com/yochem/glucose/actions/runs/{args[2]}",
}

input_file = Path("template.html")
input_text = input_file.read_text()

result = Template(input_text).substitute(variables)

output_file = Path("public/index.html")
output_file.parent.mkdir(exist_ok=True)
output_file.write_text(result)
