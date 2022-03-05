# COVID-19 Vaccine-related CVX (vaccines administered) coding for interpreting the vaccine code included in these
# barcodes.  Fetched from https://www.cdc.gov/vaccines/programs/iis/COVID-19-related-codes.html.
# Further codes can be found in the IIS HL7 Standard Code Set, though I was unable to find manufacturer there:
# https://www2a.cdc.gov/vaccines/iis/iisstandards/vaccines.asp?rpt=cvx

CVX_CODES = {
    207: {
        "name": "Moderna COVID-19 Vaccine",
        "manufacturer": {"long": "Moderna US, Inc.", "short": "Moderna", "mvx": "MOD"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, PF, 100 mcg/ 0.5 mL dose",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, preservative free, 100 mcg/0.5mL dose",
        },
    },
    221:  {
        "name": "Moderna COVID-19 Vaccine",
        "manufacturer": {"long": "Moderna US, Inc.", "short": "Moderna", "mvx": "MOD"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, PF, 50 mcg/0.5 mL dose",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, preservative free, 50 mcg/0.5 mL dose",
        },
    },
    208: {
        "name": "Pfizer COVID-19 Vaccine",
        "manufacturer": {"long": "Pfizer-BioNTech", "short": "Pfizer", "mvx": "PFR"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, preservative free, 30 mcg/0.3mL dose",
        },
    },
    210: {
        "name": "AstraZeneca COVID-19 Vaccine",
        "manufacturer": {
            "long": "AstraZeneca Pharmaceuticals LP",
            "short": "AstraZeneca",
            "mvx": "ASZ",
        },
        "description": {
            "short": "COVID-19 vaccine, vector-nr, rS-ChAdOx1, PF, 0.5 mL",
            "long": "SARS-COV-2 (COVID-19) vaccine, vector non-replicating, recombinant spike protein-ChAdOx1, preservative free, 0.5 mL",
        },
    },
    212: {
        "name": "Janssen COVID-19 Vaccine",
        "manufacturer": {
            "long": "Janssen Products, LP",
            "short": "Janssen",
            "mvx": "JSN",
        },
        "description": {
            "short": "COVID-19 vaccine, vector-nr, rS-Ad26, PF, 0.5 mL",
            "long": "SARS-COV-2 (COVID-19) vaccine, vector non-replicating, recombinant spike protein-Ad26, preservative free, 0.5 mL",
        },
    },
    211: {
        "name": "Novavax COVID-19 Vaccine",
        "manufacturer": {"long": "Novavax, Inc.", "short": "Novavax", "mvx": "NVX"},
        "description": {
            "short": "COVID-19 vaccine, Subunit, rS-nanoparticle+Matrix-M1 Adjuvant, PF, 0.5 mL",
            "long": "SARS-COV-2 (COVID-19) vaccine, Subunit, recombinant spike protein-nanoparticle+Matrix-M1 Adjuvant, preservative free, 0.5mL per dose",
        },
    },
    213: {
        "name": "Unspecified COVID-19 Vaccine",
        "description": {
            "short": "SARS-COV-2 (COVID-19) vaccine, UNSPECIFIED",
            "long": "SARS-COV-2 (COVID-19) vaccine, UNSPECIFIED",
        }
    },
    217: {
        "name": "Pfizer COVID-19 Vaccine",
        "manufacturer": {"long": "Pfizer-BioNTech", "short": "Pfizer", "mvx": "PFR"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, preservative free, 30 mcg/0.3 mL dose",
        },
    },
    218: {
        "name": "Pfizer COVID-19 Vaccine",
        "manufacturer": {"long": "Pfizer-BioNTech", "short": "Pfizer", "mvx": "PFR"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, PF, 10 mcg/0.2 mL dose, tris-sucrose",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, preservative free, 10 mcg/0.2 mL dose, tris-sucrose formulation",
        },
    },
    219: {
        "name": "Pfizer COVID-19 Vaccine",
        "manufacturer": {"long": "Pfizer-BioNTech", "short": "Pfizer", "mvx": "PFR"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, PF, 3 mcg/0.2 mL dose, tris-sucrose",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, preservative free, 3 mcg/0.2 mL dose, tris-sucrose formulation",
        },
    }
}
