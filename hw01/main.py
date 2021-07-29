def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
  if query == '':
    return{}
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
  #assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
  assert parse_cookie('name=') == {'name': ''}
  assert parse_cookie('name=Dima;age=28;city=Kharkov') == {'name': 'Dima', 'age': '28', 'city': 'Kharkov'}
  assert parse_cookie('name=Dima;family name=Ivanov;gender=male') == {'name': 'Dima', 'family name': 'Ivanov', 'gender': 'male'}
