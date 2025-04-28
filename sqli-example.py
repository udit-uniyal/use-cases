import sqlite3

# Vulnerable Code: SQL Injection Example
def get_user_data_vulnerable(username):
    # Directly embedding user input into the query (SQL Injection vulnerability)
    query = "SELECT * FROM users WHERE username = '" + username + "';"
    print(f"Executing query: {query}")
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Secure Code: Fix using Parameterized Queries (Prevents SQL Injection)
def get_user_data_secure(username):
    # Using parameterized queries to prevent SQL Injection
    query = "SELECT * FROM users WHERE username = ?;"
    print(f"Executing query: {query} with parameterized input")
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute(query, (username,))
    results = cursor.fetchall()
    conn.close()
    return results

# Example: Vulnerable function call (Unsecure)
# Uncomment to test the vulnerable function
# print(get_user_data_vulnerable("admin' OR '1'='1"))

# Example: Secure function call (Safe)
print(get_user_data_secure("admin"))
