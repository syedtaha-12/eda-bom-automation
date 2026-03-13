# EDA BOM Automation Script

This project demonstrates a simple Python automation script that processes PCB component data and generates a Bill of Materials (BOM).

The goal of the script is to simulate automation tasks commonly performed around Electronic Design Automation (EDA) tools, such as extracting and summarizing component data used in hardware designs.

## Overview

In PCB design workflows, engineers work with large sets of component data including:

- Symbols (schematic representations)
- Footprints (physical PCB packages)
- Component properties (value, part number, etc.)
- BOMs (Bill of Materials)

Manually organizing and validating this data can be time-consuming. This script demonstrates how Python can be used to automate part of that workflow.

The script reads component records from a file and automatically groups identical components to generate a BOM summary.

## Example Input

File: `pcb_components.txt`
R1,Resistor,10k,0603
R2,Resistor,10k,0603
C1,Capacitor,100nF,0603
C2,Capacitor,100nF,0603
U1,Microcontroller,STM32,QFP64

Each line represents a component with the following fields:
Reference,ComponentType,Value,Footprint


Example:

- **R1** → Reference designator
- **Resistor** → Component type
- **10k** → Component value
- **0603** → PCB footprint

## Example Output
BOM Summary:
Resistor 10k (0603) → 2
Capacitor 100nF (0603) → 2
Microcontroller STM32 (QFP64) → 1


The script automatically counts identical components based on their type, value, and footprint.

## How It Works

1. The script reads the component file line by line.
2. Each line is parsed to extract component properties.
3. A dictionary is used to group identical components.
4. The script generates a BOM summary showing the quantity of each part.

This demonstrates a common automation pattern used in engineering workflows.

## Technologies Used

- Python
- File parsing
- Dictionary-based data aggregation

## How to Run

1. Clone the repository:

The script automatically counts identical components based on their type, value, and footprint.

## How It Works

1. The script reads the component file line by line.
2. Each line is parsed to extract component properties.
3. A dictionary is used to group identical components.
4. The script generates a BOM summary showing the quantity of each part.

This demonstrates a common automation pattern used in engineering workflows.

## Technologies Used

- Python
- File parsing
- Dictionary-based data aggregation

## How to Run

1. Clone the repository:
git clone https://github.com/YOUR_USERNAME/eda-bom-automation.git

2. Navigate to the project folder:
cd eda-bom-automation

3. Run the script:
python generate_bom.py

## Possible Improvements

Future enhancements could include:

- Exporting the BOM to CSV
- Detecting missing footprints
- Detecting duplicate reference designators
- Validating component properties
- Integrating with EDA tool exports

## Why This Project

This project demonstrates how scripting can be used to automate engineering workflows around EDA tools, such as extracting and managing component data used in PCB design.

It highlights basic concepts relevant to hardware design automation including:

- component data processing
- BOM generation
- engineering workflow automation
