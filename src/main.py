# from .utils.create_secrets import check_if_secrets_exists
# from .utils.load_secrets import load_secrets
# from .meal_plans import MealPlan
from .errors import (
    ChoiceNotAvailableError
)


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


def main():
    # check_if_secrets_exists()
    # secrets = load_secrets("secrets.json")

    defaults = {
        "diet": "",
        "cuisineType": "",
        "excluded": [],
        "calories": 0
    }
    input_dict = defaults.copy()

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
    print(input_dict["diet"])

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
    print(input_dict["cuisineType"])
    # write_to_output_file(data)


if __name__ == "__main__":
    main()
