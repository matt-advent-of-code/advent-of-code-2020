import re


def find_allergy_free_ingredients(input: str) -> list:
    foods = parse(input)

    allergens = find_allergy_ingredients(input)
    allergy_free_ingredients = []

    for food in foods:
        for ingredient in food['ingredients']:
            if not contains_allergen(ingredient, allergens):
                allergy_free_ingredients.append(ingredient)

    return allergy_free_ingredients


def find_allergy_ingredients(input: str):
    foods = parse(input)

    allergens = {}
    for food in foods:
        for allergen in food['allergens']:
            if allergen in allergens:
                ingredients = [ingredient for ingredient in allergens[allergen] if ingredient in food['ingredients']]
                allergens[allergen] = ingredients
            else:
                allergens[allergen] = food['ingredients'].copy()
    reduce(allergens)
    return allergens


def reduce(allergens: dict):
    for allergen in allergens:
        if len(allergens[allergen]) == 1:
            ingredient = allergens[allergen][0]
            for allergen_to_remove_ingredient in allergens:
                if allergen != allergen_to_remove_ingredient:
                    if ingredient in allergens[allergen_to_remove_ingredient]:
                        allergens[allergen_to_remove_ingredient].remove(ingredient)
                        reduce(allergens)


def contains_allergen(ingredient: str, allergens: dict) -> bool:
    for allergen in allergens:
        if ingredient in allergens[allergen]:
            return True
    return False


def parse(input: str) -> list:
    foods = []
    for food in input.split('\n'):
        food_split = food.split('(')
        ingredients = food_split[0].strip().split(' ')
        m = re.match('contains ([^)]*)', food_split[1])
        if m:
            allergens = [allergen.strip() for allergen in m.group(1).split(',')]
        foods.append({
            'ingredients': ingredients,
            'allergens': allergens
        })
    return foods


if __name__ == '__main__':
    with open('input.txt') as data:
        allergy_ingredients = find_allergy_ingredients(data.read())
        keys = list(allergy_ingredients.keys())
        keys.sort()
        ingredients = [allergy_ingredients[key][0] for key in keys]
        print(','.join(ingredients))