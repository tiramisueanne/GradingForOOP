import webbrowser
import json
import sys

submission = json.load(sys.stdin);

print submission["Project #1"]["Name"], "'s Submission "
webbrowser.open_new_tab(submission["Project #1"]["GitHub URL"])
webbrowser.open_new_tab(submission["Project #1"]["Travis CI URL"])

