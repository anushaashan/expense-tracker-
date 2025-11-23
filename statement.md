# Problem Statement

Many individuals struggle to track their daily and monthly expenses in an organized manner. While digital wallets and banking apps show raw transaction data, they rarely provide personalized insights, spending patterns, or category-based analysis. Users need a simple, offline tool that allows them to record expenses easily and analyze their spending habits to make informed financial decisions.

# Scope

The Expense Tracker is a desktop-based Python application that:

* Allows users to log, view, and manage daily expenses.
* Uses CSV files for data storage, ensuring portability and offline usage.
* Calculates totals, weekly summaries, and monthly spending breakdowns.
* Provides analytical insights such as category trends, unusual expenses, and most/least expensive days.
* Offers simple predictions based on historical spending.

Advanced financial planning, multi-user accounts, cloud syncing, and UI-based dashboards are outside the current scope.

# Target Users

* **Students:** Individuals who want a lightweight tool to keep track of everyday spending.
* **Working Professionals:** Users who prefer manual offline expense logging without relying on mobile apps.
* **Budget-Conscious Individuals:** Anyone who wants to understand their spending habits and reduce unnecessary expenses.

# High-Level Features

* **Add Expenses:** Input transactions with date, category, amount, and notes.
* **View All Expenses:** Display all recorded entries from the CSV file.
* **Monthly Summary:** Calculate total spending for a chosen month.
* **Weekly Summary:** Group expenses by ISO week number for better tracking.
* **Savings Calculator:** Compare monthly spending against a user-defined budget.
* **Prediction:** Estimate next month’s spending based on historical averages.
* **Unusual Expense Detection:** Identify entries significantly above normal spending.
* **Category Trend Analysis:** Compare category totals between different months.
* **Duplicate Finder:** Detect repeated expense entries.
* **Most/Least Expensive Day:** Highlight the highest and lowest spending days of a month.
