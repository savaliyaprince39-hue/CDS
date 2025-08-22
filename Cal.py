#!/usr/bin/env python3
"""
Simple Calendar Program
- Show full year calendar
- Show specific month calendar
- Show today’s date and day
"""

import calendar
from datetime import datetime

def show_year_calendar(year: int):
    """Display full year calendar"""
    print("\n" + calendar.TextCalendar(calendar.SUNDAY).formatyear(year))

def show_month_calendar(year: int, month: int):
    """Display specific month calendar"""
    print("\n" + calendar.month(year, month))

def today_info():
    """Display today’s date and day"""
    today = datetime.now()
    print("\n📅 Today is:", today.strftime("%A, %d %B %Y"))

def main():
    print("===== PYTHON CALENDAR PROGRAM =====")
    today_info()

    while True:
        print("\nOptions:")
        print("1. Show full year calendar")
        print("2. Show month calendar")
        print("3. Show today’s info again")
        print("4. Exit")

        choice = input("Enter choice (1–4): ").strip()

        if choice == "1":
            year = int(input("Enter year (e.g. 2025): "))
            show_year_calendar(year)

        elif choice == "2":
            year = int(input("Enter year (e.g. 2025): "))
            month = int(input("Enter month (1–12): "))
            show_month_calendar(year, month)

        elif choice == "3":
            today_info()

        elif choice == "4":
            print("Goodbye 👋")
            break

        else:
            print("❗ Invalid choice. Try again.")

if _name_ == "_main_":
    main()
