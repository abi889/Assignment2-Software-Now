# Assignment 2 – Software Now

## Group Members
- Abichal Paudel (s404281)
- Anuj Jung Karki (s403813)
- Krishna Dev Bhatta (s405010)
- Diwan Paija (s396523)

---

## Overview
This repository contains the complete solution for Assignment 2 covering two major programming tasks:
This project demonstrates practical implementation of file handling, algorithm design, and parsing techniques using Python. It focuses on both data transformation and structured expression evaluation.

- **Question 1 – Text Encryption & Decryption System**  
  Implements a rule-based character shifting algorithm that encrypts text from `raw_text.txt` into `encrypted_text.txt`, then fully decrypts it back to `decrypted_text.txt`. The system preserves case sensitivity (uppercase letters shift differently from lowercase) and leaves all non-alphabetic characters (digits, punctuation, spaces) untouched. A built-in verification step automatically confirms that decrypted text matches the original.

- **Question 2 – Mathematical Expression Evaluator (Recursive Descent Parsing)**  
  Builds a recursive descent parser that tokenizes mathematical expressions, constructs a parse tree following operator precedence rules, and evaluates the result. The parser supports nested parentheses, unary minus operators, and handles edge cases like division by zero or malformed expressions. Output includes the token stream, parse tree structure, and numeric result for each expression from `sample_input.txt`.

All development, testing, and version tracking were managed through GitHub as required. The repository includes:
- Full commit history with descriptive messages
- Branching strategy for feature development
- Issue tracking for bugs and improvements
- Collaborative code reviews via pull requests


---

## Question 1: Encryption & Decryption System

### Objective
Develop a program that:
- Reads text from `raw_text.txt`
- Encrypts it using a rule-based shifting algorithm
- Decrypts the encrypted text
- Verifies correctness by comparing original and decrypted outputs

### Features
- Custom dual-shift encryption using `shift1` and `shift2`
- Case-sensitive transformations (uppercase & lowercase handled differently)
- Non-alphabet characters remain unchanged
- Automatic file handling:
  - raw_text.txt → encrypted_text.txt → decrypted_text.txt
- Built-in verification system

### Files
- question1.py
- raw_text.txt
- encrypted_text.txt
- decrypted_text.txt

---

## Question 2: Expression Evaluator

### Objective
Build a mathematical expression evaluator using recursive descent parsing.

### Features
- Supports:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)
- Handles:
  - Nested parentheses
  - Unary negation (e.g., -5, -(3+2))
  - Correct operator precedence
- Detects invalid expressions

### Outputs
- Parse Tree
- Tokens
- Result

### Files
- evaluator.py
- sample_input.txt
- output.txt

---

## How to Run

### Question 1
```bash
cd Q1
python question1.py
```

### Question 2
```bash
cd Q2
python evaluator.py
```

---

## Technologies Used
- Python 3
- File Handling
- Recursive Descent Parsing
- Git & GitHub for version control

---

## Repository Link
The GitHub repository link has been provided in `github_link.txt` as required.

---

## Contribution
This assignment was collaboratively completed by all group members.  
Each member contributed to design, implementation, testing, and debugging across both questions.
