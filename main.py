import sys
import re
import math

def inputs():

    # Checks if the user added the correct number of arguments
    if len(sys.argv) != 4:
        sys.exit("USAGE ERROR: python3 main.py (dielectric constant) (dielectric height + unit) "
        "(operation freuqnecy + unit) \n Example: python3 main.py 0.25 2mm 230mhz")

    # Checks if the dielectric constant is number
    try:
        dielectric_constant = float(sys.argv[1])
    except ValueError:
        sys.exit("Dielectric constant must be a number.")

    # Parshing the inputs to seperate the number and unit
    # Made this before learning about pint
    dielectric_height = re.fullmatch(r"\s*(-?\d+(?:\.\d+)?)\s*([A-Za-z]+)\s*", sys.argv[2])
    operation_frequency = re.fullmatch(r"\s*(-?\d+(?:\.\d+)?)\s*([A-Za-z]+)\s*", sys.argv[3])

    # Another check 
    if not dielectric_height or not operation_frequency:
        sys.exit("Arguments must look like 1 3mm 45mhz")

    # Giving each number and unit its own variable
    dh = float(dielectric_height.group(1))
    dh_unit = dielectric_height.group(2).lower()
    of = float(operation_frequency.group(1))
    of_unit = operation_frequency.group(2).lower()

    # Checks to see if the correct unit is used
    if dh_unit not in ("in", "cm", "mm"):
        sys.exit("Incorrect Unit Found: For dielectric height use in, cm, mm")
    if of_unit not in ("ghz", "mhz"):
        sys.exit("Incorrect Unit Found: For operation freuqnecy use ghz, mhz")

    # Calls the conversion func
    dh, of = conversion(dh, dh_unit, of, of_unit)
    
    return dielectric_constant, dh, of

def conversion(dh, dh_unit, of, of_unit):

    if dh_unit == "in":
        dh *= 25.4
    elif dh_unit == "cm":
        dh *= 10
    if of_unit == "ghz":
        of *= 1000

    return dh, of

def calculate_patch_antenna(epsilon_r, h_mm, frequency_mhz):

    # Constants and unit conversions
    c = 299_792_458_000  # Speed of light in m/s
    h = h_mm  # Convert substrate height to meters
    frequency = frequency_mhz * 1e6  # Convert MHz to Hz

    # Validate inputs
    if epsilon_r <= 0:
        raise ValueError("Dielectric constant must be positive.")
    if h <= 0 or frequency <= 0:
        raise ValueError("Height and frequency must be positive.")

    # Calculate patch width (W)
    width = (c / (2 * frequency)) * math.sqrt(2 / (epsilon_r + 1))

    # Calculate effective dielectric constant (epsilon_eff)
    epsilon_eff = (
        (epsilon_r + 1) / 2
        + ((epsilon_r - 1) / 2)
        * (1 / math.sqrt(1 + 12 * (h / width)))
    )

    # Calculate patch length (L)
    length = (
        c / (2 * frequency * math.sqrt(epsilon_eff))
        - 0.824 * h
        * (
            ((epsilon_eff + 0.3) * ((width / h) + 0.264))
            / ((epsilon_eff - 0.258) * ((width / h) + 0.8))
        )
    )

    # Return dimensions in millimeters
    return {
        "epsilon_eff": epsilon_eff,
        "width_mm": width,
        "length_mm": length,
    }

def main():

    dielectric_constant, dh, of = inputs()
    try:
        results = calculate_patch_antenna(dielectric_constant, dh, of)
    except ValueError as error:
        sys.exit(str(error))

    print("Microstrip Patch Antenna Calculator")
    print("-----------------------------------")
    print(f"Patch width:  {results['width_mm']:.3f} mm")
    print(f"Patch length: {results['length_mm']:.3f} mm")


if __name__ == "__main__":
    main()