import webbrowser
import json
import sys
import os

directory = "./submissions";
project_num = "Project #4";
your_hackerrank = "tiramisueanne";
hackerrank_url = "https://www.hackerrank.com/contests/cs371p-spring-2018-darwin/compare/" + your_hackerrank + "/";
for file in os.listdir(directory):
    filename = directory + "/"+ file;
    open_file = open(filename);
    if filename.endswith(".json"):
        submission = json.load(open_file);
        webbrowser.open_new_tab(hackerrank_url + submission[project_num]["HackerRank ID"]);
        webbrowser.open_new_tab(submission[project_num]["GitHub URL"])
        webbrowser.open_new_tab(submission[project_num]["Travis CI URL"])
        raw_input("Press enter to continue..");


