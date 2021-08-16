import  requests

app_id = "c71a7ea1"
app_key = "53b8e9c03bb2f03b3a985091000fc3b9"
language = "en-gb"

def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res = r.json()
    if 'eror' in res.keys():
        return False

    output = {}
    senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        definitions.append(f"👉{sense['definitions'][0]}")
    output['definitions'] = "\n".join(definitions)

    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio'] = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

    return output
if __name__ == '__main__':
    from pprint import pprint as print
    print(getDefinitions('Great Britain'))
    print(getDefinitions('america'))


