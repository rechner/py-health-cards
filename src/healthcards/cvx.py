# COVID-19 Vaccine-related CVX (vaccines administered) coding for interpreting the vaccine code included in these
# barcodes.  Fetched from https://www.cdc.gov/vaccines/programs/iis/COVID-19-related-codes.html.
# Further codes can be found in the IIS HL7 Standard Code Set, though I was unable to find manufacturer there:
# https://www2a.cdc.gov/vaccines/iis/iisstandards/vaccines.asp?rpt=cvx

CVX_CODES = {
    206: {
        "name": "JYNNEOS Smallpox Vaccine",
        "manufacturer": {"long": "JYNNEOS, Inc", "short": "JYNNEOS", "mvx": "JYN"},
        "description": {
            "short": "Vaccinia, smallpox monkeypox vaccine live, PF, SQ or ID injection",
            "long": "Vaccinia, smallpox monkeypox vaccine, live attenuated, preservative free, subcutaneous or "
                    "intradermal injection",
        }
    },
    207: {
        "name": "Spikevax",
        "manufacturer": {"long": "Moderna US, Inc.", "short": "Moderna", "mvx": "MOD"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, PF, 100 mcg/0.5mL dose or 50 mcg/0.25mL dose",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, preservative free, 100 mcg/0.5mL dose or 50 mcg/0.25mL dose",
        },
    },
    208: {
        "name": "Pfizer COVID-19 Vaccine ",
        "manufacturer": {"long": "Pfizer-BioNTech", "short": "Pfizer", "mvx": "PFR"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, preservative free, 30 mcg/0.3 mL dose",
        },
    },
    211: {
        "name": "Novavax COVID-19 Vaccine",
        "manufacturer": {"long": "Novavax, Inc.", "short": "Novavax", "mvx": "NVX"},
        "description": {
            "short": "COVID-19, subunit, rS-nanoparticle+Matrix-M1 Adjuvant, PF, 0.5 mL",
            "long": "SARS-COV-2 (COVID-19) vaccine, subunit, recombinant spike protein-nanoparticle+Matrix-M1 Adjuvant, preservative free, 0.5mL dose",
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
            "short": "COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose, tris-sucrose",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, preservative free, 30 mcg/0.3 mL dose, tris-sucrose formulation",
        },
    },
    218: {
        "name": "Pfizer COVID-19 Vaccine ",
        "manufacturer": {"long": "Pfizer-BioNTech", "short": "Pfizer", "mvx": "PFR"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, PF, 10 mcg/0.2 mL dose, tris-sucrose",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, preservative free, 10 mcg/0.2 mL dose, tris-sucrose formulation",
        },
    },
    219: {
        "name": "Pfizer COVID-19 Vaccine ",
        "manufacturer": {"long": "Pfizer-BioNTech", "short": "Pfizer", "mvx": "PFR"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, PF, 3 mcg/0.2 mL dose, tris-sucrose",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, preservative free, 3 mcg/0.2 mL dose, tris-sucrose formulation",
        },
    },
    221: {
        "name": "Moderna COVID-19 Vaccine Booster",
        "manufacturer": {"long": "Moderna US, Inc.", "short": "Moderna", "mvx": "MOD"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, PF, 50 mcg/0.5 mL dose",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, preservative free, 50 mcg/0.5 mL dose",
        },
    },
    225: {
        "name": "Sanofi Pasteur COVID-19 Vaccine Booster",
        "manufacturer": {"long": "Sanofi Pasteur", "short": "Sanofi", "mvx": "PMC"},
        "description": {
            "short": "COVID-19, D614, recomb, preS dTM, AS03 adjuvant add, PF, 5mcg/0.5mL",
            "long": "SARS-COV-2 (COVID-19) vaccine, D614, prefusion spike recombinant protein subunit (CoV2 preS dTM), AS03 adjuvant added, preservative free, 5mcg/0.5mL dose",
        },
    },
    228: {
        "name": "Moderna COVID-19 Vaccine",
        "manufacturer": {"long": "Moderna US, Inc.", "short": "Moderna", "mvx": "MOD"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, PF, pediatric 25 mcg/0.25 mL dose",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, preservative free, pediatric 25 mcg/0.25 mL dose",
        },
    },
    229: {
        "name": "Moderna COVID-19 Vaccine Bivalent Booster",
        "manufacturer": {"long": "Moderna US, Inc.", "short": "Moderna", "mvx": "MOD"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, bivalent booster, PF, 50 mcg/0.5 mL or 25mcg/0.25mL dose",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, bivalent booster, preservative free, 50 mcg/0.5 mL or 25mcg/0.25mL dose",
        },
    },
    230: {
        "name": "Moderna COVID-19 Vaccine Bivalent Booster",
        "manufacturer": {"long": "Moderna US, Inc.", "short": "Moderna", "mvx": "MOD"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, bivalent booster, PF, 10 mcg/0.2 mL",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, bivalent booster, preservative free, 10 mcg/0.2 mL dose",
        },
    },
    300: {
        "name": "Pfizer COVID-19 Vaccine Bivalent Booster",
        "manufacturer": {"long": "Pfizer-BioNTech", "short": "Pfizer", "mvx": "PFR"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, bivalent booster, PF, 30 mcg/0.3 mL dose",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, bivalent booster, preservative free, 30 mcg/0.3mL dose, tris-sucrose formulation",
        },
    },
    301: {
        "name": "Pfizer COVID-19 Vaccine Bivalent Booster",
        "manufacturer": {"long": "Pfizer-BioNTech", "short": "Pfizer", "mvx": "PFR"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, bivalent booster, PF, 10 mcg/0.2 mL dose",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, bivalent booster, preservative free, 10 mcg/0.2 mL dose, tris-sucrose formulation",
        },
    },
    302: {
        "name": "Pfizer COVID-19 Vaccine Bivalent ",
        "manufacturer": {"long": "Pfizer-BioNTech", "short": "Pfizer", "mvx": "PFR"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, bivalent, PF, 3 mcg/0.2 mL dose",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, bivalent, preservative free, 3 mcg/0.2 mL dose, tris-sucrose formulation",
        },
    },
    308: {
        "name": "Pfizer COVID-19 Vaccine (2023-2024)",
        "manufacturer": {"long": "Pfizer-BioNTech", "short": "Pfizer", "mvx": "PFR"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, PF, tris-sucrose, 3 mcg/0.3 mL",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, preservative free, tris-sucrose, 3 mcg/0.3 mL dose",
        },
    },
    309: {
        "name": "COMIRNATY (COVID-19 Vaccine, mRNA, 2023-2024)",
        "manufacturer": {"long": "Pfizer-BioNTech", "short": "Pfizer", "mvx": "PFR"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, PF, tris-sucrose, 30 mcg/0.3 mL",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, preservative free, tris-sucrose, 30 mcg/0.3 mL dose",
        },
    },
    310: {
        "name": "Pfizer COVID-19 Vaccine (2023-2024)",
        "manufacturer": {"long": "Pfizer-BioNTech", "short": "Pfizer", "mvx": "PFR"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, PF, tris-sucrose, 10 mcg/0.3 mL",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, preservative free, tris-sucrose, 10 mcg/0.3 mL dose",
        },
    },
    311: {
        "name": "Moderna COVID-19 Vaccine",
        "manufacturer": {"long": "Moderna US, Inc.", "short": "Moderna", "mvx": "MOD"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, PF, 25 mcg/0.25 mL ",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, preservative free, 25 mcg/0.25 mL dose",
        },
    },
    313: {
        "name": "Novavax COVID-19 Vaccine, Adjuvanted",
        "manufacturer": {"long": "Novavax, Inc.", "short": "Novavax", "mvx": "NVX"},
        "description": {
            "short": "COVID-19, subunit, rS-nanoparticle, adjuvanted, PF, 5 mcg/0.5 mL",
            "long": "SARS-COV-2 (COVID-19) vaccine, subunit, recombinant spike protein-nanoparticle+Matrix-M1 Adjuvant, preservative free, 5 mcg/0.5 mL dose",
        },
    },
    312: {
        "name": "Spikevax",
        "manufacturer": {"long": "Moderna US, Inc.", "short": "Moderna", "mvx": "MOD"},
        "description": {
            "short": "COVID-19, mRNA, LNP-S, PF, 50 mcg/0.5 mL",
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike protein, LNP, preservative free, 50 mcg/0.5 mL dose",
        },
    },
    500: {
        "name": "COVID-19 Non-US Vaccine, Product Unknown",
        "description": {
            "short": "SARS-COV-2 COVID-19 Non-US Vaccine, Specific Product Unknown",
            "long": "Pandemic Non-US Covid Administration - specific CVX or product unknown",
        },
        "manufacturer": {"long": "Unknown, Non-US", "mvx": "UNK", "short": "Unknown"},
    },
}
