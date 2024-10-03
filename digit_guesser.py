import random 

def get_question():
    digits = list(range(10)) 
    random.shuffle(digits) 
    return digits[:3]

def get_answer():
    user_input = input("What is your guess? ")
    while True:
        if len(user_input) == 3 and " " not in user_input:
            try:
                int(user_input)
            except ValueError:
                user_input = input("Enter three numbers. No other characters. ")
            else:
                return user_input
        else:
            user_input = input("Enter three numbers. No other characters. ")

def is_index_matched(q_index, a_index):
    if q_index == int(a_index):
        return True
    else:
        return False

def is_close(question_numbers, answer_numbers):
    for i in answer_numbers:
        if int(i) in question_numbers:
            return True
    return False

def is_match(question_numbers, answer_numbers):
    q = question_numbers
    a = answer_numbers
    return is_index_matched(q[0], a[0]) or is_index_matched(q[1], a[1]) or is_index_matched(q[2], a[2])

def is_perfect_match(question_numbers, answer_numbers):
    q = question_numbers
    a = answer_numbers
    return is_index_matched(q[0], a[0]) and is_index_matched(q[1], a[1]) and is_index_matched(q[2], a[2])

def is_result_correct(question_numbers, answer_numbers):
    if is_perfect_match(question_numbers, answer_numbers):
        print("Perfect Match")
        return True
    elif is_match(question_numbers, answer_numbers):
        print("Match")
        return False
    elif is_close(question_numbers, answer_numbers):
        print("Close")
        return False
    print("Nope")
    return False


intro = """Welcome to 'Digit Guesser'!
1. The computer will think of 3 digit number that has no repeating digits. 
2. You will then guess a 3 digit number.
3. The computer will then give back clues, the possible clues are: 
    - Nope: You haven't guess any of the numbers correctly 
    - Close: You've guessed a correct number but in the wrong position. 
    - Match: You've guessed a correct number in the correct position.
    - Perfect Match: You've guessed all correct numbers in their correct positions.
4. You have 20 tries."""

print(intro)

question = get_question()
answer = get_answer()
tries = 20


while not is_result_correct(question, answer) and tries != 0:
    tries -= 1
    if tries == 0:
        print("Oups... too many wrong guesses.")
    else:
        print(f"{tries} left.")
        answer = get_answer()