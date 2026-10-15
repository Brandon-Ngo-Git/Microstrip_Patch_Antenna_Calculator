import sys
import re

# Variables
# HELP

def input():
    if len(sys.argv) != 4:
        sys.exit("USAGE ERROR: python3 main.py (dielectric constant) (dielectric height + unit) (operation freuqnecy + unit) \n Example: python3 main.py 0.25 2mm 230mhz")

    dielectric_constant = sys.argv[1]
    dielectric_height = re.fullmatch(r"\s*(-?\d+(?:\.\d+)?)\s*([A-Za-z]+)\s*", sys.argv[2])
    operation_frequency = re.fullmatch(r"\s*(-?\d+(?:\.\d+)?)\s*([A-Za-z]+)\s*", sys.argv[3])

    if not dielectric_height or not operation_frequency:
        sys.exit("Arguments must look like 1 3mm 45mhz")

    dh = float(dielectric_height.group(1))
    dh_unit = dielectric_height.group(2)

    of = float(operation_frequency.group(1))
    of_unit = operation_frequency.group(2)

    if dh_unit not in ("in", "cm", "mm"):
        sys.exit("Incorrect Unit Found: For dielectric height use in, cm, mm")
    if of_unit not in ("ghz", "mhz"):
        sys.exit("Incorrect Unit Found: For operation freuqnecy use ghz, mhz")

    print(dh, dh_unit)   
    print(of, of_unit)

def main():

    print("hi")


if __name__ == "__main__":
    main()