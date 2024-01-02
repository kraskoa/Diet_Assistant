from .utils.create_secrets import check_if_secrets_exists


available_diets = {
    1: "balanced",
    2: "high-fiber",
    3: "high_protein",
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
    write_to_output_file("A\n\tB")


if __name__ == "__main__":
    main()
