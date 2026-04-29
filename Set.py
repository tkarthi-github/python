my_card = set()
print(type(my_card))
new_card = {"Karthi",1,5.5,2}
print(type(new_card))

for i in range(5):
    my_card.add(i)

my_card.add("Karthi")

# print(my_card)
# print(new_card)

# new_card.update(my_card)
# print(new_card)


# The Challenge: The "Mutual Friends" Problem
# Imagine you are building a small social network. You have two users, Karthi and Priya. You want to find out:

# Which friends they have in common (Mutual Friends).

# A complete list of everyone in their combined social circle (Total Network).

# Friends that Karthi knows, but Priya does not (Suggestions for Priya).

karthi_friends = {"Alice", "Bob", "Charlie", "David"}
priya_friends = {"Charlie", "David", "Eve", "Frank"}

# Your Tasks:

# Find Mutual Friends: Use the Intersection (&) operator.

mutual_friends = karthi_friends & priya_friends

print(mutual_friends)

# Combine the Networks: Use the Union (|) operator.

combine_friends = karthi_friends | priya_friends

print(combine_friends)

# Find Unique Friends: Use the Difference (-) operator to see who Karthi knows that Priya doesn't.

karthi_unique_friends = karthi_friends - priya_friends

print(karthi_unique_friends)

# ======================================================

# 1. The "Spam Filter" (Filtering Forbidden Words)
# In this scenario, you have a sentence from a user and a set of "forbidden" words. 
# You want to see if the user used any bad language. 
# Using a Set Intersection makes this incredibly fast.

forbidden_words = {"spam", "ad", "buy", "click"}

message = "Hello friend, please here to  my product"

words_set = set(message.lower().split())

found_any_forbidden_words = words_set & forbidden_words

print(found_any_forbidden_words)


if found_any_forbidden_words:
    print(f"Forbidden words are found in the message {found_any_forbidden_words}")
else:
    print(f"Given message is clean")

# ===========================================================

# Try to combine everything you've learned into one final script. Suppose you have two lists of email addresses (maybe from two different newsletters) and you want to clean them up.

# Try to write a script that:

# Removes duplicates from each list.

# Finds people who are subscribed to both newsletters.

# Finds the total number of unique subscribers across both lists.

# Hint:

# Use set() to clean the lists.

# Use & for the common subscribers.

# Use | for the total unique count.

# List 1: Newsletter A subscribers (with some repeats)
newsletter_a = [
    "karthi@email.com", "priya@email.com", "arun@email.com", 
    "karthi@email.com", "vijay@email.com"
]

# List 2: Newsletter B subscribers (with some overlaps from A)
newsletter_b = [
    "deepa@email.com", "arun@email.com", "suresh@email.com", 
    "priya@email.com", "deepa@email.com"
]

set_a = set(newsletter_a)
set_b = set(newsletter_b)

common_subscribers = set_a & set_b
total_subscribers = set_a | set_b
print(f"Common Subscribers - {common_subscribers}")
print(f"Total Subscribers - {len(total_subscribers)}")