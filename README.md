# yochem.nl/glucose

A simple web page (in Dutch) that shows my last measured glucose value

## But why?
- I have T1D
- Playing with GH Actions is fun
- I want to to be simple, static, and keep my privacy
- Free, simpler and easier than Nightscout

## How it works

Using Apple Shortcuts, a shortcut is fired when I open the
[xdrip4ios](https://github.com/paulplant/xdripswift) app. The shortcut reads
the last glucose value from the Health app (which xdrip puts in there), and
sends it to a GitHub API using the action provided by the GitHub app. TODO: add
screenshot.

The GitHub API allows to run an action with input values. The [GH action
workflow](./.github/workflows/new-entry.yaml) then runs a [Python
script](./convert.py) to convert the data provided by the shortcut to be human
readable, and fills in the values to a [template html](./template.html) file
using simple placeholders. Lastly, the GH action deploys the built site (a
single index.html file in the `public/` folder) to GH pages and serves it for
free!
