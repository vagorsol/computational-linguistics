'''    
    Extracts and prints the current weather conditions in Philadelphia
    from the NOAA's weather server
    Author: Audrey Yang
    Date: September 18, 2022
''' 

import re
import urllib.request

def main():
    url = "https://w1.weather.gov/xml/current_obs/display.php?stid=KPHL"
    ps = urllib.request.urlopen(url).read()
    ps = urllib.request.urlopen(url).read().decode('utf-8')

    ps_list = ps.split('\n')
    text = " ".join(ps_list)

    # get the weather status
    weather_regex = re.escape("<weather>") + r"[\w+ ]+" + re.escape("</weather")
    weather = re.findall(weather_regex, text)
    print(weather)

    # get the temperature
    temp_regex = re.escape("<temperature_string>") + r"[\s|\w|\(|\)|.|\S]+" + re.escape("</temp_c")
    temp = re.findall(temp_regex, text)
    print(temp)

main()