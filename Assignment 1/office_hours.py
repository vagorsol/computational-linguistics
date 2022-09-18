'''    
    Extract and print the office hours of the instructor
    from the CS325 homepage
    Author: Audrey Yang
    Date: September 17, 2022
''' 

import re
import urllib.request

def main():
    url = "https://cs.brynmawr.edu/Courses/cs325/fall2022/"
    ps = urllib.request.urlopen(url).read().decode('utf-8')


    # split intto lines and etc.
    ps_list = ps.split('\n')
    text = " ".join(ps_list)

    # get the specificed line
    my_regex = re.escape("<strong>Office") + r"[\w+ ]+:" + re.escape("</strong>") + r"[\s|\w|:|,|.]+"
    strong_list = re.findall(my_regex, text)
    print(strong_list)

main()