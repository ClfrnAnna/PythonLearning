import pickle, json
import yaml
from yaml.loader import SafeLoader
def from_pickle(file):
    with open(file, "rb") as f:
        data=pickle.load(f)
        return data


def from_json(file):
    with open(file, "rt") as f:
        data=json.load(f)
        return data


def from_yaml(file):
    with open(file, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data