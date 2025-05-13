import random
import string
import matplotlib.pyplot as plt

# Custom Hash Function
def custom_hash(key, table_size):
    return sum(ord(c) for c in key) % table_size

# Function to generate random strings
def generate_random_string(length=5):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Function to simulate inserting into a hash table
def insert_into_hash_table(hash_function, table_size, data):
    table = [0] * table_size  # Initialize a table with zero values (empty buckets)
    collisions = 0

    for key in data:
        hash_value = hash_function(key, table_size)
        if table[hash_value] != 0:
            collisions += 1
        table[hash_value] += 1

    return collisions, table

# Generate a large dataset of random strings
dataset_size = 1000
random_data = [generate_random_string() for _ in range(dataset_size)]

# Set table size
table_size = 50

# Using custom hash function
custom_collisions, custom_table = insert_into_hash_table(custom_hash, table_size, random_data)

# Using Python's built-in hash function
def python_builtin_hash(key, table_size):
    return hash(key) % table_size

builtin_collisions, builtin_table = insert_into_hash_table(python_builtin_hash, table_size, random_data)

# Output collision analysis
print(f"Collisions with custom hash function: {custom_collisions}")
print(f"Collisions with built-in hash function: {builtin_collisions}")

# Plotting histograms to compare the distribution of hash values
def plot_histogram(table, title):
    plt.hist(table, bins=range(len(set(table))), edgecolor='black', alpha=0.7)
    plt.title(title)
    plt.xlabel("Hash Value")
    plt.ylabel("Frequency")
    plt.show()

# Plot for custom hash function
plot_histogram(custom_table, "Distribution of Hash Values (Custom Hash Function)")

# Plot for built-in hash function
plot_histogram(builtin_table, "Distribution of Hash Values (Built-in Hash Function)")
