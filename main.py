# print("hello from Python")

# import pandas as pd

# # Define the path to the CSV file
# file_path = 'data/october-2024.csv'

# # Read the CSV file into a DataFrame
# transactions = pd.read_csv(file_path)

# # Parse the 'Date' column to datetime format
# transactions['Date'] = pd.to_datetime(transactions['Date'])

# # Convert the 'Amount' column to numeric, handling any errors
# transactions['Amount'] = pd.to_numeric(transactions['Amount'], errors='coerce')

# # Display the first few rows of the DataFrame
# print(transactions.head())

# # Optionally, check for any missing values
# print(transactions.isnull().sum())

# # Summary statistics for the Amount column
# print("\nSummary Statistics for Amount:")
# print(transactions['Amount'].describe())

# # Group by Category and calculate total expenses per category
# category_totals = transactions.groupby('Category')['Amount'].sum().reset_index()
# category_totals['Amount'] = category_totals['Amount'].abs()  # Make amounts positive for clarity

# # Display total expenses per category
# print("\nTotal Expenses per Category:")
# print(category_totals)

# import pandas as pd

# # Define the path to the CSV file
# file_path = 'data/october-2024.csv'

# # Read the CSV file into a DataFrame
# transactions = pd.read_csv(file_path)

# # Parse the 'Date' column to datetime format
# transactions['Date'] = pd.to_datetime(transactions['Date'])

# # Convert the 'Amount' column to numeric, handling any errors
# transactions['Amount'] = pd.to_numeric(transactions['Amount'], errors='coerce')

# # Display the first few rows of the DataFrame
# print("Transactions Data:")
# print(transactions.head())

# # Optionally, check for any missing values
# print("\nMissing Values Count:")
# print(transactions.isnull().sum())

# # Summary statistics for the Amount column
# print("\nSummary Statistics for Amount:")
# print(transactions['Amount'].describe())

# # Calculate total spending for the month
# total_spending = transactions['Amount'].sum()
# print(f"\nTotal Spending for the Month: ${total_spending:.2f}")

# # Compare spending to the monthly budget
# monthly_budget = 5000.00
# budget_comparison = "under" if total_spending < monthly_budget else "over"
# print(f"Comparison to Monthly Budget of ${monthly_budget:.2f}: ${total_spending:.2f} ({budget_comparison})")

# # Group by Category and calculate total expenses per category
# category_totals = transactions.groupby('Category')['Amount'].sum().reset_index()
# category_totals['Amount'] = category_totals['Amount'].abs()  # Make amounts positive for clarity

# # Display total expenses per category
# print("\nTotal Expenses per Category:")
# print(category_totals)

# # Identify the top 5 individual expenses
# top_expenses = transactions.nlargest(5, 'Amount')
# top_expenses['Amount'] = top_expenses['Amount'].abs()  # Make amounts positive for clarity

# # Display the top 5 individual expenses
# print("\nTop 5 Individual Expenses:")
# print(top_expenses[['Date', 'Description', 'Amount', 'Category']])

# import pandas as pd
# import matplotlib.pyplot as plt

# # Define the path to the CSV file
# file_path = 'data/october-2024.csv'

# # Read the CSV file into a DataFrame
# transactions = pd.read_csv(file_path)

# # Parse the 'Date' column to datetime format
# transactions['Date'] = pd.to_datetime(transactions['Date'])

# # Convert the 'Amount' column to numeric, handling any errors
# transactions['Amount'] = pd.to_numeric(transactions['Amount'], errors='coerce')

# # Group by Category and calculate total expenses per category
# category_totals = transactions.groupby('Category')['Amount'].sum().reset_index()
# category_totals['Amount'] = category_totals['Amount'].abs()  # Make amounts positive for clarity

# # Visualization: Pie Chart for Spending by Category
# plt.figure(figsize=(10, 6))
# plt.pie(category_totals['Amount'], labels=category_totals['Category'], autopct='%1.1f%%', startangle=140)
# plt.title('Percentage of Spending by Category')
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# # Save the pie chart as an image file
# plt.savefig('data/spending_by_category.png')
# plt.close()  # Close the plot

# print("Pie chart saved as 'data/spending_by_category.png'.")

# import pandas as pd
# import matplotlib.pyplot as plt

# # Define the path to the CSV file
# file_path = 'data/october-2024.csv'

# # Read the CSV file into a DataFrame
# transactions = pd.read_csv(file_path)

# # Parse the 'Date' column to datetime format
# transactions['Date'] = pd.to_datetime(transactions['Date'])

# # Convert the 'Amount' column to numeric, handling any errors
# transactions['Amount'] = pd.to_numeric(transactions['Amount'], errors='coerce')

# # Group by Category and calculate total expenses per category
# category_totals = transactions.groupby('Category')['Amount'].sum().reset_index()
# category_totals['Amount'] = category_totals['Amount'].abs()  # Make amounts positive for clarity

# # Calculate total spending for the month
# total_spending = transactions['Amount'].sum()
# monthly_budget = 5000.00
# remaining_budget = monthly_budget - total_spending
# percentage_spent = (total_spending / monthly_budget) * 100

# # Identify the top 5 individual expenses
# top_expenses = transactions.nlargest(5, 'Amount')
# top_expenses['Amount'] = top_expenses['Amount'].abs()  # Make amounts positive for clarity

# # Budget status
# budget_status = "under budget" if total_spending < monthly_budget else "over budget"

# # Create the report
# report = f"""
# ==========================
#          REPORT
# ==========================
# Reporting Period: October 2024
# Total Spent: ${total_spending:.2f}
# Monthly Budget: ${monthly_budget:.2f}
# Remaining Budget: ${remaining_budget:.2f}
# Percentage of Budget Spent: {percentage_spent:.2f}%

# Breakdown of Spending by Category:
# """
# for index, row in category_totals.iterrows():
#     report += f"  - {row['Category']}: ${row['Amount']:.2f}\n"

# report += "\nTop 5 Expenses:\n"
# for index, row in top_expenses.iterrows():
#     report += f"  - {row['Description']} on {row['Date'].date()}: ${row['Amount']:.2f}\n"

# report += f"\nBudget Status: You are {budget_status}.\n"
# report += "=========================="

# # Print the report
# print(report)

# # Visualization: Pie Chart for Spending by Category
# plt.figure(figsize=(10, 6))
# plt.pie(category_totals['Amount'], labels=category_totals['Category'], autopct='%1.1f%%', startangle=140)
# plt.title('Percentage of Spending by Category')
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# # Save the pie chart as an image file
# plt.savefig('data/spending_by_category.png')
# plt.close()  # Close the plot

# print("Pie chart saved as 'data/spending_by_category.png'.")

import pandas as pd
import matplotlib.pyplot as plt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

# Define the path to the CSV file
file_path = 'data/october-2024.csv'

# Read the CSV file into a DataFrame
transactions = pd.read_csv(file_path)

# Parse the 'Date' column to datetime format
transactions['Date'] = pd.to_datetime(transactions['Date'])

# Convert the 'Amount' column to numeric, handling any errors
transactions['Amount'] = pd.to_numeric(transactions['Amount'], errors='coerce')

# Group by Category and calculate total expenses per category
category_totals = transactions.groupby('Category')['Amount'].sum().reset_index()
category_totals['Amount'] = category_totals['Amount'].abs()  # Make amounts positive for clarity

# Calculate total spending for the month
total_spending = transactions['Amount'].sum()
monthly_budget = 5000.00
remaining_budget = monthly_budget - total_spending
percentage_spent = (total_spending / monthly_budget) * 100

# Identify the top 5 individual expenses
top_expenses = transactions.nlargest(5, 'Amount')
top_expenses['Amount'] = top_expenses['Amount'].abs()  # Make amounts positive for clarity

# Budget status
budget_status = "under budget" if total_spending < monthly_budget else "over budget"

# Create the report
report = f"""
==========================
         REPORT
==========================
Reporting Period: October 2024
Total Spent: ${total_spending:.2f}
Monthly Budget: ${monthly_budget:.2f}
Remaining Budget: ${remaining_budget:.2f}
Percentage of Budget Spent: {percentage_spent:.2f}%

Breakdown of Spending by Category:
"""
for index, row in category_totals.iterrows():
    report += f"  - {row['Category']}: ${row['Amount']:.2f}\n"

report += "\nTop 5 Expenses:\n"
for index, row in top_expenses.iterrows():
    report += f"  - {row['Description']} on {row['Date'].date()}: ${row['Amount']:.2f}\n"

report += f"\nBudget Status: You are {budget_status}.\n"
report += "=========================="

# Print the report
print(report)

# Visualization: Pie Chart for Spending by Category
plt.figure(figsize=(10, 6))
plt.pie(category_totals['Amount'], labels=category_totals['Category'], autopct='%1.1f%%', startangle=140)
plt.title('Percentage of Spending by Category')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Save the pie chart as an image file
image_path = 'data/spending_by_category.png'
plt.savefig(image_path)
plt.close()  # Close the plot

print(f"Pie chart saved as '{image_path}'.")

# Email functionality
def send_email(report, image_path, to_email):
    from_email = 'your_email@example.com'  # Replace with your email
    password = 'your_password'  # Replace with your email password

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = 'Monthly Spending Report'

    # Attach the report
    msg.attach(MIMEText(report, 'plain'))

    # Attach the image
    with open(image_path, 'rb') as img:
        img_attach = MIMEImage(img.read())
        img_attach.add_header('Content-ID', '<{}>'.format(os.path.basename(image_path)))
        msg.attach(img_attach)

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
            print(f"Email sent to {to_email}.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Specify the recipient email address
recipient_email = 'recipient@example.com'  # Replace with the recipient's email

# Send the email
send_email(report, image_path, recipient_email)