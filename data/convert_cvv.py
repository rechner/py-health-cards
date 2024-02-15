import csv

CVX_CODES = {}
MANUFACTURERS = {
    "Janssen Products, LP":  {
            "long": "Janssen Products, LP",
            "short": "Janssen",
            "mvx": "JSN",
    },
    "Moderna US, Inc.":  {"long": "Moderna US, Inc.", "short": "Moderna", "mvx": "MOD"},
    "Pfizer-BioNTech": {"long": "Pfizer-BioNTech", "short": "Pfizer", "mvx": "PFR"},
    "Novavax, Inc.": {"long": "Novavax, Inc.", "short": "Novavax", "mvx": "NVX"},
    "Sanofi Pasteur": {"long": "Sanofi Pasteur", "short": "Sanofi", "mvx": "PMC"},
}

with open('cvv_codes.csv', newline='') as csvfile:
    rowreader = csv.DictReader(csvfile)
    for row in rowreader:
        name = row.get("Sale Proprietary Name").split('\n')[0]
        try:
            CVX_CODES[int(row["CVX Code"])] = {
                "name": name,
                "manufacturer": MANUFACTURERS.get(row.get("Manufacturer")),
                "description": {
                    "short": row.get("CVX Short Description"),
                    "long": row.get("CVX Long Description"),
                },
            }
        except ValueError:
            pass


from pprint import pprint
print(CVX_CODES)
