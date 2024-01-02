from .utils.create_secrets import check_if_secrets_exists


diets_list = [
    "balanced",
    "high-fiber",
    "high_protein",
    "low-carb",
    "low-fat",
    "low-sodium"
]

cuisine_types = [
    "American",
    "Asian",
    "British",
    "Caribbean",
    "Central Europe",
    "Chinese",
    "Eastern Europe",
    "French",
    "Indian",
    "Italian",
    "Japanese",
    "Kosher",
    "Mediterranean",
    "Mexican",
    "Middle Eastern",
    "Nordic",
    "South American",
    "South East Asian"
]


def main():
    check_if_secrets_exists()


if __name__ == "__main__":
    main()
