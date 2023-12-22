class Meal:
    """
    Class representing a single meal created based on the API data
    """
    def __init__(self, recipe_data):
        """
        Meal class constructor

        Args:
            recipe_data (json): Data about the recipe
        """
        self._name = recipe_data["label"]
        self._portions = recipe_data["yield"]
        self._calories = recipe_data["calories"]
        self._weight = recipe_data["weight"]
        self._link = recipe_data["shareAs"]
        self.diet_labels = list(recipe_data["dietLabels"].values())
        self.health_labels = list(recipe_data["healthLabels"].values())
        self.meal_type = recipe_data["mealType"]
        self.nutrients = recipe_data["totalNutrients"]
        self.cuisine_type = recipe_data["cuisineType"]

    @property
    def name(self):
        return self._name

    @property
    def portions(self):
        return self._portions

    @property
    def calories(self):
        return self._calories

    @property
    def weight(self):
        return self._weight

    @property
    def link(self):
        return self._link

    def calculate_calories_per_portion(self):
        return round(self.calories / self.portions, 2)

    def calculate_calories_per_100g(self):
        return round(self.calories / (self.weight / 100), 2)
