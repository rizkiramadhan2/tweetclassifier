# For more info: https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/python/latest/customsearch_v1.cse.html#list
# To get yours Google APIs Key, enter: <http://code.google.com/apis/console>
# To get your Custom Search Engine Key, enter <https://cse.google.com/cse/all>

#__author__ = 'Caio Granero'
#
#import json
#from pprint import pprint
#from googleapiclient.discovery import build
#
#def getService():
#    service = build("customsearch", "v1",
#            developerKey="AIzaSyDxpJfGwM9KzeTFlKa-_Z-wEgI1sKMcKKo")
#
#    return service
#
#def search_(keyword,amount=3):
#    print(keyword)
#    pageLimit = 1
#    service = getService()
#    startIndex = 1
#    response = []
#
#    for nPage in range(0, pageLimit):
#        #print("Reading page number:"),nPage+1
#
#        response.append(service.cse().list(
#            q=keyword, #Search words
#            cx='001132580745589424302:jbscnf14_dw',  #CSE Key
#            lr='lang_id', #Search language
#            start=startIndex
#        ).execute())
#
#        startIndex = response[nPage].get("queries").get("nextPage")[0].get("startIndex")
#        print(startIndex)
#    with open('data.json', 'w') as outfile:
#        json.dump(response, outfile)
#
#    
#    with open('data.json') as f:
#        data = json.load(f)
#    url=[]
#    i=1
#    for x in data[0]['items']:
#        url.append(x['link'])
#        if i==amount:
#            break
#        i+=1
#        
#    return url



from gsearch.googlesearch import search

class gs:
	def search_(keyword,amount=3):
	    title=[]
	    j=1
	    for u in search(keyword):
	        title.append(u)
	        if j==amount:
	            break
	        j+=1   
	    return title
