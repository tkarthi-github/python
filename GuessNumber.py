import random
import datetime as dt

MIN_VALUE = 1
MAX_VALUE = 100
MAX_ATTEMPTS = 5

def play_guessing_game(min_val, max_val, max_attempts, secret_number):

    attempt_count = 0

    logFileName = str(dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".txt"
    with open(logFileName, "w") as log_file:
        while attempt_count < max_attempts:
            user_input_str = input(f"Enter a number ({min_val}-{max_val}) -> ")
            try:
                user_input = int(user_input_str)
            except ValueError:
                log_file.write(f"Invalid input: {user_input_str}\n")
                print("Invalid input! Please enter a whole number (e.g., 54).")
                continue
            except KeyboardInterrupt:
                log_file.write("Game interrupted by user.\n")
                print("\nGame Interrupted by User. Exiting...")
                return
            if user_input > max_val or user_input < min_val:
                log_file.write(f"Out of range: {user_input}\n")
                print(f"Out of range! Please enter a number between {min_val} and {max_val}.")
                continue

            attempt_count += 1

            log_file.write(f"Attempt {attempt_count}: {user_input}\n")

            if user_input == secret_number:
                log_file.write(f"Guessed correctly in {attempt_count} attempts.\n")
                print(f"Well Done! You guessed it in {attempt_count} attempts.")
                return
            elif user_input < secret_number:
                print(f"Too small! Remaining attempts: {max_attempts - attempt_count}")
            else:
                print(f"Too high! Remaining attempts: {max_attempts - attempt_count}")
                
        log_file.write(f"Failed after {max_attempts} attempts. Secret number was {secret_number}.\n")
        log_file.write(f"Game Over.!\n")
        print(f"You have used all your attempts. The Secret Number was {secret_number}.")


if __name__ == "__main__":
    generated_secret = random.randint(MIN_VALUE, MAX_VALUE)
    play_guessing_game(MIN_VALUE, MAX_VALUE, MAX_ATTEMPTS, generated_secret)
    print("Game Over..!")