import random

def generate_question():
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    operator = random.choice(['+', '-', '*', '/'])
    
    question = f"What is {num1} {operator} {num2}?"
    return question, eval(str(num1) + operator + str(num2))

def main():
    while True:
        question, correct_answer = generate_question()
        user_answer = input(question + "\nYour answer: ")
        
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if user_answer == correct_answer:
            print("You got the correct answer!")
        else:
            print(f"Sorry, that's incorrect. The correct answer is {correct_answer}.")
        
        play_again = input("Try again? (Y/N): ").upper()
        if play_again != 'Y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()