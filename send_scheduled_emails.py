import sqlite3
import smtplib
from email.mime.text import MIMEText
import schedule
import time

def get_table_insights():
    conn = sqlite3.connect("data_check.db")
    cursor = conn.cursor()

    table_name = "daily_data_load"

    # Get record count
    cursor.execute(f"SELECT COUNT(*) FROM daily_data_load")
    record_count = cursor.fetchone()[0]

    # Get data types of columns
    cursor.execute(f"PRAGMA table_info(daily_data_load)")
    columns_info = cursor.fetchall()
    data_types = {col[1]: col[2] for col in columns_info}

    # Get max date of a specific column
    date_column = "your_date_column"
    cursor.execute(f"SELECT MAX(order_date) FROM daily_data_load")
    max_date = cursor.fetchone()[0]

    conn.close()
    return record_count, data_types, max_date

def send_email():
    record_count, data_types, max_date = get_table_insights()
    
    # Email content
    email_body = f"""
    Table Insights:
    - Record Count: {record_count}
    - Data Types: {data_types}
    - Max Date: {max_date}
    """

    msg = MIMEText(email_body)
    msg["Subject"] = "Daily Database Insights"
    msg["From"] = "priyankapooranachandran@gmail.com"
    msg["To"] = "priyankapooranachandran@gmail.com"

    # Gmail SMTP Setup
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("priyankapooranachandran@gmail.com","*****")  # Use App Password
        server.sendmail("priyankapooranachandran@gmail.com", "priyankapooranachandran@gmail.com", msg.as_string())

schedule.every().day.at("11:34").do(send_email)  # Runs daily at 8 AM

while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for a minute before checking again

# - Using Task Scheduler or Cron Jobs: If you've scheduled the script using Windows Task Scheduler or a cron job on Linux/macOS, it will execute on schedule regardless of whether the editor is open.
# Would you like help setting up your script to keep running even after closing the editor? 🚀
# C:\Users\YourName\Desktop\script.py


# Step 2: Open Task Scheduler
# - Press Win + R, type taskschd.msc, and hit Enter to open Task Scheduler.
# - Click "Create Basic Task" on the right panel.
# Step 3: Set Up the Task
# - Name your task (e.g., "Daily Database Insights").
# - Click Next, and choose a schedule:
# - Daily for everyday execution.
# - Weekly for specific days.
# - Monthly for a certain date.
# - One Time for a single execution.
# - Select the time you want the script to run and click Next.

# Your error message:

# means Google is blocking your login because you are not using an App Password.

# How to Fix
# Enable 2-Step Verification on your Google account:
# Google 2-Step Verification

# Create an App Password for your Gmail account:
# Google App Passwords

# Replace your password in the script with the generated App Password (a 16-character code, not your regular Gmail password).