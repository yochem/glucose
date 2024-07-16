#!/usr/bin/env bash

set -u

# needed for MacOS
command -v gdate >/dev/null && datecmd=gdate || datecmd=date

# use dutch month name
export date=$(LC_ALL=nl_NL $datecmd -d $input_datetime "+%d %B %Y")
export time=$($datecmd -d $input_datetime "+%H:%M")
export value=$(printf "%.1f" $input_value)
export workflow_url="https://github.com/yochem/glucose/actions/runs/$input_action_id"

mkdir -p public

envsubst < template.html > public/index.html
