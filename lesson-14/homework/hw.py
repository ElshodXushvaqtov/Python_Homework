import json
import os
import requests
import random


1.

STUDENTS_FILE = "students.json"

def create_initial_students_file():
    if not os.path.exists(STUDENTS_FILE):
        initial_data = {
            "students": [
                {"id": 1, "name": "Alice Smith", "major": "Computer Science", "gpa": 3.8},
                {"id": 2, "name": "Bob Johnson", "major": "Electrical Engineering", "gpa": 3.5},
                {"id": 3, "name": "Charlie Brown", "major": "Mathematics", "gpa": 3.9},
                {"id": 4, "name": "Diana Miller", "major": "Physics", "gpa": 3.7}
            ]
        }
        with open(STUDENTS_FILE, 'w') as f:
            json.dump(initial_data, f, indent=4)
        print(f"Created initial {STUDENTS_FILE} with sample data.")

def read_and_print_student_details():
    if not os.path.exists(STUDENTS_FILE):
        print(f"Error: {STUDENTS_FILE} not found. Please run the script once to create it.")
        return

    try:
        with open(STUDENTS_FILE, 'r') as f:
            data = json.load(f)
            
            if "students" in data and isinstance(data["students"], list):
                print(f"\n--- Student Details from {STUDENTS_FILE} ---")
                for student in data["students"]:
                    print(f"ID: {student.get('id', 'N/A')}")
                    print(f"Name: {student.get('name', 'N/A')}")
                    print(f"Major: {student.get('major', 'N/A')}")
                    print(f"GPA: {student.get('gpa', 'N/A')}")
                    print("-" * 20)
            else:
                print(f"No 'students' list found in {STUDENTS_FILE}.")
                
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {STUDENTS_FILE}. Check file integrity.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

create_initial_students_file()
read_and_print_student_details()


2.

API_KEY = "dcab81d11ffbb6d87c652888176e96d2"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def print_weather_details(weather_data):
    if weather_data is None:
        return

    if weather_data.get("cod") == 200:
        city = weather_data["name"]
        country = weather_data["sys"]["country"]
        temp = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        
        print(f"\n--- Current Weather in {city}, {country} ---")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
    else:
        print(f"Error: {weather_data.get('message', 'Could not retrieve weather data')}")

print("Weather Checker")
city = input("Enter the city name (e.g., Tashkent): ")
weather = get_weather(city)
print_weather_details(weather)


3.

BOOKS_FILE = "books.json"

def create_initial_books_file():
    if not os.path.exists(BOOKS_FILE):
        initial_data = {
            "books": [
                {"id": 101, "title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "year": 1979},
                {"id": 102, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
                {"id": 103, "title": "1984", "author": "George Orwell", "year": 1949}
            ]
        }
        with open(BOOKS_FILE, 'w') as f:
            json.dump(initial_data, f, indent=4)
        print(f"Created initial {BOOKS_FILE} with sample data.")

def load_books():
    if not os.path.exists(BOOKS_FILE):
        return {"books": []}
    try:
        with open(BOOKS_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {BOOKS_FILE}. Initializing with empty data.")
        return {"books": []}
    except Exception as e:
        print(f"An unexpected error occurred while loading books: {e}")
        return {"books": []}

def save_books(data):
    try:
        with open(BOOKS_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"An unexpected error occurred while saving books: {e}")

def list_books(books_data):
    if not books_data["books"]:
        print("No books in the collection.")
        return
    print("\n--- Current Books ---")
    for book in books_data["books"]:
        print(f"ID: {book.get('id', 'N/A')}, Title: {book.get('title', 'N/A')}, Author: {book.get('author', 'N/A')}, Year: {book.get('year', 'N/A')}")
    print("---------------------")

def add_book(books_data):
    title = input("Enter new book title: ")
    author = input("Enter new book author: ")
    try:
        year = int(input("Enter publication year: "))
    except ValueError:
        print("Invalid year. Please enter a number.")
        return

    new_id = max([b.get('id', 0) for b in books_data["books"]]) + 1 if books_data["books"] else 101
    
    new_book = {"id": new_id, "title": title, "author": author, "year": year}
    books_data["books"].append(new_book)
    save_books(books_data)
    print(f"Book '{title}' added with ID: {new_id}.")

def update_book(books_data):
    try:
        book_id = int(input("Enter the ID of the book to update: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    found = False
    for book in books_data["books"]:
        if book.get("id") == book_id:
            print(f"Updating book: {book.get('title')} by {book.get('author')}")
            new_title = input(f"Enter new title (current: {book.get('title')}, leave blank to keep): ")
            new_author = input(f"Enter new author (current: {book.get('author')}, leave blank to keep): ")
            new_year_str = input(f"Enter new year (current: {book.get('year')}, leave blank to keep): ")

            if new_title:
                book["title"] = new_title
            if new_author:
                book["author"] = new_author
            if new_year_str:
                try:
                    book["year"] = int(new_year_str)
                except ValueError:
                    print("Invalid year format, year not updated.")
            
            save_books(books_data)
            print(f"Book ID {book_id} updated.")
            found = True
            break
    if not found:
        print(f"Book with ID {book_id} not found.")

def delete_book(books_data):
    try:
        book_id = int(input("Enter the ID of the book to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    initial_len = len(books_data["books"])
    books_data["books"] = [book for book in books_data["books"] if book.get("id") != book_id]
    
    if len(books_data["books"]) < initial_len:
        save_books(books_data)
        print(f"Book ID {book_id} deleted.")
    else:
        print(f"Book with ID {book_id} not found.")

create_initial_books_file()
books_data = load_books()

print("\nBook Management System")
while True:
    print("\nOptions:")
    print("1. List all books")
    print("2. Add new book")
    print("3. Update book")
    print("4. Delete book")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        list_books(books_data)
    elif choice == '2':
        add_book(books_data)
    elif choice == '3':
        update_book(books_data)
    elif choice == '4':
        delete_book(books_data)
    elif choice == '5':
        print("Exiting Book Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


4.

OMDB_API_KEY = "581449fe"
OMDB_BASE_URL = "http://www.omdbapi.com/"

def search_movies_by_genre_keyword(genre_keyword):
    if OMDB_API_KEY == "YOUR_OMDB_API_KEY":
        print("Error: Please replace 'YOUR_OMDB_API_KEY' with your actual OMDb API key.")
        return None

    params = {
        "s": genre_keyword,
        "apikey": OMDB_API_KEY,
        "type": "movie"
    }

    try:
        response = requests.get(OMDB_BASE_URL, params=params)
        response.raise_for_status()
        search_results = response.json()
        
        if search_results.get("Response") == "True" and search_results.get("Search"):
            return search_results["Search"]
        else:
            print(f"No movies found for genre keyword '{genre_keyword}'.")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movie search results: {e}")
        return None

def get_movie_details(imdb_id):
    if OMDB_API_KEY == "YOUR_OMDB_API_KEY":
        return None

    params = {
        "i": imdb_id,
        "apikey": OMDB_API_KEY,
        "plot": "full"
    }

    try:
        response = requests.get(OMDB_BASE_URL, params=params)
        response.raise_for_status()
        movie_details = response.json()
        
        if movie_details.get("Response") == "True":
            return movie_details
        else:
            print(f"Could not fetch details for IMDb ID {imdb_id}: {movie_details.get('Error', 'Unknown error')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movie details: {e}")
        return None

def recommend_movie(genre_input):
    print(f"Searching for movies related to '{genre_input}'...")
    movies = search_movies_by_genre_keyword(genre_input)

    if movies is None:
        return

    if not movies:
        return

    while movies:
        random_movie = random.choice(movies)
        imdb_id = random_movie["imdbID"]
        details = get_movie_details(imdb_id)
        
        if details and details.get("Genre") and genre_input.lower() in details["Genre"].lower():
            print("\n--- Your Movie Recommendation ---")
            print(f"Title: {details.get('Title', 'N/A')}")
            print(f"Year: {details.get('Year', 'N/A')}")
            print(f"Genre: {details.get('Genre', 'N/A')}")
            print(f"Director: {details.get('Director', 'N/A')}")
            print(f"Actors: {details.get('Actors', 'N/A')}")
            print(f"Plot: {details.get('Plot', 'N/A')}")
            print(f"IMDb Rating: {details.get('imdbRating', 'N/A')}")
            print("---------------------------------")
            return
        else:
            movies.remove(random_movie)
            if not movies:
                print(f"Could not find a matching movie for '{genre_input}' after several attempts.")
                return

print("Movie Recommendation System")
print("Find a random movie recommendation based on your preferred genre.")
genre = input("Enter a movie genre (e.g., Action, Comedy, Drama): ")

recommend_movie(genre)
