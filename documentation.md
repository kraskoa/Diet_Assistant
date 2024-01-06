# DOCUMENTATION
# Diet Assistant – a project by Adam Kraś

This is the documentation for my project called Diet Assistant. Its main purpose is to generate a diet based on user input, taking the data from Edamam Recipe Search API. It allows the user to personalise their diet based on parameters such as: list of ingredients to exclude, number of meals per day, type of diet (high protein, low fat etc.) and preferred cuisine (Asian, Italian).

The diet is saved to a .txt file which makes it easier to reuse, store and follow.

Also, part of the program's functionality is to create a secrets.json file which contains API credentials taken from the user. This step is necessary to allow for the program to use these credentials and properly execute API requests.

To run the program, just clone the project and while you're in your terminal in the project directory, just enter the command

```
make
```

You will be asked to provide the credentials to your API Recipe Search application created on the Edamam website.

Then, you'll be asked to provide (if you'd like) some specific ionformation about the diet.

That's it for the general introduction, enjoy the diet!

## Project structure

All of the project's files containing the source code are kept in the [src](src/) directory. There is a seperate directory for [tests](src/tests/) inside of it and also one for various [utility functions](src/utils/) that I've used.

The core directory of the project's source code contains five different files.

### Meals

The [meals](src/meals.py) file contains the class Meal, which represents a single recipe taken from the API. It formats the input data and stores it in a way that enables further work with Meal objects.

Two main methods in the class enable calculating specific information (nutrition values, calories) about the recipe that are then reused in the Day class. The same goes for the Meal's __ str __ (the spaces before and after str are necessary, otherwise markdown reads it as bold text) method.

### Days

The [days](src/days.py) file contains the class Day, which represents a day of eating. It keeps a dictionary with all of the meals for the day.

It has methods that calculate some information about the total daily menu and one that creates the menu itself.

One of the most important methods is the __ str __ that is reused in MealPlan class to generate the final .txt file with the user's diet

### Meal Plans

The [meal plans](src/meal_plans.py) file contains the MealPlan class which represents the entire diet, storing each Day.

The classes' main functionalities are:
- generating the meal plan (your entire diet) based on parameters previously collected by the program
- generating information about the diet to store in the final YourDiet.txt file

### Main

This file connects all of the classes and functions created for the project and handles user interaction. It takes input data from the user and passes it accordingly.

At the end, it saves generated data to a .txt file

### Others

Aside for the [tests](src/tests/), the program's source code consists of [errors](src/errors.py) file in which there are defined custom exception and some [utility functions](src/utils/):

 - [get_meals](src/utils/get_meals.py), ___the heart of the application___, function that actually executes the API requests and passes all arguments
 - [load_secrets](src/utils/load_secrets.py), reads from the secrets.json and returns a nice and neat dictionary with the read data
 - [create_secrets](src/utils/create_secrets.py), checks whether there is an existing secrets.json and creates one with user-provided data


## The problems I've encountered and potential solutions:

- The proposed portions are probably too small, resulting in very low calories per portion for most meals. This is a problem that basically completely prevented me from being able to create diets with "normal" caloric values.
- Inconsistently named dishTypes in the API (for example recipe for Persimmon tea is assigned a "Main course" dishType). This problem partially correlates with the first one
- Free API plan limitations cause problems with running tests (limited frequency and number of API calls). It also causes some of them to be running for a very long time due to API reponse duration - up to around a minute.

The potential solution that probably could be implemented to face the low calories problem would be to always take the most caloric meal from the data set returned by the API (it's always 20 recipes long). It would however require the program to create 20 seperate Meal objects every time an API request is made, which would even further lengthen the program's runtime.