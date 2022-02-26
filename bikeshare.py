import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

cities = ('chicago', 'new york city', 'washington')
months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')


def get_filters():
    # Function to filter data
    print("Hello! Let's explore some US bike-sharing data!")
    while True:
        city = input('\nWhich city would you like to explore? (Chicago, Washington or New York City): \n')
        city = city.lower()
        if city in cities:
            break
        else:
            print("Invalid Input! Please try again")

    while True:
        month = input(
            '\nDo you want to explore a particular month? If yes then type of name one of the first six months or '
            'else type all:\n')
        month = month.lower()
        if month in months:
            break
        else:
            print("Invalid Input! Please try again")

    while True:
        day = input(
            '\nDo you want to explore a particular day of week? If yes then type of name of one of day of week or '
            'else type all:\n')
        day = day.lower()
        if day in days:
            break
        else:
            print("Invalid Input! Please try again")
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    # Function to load data into a data frame based upon our filters   
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months1 = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months1.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    pop_mon = months[(df['month'].mode()[0])].title()
    print("The most popular month is: {}".format(pop_mon))

    # display the most common day of week
    df['day'] = df['Start Time'].dt.dayofweek
    pop_day = days[df['day'].mode()[0] + 1].title()
    print("The most popular day of week is : {}".format(pop_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most popular hour is: {}".format(df['hour'].mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    return pop_mon, pop_day


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most popular starting station is: {}".format(df['Start Station'].mode()[0]))
    # display most commonly used end station

    print("The most popular end station is: {}".format(df['End Station'].mode()[0]))
    # display most frequent combination of start station and end station trip
    df['combination'] = "from \"" + df['Start Station'] + "\" to \"" + df['End Station'] + "\""
    print("The most popular trip is: {}".format(df['combination'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total trip duration is: {} seconds".format(df['Trip Duration'].sum()))
    # display mean travel time
    print("Average duration trip is : {} seconds".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bike share users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    type_count = df['User Type'].value_counts()
    print("Number of subscribers: {}".format(type_count[0]))
    print("Number of customers: {}".format(type_count[1]))
    if len(type_count) > 2:
        print("Number of dependent(s): {}".format(type_count[2]))
    else:
        print("Number of dependent(s): 0")

    if city != 'washington':
        # Display counts of gender
        gender_count = df['Gender'].value_counts()
        print("Number of male users: {}".format(gender_count[0]))
        print("Number of female users: {}".format(gender_count[1]))

        # Display earliest, most recent, and most common year of birth
        print("\nYoungest user was born in year: {}".format(int(df['Birth Year'].max())))
        print("Oldest user was born in year: {}".format(int(df['Birth Year'].min())))
        print("Most users were born in year: {}".format(int(df['Birth Year'].mode())))

    else:
        print("\n\n There is no data about genders and year of birth of users")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def raw_data(df):
    print("Press any key to see raw data or type no key to skip")
    while input().lower() != 'no':
        print(df.sample(5))
        print('\nPress any key to see more raw data or type no key to skip')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
