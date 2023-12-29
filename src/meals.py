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
        ingredients = []
        for entry in recipe_data["ingredients"].values():
            ingredients.append(entry["food"])
        self.ingredients = ingredients

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

    def __str__(self):
        result = f"The {self.name} meal weighs {self.weight} grams total"
        result += f" and has {self.calculate_calories('portion')} "
        result += "calories per portion"
        return result

    def calculate_calories(self, scale: str) -> float:
        """
        Function that calculates the meal's amount of calories

        Args:
            scale (str): specifies whether to calculate calories
                         per portion of meal or per 100g

        Raises:
            ValueError: if scale is not a supported value

        Returns:
            float: calculated amount of calories based on given scale
        """
        scales = ("portion", "100g")
        if scale.lower() not in scales:
            msg = f"Cannot calculate calories per {scale}, "
            msg += "use 'portion' or '100g'"
            raise ValueError(msg)
        if scale == "portion":
            return round(self.calories / self.portions, 2)
        else:
            return round(self.calories / (self.weight / 100), 2)

    def calculate_nutrients(self, scale: str) -> dict:
        """
        Function that calculates the meal's amount of calories

        Args:
            scale (str): specifies whether to calculate calories
                         per portion of meal or per 100g

        Raises:
            ValueError: if scale is not a supported value

        Returns:
            dict: a dictionary with nutritional values of the product
                  (name: quantity [in grams])
        """
        scales = ("portion", "100g")
        data_sets = [
            self.nutrients["FAT"],
            self.nutrients["CHOCDF"],
            self.nutrients["PROCNT"],
            self.nutrients["FIBTG"],
            self.nutrients["SUGAR"],
        ]
        if scale.lower() not in scales:
            msg = f"Cannot calculate nutrients per {scale}, "
            msg += "use 'portion' or '100g'"
            raise ValueError(msg)
        if scale == "portion":
            div = self.portions
        else:
            div = self.weight / 100
        nutrients = {
            data_set["label"]: round(data_set["quantity"] / div, 2)
            for data_set in data_sets
        }
        return nutrients
