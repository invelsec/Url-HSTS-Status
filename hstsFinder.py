import optparse
from module.get_hsts_list import downloadList
import json

parser = optparse.OptionParser()
parser.add_option("-u","--url",dest="url",help="url for search in hsts preload list",)
(userIn , arg) = parser.parse_args()
    
if userIn.url != None:
    print(f"HSTS FINDER STARTED! for {userIn.url}")
    downloadList()
    hsts_list = json.load(open("hsts_list.json"))
    try:
        if hsts_list[userIn.url]:
            print("URL FIND IN LIST !!")
            print(f"URL DATA : {hsts_list[userIn.url]}")
    except KeyError:
        print("URL not in List :)")            
else:
    print("Give any url!!")
    exit()
