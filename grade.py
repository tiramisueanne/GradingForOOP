import webbrowser
import re
import json
import sys
import os

directory = "./submissions";
project_num = "Project #4";
your_hackerrank = "tiramisueanne";
hackerrank_url = "https://www.hackerrank.com/contests/cs371p-spring-2018-darwin/compare/" + your_hackerrank + "/";
#thank you python, for the one good thing you do
named_proj = [x for x in os.listdir(directory) if not x.startswith("project") ];
group_proj = [x for x in os.listdir(directory) if x.startswith("project") ];
# Note to self, don't need the delimeters in python
# Essentially, sort on the first set of numbers that canvas spits at us
regex = '\d+(?=_)';
regex = re.compile(regex);
group_proj = sorted(group_proj, key=lambda x: int(re.search(regex, x).group(0))); 
# So, Canvas does a really annoying thing, where group/unnamed submission are still in there alphabetically
for file in sorted(os.listdir(directory)):
    index = 0;
    #Check if we are in the group range
    if file in group_proj: 
        #Rename the filename with one from our sorted list 
        file = group_proj[index];
        index += 1
    filename = directory + "/" + file;
    open_file = open(filename);
    print(filename);
    if filename.endswith(".json"):
        submission = json.load(open_file);
        webbrowser.open_new_tab(hackerrank_url + submission[project_num]["HackerRank ID"]);
        webbrowser.open_new_tab(submission[project_num]["GitHub URL"])
        webbrowser.open_new_tab(submission[project_num]["Travis CI URL"])
        check_remove = raw_input("If you want to remove the file, then please type 'r', otherwise, hit any key");
        if check_remove == 'r':
            os.remove(filename);
    

