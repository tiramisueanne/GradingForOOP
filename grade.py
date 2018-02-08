import webbrowser
import json


submission = json.load();

print submission["Name"], "'s Submission "
webbrowser.open_new_tab(submission["GitHub URL"])
webbrowser.open_new_tab(submission["Travis CI URL"])

