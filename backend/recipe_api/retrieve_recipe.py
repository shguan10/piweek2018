import requests

APP_ID = 'e811971b'
APP_KEY = 'a3c3643b01d6b5ad082737af19af71a6'
URL = 'https://api.edamam.com/search'

def retrieve(ingredients):
  query = ''
  for ingr in ingredients:
    query = ingr + ',' + query
  param = {'q': query, 'app_id': APP_ID, 'app_key': APP_KEY}
  r = requests.get(URL, params=param)
  return r.json()

def main():
  retrieve(['apple','flour'])

if __name__=='__main__': main()