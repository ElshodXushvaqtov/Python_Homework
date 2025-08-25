from datetime import date, timedelta, timezone, datetime
import time
import re



1.

def calculate_age(birthdate):
    today = date.today()
    years = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        years -= 1
    months = today.month - birthdate.month
    if months < 0:
        months += 12
    days = today.day - birthdate.day
    if days < 0:
        months -= 1
        if today.month == 1:
            days_in_prev_month = 31
        else:
            temp_date = date(today.year, today.month, 1)
            days_in_prev_month = (temp_date - date.resolution).day
        days += days_in_prev_month
    if months < 0:
        years -= 1
        months += 12
    return years, months, days

print("Age Calculator")
print("Please enter your birthdate to find out your age.")

try:
    year = int(input("Year (YYYY): "))
    month = int(input("Month (MM): "))
    day = int(input("Day (DD): "))

    birthdate = date(year, month, day)

    if birthdate > date.today():
        print("Your birthdate cannot be in the future. Please try again.")
    else:
        age_years, age_months, age_days = calculate_age(birthdate)
        print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")

except ValueError:
    print("Invalid input. Please ensure you enter valid numbers for year, month, and day.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")



2.

def days_until_next_birthday(birthdate_month, birthdate_day):
    today = date.today()
    
    current_year_birthday = date(today.year, birthdate_month, birthdate_day)
    
    if current_year_birthday > today:
        days_left = (current_year_birthday - today).days
    else:
        next_year_birthday = date(today.year + 1, birthdate_month, birthdate_day)
        days_left = (next_year_birthday - today).days
        
    return days_left

print("Days Until Next Birthday")
print("Let's see how many days until your next celebration.")

try:
    month = int(input("Your birth month (MM): "))
    day = int(input("Your birth day (DD): "))
    
    if not (1 <= month <= 12 and 1 <= day <= 31):
        print("Invalid month or day. Please enter values like MM (1-12) and DD (1-31).")
    else:
        days_left = days_until_next_birthday(month, day)
        print(f"There are {days_left} days until your next birthday!")

except ValueError:
    print("Invalid input. Please enter numbers for the month and day.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")



3.

def schedule_meeting_end(current_dt_str, duration_hours, duration_minutes):
    current_datetime = datetime.strptime(current_dt_str, "%Y-%m-%d %H:%M")
    meeting_duration = timedelta(hours=duration_hours, minutes=duration_minutes)
    end_datetime = current_datetime + meeting_duration
    return end_datetime

print("Meeting Scheduler")
print("Let's figure out when your meeting will wrap up.")

try:
    current_dt_input = input("Enter current date and time (YYYY-MM-DD HH:MM, e.g., 2025-08-21 10:30): ")
    hours = int(input("Enter meeting duration in hours: "))
    minutes = int(input("Enter meeting duration in minutes: "))
    
    meeting_end_time = schedule_meeting_end(current_dt_input, hours, minutes)
    
    print(f"Your meeting will end on: {meeting_end_time.strftime('%Y-%m-%d %H:%M:%S')}")

except ValueError:
    print("Invalid input. Please check your date/time format or duration inputs.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


4.

def convert_timezone_with_offset(dt_str, current_offset_str, target_offset_str):
    naive_dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")

    def parse_offset(offset_str):
        sign = 1 if offset_str[0] == '+' else -1
        hours = int(offset_str[1:3])
        minutes = int(offset_str[4:6])
        return timezone(timedelta(hours=sign * hours, minutes=sign * minutes))

    current_tz = parse_offset(current_offset_str)
    target_tz = parse_offset(target_offset_str)

    aware_dt = naive_dt.replace(tzinfo=current_tz)
    converted_dt = aware_dt.astimezone(target_tz)
    
    return converted_dt

print("Timezone Converter (UTC Offset)")
print("Note: This program handles fixed UTC offsets, not named timezones like 'EST'.")

try:
    dt_input = input("Enter date and time (YYYY-MM-DD HH:MM, e.g., 2025-08-21 10:30): ")
    current_offset = input("Enter current UTC offset (e.g., +05:00, -04:00): ")
    target_offset = input("Enter target UTC offset (e.g., -07:00, +01:00): ")
    
    converted_time = convert_timezone_with_offset(dt_input, current_offset, target_offset)
    
    print(f"Original time: {dt_input} {current_offset}")
    print(f"Converted time: {converted_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")

except ValueError:
    print("Invalid input. Please check your date/time format or offset inputs (e.g., +05:00).")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


5.

def start_countdown_timer(target_dt_str):
    target_datetime = datetime.strptime(target_dt_str, "%Y-%m-%d %H:%M:%S")
    
    print(f"Starting countdown to {target_datetime.strftime('%Y-%m-%d %H:%M:%S')}")

    while True:
        now = datetime.now()
        time_remaining = target_datetime - now

        if time_remaining.total_seconds() <= 0:
            print("Time's up! The event has begun!")
            break
        
        days = time_remaining.days
        seconds = int(time_remaining.total_seconds())
        hours = seconds // 3600 % 24
        minutes = seconds // 60 % 60
        remaining_seconds = seconds % 60

        print(f"Time Remaining: {days} days, {hours:02d} hours, {minutes:02d} minutes, {remaining_seconds:02d} seconds", end='\r')
        
        time.sleep(1)

print("Countdown Timer")
print("Enter a future date and time to start the countdown.")

try:
    target_dt_input = input("Enter target date and time (YYYY-MM-DD HH:MM:SS, e.g., 2025-09-01 09:00:00): ")
    
    if datetime.strptime(target_dt_input, "%Y-%m-%d %H:%M:%S") <= datetime.now():
        print("The target date and time must be in the future. Please try again.")
    else:
        start_countdown_timer(target_dt_input)

except ValueError:
    print("Invalid input. Please ensure you enter the date and time in the correct format (YYYY-MM-DD HH:MM:SS).")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


6.

def validate_email(email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$"
    
    if re.match(email_pattern, email):
        return True
    else:
        return False

print("Email Validator")
print("Enter an email address to check its validity.")

email_address = input("Enter an email address: ")

if validate_email(email_address):
    print(f"'{email_address}' is a VALID email address!")
else:
    print(f"'{email_address}' is NOT a valid email address.")


7.

def format_phone_number(number_str):
    digits = re.sub(r'\D', '', number_str)
    
    if len(digits) == 10:
        return f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"
    else:
        return "Invalid phone number: Must contain 10 digits."

print("Phone Number Formatter")
print("Enter a 10-digit phone number (e.g., 1234567890 or 123-456-7890).")

phone_input = input("Enter phone number: ")

formatted_number = format_phone_number(phone_input)
print(f"Formatted number: {formatted_number}")


8.

def check_password_strength(password):
    min_length = 8
    
    criteria = []
    if len(password) < min_length:
        criteria.append(f"Must be at least {min_length} characters long.")
    if not re.search(r"[A-Z]", password):
        criteria.append("Must contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        criteria.append("Must contain at least one lowercase letter.")
    if not re.search(r"\d", password):
        criteria.append("Must contain at least one digit.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        criteria.append("Must contain at least one special character (e.g., !@#$%^&*).")

    if not criteria:
        return True, "Strong password."
    else:
        return False, "\n".join(criteria)

print("Password Strength Checker")
print("Enter a password to check its strength.")

password_input = input("Enter your password: ")

is_strong, message = check_password_strength(password_input)

if is_strong:
    print(f"\nPassword is: {message}")
else:
    print("\nPassword is weak. Reasons:")
    print(message)


9.
def find_word_occurrences(text, word):
    word = word.lower()
    text_lower = text.lower()
    
    occurrences = []
    start_index = 0
    while True:
        index = text_lower.find(word, start_index)
        if index == -1:
            break
        occurrences.append(index)
        start_index = index + len(word)
    
    return occurrences

print("Word Finder")
print("This program finds all occurrences of a word in a sample text.")

sample_text = """
The quick brown fox jumps over the lazy dog. The dog was very lazy. 
The fox was quick. This is a test.
"""
print(f"Sample Text:\n---\n{sample_text.strip()}\n---")

search_word = input("Enter the word to find: ")

found_indices = find_word_occurrences(sample_text, search_word)

if found_indices:
    print(f"\nThe word '{search_word}' found at indices: {found_indices}")
    print(f"Total occurrences: {len(found_indices)}")
else:
    print(f"\nThe word '{search_word}' was not found in the text.")


10.

def extract_dates(text):
    date_patterns = [
        r'\d{4}-\d{2}-\d{2}', # YYYY-MM-DD
        r'\d{2}/\d{2}/\d{4}', # MM/DD/YYYY
        r'\d{2}\.\d{2}\.\d{4}'  # DD.MM.YYYY
    ]
    
    found_dates = []
    for pattern in date_patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            try:
                if '-' in match:
                    dt_obj = datetime.strptime(match, '%Y-%m-%d').date()
                elif '/' in match:
                    dt_obj = datetime.strptime(match, '%m/%d/%Y').date()
                elif '.' in match:
                    dt_obj = datetime.strptime(match, '%d.%m.%Y').date()
                found_dates.append(dt_obj.strftime('%Y-%m-%d'))
            except ValueError:
                continue
    
    return sorted(list(set(found_dates)))

print("Date Extractor")
print("This program identifies and prints dates from a given text.")

input_text = input("Enter a text containing dates (e.g., 'Meeting on 2025-08-25 and 09/15/2026. Another one on 01.01.2027.'): ")

extracted_dates = extract_dates(input_text)

if extracted_dates:
    print(f"\nExtracted dates: {', '.join(extracted_dates)}")
else:
    print("\nNo dates were found in the text.")
