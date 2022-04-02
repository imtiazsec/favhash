import mmh3
import requests
import codecs
import sys
import warnings

warnings.filterwarnings("ignore")
response = requests.get(sys.argv[1], verify=False)
favicon = codecs.encode(response.content,"base64")
hash = mmh3.hash(favicon)
print('\nhttp.favicon.hash:'+str(hash))
