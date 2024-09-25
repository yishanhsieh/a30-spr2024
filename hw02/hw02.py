#Craps Problem
import random

def calculate_expected_value():
    # P(win) = 1/6, payout on win = 4 (since you get back your bet), payout on loss = -1
    P_win = 1/6
    P_loss = 5/6
    payout_win = 4  # Net gain (house pays 4 chips)
    payout_loss = -1  # Net loss (you lose your bet)

    # Expected Value
    EV = (P_win * payout_win) + (P_loss * payout_loss)
    return EV

def simulate_craps_game(num_games):
    """Simulates the Craps game for a given number of games and returns the net chips gained."""
    net_chips = 0  # Keeps track of net winnings
    
    for _ in range(num_games):
        # Simulate rolling two dice
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        
        if total == 7:
            net_chips += 4  # You win 4 chips (net gain)
        else:
            net_chips -= 1  # You lose 1 chip

    return net_chips

# Calculate expected value
EV = calculate_expected_value()
print(f"Expected value of playing the game: {EV} chips per game")

# Simulate playing 10,000 games
num_games = 10000
net_gain = simulate_craps_game(num_games)
average_gain = net_gain / num_games
print(f"After {num_games} games, the average gain per game is: {average_gain:.4f} chips")

# Determine if the game is fair based on EV
if EV == 0:
    print("The game is perfectly fair.")
elif EV > 0:
    print("The game favors the player.")
else:
    print("The game favors the house.")

#Dice Problem
import itertools

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_non_prime_sums():
    """Counts how many of the sums of three dice rolls are not prime."""
    non_prime_count = 0
    total_outcomes = 0
    prime_numbers = {3, 5, 7, 11, 13, 17}  # Prime numbers between 3 and 18

    # Generate all possible outcomes for rolling 3 dice
    for roll in itertools.product(range(1, 7), repeat=3):
        dice_sum = sum(roll)
        total_outcomes += 1
        
        if dice_sum not in prime_numbers:
            non_prime_count += 1

    return non_prime_count, total_outcomes

# Get non-prime counts and total outcomes
non_prime_count, total_outcomes = count_non_prime_sums()

# Probability calculation
probability_non_prime = non_prime_count / total_outcomes

# Output results
print(f"Total possible outcomes: {total_outcomes}")
print(f"Number of outcomes where the sum is not prime: {non_prime_count}")
print(f"Probability that the sum is not a prime number: {probability_non_prime:.4f}")

#Math Problem
def toggle_lockers(num_lockers):
    # Initialize the lockers: False means closed, True means open
    lockers = [False] * num_lockers

    # Go through each student
    for student in range(1, num_lockers + 1):
        for locker in range(student - 1, num_lockers, student):
            # Toggle the locker (True <=> open, False <=> closed)
            lockers[locker] = not lockers[locker]

        # Display the state of lockers after each student passes
        lockers_state = ['O' if state else 'C' for state in lockers]
        print(f"After student {student}: {lockers_state}")

    # Return the final state of lockers
    return lockers

def find_open_lockers(lockers):
    # Return the indices (locker numbers) of lockers that are open
    open_lockers = [i + 1 for i, state in enumerate(lockers) if state]
    return open_lockers

# Number of lockers
num_lockers = 100

# Toggle the lockers
print("------------------- Locker Toggling Stages -------------------")
final_lockers = toggle_lockers(num_lockers)

# Find out which lockers are open
open_lockers = find_open_lockers(final_lockers)

# Print final result
print("\n------------------- Final Open Lockers -------------------")
print(f"Lockers that remain open: {open_lockers}")


# Coin Flip Problem
import random

def simulate_flips(num_flips):
    """Simulates a series of coin flips, returns a list of 'H' for heads and 'T' for tails."""
    flips = []
    for _ in range(num_flips):
        flip = 'H' if random.randint(0, 1) == 0 else 'T'
        flips.append(flip)
    return flips

def has_streak(coin_flips, streak_length):
    """Checks if there's a streak of the specified length in the coin flips."""
    current_streak = 1  # Initialize streak count at 1
    
    for i in range(1, len(coin_flips)):
        if coin_flips[i] == coin_flips[i - 1]:
            current_streak += 1
        else:
            current_streak = 1  # Reset streak if the current flip doesn't match the previous
        
        if current_streak == streak_length:
            return True
    return False

def perform_experiment(num_experiments, num_flips, streak_length):
    """Runs the experiment multiple times and calculates how often a streak occurs."""
    streak_count = 0

    for _ in range(num_experiments):
        flips = simulate_flips(num_flips)
        if has_streak(flips, streak_length):
            streak_count += 1

    # Calculate the percentage of experiments that had a streak
    return (streak_count / num_experiments) * 100

# Set parameters
num_experiments = 10000  # Number of times to repeat the experiment
num_flips = 100  # Number of coin flips in each experiment
streak_length = 6  # Length of streak to look for

# Run the experiment and print the result
print("Running the coin flip streak experiment 10,000 times...")
streak_percentage = perform_experiment(num_experiments, num_flips, streak_length)
print(f"Percentage of experiments with a streak of six heads or tails: {streak_percentage:.2f}%")



#Problem 1 Lee and Hubbard
class Complex:
    """Class to represent complex numbers of the form a + ib."""
    
    def __init__(self, real, imag):
        """Initializes the complex number."""
        self.real = real
        self.imag = imag

    def __str__(self):
        """Returns a string representation of the complex number."""
        return f"({self.real} + {self.imag}i)"

    def __add__(self, other):
        """Defines the addition of two complex numbers."""
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return Complex(real_part, imag_part)

    def __mul__(self, other):
        """Defines the multiplication of two complex numbers."""
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

# Testing the Complex class
print("---------------------------Complex Numbers---------------------------")
c1 = Complex(2, 3)
c2 = Complex(1, 4)

# Addition
sum_result = c1 + c2
print(f"{c1} + {c2} = {sum_result}")

# Multiplication
mul_result = c1 * c2
print(f"{c1} * {c2} = {mul_result}")
#Problem 2 Lee and Hubbard
class Creature:
    """Base class for a creature."""
    
    def __init__(self, name):
        """Initializes the creature with a name."""
        self.name = name
    
    def speak(self):
        """Default speak method for a generic creature."""
        return f"My name is {self.name} and I am a Creature."

class Dog(Creature):
    """Dog class, subclass of Creature."""
    
    def speak(self):
        """Override speak method for a Dog."""
        return f"My name is {self.name} and I am a Dog: woof."

class Cow(Creature):
    """Cow class, subclass of Creature."""
    
    def speak(self):
        """Override speak method for a Cow."""
        return f"My name is {self.name} and I am a Cow: moo."

# Testing the Creature hierarchy
print("---------------------------Creatures---------------------------")
creature = Creature("Generic Creature")
dog = Dog("Rex")
cow = Cow("Bessie")

print(creature.speak())  # Output: My name is Generic Creature and I am a Creature.
print(dog.speak())       # Output: My name is Rex and I am a Dog: woof.
print(cow.speak())       # Output: My name is Bessie and I am a Cow: moo.