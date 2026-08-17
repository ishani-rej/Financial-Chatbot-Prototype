# Financial Analysis Chatbot Prototype

## 1. Objective
This project implements a simplified AI chatbot prototype for financial analysis.
The chatbot responds to a fixed set of predefined financial questions using
Python `if`/dictionary-based matching.

## 2. Preparation
The chatbot uses example analyzed financial values because the Task 1 financial
dataset/results were not included with the chatbot instructions.

Example values used:
- Total revenue: $120,000,000
- Revenue growth: 8.0%
- Net income change: +10.0%
- Total expenses: $95,000,000
- Gross profit: $45,000,000

If your Task 1 produced different values, replace the values in
`FINANCIAL_DATA` in `financial_chatbot.py`.

## 3. Predefined Queries
The chatbot supports these five questions:

1. What is the total revenue?
2. How has net income changed over the last year?
3. What is the total expense?
4. What is the gross profit?
5. What is the revenue growth?

It also supports:
- `help` - displays all supported questions.
- `exit` - closes the chatbot.

## 4. Requirements
- Python 3.x
- No external libraries are required.

Pandas and Flask are not necessary for this simplified command-line prototype.

## 5. How to Run
Open a terminal in this folder and run:

```bash
python financial_chatbot.py
```

Then enter one of the predefined questions.

## 6. How It Works
1. The user enters a question.
2. The input is converted to lowercase and extra spaces are removed.
3. The chatbot compares the question with the predefined queries.
4. If a match is found, the corresponding financial response is returned.
5. If there is no match, the chatbot displays a limitation message.

## 7. Limitations
- It only answers predefined questions.
- It does not understand free-form natural language.
- It does not automatically read or analyze new financial datasets.
- It does not use a machine-learning or deep-learning model.
- The example financial values should be replaced with the actual Task 1 results.

## 8. Task Completion
Completed:
- Step 1: Preparation
- Step 2: Chatbot design and data preparation
- Step 3: Basic chatbot development
- Step 4: Demonstration and documentation

The ZIP package contains the Python script, test results, and documentation.
