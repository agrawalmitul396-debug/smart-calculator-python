# Smart Calculator Application

A menu-driven calculator developed using Python. This project demonstrates the practical implementation of user-defined functions, different argument types, lambda functions, map(), filter(), global variables, and Python modules.

## Project Overview

The Smart Calculator performs basic mathematical operations and demonstrates different Python programming concepts through an interactive menu-driven application.

## Features

- Addition of two numbers
- Subtraction of two numbers
- Multiplication of two numbers
- Division with zero-division handling
- Power calculation with a default exponent of 2
- Sum and average of multiple numbers
- Square calculation using a lambda function
- Use of map() to process multiple values
- Use of filter() to identify even results
- Global counter to track total calculations
- Separate module for calculator functions

## Technologies Used

- **Programming Language:** Python
- **IDE:** Python IDLE
- **Concepts:** Functions, Default Arguments, Keyword Arguments, Variable-Length Arguments, Lambda, map(), filter(), Global Variables and Modules.

## Project Structure

```text
SmartCalculator/
│
├── main.py
├── calc_utils.py
└── README.md
```

### File Description

| File | Description |
|---|---|
| main.py | Main application containing the menu and user interaction. |
| calc_utils.py | Contains calculator functions and the global operation counter. |
| README.md | Project documentation and execution instructions. |

## How to Run the Project

1. Download or clone this repository.
2. Make sure Python 3 is installed on your computer.
3. Open the project folder.
4. Run the main.py file.

```bash
python main.py
```

No external Python libraries are required.

## Calculator Menu

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power
6. Sum and Average
7. Square using Lambda and Map
8. Filter Even Results
9. Exit

## Python Concepts Demonstrated

- **User-Defined Functions:** Creating separate functions for mathematical operations.
- **Default Arguments:** Using a default exponent value in the power function.
- **Keyword Arguments:** Passing arguments using parameter names.
- **Variable-Length Arguments:** Accepting multiple numbers using *args.
- **Lambda Functions:** Performing square calculations.
- **map():** Applying a function to multiple values.
- **filter():** Selecting even results from a list.
- **Global Keyword:** Maintaining a counter of calculations.
- **Modules:** Separating calculator functions into calc_utils.py and importing them into main.py.

## Example

```text
Enter your choice: 1

Enter first number: 10
Enter second number: 20

Addition = 30.0
```

## Learning Objective

The objective of this project is to understand Python functions, argument handling, functional programming concepts, global variables, and modular programming through a practical application.

---

**Project Type:** Python Programming Practical  
**Status:** Completed
