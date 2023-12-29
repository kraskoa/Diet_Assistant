import json


def load_secrets(path: str) -> dict:
    """
    Function that reads data from secrets.json file

    Args:
        path (str): path to secrets.json file

    Returns:
        secrets (dict): a Python dictionary with data from secrets.json
    """
    secrets = {}
    with open(path, "r") as file:
        secrets = json.load(file)
    return secrets
