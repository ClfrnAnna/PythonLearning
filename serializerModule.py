import pickle, json
import yaml
from yaml.loader import SafeLoader


def to_yaml(obj, file):
    with open(file, "wt") as f:
        yaml.dump(obj, f)


def to_json(obj, file):
    with open(file, "wt") as f:
        json.dump(obj, f)


def to_pickle(obj, file):
    with open(file, "wb") as f:
        pickle.dump(obj, f)