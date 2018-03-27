with open('imagenetfoods.txt','r') as f:
  valid_foods = [word for line in f for word in line.split()]


def map_item(food):
  if food == 'pineapple, ananas': return 'pineapple'
  elif food == 'gondola':  return 'fish'
  elif food == 'Granny_Smith': return 'apple'
  elif food == 'carton': return 'milk'
  elif food == 'plate': return ''
  elif food == 'beer_bottle': return 'beer'
  elif food == 'bottle_cap': return 'water'
  elif food == 'soup_bowl': return 'soup'
  elif food == 'wine_bottle': return 'wine'
  elif food == 'milk_can': return 'milk'
  elif food == 'pill_bottle': return 'vitamins'
  elif food == 'packet': return 'ketchup'
  elif food == 'measuring_cup': return 'flour'
  elif food == 'goblet': return 'wine'
  elif food == 'water_bottle': return 'water'
  elif food == 'coffee_mug': return 'coffee'
  elif food not in valid_foods: return None
  return food

