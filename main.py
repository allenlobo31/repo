import random

def generate_random_number(start, end):
    """Generate a random number between start and end (inclusive)."""
    return random.randint(start, end)

generated_number = generate_random_number(1, 100)
print(f"Generated random number: {generated_number}")