import threading
import time
import math
import re
from collections import Counter

# --- Exercise 1: Threaded Prime Number Checker ---

def is_prime(n):
    """
    Checks if a number is prime using trial division.
    This is a simple but effective method for this exercise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check divisors from 5 up to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_in_chunk(start, end, result_list, lock):
    """
    Worker function for each thread. Finds primes in a given sub-range.
    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).
        result_list (list): A shared list to store found prime numbers.
        lock (threading.Lock): A lock to safely append to the result_list.
    """
    primes_found = []
    print(f"Thread {threading.current_thread().name}: Checking range {start}-{end}")
    for number in range(start, end + 1):
        if is_prime(number):
            primes_found.append(number)
    
    # Acquire the lock to safely update the shared list
    with lock:
        result_list.extend(primes_found)
    print(f"Thread {threading.current_thread().name}: Finished, found {len(primes_found)} primes.")

def run_prime_checker(max_number=100000, num_threads=4):
    """
    Main function to orchestrate the threaded prime number checking.
    """
    print(f"--- Starting Prime Number Checker for numbers up to {max_number} using {num_threads} threads ---")
    start_time = time.time()
    
    # Shared resources for all threads
    all_primes = []
    lock = threading.Lock()
    threads = []
    
    # Divide the range into chunks for each thread
    chunk_size = max_number // num_threads
    for i in range(num_threads):
        start_range = i * chunk_size + 1
        end_range = (i + 1) * chunk_size
        if i == num_threads - 1:
            end_range = max_number # Ensure the last thread covers the remainder
        
        # Create and start the thread
        thread = threading.Thread(target=find_primes_in_chunk, args=(start_range, end_range, all_primes, lock), name=f"PrimeThread-{i+1}")
        threads.append(thread)
        thread.start()
        
    # Wait for all threads to complete their execution
    for thread in threads:
        thread.join()
        
    end_time = time.time()
    
    # Sort the final list for clean output
    all_primes.sort()
    
    print("\n--- Results ---")
    print(f"Found {len(all_primes)} prime numbers.")
    # print(f"Primes: {all_primes}") # Uncomment to see the full list
    print(f"Total execution time: {end_time - start_time:.2f} seconds.")


# --- Exercise 2: Threaded File Word Counter ---

def create_dummy_file(filename="large_text_file.txt", lines=50000):
    """
    Generates a large text file for the word counting exercise.
    """
    print(f"Creating a dummy file named '{filename}'...")
    words = ["python", "threading", "is", "fun", "and", "powerful", "for", "io", "bound", "tasks", "like", "file", "processing"]
    with open(filename, "w") as f:
        for i in range(lines):
            f.write(f"Line {i}: {' '.join(words[i % len(words):] + words[:i % len(words)])}\n")
    print("Dummy file created successfully.")

def count_words_in_chunk(lines_chunk, global_word_counts, lock):
    """
    Worker function for each thread. Counts words in a list of lines.
    Args:
        lines_chunk (list): A list of strings (lines from the file).
        global_word_counts (Counter): A shared Counter object to store final word counts.
        lock (threading.Lock): A lock to safely update the global Counter.
    """
    local_word_counts = Counter()
    print(f"Thread {threading.current_thread().name}: Processing {len(lines_chunk)} lines.")
    for line in lines_chunk:
        # Use regex to find all words, convert to lowercase
        words = re.findall(r'\b\w+\b', line.lower())
        local_word_counts.update(words)
        
    # Acquire the lock to safely update the shared global counter
    with lock:
        global_word_counts.update(local_word_counts)
    print(f"Thread {threading.current_thread().name}: Finished processing.")

def run_word_counter(filename="large_text_file.txt", num_threads=4):
    """
    Main function to orchestrate the threaded word counting.
    """
    # First, ensure the file exists
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        create_dummy_file(filename)
        with open(filename, "r") as f:
            lines = f.readlines()

    print(f"\n--- Starting Word Counter for '{filename}' using {num_threads} threads ---")
    start_time = time.time()

    # Shared resources for all threads
    total_word_counts = Counter()
    lock = threading.Lock()
    threads = []
    
    # Divide the lines into chunks for each thread
    total_lines = len(lines)
    chunk_size = total_lines // num_threads
    
    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = start_index + chunk_size
        if i == num_threads - 1:
            end_index = total_lines # Ensure the last thread gets the remainder
            
        chunk = lines[start_index:end_index]
        
        # Create and start the thread
        thread = threading.Thread(target=count_words_in_chunk, args=(chunk, total_word_counts, lock), name=f"WordThread-{i+1}")
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    end_time = time.time()
    
    print("\n--- Results ---")
    print(f"Top 10 most common words:")
    for word, count in total_word_counts.most_common(10):
        print(f"- {word}: {count} times")
    print(f"Total execution time: {end_time - start_time:.2f} seconds.")


def demo_prime_checker():
    """Demonstrate the threaded prime checker with user input."""
    print("EXERCISE 1: Threaded Prime Number Checker")
    print("=" * 50)
    
    try:
        start_range = int(input("Enter the start of the range: "))
        end_range = int(input("Enter the end of the range: "))
        num_threads = int(input("Enter the number of threads: "))
        
        if start_range > end_range:
            print("Start range must be less than or equal to end range.")
            return
            
        if num_threads <= 0:
            print("Number of threads must be positive.")
            return
            
        # Adjust the run_prime_checker function to accept start_range and end_range
        print(f"\n--- Starting Prime Number Checker for numbers from {start_range} to {end_range} using {num_threads} threads ---")
        start_time = time.time()
        
        # Shared resources for all threads
        all_primes = []
        lock = threading.Lock()
        threads = []
        
        # Calculate the range size
        range_size = end_range - start_range + 1
        chunk_size = range_size // num_threads
        
        for i in range(num_threads):
            start_num = start_range + i * chunk_size
            end_num = start_range + (i + 1) * chunk_size - 1
            if i == num_threads - 1:
                end_num = end_range  # Ensure the last thread covers the remainder
            
            # Create and start the thread
            thread = threading.Thread(target=find_primes_in_chunk, args=(start_num, end_num, all_primes, lock), name=f"PrimeThread-{i+1}")
            threads.append(thread)
            thread.start()
            
        # Wait for all threads to complete their execution
        for thread in threads:
            thread.join()
            
        end_time = time.time()
        
        # Sort the final list for clean output
        all_primes.sort()
        
        print("\n--- Results ---")
        print(f"Found {len(all_primes)} prime numbers.")
        if all_primes:
            print(f"First 10 primes: {all_primes[:10]}")
            print(f"Last 10 primes: {all_primes[-10:]}")
        print(f"Total execution time: {end_time - start_time:.2f} seconds.")
        
    except ValueError:
        print("Please enter valid integers for range and number of threads.")
    except Exception as e:
        print(f"An error occurred: {e}")

def demo_file_processor():
    """Demonstrate the threaded file processor with user input."""
    print("EXERCISE 2: Threaded File Word Counter")
    print("=" * 50)
    
    try:
        filename = input("Enter the filename (or press Enter for 'large_text_file.txt'): ").strip()
        if not filename:
            filename = "large_text_file.txt"
            
        num_threads = int(input("Enter the number of threads: "))
        
        if num_threads <= 0:
            print("Number of threads must be positive.")
            return
            
        run_word_counter(filename, num_threads)
        
    except ValueError:
        print("Please enter a valid integer for number of threads.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main_menu():
    """Main menu for the threading homework."""
    while True:
        print("\n--- Threading Homework Menu ---")
        print("1. Run Prime Number Checker")
        print("2. Run File Word Counter")
        print("3. Run Both")
        print("4. Exit")
        
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                demo_prime_checker()
            elif choice == "2":
                demo_file_processor()
            elif choice == "3":
                print("\n--- Running Both Programs ---")
                demo_prime_checker()
                print("\n" + "-" * 25 + "\n")
                demo_file_processor()
                print("\n--- Both Programs Finished ---")
            elif choice == "4":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main_menu()
