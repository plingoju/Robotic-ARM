# FDE Technical Screen – Package Sorter

## Objective
This project implements a function `sort(width, height, length, mass)` to classify packages in Thoughtful’s robotic automation factory.

## Rules
- **Bulky** if:
  - Volume ≥ 1,000,000 cm³ (width × height × length), OR  
  - Any dimension ≥ 150 cm  
- **Heavy** if mass ≥ 20 kg

## Stacks
- `STANDARD`: Neither bulky nor heavy  
- `SPECIAL`: Bulky or heavy (but not both)  
- `REJECTED`: Both bulky and heavy  

## Usage
Clone this repo and run:


