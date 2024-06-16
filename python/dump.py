# isort: skip_file
import copy
import os
import yaml

from src.netbek.periodic_table.data import elements

data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data")


def main():
    data = copy.deepcopy(list(elements.values()))
    for d in data:
        d["category"] = d["category"].value
        del d["show_at_default"]

    with open(os.path.join(data_dir, "elements.yml"), "wt") as fp:
        yaml.safe_dump(data, fp, sort_keys=False)


if __name__ == "__main__":
    main()
