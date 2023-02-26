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
            "long": "Vaccinia, smallpox monkeypox vaccine, live attenuated, preservative free, subcutaneous or intradermal injection",
        }
    },
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
            "long": "SARS-COV-2 (COVID-19) vaccine, vector non-replicating, recombinant spike protein-ChAdOx1, "
                    "preservative free, 0.5 mL",
        },
    },
    211: {
        "name": "Novavax COVID-19 Vaccine",
        "manufacturer": {"long": "Novavax, Inc.", "short": "Novavax", "mvx": "NVX"},
        "description": {
            "short": "COVID-19 vaccine, Subunit, rS-nanoparticle+Matrix-M1 Adjuvant, PF, 0.5 mL",
            "long": "SARS-COV-2 (COVID-19) vaccine, Subunit, recombinant spike protein-nanoparticle+Matrix-M1 "
                    "Adjuvant, preservative free, 0.5mL per dose",
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
            "long": "SARS-COV-2 (COVID-19) vaccine, vector non-replicating, recombinant spike protein-Ad26, "
                    "preservative free, 0.5 mL",
        },
    },
    217: {
        "description": {
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike "
            "protein, LNP, preservative free, 30 mcg/0.3 "
            "mL dose, tris-sucrose formulation",
            "short": "COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL " "dose, tris-sucrose",
        },
        "manufacturer": {"long": "Pfizer-BioNTech", "mvx": "PFR", "short": "Pfizer"},
        "name": "COMIRNATY",
    },
    218: {
        "description": {
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike "
            "protein, LNP, preservative free, 10 mcg/0.2 "
            "mL dose, tris-sucrose formulation",
            "short": "COVID-19, mRNA, LNP-S, PF, 10 mcg/0.2 mL " "dose, tris-sucrose",
        },
        "manufacturer": {"long": "Pfizer-BioNTech", "mvx": "PFR", "short": "Pfizer"},
        "name": "Pfizer-BioNTech COVID-19 Vaccine ",
    },
    219: {
        "description": {
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike "
            "protein, LNP, preservative free, 3 mcg/0.2 "
            "mL dose, tris-sucrose formulation",
            "short": "COVID-19, mRNA, LNP-S, PF, 3 mcg/0.2 mL " "dose, tris-sucrose",
        },
        "manufacturer": {"long": "Pfizer-BioNTech", "mvx": "PFR", "short": "Pfizer"},
        "name": "Pfizer-BioNTech COVID-19 Vaccine ",
    },
    221: {
        "description": {
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike "
            "protein, LNP, preservative free, 50 mcg/0.5 "
            "mL dose",
            "short": "COVID-19, mRNA, LNP-S, PF, 50 mcg/0.5 mL " "dose",
        },
        "manufacturer": {"long": "Moderna US, Inc.", "mvx": "MOD", "short": "Moderna"},
        "name": "Moderna COVID-19 Vaccine Booster",
    },
    225: {
        "description": {
            "long": "SARS-COV-2 (COVID-19) vaccine, D614, "
            "prefusion spike recombinant protein subunit "
            "(CoV2 preS dTM), AS03 adjuvant added, "
            "preservative free, 5mcg/0.5mL dose",
            "short": "COVID-19, D614, recomb, preS dTM, AS03 "
            "adjuvant add, PF, 5mcg/0.5mL",
        },
        "manufacturer": {"long": "Sanofi Pasteur", "mvx": "PMC", "short": "Sanofi"},
        "name": "Sanofi Pasteur COVID-19 Vaccine, booster dose, adult",
    },
    228: {
        "description": {
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike "
            "protein, LNP, preservative free, pediatric "
            "25 mcg/0.25 mL dose",
            "short": "COVID-19, mRNA, LNP-S, PF, pediatric 25 " "mcg/0.25 mL dose",
        },
        "manufacturer": {"long": "Moderna US, Inc.", "mvx": "MOD", "short": "Moderna"},
        "name": "Moderna COVID-19 Vaccine ",
    },
    229: {
        "description": {
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike "
            "protein, LNP, bivalent booster, preservative "
            "free, 50 mcg/0.5 mL or 25mcg/0.25mL dose",
            "short": "COVID-19, mRNA, LNP-S, bivalent booster, "
            "PF, 50 mcg/0.5 mL or 25mcg/0.25mL dose",
        },
        "manufacturer": {"long": "Moderna US, Inc.", "mvx": "MOD", "short": "Moderna"},
        "name": "Moderna COVID-19 Vaccine Bivalent Booster",
    },
    230: {
        "description": {
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike "
            "protein, LNP, bivalent booster, preservative "
            "free, 10 mcg/0.2 mL dose",
            "short": "COVID-19, mRNA, LNP-S, bivalent booster, " "PF, 10 mcg/0.2 mL",
        },
        "manufacturer": {"long": "Moderna US, Inc.", "mvx": "MOD", "short": "Moderna"},
        "name": "Moderna COVID-19 Vaccine Bivalent Booster",
    },
    300: {
        "description": {
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike "
            "protein, LNP, bivalent booster, preservative "
            "free, 30 mcg/0.3mL dose, tris-sucrose "
            "formulation",
            "short": "COVID-19, mRNA, LNP-S, bivalent booster, "
            "PF, 30 mcg/0.3 mL dose",
        },
        "manufacturer": {"long": "Pfizer-BioNTech", "mvx": "PFR", "short": "Pfizer"},
        "name": "Pfizer-BioNTech COVID-19 Vaccine Bivalent Booster",
    },
    301: {
        "description": {
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike "
            "protein, LNP, bivalent booster, preservative "
            "free, 10 mcg/0.2 mL dose, tris-sucrose "
            "formulation",
            "short": "COVID-19, mRNA, LNP-S, bivalent booster, "
            "PF, 10 mcg/0.2 mL dose",
        },
        "manufacturer": {"long": "Pfizer-BioNTech", "mvx": "PFR", "short": "Pfizer"},
        "name": "Pfizer-BioNTech COVID-19 Vaccine Bivalent Booster",
    },
    302: {
        "description": {
            "long": "SARS-COV-2 (COVID-19) vaccine, mRNA, spike "
            "protein, LNP, bivalent, preservative free, 3 "
            "mcg/0.2 mL dose, tris-sucrose formulation",
            "short": "COVID-19, mRNA, LNP-S, bivalent, PF, 3 " "mcg/0.2 mL dose",
        },
        "manufacturer": {"long": "Pfizer-BioNTech", "mvx": "PFR", "short": "Pfizer"},
        "name": "Pfizer-BioNTech COVID-19 Vaccine Bivalent ",
    },
    500: {
        "name": "COVID-19 Non-US Vaccine, Product Unknown",
        "description": {
            "short": "SARS-COV-2 COVID-19 Non-US Vaccine, Specific Product Unknown",
            "long": "Pandemic Non-US Covid Administration - specific CVX or product unknown",
        },
        "manufacturer": {"long": "Unknown, Non-US", "mvx":"UNK", "short": "Unknown"},
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
