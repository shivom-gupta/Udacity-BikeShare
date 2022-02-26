import streamlit as st
from bikeshare import *

st.title('US Bike Sharing')
st.sidebar.title('Options')
city = st.sidebar.selectbox('Select the City: ', ('Chicago', 'Washington', 'New York'))
city = city.lower()
month = st.sidebar.selectbox('Select month: ', months)
day = st.sidebar.selectbox('Select day of week', days)
df = load_data(city, month, day)

pop_mon, pop_day = time_stats(df)
st.subheader('\nCalculating The Most Frequent Times of Travel...\n')
st.write("The most popular month is: {}".format(pop_mon))
st.write("The most popular day of week is : {}".format(pop_day))
st.write("The most popular hour is: {}".format(df['hour'].mode()[0]))

st.subheader('\nCalculating The Most Popular Stations and Trip...\n')
st.write("The most popular starting station is: {}".format(df['Start Station'].mode()[0]))
st.write("The most popular end station is: {}".format(df['End Station'].mode()[0]))
df['combination'] = "from \"" + df['Start Station'] + "\" to \"" + df['End Station'] + "\""
st.write("The most popular trip is: {}".format(df['combination'].mode()[0]))

st.subheader('\nCalculating Trip Duration...\n')
st.write("Total trip duration is: {} seconds".format(df['Trip Duration'].sum()))
st.write("Average duration trip is : {} seconds".format(df['Trip Duration'].mean()))

st.subheader('\nCalculating User Stats...\n')
type_count = df['User Type'].value_counts()
st.write("Number of subscribers: {}".format(type_count[0]))
st.write("Number of customers: {}".format(type_count[1]))
if len(type_count) <= 2:
    st.write("Number of dependent(s): 0")
else:
    st.write("Number of dependent(s): {}".format(type_count[2]))

if city != 'washington':
    # Display counts of gender
    gender_count = df['Gender'].value_counts()
    st.write("Number of male users: {}".format(gender_count[0]))
    st.write("Number of female users: {}".format(gender_count[1]))
    # Display earliest, most recent, and most common year of birth
    st.write("\nYoungest user was born in year: {}".format(int(df['Birth Year'].max())))
    st.write("Oldest user was born in year: {}".format(int(df['Birth Year'].min())))
    st.write("Most users were born in year: {}".format(int(df['Birth Year'].mode())))
else:
    st.write("\n\n There is no data about genders and year of birth of users")
