.SILENT:

all:
	python3 -m src.main
	echo "Your custom diet has been saved to YourDiet.txt\n"
	cat YourDiet.txt