def isint(value):
  try:
    int(value)
    return True
  except ValueError:
    return False


def try_int(str):
  str = str.strip(' ')
  if isint(str):
    return int(str)
  else:
    return str


def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def get_shop_list_by_dishes(dishes, person_count, cook_book):
  shop_list = {}
  for dish in dishes:
    dish = dish.strip(' ')
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
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(',')
  shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
  print_shop_list(shop_list)


def get_reciept(file):
  counter = 0
  dish = ''
  keys = ['ingridient_name', 'quantity', 'measure']

  with open(file) as f:
    cook_book = {}
    dish = ''
    flag_dish = False #true - прочитали блюдо, false - прочитали рецепт
    for line in f:
      line = line.strip('\n').strip().lower()
      if not line: #пустая строка
        dish = ''
        flag_dish = False
      elif not isint(line): #не цифра
        if not flag_dish:
          dish = line
          flag_dish = True
          cook_book[dish] = []
        else:
          str = list(map(try_int, line.split('|')))
          cook_book[dish].append(dict(zip(keys, str)))

  return cook_book


print(get_reciept('reciept.txt'))
create_shop_list(get_reciept('reciept.txt'))



