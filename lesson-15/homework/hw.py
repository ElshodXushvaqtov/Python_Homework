import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

print("Database created in memory.")

try:
    cursor.execute('''
        CREATE TABLE Roster (
            Name TEXT,
            Species TEXT,
            Age INTEGER
        )
    ''')
    print("Table 'Roster' created successfully.")
except sqlite3.Error as e:
    print(f"Error creating table: {e}")

roster_data = [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
]

try:
    cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", roster_data)
    conn.commit()
    print("Initial data populated.")
except sqlite3.Error as e:
    print(f"Error inserting data: {e}")

try:
    cursor.execute("UPDATE Roster SET Name = 'EzriDax' WHERE Name = 'JadziaDax'")
    conn.commit()
    print("Updated 'Jadzia Dax' to 'EzriDax'.")
except sqlite3.Error as e:
    print(f"Error updating data: {e}")

print("\n--- Bajoran Roster ---")
try:
    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
    bajoran_roster = cursor.fetchall()

    if bajoran_roster:
        for row in bajoran_roster:
            print(f"Name: {row[0]}, Age: {row[1]}")
    else:
        print("No Bajoran species found in the roster.")
except sqlite3.Error as e:
    print(f"Error querying data: {e}")

conn.close()
print("\nDatabase connection closed.")
