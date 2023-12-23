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

    def calculate_nutrients(self, scale: str):
        nutrients = {}
        scales = ("portion", "100g")
        if scale.lower() not in scales:
            msg = f"Cannot calculate nutrients per {scale}, "
            msg += "use 'portion' or '100g'"
            raise ValueError(msg)
        if scale == "portion":
            fat_data = self.nutrients["FAT"]
            carbs_data = self.nutrients["CHOCDF"]
            protein_data = self.nutrients["PROCNT"]
            fiber_data = self.nutrients["FIBTG"]
            sugar_data = self.nutrients["SUGAR"]
            nutrients[fat_data["label"]] = fat_data["quantity"]
            nutrients[carbs_data["label"]] = carbs_data["quantity"]
            nutrients[protein_data["label"]] = protein_data["quantity"]
            nutrients[fiber_data["label"]] = fiber_data["quantity"]
            nutrients[sugar_data["label"]] = sugar_data["quantity"]
            return nutrients
