import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')


    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    """Get user input for city (Chicago, New York City, Washington)"""
    while True:
        city = input("Please type the name of the city for which you would like to get data. \nAvailable cities: Chicago, New York City, Washington\n").lower()
        if city in ('chicago', 'new york city', 'washington'):
            break
        else:
            print("\n" + "Sorry, I did not get that. Please try again! \nHint: Be aware of correct spelling.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    """Get user input for month (January, February, March, April, May, June) or let her choose 'all' if no filter should be applied."""
    while True:
        month = input("\nPlease type the month for which you would like to get data (January, February, March, April, May, or June)...\n...or type \'all\' if you want data for the entire period.\n").lower()
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            break
        else:
            print("\n" + "Sorry, I did not get that. Please try again! \nHint: Be aware of correct spelling.\n")

    print('-'*40)
    print()
    print("You chose {} as a filter for city, {} as a filter for month, and {} as a filter for day of week.".format(city.upper(), month.upper(), day.upper()))
    print("Let\'s take a look at the data... :-)")
    print()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    """loading data into our Pandas DataFrame"""
    df = pd.read_csv(CITY_DATA[city])

    """converting the Start Time column in the respective csv to datetime"""
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    """Extracting the month number and weekday name into separate columns using the datetime module"""
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    """Filter by month if applicable; converting month into corresponding month number"""
    if month != 'all':
        """use the index of the months list to get the corresponding int"""
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        """filter by month to create the new dataframe"""
        df = df[df['month'] == month]
        """filter by day of week if applicable"""
    if day != 'all':
        """filter by day of week to create the new dataframe"""
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    """Display the most common month; use .mode()[0] to identify the most common value of discrete data"""
    most_common_month = df['month'].mode()[0]
    print("Most common month:       ", most_common_month)

    # TO DO: display the most common day of week
    """Display the most common day of week"""
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print("Most common day of week: ", most_common_day_of_week)

    # TO DO: display the most common start hour
    """Display the most common start hour; first, extract hour from the Start Time column to create an hour column; according to Practice Problem #1"""
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("Most common start hour:  ", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    """display most commonly used start station"""
    most_common_start_station = df['Start Station'].value_counts().idxmax('index')
    print("Most commonly used start station:   ", most_common_start_station)

    # TO DO: display most commonly used end station
    """display most commonly used end station"""
    most_common_end_station = df['End Station'].value_counts().idxmax('index')
    print("Most commonly used end   station:   ", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    """display most frequent combination of start station and end station"""
    most_common_combination_station = df.groupby(['Start Station',  'End Station']).count()
    print("Most commonly occuring combination:  {} - {}".format(most_common_start_station, most_common_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    """Displaying total travel time (in seconds)"""
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time (in sec.): ", total_travel_time)

    # TO DO: display mean travel time
    """Displaying mean travel time (in seconds)"""
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean  travel time (in sec.): ", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    """print value counts for each user type; using value_counts() function to return a Series containing counts of unique values, here: user types; according to Practice Problem #2; use 'try' to account for possibly missing data in the table because otherwise you might run into KeyError"""
    try:
        counts_of_user_types = df['User Type'].value_counts()
        #print(user_types)
        print("\n" + "Counts of user types:\n", counts_of_user_types)
    except KeyError:
        print("\n" + "Counts of user types:      No data available for this filter.")

    # TO DO: Display counts of gender
    """"Displaying counts of gender; use 'try' to account for possibly missing data in the table"""
    try:
        counts_of_gender = df['Gender'].value_counts()
        print("\n" + "Counts of gender types:\n ", counts_of_gender)
    except KeyError:
        print("\n" + "Counts of gender types:    No data available for this filter.")

    # TO DO: Display earliest, most recent, and most common year of birth
    """"Displaying earliest, most recent, and most common year of birth; use 'try' to account for possibly missing data in the table"""
    try:
        earliest_year = df['Birth Year'].min()
        print("\n" + "Earliest year:             ", earliest_year)
    except KeyError:
        print("\n" + "Earliest year:             No data available for this filter.")

    try:
        most_recent_year = df['Birth Year'].max()
        print("Most recent year:          ", most_recent_year)
    except KeyError:
        print("Most recent year:          No data available for this filter.")

    try:
        most_common_year_of_birth = df['Birth Year'].value_counts().idxmax()
        print("Most common year of birth: ", most_common_year_of_birth)
    except KeyError:
        print("Most common year of birth: No data available for this filter.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def raw_data2(df):
    """Displays rows of raw data as according to user input."""

    while True:
        try:
            raw_data = int(input("How many rows of raw data would you like to see? (Type \'0\' if you do not want to see any raw data): "))
        except ValueError:
            print("\n" + "Sorry, this is not a valid input. Please try again! \nHint: Be aware that only integers are allowed here.\n")
            continue
        else:
            check_if_int = isinstance(raw_data, int)
            print("\n" + "Check step: Validity of your inputy is {}\n".format(check_if_int))
            print()
            print("\nYou requested to see {} row(s) of raw data. Here they are: ".format(raw_data))
            print()
            print(df.head(int(raw_data)))
            break


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data2(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
