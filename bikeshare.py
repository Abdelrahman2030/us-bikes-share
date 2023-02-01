import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

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


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    ask = "N"

    while ask == "N":

        cities_list = ["Chicago", "New York City", "Washington"]
        city = input("Please enter the name of the city here: ").lower().title()
        city = city.strip()

        while city not in cities_list:
            print("Sorry!! you enterd it wrong\nYou have a list of cities (\"Chicago\", \"New York City\", \"Washington\") Please choose one of them")
            city = input("Please renter the city name: ").lower()
            city = city.title().strip()

        ask = input("You choose {} is this correct?\n(Y or N) ".format(city)).lower().title().strip()
        if ask == "N" :
            print("please try again") 

    #now to the month entry

    filter_answer = input("Do you want to filter by month, type \"yes\" or type \"non\" if you don't want a filter ").lower()
    filter_answer = filter_answer.title().strip()
    options_list = ["Yes", "Non"]

    while filter_answer not in options_list:
        filter_answer = input("The value that you enterd is invalid, please choose (\"Yes\" OR \"Non\") ").lower()
        filter_answer = filter_answer.title().strip()

    months_list = ["January", "February", "March", "April", "May", "June"]

    if filter_answer == "Yes":
        filter_answer = input("Choose a month (\"January\", \"February\", \"march\", \"April\", \"May\" or \"June\") ").lower()
        filter_answer = filter_answer.title().strip()

        while filter_answer not in months_list:
            print("Sorry you enterd it wrong, try again.")
            filter_answer = input("Choose a month (\"January\", \"February\", \"march\", \"April\", \"May\" or \"June\") ").lower()
            filter_answer = filter_answer.title().strip()

    print("you choosed {}.".format(filter_answer))

    #the day filter entry

    options_list = ["Yes", "Non"]

    day_filter = input("Do you want to filter by day, type \"yes\" or type \"non\" if you don't want a filter ").lower()
    day_filter = day_filter.title().strip()


    while day_filter not in options_list:
        day_filter = input("The value that you enterd is invalid, please choose (\"Yes\" OR \"Non\") ").lower()
        day_filter = day_filter.title().strip()

    days_list = {1: "Saturday", 2: "Sunday", 3: "Monday", 4: "Tuesday", 5: "Wednesday", 6: "Thursday", 7: "Friday"}

    if day_filter == "Yes":
        try:
            day_filter = int(input("write a number for a day, (Eg: 1: saturday, 2:sunday, etc.... ) "))
        except:
            while day_filter not in days_list:
                print("Sorry you enterd it wrong, try again.")
                try:
                    day_filter = int(input("write a number for a day, Eg: 1: saturday, 2:sunday, etc.... "))
                except:
                    continue

        
    try:
        day_filter = days_list[day_filter]
        print("you choosed {}.".format(day_filter))
    except:
        print("you choosed {}.".format(day_filter))




    # TO DO: get user input for month (all, january, february, ... , june)



    print('-'*40)
    return city, day_filter, filter_answer


month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6}

def load_data(city, day_filter, filter_answer):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    file_name = CITY_DATA[city]
    df = pd.read_csv(file_name)

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day_name()

    if filter_answer != "Non":
        month_number = month_dict[filter_answer]
        df = df[df['Month'] == month_number]
 
    if day_filter != "Non":
        df = df[df['Day'] == day_filter]
    
       
    return df, file_name




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour

    df["Hour"] = df['Start Time'].dt.hour
    #print(df)

    common_month = df['Month'].mode()[0]
    common_day = df['Day'].mode()[0]
    common_hour = df['Hour'].mode()[0]

    print("The most common month is: ", common_month)
    print("The most common day of the week is: ", common_day)
    print("The most common hour of the day is: ", common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip

    df["Trip"] = "from " + df["Start Station"] + " to " + df["End Station"]

    common_start = df['Start Station'].mode()[0]
    common_end = df['End Station'].mode()[0]
    common_trip = df['Trip'].mode()[0]

    print("The most common start station is: ", common_start)
    print("The most common end station is: ", common_end)
    print("The most common trip is: ", common_trip)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time

    total_duration = df["Trip Duration"].sum()
    average_duration = df["Trip Duration"].mean()


    print("The total trip duration time in seconds: ", total_duration)
    print("The averge trip duration time in secods: ", average_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, file_name):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth

    user_types = df['User Type'].value_counts()
    print(user_types)

    if file_name == "washington.csv":
        print("Sorry but the file \"washington.csv\" doesn't have a \"gender\" or \"birth\" coloumns")
    else:
        gender = df["Gender"].value_counts()
        earliest = df["Birth Year"].max()
        recent = df["Birth Year"].min()
        common_year_of_birth = df["Birth Year"].mode()[0]
        print(gender)
        print("the earliest birth year is: ", earliest)
        print("The most recent birth year is: ", recent)
        print("The most common birth year is: ", common_year_of_birth)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def random(file_name):
    '''Gives the user five random rows
    input: the filtered data frame
    output: five random rows
    '''
    df = pd.read_csv(file_name)

    answer = input("Do you want five random rows (Yes or No): ").lower().title()
    answer = answer.strip()

    options_list = ["Yes", "No"]

    while answer not in options_list:
        answer = input("The value that you enterd is invalid, please choose (\"Yes\" OR \"No\") ").lower()
        answer = answer.title().strip()

    while answer == "Yes":
        print(df.sample(n = 5))
        answer = input("Do you want another five random rows (Yes or No): " ).lower().title()
        answer = answer.strip()
        while answer not in options_list:
            answer = input("The value that you enterd is invalid, please choose (\"Yes\" OR \"No\") ").lower()
            answer = answer.title().strip()







def main():
    while True:
        city, filter_answer, day_filter = get_filters()
        df, file_name = load_data(city, filter_answer, day_filter)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, file_name)
        random(file_name)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
