from pathlib import Path
import json


root_path = Path(__file__).resolve().parent.parent
secrets_path = root_path / "secrets.json"


def check_if_secrets_exists():
    if secrets_path.exists():
        print("We see that you've already got a secrets.json file!")
        answer = input("Would you like to create a new one? y/n: ")
        if answer.lower() == "y" or answer.lower() == "yes":
            create_secrets()
        elif answer.lower() == "n" or answer.lower() == "no":
            print("\nOkay, let's proceed!")
        else:
            print("Incorrect input!\n")
            check_if_secrets_exists()
    else:
        create_secrets()


def create_secrets():
    secrets_data = {"url": "adres"}
    msg = "Once you've created an account with Edamam and a Recipe Search API"
    msg += " application please keep the App Key and App ID handy"
    print(msg)

    app_key = input("Enter your App Key here: ")
    app_id = input("Enter your App ID here: ")
    secrets_data["app_key"] = app_key
    secrets_data["app_id"] = app_id

    with open(secrets_path, "w") as secrets:
        json.dump(secrets_data, secrets, indent=4)
    print(f"Data has been written to {secrets_path}")


check_if_secrets_exists()
