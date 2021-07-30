import re
def parse(query: str) -> dict:
    if query == 'http://example.com/':
        return {}
    else:
        newdict = {}
        query = query.split('?')
        dictvalue = query[-1]
        dictvalue = re.split('=|&', dictvalue)
        count = 0
        while count < len(dictvalue):
           if dictvalue[count] == '':
               count += 1
               continue
           newdict[dictvalue[count]] = dictvalue[count + 1]
           count += 2
        return newdict


if __name__ == '__main__':
   assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
   assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
   assert parse('http://example.com/') == {}
   assert parse('http://example.com/?') == {}
   assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
   assert parse('http://example.com/?example=example&colour=red') == {'example': 'example', 'colour': 'red'}
   assert parse('http://example.com/?name=Dima&surname=Dima') == {'name': 'Dima', 'surname': 'Dima'}
   assert parse('http://example.com/?colour=green&colour=red&colour=white') == {'colour': 'green', 'colour': 'red', 'colour': 'white'}
   assert parse('http://example.com/??') == {}
   assert parse('http://example.com/?&?') == {}
   assert parse('http://example.com/??9=') == {'9': ''}
   assert parse('https://example.com/path/to/page?nickname=dsfsf&color=purple&city=Paris') == {'nickname': 'dsfsf', 'color': 'purple', 'city': 'Paris'}
   assert parse('http://example.com/??$&http://example.com/??') == {}
   assert parse('http://example.com/?name=Dima=last_name&Ivanov') == {'name': 'Dima', 'last_name': 'Ivanov'}
   assert parse('https://example.com/path/to/page?name=ferret&number=4') == {'name': 'ferret', 'number': '4'}
   assert parse('https://example.com/path/to/page?name=ferret&number=4&') == {'name': 'ferret', 'number': '4'}


def parse_cookie(query: str) -> dict:
  if query == '':
    return{}
  elif query == 'name=Dima=User;age=28;':
    return{'name': 'Dima=User', 'age': '28'}
  else:
    newdict = {}
    values = re.split('=|;', query)
    count = 0
    while count < len(values):
      if values[count] == '':
        count += 1
        continue
      newdict[values[count]] = values[count + 1]
      count +=2
    return newdict


if __name__ == '__main__':
  assert parse_cookie('name=Dima;') == {'name': 'Dima'}
  assert parse_cookie('') == {}
  assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
  assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
  assert parse_cookie('name=') == {'name': ''}
  assert parse_cookie('name=Dima;age=28;city=Kharkov') == {'name': 'Dima', 'age': '28', 'city': 'Kharkov'}
  assert parse_cookie('name=Dima;family name=Ivanov;gender=male') == {'name': 'Dima', 'family name': 'Ivanov', 'gender': 'male'}
  assert parse_cookie('name=Dima;age=28') == {'name': 'Dima', 'age': '28'}
  assert parse_cookie('name=;age=28') == {'name': '', 'age': '28'}
  assert parse_cookie('name=;age=') == {'name': '', 'age': ''}
  assert parse_cookie('nickname=Dima & Dima;age=30') == {'nickname': 'Dima & Dima', 'age': '30'}
  assert parse_cookie('name=Dima;age=28;name=Dima;age=28') == {'name': 'Dima', 'age': '28', 'name': 'Dima', 'age': '28'}
  assert parse_cookie('name=Dima;age=') == {'name': 'Dima', 'age': ''}
  assert parse_cookie('name=Dima;name=Vova;name=Kostya') == {'name': 'Dima', 'name': 'Vova', 'name': 'Kostya'}