spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
    

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return None
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods + [spicy_food]

print("Names:", get_names(spicy_foods))
print("Spiciest Foods:", get_spiciest_foods(spicy_foods))
print("Print Spicy Foods:")
print_spicy_foods(spicy_foods)
print("Spicy Food by Cuisine (American):", get_spicy_food_by_cuisine(spicy_foods, "American"))
print("Print Spiciest Foods:")
print_spiciest_foods(spicy_foods)
print("Average Heat Level:", get_average_heat_level(spicy_foods))
print("Create Spicy Food:")
new_spicy_foods = create_spicy_food(spicy_foods, {"name": "Griot", "cuisine": "Haitian", "heat_level": 10})
print(new_spicy_foods)
