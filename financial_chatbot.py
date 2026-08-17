"""
Financial Analysis Chatbot Prototype
Task: Simplified rule-based chatbot for predefined financial queries.
"""

# Example analyzed financial data.
# Replace these values with the values from your Task 1 analysis if required.
FINANCIAL_DATA = {
    "total_revenue": 120_000_000,
    "revenue_growth": 8.0,
    "net_income_change": 10.0,
    "total_expenses": 95_000_000,
    "gross_profit": 45_000_000,
}

RESPONSES = {
    "what is the total revenue?":
        f"The total revenue is ${FINANCIAL_DATA['total_revenue']:,.0f}.",

    "how has net income changed over the last year?":
        f"Net income has increased by {FINANCIAL_DATA['net_income_change']:.1f}% over the last year.",

    "what is the total expense?":
        f"The total expense is ${FINANCIAL_DATA['total_expenses']:,.0f}.",

    "what is the gross profit?":
        f"The gross profit is ${FINANCIAL_DATA['gross_profit']:,.0f}.",

    "what is the revenue growth?":
        f"The revenue growth is {FINANCIAL_DATA['revenue_growth']:.1f}%."
}


def simple_chatbot(user_query):
    """Return a predefined financial response."""
    query = user_query.strip().lower()

    if query in RESPONSES:
        return RESPONSES[query]

    return (
        "Sorry, I can only provide information on predefined financial "
        "queries. Please choose one of the supported questions."
    )


def show_queries():
    """Display all supported questions."""
    print("\nAvailable financial queries:")
    for i, query in enumerate(RESPONSES.keys(), start=1):
        print(f"{i}. {query}")


def main():
    print("=" * 55)
    print("       FINANCIAL ANALYSIS CHATBOT PROTOTYPE")
    print("=" * 55)
    print("Type 'help' to see available questions.")
    print("Type 'exit' to close the chatbot.")

    while True:
        user_query = input("\nYou: ").strip()

        if user_query.lower() == "exit":
            print("Bot: Thank you for using the Financial Analysis Chatbot!")
            break

        if user_query.lower() == "help":
            show_queries()
            continue

        print("Bot:", simple_chatbot(user_query))


if __name__ == "__main__":
    main()
