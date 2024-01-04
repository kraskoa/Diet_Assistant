# from .utils.create_secrets import check_if_secrets_exists
from .utils.load_secrets import load_secrets
from .meal_plans import MealPlan
from .errors import (
    ChoiceNotAvailableError
)
import os


available_diets = {
    1: "balanced",
    2: "high-fiber",
    3: "high-protein",
    4: "low-carb",
    5: "low-fat",
    6: "low-sodium"
}

cuisine_types = {
    1: "American",
    2: "Asian",
    3: "British",
    4: "Central Europe",
    5: "Chinese",
    6: "French",
    7: "Indian",
    8: "Italian",
    9: "Japanese",
    10: "Kosher",
    11: "Mediterranean",
    12: "Mexican",
    13: "Middle Eastern",
    14: "Nordic",
    15: "South American"
}


def write_to_output_file(data):
    with open("YourDiet.txt", "w") as output_file:
        output_file.write(data)


def choose_num_of_meals() -> int:
    num_of_meals_prompt = "\n\nHow many meals a day would you like to have in "
    num_of_meals_prompt += "your diet? (you can choose between 3 and 5): "
    num_of_meals = int(input(num_of_meals_prompt))
    return num_of_meals


def choose_num_of_days() -> int:
    num_of_days_prompt = "\n\nHow long would you like you like one block of  "
    num_of_days_prompt += "your diet to be? "
    num_of_days_prompt += "(choose a number of days, max is 14): "
    num_of_days = int(input(num_of_days_prompt))
    return num_of_days


def choose_diet(defaults: dict, input_dict: dict):
    print("\n\nAvailable diets:")
    for number, diet in available_diets.items():
        print(f"{number}: {diet}")

    diet_prompt = "\nIf you'd like to choose a specific diet please pick"
    diet_prompt += " a number or enter the name of the diet.\nIf not, please"
    diet_prompt += " press Enter: "
    chosen_diet = input(diet_prompt)
    if chosen_diet != "":
        if chosen_diet in str(available_diets.keys()):
            input_dict["diet"] = available_diets[int(chosen_diet)]
        elif chosen_diet.lower() in available_diets.values():
            input_dict["diet"] = chosen_diet.lower()
        else:
            raise ChoiceNotAvailableError


def choose_cuisine_type(defaults: dict, input_dict: dict):
    print("\n\nAvailable cuisine types:")
    for number, cuisine in cuisine_types.items():
        print(f"{number}: {cuisine}")

    cuisine_prompt = "\nIf you'd like to choose a specific cuisine  type"
    cuisine_prompt += " please pick a number or enter the name of the cuisine."
    cuisine_prompt += "\nIf not, please press Enter: "
    chosen_cuisine = input(cuisine_prompt)
    if chosen_cuisine != "":
        if chosen_cuisine in str(cuisine_types.keys()):
            input_dict["cuisineType"] = cuisine_types[int(chosen_cuisine)]
        elif chosen_cuisine.title() in cuisine_types.values():
            input_dict["cuisineType"] = chosen_cuisine.title()
        else:
            raise ChoiceNotAvailableError


def get_ingrediets_to_exclude(defaults: dict, input_dict: dict):
    prompt = "Are there any food ingredients you'd like to exclude? y/n: "
    answer = input(prompt)
    if answer.lower() == "y" or answer.lower() == "yes":
        exclude_prompt = "Okay, please enter their names one by one, "
        exclude_prompt += "separated by spaces. When you're done just "
        exclude_prompt += "press Enter"
        excluded = input(exclude_prompt).split()
    elif answer.lower() == "n" or answer.lower() == "no":
        excluded = []
    else:
        print("Incorrect input!\n")
        get_ingrediets_to_exclude()
    input_dict["excluded"] = excluded


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    # check_if_secrets_exists()
    secrets = load_secrets("secrets.json")

    defaults = {
        "diet": "",
        "cuisineType": "",
        "excluded": [],
        "calories": 0
    }
    input_dict = defaults.copy()

    clear_screen()
    num_of_meals = choose_num_of_meals()
    clear_screen()
    num_of_days = choose_num_of_days()
    clear_screen()

    choose_diet(defaults, input_dict)
    clear_screen()
    choose_cuisine_type(defaults, input_dict)
    clear_screen()
    get_ingrediets_to_exclude(defaults, input_dict)
    clear_screen()

    meal_plan = MealPlan(num_of_days, num_of_meals)

    for key, value in defaults.items():
        if input_dict[key] == value:
            input_dict.pop(key)

    meal_plan.generate_meal_plan(secrets, **input_dict)
    print(meal_plan)


if __name__ == "__main__":
    main()
