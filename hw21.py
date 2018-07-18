def isint(value):
  try:
    int(value)
    return True
  except ValueError:
    return False


def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def get_shop_list_by_dishes(dishes, person_count, cook_book):
  shop_list = {}
  for dish in dishes:
    if not dish in cook_book:
      print('Блюдо "{}" не описано в кулинарной книге'.format(dish))
      continue
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def create_shop_list(cook_book):
  person_count = int(input('Введите количество человек: '))
  dishes = ['салат', 'стейк', 'омлет']
  shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
  print_shop_list(shop_list)


def get_reciept(file):
  counter = 0
  dish = ''

  with open(file) as f:
    cook_book = {}
    for line in f:
      line = line.strip('\n').strip().lower()
      if not line:
        counter = 0
        dish = ''
        continue

      if counter == 0:
        if isint(line):
          counter = int(line)
        else:
          dish = line
          cook_book[dish] = []
      else:
        my = '{' + '"ingridient_name":"{str[0]}","quantity":{str[1]},"measure":"{str[2]}"'.format(str = list(map(str.strip, line.split('|')))) + '}'
        cook_book[dish].append(eval(my))

  return cook_book

create_shop_list(get_reciept('reciept.txt'))

