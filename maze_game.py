#Final Project
#Jade Hao
#CS110

import os #operating systems
import csv #reads from language csv file
import random #deals with questions
import time #deals with timer

def load_language_data(file_path): #reads data from file
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile: #unicode transformation format
            reader = csv.reader(csvfile)
            next(reader)  #skips the header row
            language_data = {row[0]: row[1] for row in reader if row}
        return language_data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while loading language data: {e}")
    return None

def load_questions(file_path): 
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  #skips the header
        questions = [row for row in reader if row]  #filter out the empty rows
    return questions

def translate_word(language_data, word): #gets the translation of the word from csv file
    return language_data.get(word, "Translation not found.")

def select_language(language_data): #when user selects a langauge makes sure it exists
    while True:
        print("Select a language:")
        for i, language in enumerate(language_data.keys(), start=1):
            print(f"{i}. {language}")

        choice = input("Enter the number corresponding to your choice: ").strip()

        try:
            choice_index = int(choice)
            if 1 <= choice_index <= len(language_data):
                return list(language_data.keys())[choice_index - 1]
            else:
                print("Invalid input. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def select_difficulty():
    while True:
        print('\033[36m' + '\033[1m'+"Select difficulty:"+'\033[0m') #added to make the menu seem more fun
        print("1. Easy (3 questions)")
        print("2. Medium (6 questions)")
        print("3. Hard (9 questions)")
        choice = input("Enter the number corresponding to your choice: ")
        if choice == '1':
            return "easy_maze.txt"
        elif choice == '2':
            return "medium_maze.txt"
        elif choice == '3':
            return "hard_maze.txt"
        else:
            print("Invalid input. Please enter a number between 1 and 3.")

def load_maze(file_path): #if there is an issue with loading the text file it will let the user know
    try:
        with open(file_path, 'r') as file:
            maze = [list(line.strip()) for line in file]
        return maze
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while loading the maze: {e}")
    return None
    pass

def display_maze(maze):
    for row in maze:
        print("".join(row))
    print()
    pass

def get_player_position(maze): #s= start, p=player position- Updates everytime the player moves
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell in {'S','P'}:
                return i, j
    return None

def move_player(maze, direction, language_data): #how the player moves in the maze
    directions = {'w': (-1, 0), 'a': (0, -1), 's': (1, 0), 'd': (0, 1)}
    player_position = get_player_position(maze)

    if player_position is None:
        print("Error: Player ('P') not found in the maze.")
        return False

    current_row, current_col = player_position #looks at the row/colum the player is in
    new_row, new_col = current_row + directions[direction][0], current_col + directions[direction][1]

    if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != '#':
        if maze[new_row][new_col] == 'E': #E= end/exit of the game. Once player reaches that it will display this message
            print('\033[92m'+'\033[1m'"Congratulations! You've reached the end of the maze."+'\033[0m')
            return True  # Signal to end the game
        elif maze[new_row][new_col] == '+':
            print("You've encountered a '+'. Answer the question to continue.")
            question_language = select_language(language_data)
            questions = [q for q in load_questions("language.csv") if q[0] == question_language]

            if not questions:
                print(f"No questions available for {question_language}. Exiting.")
                return True  #signals to end the game

            random_question = random.choice(questions)
            display_question(random_question)

            user_answer = get_user_answer_with_timer()

            if user_answer == "timeout":
                print()
                return True  #ends the game

            correct_answer = random_question[-1].lower()

            if is_correct(user_answer, correct_answer):
                print("Correct! You can continue.\n")
                maze[current_row][current_col] = '.'
                maze[new_row][new_col] = 'P'
                display_maze(maze)
            else:
                print(f"Wrong! The correct answer is {correct_answer.capitalize()}\n")
        else:
            maze[current_row][current_col] = '.'
            maze[new_row][new_col] = 'P'
            display_maze(maze)
        return False
    else:
        return False

def ask_replay():
    restart = input("Do you want to play again? (y/n): ").lower()
    if restart=="y":
        return restart == 'y'
    else:
        print('\033[1m'+ '\033[36m' +'Thank you for playing!'+  '\033[0m')

def display_question(question):
    print('\033[1m'+'\033[94m'+"You have 7 seconds to answer the following question:"+'\033[0m')
    print(f"What is the English translation of '{question[1]}' in {question[0]}?")
    print()

def get_user_answer_with_timer(): #timer portion
    start_time = time.time()
    user_answer = input("Your answer: ").strip().lower()
    elapsed_time = time.time() - start_time

    if elapsed_time > 7: #made it seven seconds, if the time is up will display a Game over message
        print('\033[1m'+ '\033[91m'+ "GAME OVER!!"+'\033[0m')
        print("Time's up! You took 7 seconds to answer.")
        return "timeout"
    else:
        return user_answer

def get_user_answer():
    return input("Your answer: ").strip().lower()

def is_correct(answer, correct_answer):
    return answer == correct_answer.lower()

def play_game(difficulty, language_data):
    maze_file = difficulty
    maze = load_maze(maze_file)

    if maze is None:
        return

    display_maze(maze)

    game_ended = False  # initialize game ended flag

    while not game_ended:
        move = input("Enter your move (w= move UP, a= move LEFT, s=move DOWN, d=move RIGHT), or 'r' to restart, or 'q' to quit: ").lower()

        if move == 'q':
            print('\033[1m'+'\033[91m'+"Quitting the game. Goodbye!"+'\033[0m')
            exit()
        elif move == 'r':
            return True  #restart the game
        elif move in {'w', 'a', 's', 'd'}: #the keys to control movement in the game
            game_ended = move_player(maze, move, language_data)
        else:
            print("Invalid input. Use 'w' to move up, 'a' to move left, 's' to move down, 'd' to move right.")

    if ask_replay():
        return True  #restarts the game
    else:
        exit()

def main():
    print('\033[1m'+'\033[4m'+ "Welcome to the Maze Game!"+ '\033[0m') #allows the text to be bolded and underline
    print('\033[36m' + '\033[1m'+ "Menu:"+'\033[0m')
    print("S= Start point")
    print("P= Postion in Maze")
    print("E= End/Exit of the Maze")
    print("#= Barries that you cannot move to")
    print(".= The path you can take")
    print("+= A question")
    print("\n")
    
    print('\033[1m'+ '\033[94m' + "Enjoy the game!" + '\033[0m')
    print("\n")

    language_file = "language.csv"
    language_data = load_language_data(language_file)

    if language_data is None:
        print("Exiting due to an error loading language data.")
        exit()

    while True:
        difficulty = select_difficulty()

        restart_game = play_game(difficulty, language_data)

        if not restart_game:
            break  # exit the loop if the user chooses not to restart

    if not selected_questions:
        print("No questions available. Exiting.")
        exit()

if __name__ == "__main__":
    main()