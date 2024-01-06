# DOCUMENTATION

To run the program, just clone the project and while you're in your terminal in the project directory, just enter the command
```
make
```

# Project structure

All of the project's files containing the source code are kept in the [src](src/) directory. There is a seperate directory for [tests](src/tests/) inside of it and also one for various [utility functions](src/utils/) that I've used.

The core directory of the project's source code contains five different files.

## Days

The [days](src/days.py) file contains the class Day, which represents a day of eating. It keeps a dictionary with all of the meals for the day.

The problems I've encountered:

- Inconsistently named dishTypes in the API (for example recipe for Persimmon tea is assigned a "Main course" dishType)
- The proposed portions are probably too small, resulting in very low calories per portion for most meals
- Free API plan limitations may cause problems with running tests (limited frequency and number of API calls). It also causes some of them to be running for a very long time due to API reponse duration - up to around a minute.
