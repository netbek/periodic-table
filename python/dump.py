# isort: skip_file
import os
import pandas as pd
import yaml

from mendeleev.fetch import fetch_table


data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data")


def dict_merge(*dicts):
    merged = dicts[0].copy()
    for d in dicts[1:]:
        merged.update(d)
    return merged


def main():
    # Load patch data
    with open(os.path.join(data_dir, "src", "patch.yml"), "rt") as fp:
        data = yaml.safe_load(fp)

    patch_dict = {}
    for value in data:
        patch_dict[value["atomic_number"]] = {}
        for key in value.keys():
            if key != "atomic_number":
                patch_dict[value["atomic_number"]][key] = value[key]

    # Load mendeleev data
    df = fetch_table("elements")
    columns = {
        "atomic_number": "atomic_number",
        "symbol": "symbol",
        "name": "name",
        "atomic_weight": "atomic_mass",
        "en_pauling": "electronegativity",
        "block": "block",
        "group_id": "group",
        "period": "period",
    }
    df = df[columns.keys()].rename(columns=columns)
    data = df.to_dict(orient="records")

    # Patch mendeleev data
    for i, value in enumerate(data):
        for k, v in value.items():
            if pd.isna(v):
                value[k] = None

        for k in ["group"]:
            if not pd.isna(value[k]):
                value[k] = int(value[k])

    for i, value in enumerate(data):
        patch_data = patch_dict.get(value["atomic_number"])
        if patch_data:
            data[i] = dict_merge(value, patch_data)

    with open(os.path.join(data_dir, "elements.yml"), "wt") as fp:
        fp.write(yaml.safe_dump(data, sort_keys=False))


if __name__ == "__main__":
    main()
