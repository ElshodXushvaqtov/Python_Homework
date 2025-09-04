import pandas as pd
import numpy as np

# Tackoverflow

try:
    df = pd.read_csv('tackoverflow_qa.csv', parse_dates=['creationdate'])
except FileNotFoundError:
    print("Error: The file 'tackoverflow_qa.csv' was not found.")
    exit()


print(df.head())
print("-" * 50)


# Task 1: Find all questions that were created before 2014
questions_before_2014 = df[df['creationdate'].dt.year < 2014]
print(questions_before_2014)
print("-" * 50)


# Task 2: Find all questions with a score more than 50
high_score_questions = df[df['score'] > 50]
print(high_score_questions)
print("-" * 50)


# Task 3: Find all questions with a score between 50 and 100
score_50_to_100 = df[df['score'].between(50, 100, inclusive='both')]
print(score_50_to_100)
print("-" * 50)


# Task 4: Find all questions answered by Scott Boston
answered_by_scott = df[df['ans_name'] == 'Scott Boston']
print(answered_by_scott)
print("-" * 50)


# Task 5: Find all questions answered by the following 5 users
# Note: The prompt did not specify the 5 users, so I'm using a sample list
# from the provided data.
users_to_find = ['Scott Boston', 'Unutbu', 'Demetri', 'EdChum', 'James McHenry']
answered_by_users = df[df['ans_name'].isin(users_to_find)]
print(answered_by_users)
print("-" * 50)


# Task 6: Find all questions created between March, 2014 and October 2014 that
# were answered by Unutbu and have a score less than 5.
filtered_questions = df[
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['ans_name'] == 'Unutbu') &
    (df['score'] < 5)
]
print(filtered_questions)
print("-" * 50)


# Task 7: Find all questions that have a score between 5 and 10 OR have a
# view count of greater than 10,000.
filtered_questions_or = df[
    (df['score'].between(5, 10, inclusive='both')) |
    (df['viewcount'] > 10000)
]
print(filtered_questions_or)
print("-" * 50)


# Task 8: Find all questions that are not answered by Scott Boston
not_scott_boston = df[df['ans_name'] != 'Scott Boston']
print(not_scott_boston)
print("-" * 50)

# Titanic

try:
    titanic_df = pd.read_csv("titanic.csv")
except FileNotFoundError:
    print("Error: The file 'titanic.csv' was not found.")
    exit()


print(titanic_df.head())
print("-" * 50)


# Task 1: Select Female Passengers in Class 1 with Ages between 20 and 30
female_class1_20_30 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'].between(20, 30))
]
print(female_class1_20_30)
print("-" * 50)


# Task 2: Filter Passengers Who Paid More than $100
high_fare_passengers = titanic_df[titanic_df['Fare'] > 100]
print(high_fare_passengers)
print("-" * 50)


# Task 3: Select Passengers Who Survived and Were Alone
survived_alone = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]
print(survived_alone)
print("-" * 50)


# Task 4: Filter Passengers Embarked from 'C' and Paid More Than $50
embarked_c_high_fare = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]
print(embarked_c_high_fare)
print("-" * 50)


# Task 5: Select Passengers with Siblings or Spouses and Parents or Children
with_family = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]
print(with_family)
print("-" * 50)


# Task 6: Filter Passengers Aged 15 or Younger Who Didn't Survive
child_non_survivors = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]
print(child_non_survivors)
print("-" * 50)


# Task 7: Select Passengers with Cabins and Fare Greater Than $200
cabin_high_fare = titanic_df[
    (titanic_df['Cabin'].notna()) &
    (titanic_df['Fare'] > 200)
]
print(cabin_high_fare)
print("-" * 50)


# Task 8: Filter Passengers with Odd-Numbered Passenger IDs
odd_id_passengers = titanic_df[titanic_df['PassengerId'] % 2 != 0]
print(odd_id_passengers)
print("-" * 50)


# Task 9: Select Passengers with Unique Ticket Numbers
unique_ticket_passengers = titanic_df.drop_duplicates(subset=['Ticket'])
print(unique_ticket_passengers)
print("-" * 50)


# Task 10: Filter Passengers with 'Miss' in Their Name and Were in Class 1
miss_class1 = titanic_df[
    titanic_df['Name'].str.contains('Miss', na=False) &
    (titanic_df['Pclass'] == 1)
]
print(miss_class1)
print("-" * 50)
