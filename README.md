# Assignment 2- Software Now


# #Group Members

Abichal Paudel(s404281)
Anuj Jung Karki(s403813)
Krishna Dev Bhatta(s405010)
Diwan Paija(s396523)


## Overview
 This repository contains the complete solution for Assignment 2,
 covering two major programming tasks:
 
 Question 1 – Text Encryption & Decryption System
 Question 2 – Mathematical Expression Evaluator (Recursive Descent Parsing)
All development, testing, and version tracking were managed through GitHub as required.


## Question 1: Encryption & Decryption System
 
### Objective:
 Develop a program that:
 1. Reads text from raw_text.txt.
 2. Encrypts it using a rule-based shifting algorithm.
 3. Decrypts the encrypted text.
 4. Verifies correctness by comparing original and decrypted outputs

### Features:
 - Custom dual-shift encryption logic using shift1 and shift2.
 - Case-sensitive transformations:
   - Lowercase and uppercase handled differently.
 - Non-alphabet characters remain unchanged.
 - Automatic file handling:
   - raw_text.txt → encrypted_text.txt → decrypted_text.txt.
 - Built-in verification system

### Files:
question1.py
raw_text.txt
encrypted_text.txt
decrypted_text.txt


## Question 2: Expression Evaluator

### Objective:
  Build a mathematical expression evaluator using recursive descent parsing.

### Features:
 - Supports:
   - Addition(+)
   - Subtraction(-)
   - Multiplication(*)
   - Division(/)

 - Handles:
   - Nested parentheses
   - Unary negation (e.g., -5, -(3+2))
   - Operator precedence correctly

 - Detects and handles invalid expressions

 - Outputs:
   - Parse Tree
   - Tokens
   - Result

### Files:
evaluator.py
sample_input.txt
output.txt

### Output Format:
 Each expression generates:
  - Input
  - Tree
  - Tokens
  - Result

## How to Run?
### Question1:
 </>Bash
  cd Q1
  python question1.py

### Question2:
  ```bash
  cd Q2
  python evaluator.py


## Technologies Used:
 - Python 3
 - File Handling
 - Recursive Descent Parsing
 - Git & GitHub for version control

## Repository Link:
  It has been added in github_link.txt as required.

## Contribution:
 This assignment was collaboratively completed by all group members.
 Each member contributed to design, implementation, testing, and debugging across both questions.