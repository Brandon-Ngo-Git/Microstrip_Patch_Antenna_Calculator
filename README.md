# Microstrip_Patch_Antenna_Calculator
Python script to calculate physical dimentions for microstrip patch antenna for PCB.

# Installation

Note: Made for windows only  
Install dependencies:
```text
 pip install -r requirements.txt
```
# Usage

Run `main.py` with 3 arguments:  
Note: height must be either in, cm, or mm and operation frequency must be either ghz or mhz
```text
 python main.py [dielectric constant] [dielectric height] [operation frequency]
```
Example:
```text
 python main.py 0.25 16mm 2mhz
```