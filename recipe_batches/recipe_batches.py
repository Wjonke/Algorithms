#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  minimum = None
  try:
    for k, v in enumerate(recipe):
      if ingredients[v] // recipe[v] == 0:
        return 0
      elif k == 0:
        minimum = ingredients[v] // recipe[v]
      else:
        if minimum > ingredients[v] // recipe[v]:
          minimum = ingredients[v] // recipe[v]
  except KeyError:
    return 0

  return minimum


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))