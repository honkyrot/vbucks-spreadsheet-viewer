#import libraries
import pandas as pd
import numpy as np

# This script will read the csv file and spit out the data in text format
# Eg, dates sorted by most profit.
# To any one reading this, if you see missing REASON data but the CHANGE is not 0, it's because I forgot to write it down.

last_date = "March 2024"

# csv file
csv_file = 'V-Bucks Account - All Time.csv'
main_csv = pd.read_csv(csv_file, thousands=',')
# formatted heads: DATE, SEASON, AMOUNT, VALUE, CHANGE, VALUE CHANGE, REASON

main_df = pd.DataFrame(main_csv)

def convert_df():
    """Convert the data into appropriate types and fix formatting."""
    # convert to datetime
    main_df['DATE'] = pd.to_datetime(main_df['DATE'])
    
    # convert amount & change to numeric
    main_df['AMOUNT'] = pd.to_numeric(main_df['AMOUNT'])
    main_df['CHANGE'] = pd.to_numeric(main_df['CHANGE'])

    # trim the reason column whitespace
    try: 
        main_df['REASON'] = main_df['REASON'].str.strip()
    except KeyError:
        pass
    
    # some REASON values are NaN, replace with empty spaces
    try:
        main_df['REASON'] = main_df['REASON'].replace('', ' ')
    except KeyError:
        pass

# intialize the conversion
convert_df()

# menu
active = True
print("Hi, welcome to the text-based version of my data!\n")
print("Please notify me if the data is outdated by 2+ months...")
print(f"Last CSV data update: {last_date}")
print(f"Total data entries: {str(len(main_df))}\n")

print("Ensure your terminal is tall enough to view the data.\n")

def query_amount():
    """Query the user for the amount of lines to display."""
    active_query = True

    while active_query:
        print("\nHow many lines? 0 for all.")
        line_amount = input("Enter amount: ")

        try:
            line_amount = int(line_amount)
        except ValueError:
            print("\nPlease enter a number.\n")
            continue

        return line_amount

def sort_by_profit(df, ascending=True):
    """Sort the data by most profit."""
    line_amount = query_amount()

    if line_amount == 0:
        return df.sort_values(by='CHANGE', ascending=ascending).to_string()
    
    return df.sort_values(by='CHANGE', ascending=ascending).head(line_amount).to_string()

def get_avg_profit():
    """Get the average profit per day, month, year, etc."""
    # days = length of df
    total_days = len(main_df)

    # get the total profit
    total_raw_profit = main_df['CHANGE'].sum()
    total_profit = total_raw_profit

    # get the average profit
    avg_profit = total_profit / total_days

    # vars
    daily_avg = avg_profit.round(2)
    monthly_avg = (avg_profit * 30).round(2)
    yearly_avg = (avg_profit * 365).round(2)
    fortnightly_avg = (avg_profit * 14).round(2) # 2 weeks, fortnight fortnite.

    # print
    print("\n Average profit (in V-Bucks) for...")
    print(f"Daily: {daily_avg}")
    print(f"Monthly: {monthly_avg}")
    print(f"Yearly: {yearly_avg}")
    print(f"Fortnightly: {fortnightly_avg}")
        

def get_activity():
    """Get the count of empty and non-empty days."""
    # get the empty days
    empty_days = main_df[main_df['CHANGE'] == 0]
    total_empty_days = len(empty_days)

    # get the non-empty days
    non_empty_days = main_df[main_df['CHANGE'] != 0]
    total_non_empty_days = len(non_empty_days)

    # print
    print(f"\nTotal empty days: {total_empty_days}")
    print(f"Total non-empty days: {total_non_empty_days}")

def profit_per_season():
    """Get profit per season."""
    # get the season names
    seasons = main_df['SEASON'].unique()

    print("\nSeasons:")

    # get the profit per season
    for season in seasons:
        season_df = main_df[main_df['SEASON'] == season]
        season_profit = season_df['CHANGE'].sum()

        print(f"{season} profit: {season_profit}")

def profit_per_month():
    """Get profit per month."""
    # get the month names
    months = main_df['DATE'].dt.month_name().unique()

    # resort the months as may is the first month in the df, due to the first entry being in may.
    months = np.roll(months, 4)

    print("\nMonths:")

    # get the profit per month
    for month in months:
        month_df = main_df[main_df['DATE'].dt.month_name() == month]
        month_profit = month_df['CHANGE'].sum()

        print(f"{month} profit: {month_profit}")

def profit_per_year():
    """Get profit per year."""
    # get the year names
    years = main_df['DATE'].dt.year.unique()

    print("\nYears:")

    # get the profit per year
    for year in years:
        year_df = main_df[main_df['DATE'].dt.year == year]
        year_profit = year_df['CHANGE'].sum()

        print(f"{year} profit: {year_profit}")

def profit_per_day():
    """Get profit per day."""
    # get the day names
    days = main_df['DATE'].dt.day_name().unique()

    print("\nDays:")

    # get the profit per day
    for day in days:
        day_df = main_df[main_df['DATE'].dt.day_name() == day]
        day_profit = day_df['CHANGE'].sum()

        print(f"{day} profit: {day_profit}")

def profit_per_each_day():
    """Get profit per each day in a month."""
    # get the profit per day
    for day in range(1, 32):
        day_df = main_df[main_df['DATE'].dt.day == day]
        day_profit = day_df['CHANGE'].sum()

        print(f"Day {day} profit: {day_profit}")

# get profit per date, eg season, month, year, days even.
def profit_per_date():
    """Get profit per date range."""
    active_ = True

    while active_:
        print("\nSelect a date range:")
        print("[0] - Exit")
        print("[1] - By season")
        print("[2] - By month")
        print("[3] - By year")
        print("[4] - By day")
        print("[5] - By each day per month")

        input_ = input("\nEnter option: ")

        # convert input to int check
        try:
            input_ = int(input_)
        except ValueError:
            print("\nPlease enter a number.\n")
            continue

        # switch case for options
        match input_:
            case 0:
                active_ = False
            case 1:
                profit_per_season()
            case 2:
                profit_per_month()
            case 3:
                profit_per_year()
            case 4:
                profit_per_day()
            case 5:
                profit_per_each_day()
            case _:
                print("\nInvalid option.\n")
                continue

# main loop
while active:
    print("\nPlease select an option:")
    print("[0] - Exit")
    print("[1] - Show data")
    print("[2] - Show all data")
    print("[3] - Sort by most profit")
    print("[4] - Sort by least profit")
    print("[5] - Get average profit per day, month, year, etc.")
    print("[6] - Get profit per date range")
    print("[7] - Get activity type counts")
    

    input_ = input("\nEnter option: ")

    # convert input to int check
    try:
        input_ = int(input_)
    except ValueError:
        print("\nPlease enter a number.\n")
        continue

    # switch case for options
    match input_:
        case 0:
            print("\nGoodbye!")
            active = False
        case 1:
            print(main_df)
        case 2:
            print(main_df.to_string())
        case 3:
            print(sort_by_profit(main_df, ascending=False))
        case 4:
            print(sort_by_profit(main_df, ascending=True))
        case 5:
            get_avg_profit()
        case 6:
            profit_per_date()
        case 7:
            get_activity()
        case _:
            print("\nInvalid option.\n")
            continue