import urllib.request
import re

URL = 'http://www.a2zwordfinder.com/cgi-bin/scrabble.cgi'
postDictionary = {
    'SearchType': 'Scrabble',
    'Pattern': '',
    'MatchType': 'Anywhere',
    'SubmitScrabble': 'Go',
    'MinLetters' : '2',
    'SortBy': 'Score'
}

# Letter input goes here
postDictionary['Letters'] = 'rivienwasrauuanr'

postRequest = urllib.parse.urlencode(postDictionary)
req = urllib.request.Request(URL + '?' + postRequest)
response = urllib.request.urlopen(req)
rawPage = response.read().decode('utf-8')
wordsFoundPattern = re.compile('(?<=<font face=Courier>\n)\w+?(?=</font>)')
wordsPresent = wordsFoundPattern.search(rawPage)
if wordsPresent is None:
    print('No words found!')
else:
    print(wordsPresent.group(0))
response.close()