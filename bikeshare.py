import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
          'new york city': 'new_york_city.csv',
           'washington': 'washington.csv' }
months = ['january','february','march','april','may','june','all']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
def input_bike(input_print,error_print,enterable_list):
    while True:
        ret = input(input_print).lower()
        if ret in enterable_list:
            return ret
        else:
            print(error_print)
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input_bike('\nWhich city would you like to explore, chicago, new york city or washington?','\nWrong city!',
                ['chicago', 'new york city', 'washington'])

# TO DO: get user input for month (all, january, february, ... , june)
    month = input_bike('\nWhich month would you like to explore, january, february, march, april, may, june or all?','\nWrong month!',
                months)
# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input_bike('\nWhich day of week would you like to explore, monday, tuesday, wednesday, thursday, friday, saturday ,sunday or all?',
                '\nWrong day of week!',days)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.dayofweek

    if month != 'all':
        df = df[df['month'] == months.index(month) + 1]
    if day != 'all':
        df = df[df['day'] ==days.index(day)]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_common = df['month'].mode()[0]
    print('\nThe most common month of travel: ',months[month_common - 1])

    # TO DO: display the most common day of week
    day_common = df['day'].mode()[0]
    print('\nThe most common day of week of travel: ',days[day_common])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('\nThe most common start hour of travel: ',df['hour'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nThe most commonly used start station: ',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('\nThe most commonly used end station: ',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    combine_station = df['Start Station'] + '-' + df['End Station']    
    print('\nThe most frequent combination of start station and end station trip: ',combine_station.mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nThe total travel time: ',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('\nThe mean travel time: ',df['Trip Duration'].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nThe counts of user types: ',df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('\nThe counts of gender: ',df['Gender'].value_counts())
    else:
        print('\nNo gender data in Washingtoncity')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nThe earliest year of birth: ',df['Birth Year'].min())
        print('\nThe most recent year of birth: ',df['Birth Year'].max())
        print('\nThe most common year of birth: ',df['Birth Year'].mode()[0])
    else:
        print('\nNo birth year data in Washington city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()