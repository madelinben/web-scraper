import pprint, requests

url = "http://www.madelinben.co.uk/"
data = requests.get(url)

pprint.pprint(data.content)