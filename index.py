# --------------------------------------------------------------
# DODGE THE ROCKS
# A simple text game to practice while loops, conditionals, and variables.
# You’ll move your character left or right to dodge falling rocks.
# --------------------------------------------------------------

import random
import time
from enum import nonmember

# --------------------------------------------------------------
# 1️⃣ GAME INTRO
# --------------------------------------------------------------
print("🌑 Welcome to DODGE THE ROCKS!")
print("Avoid the falling rocks as long as you can!")
print("Use 'L' to move left, 'R' to move right, and 'Q' to quit.\n")

# --------------------------------------------------------------
# 2️⃣ SETUP GAME VARIABLES
# --------------------------------------------------------------

player_position = 3
score = 0
speed = 1.0
# TODO 3: Create a variable named streak and set it to 0.
# TODO 4: Create a variable named game_running and set it to True.
streak = 0
game_running = True
# --------------------------------------------------------------
# 3️⃣ MAIN GAME LOOP
# --------------------------------------------------------------
while True:

    rock_position = random.randint(1, 5)
    print(f"Rock is falling in lane {rock_position}")
    # TODO 7: Print the player’s current lane and score.
    print(f"Your current lane is {player_position} and your score is {score}")
    move = input("Move (L/R/Q): ").strip().upper()

    if move ==  "Q":
        print("You quit the game!")
        break

    # ----------------------------------------------------------
    # 5️⃣ MOVEMENT LOGIC
    # ----------------------------------------------------------
    # TODO 9: If move == "L" and player_position > 1: subtract 1
    #         elif move == "R" and player_position < 5: add 1
    #         else: print("You stayed in the same lane.")
    # TODO 10: Print the player’s new lane.
    if move == "L" and player_position > 1:
        player_position -= 1
    elif move == "R" and player_position < 5:
        player_position += 1
    else:
        print("You stayed in the same lane.")
    print(f"Your new lane is {player_position}.")
    # ----------------------------------------------------------
    # 6️⃣ COLLISION DETECTION
    # ----------------------------------------------------------
    # TODO 11: If player_position == rock_position, print hit and break.
    # TODO 12: Else, print "✅ You dodged the rock!" and add to score/streak.
    if player_position == rock_position:
        print("hit and break.")
    else:
        print("✅ You dodged the rock!")
        score += 1
        streak += 1
    # ----------------------------------------------------------
    # 7️⃣ SPEED INCREASE (DIFFICULTY)
    # ----------------------------------------------------------
    # TODO 13: Every 5 points, reduce speed by 0.1 (but not below 0.2).
    #          Print "⚡ The rocks are falling faster!" Part of #12's Else statement
    if score % 5 == 0 and speed > 0.2:
        speed -= 0.1
        print("⚡ The rocks are falling faster!")
    # ----------------------------------------------------------
    # 8️⃣ BONUS SYSTEM
    # ----------------------------------------------------------
    # TODO 14: If streak == 3, print "🔥 DODGE STREAK!" +2 points, reset streak.
    #           Part of #12's Else statement.
    if streak == 3:
        print("🔥 DODGE STREAK!")
        score += 2
        streak = 0
    # ----------------------------------------------------------
    # 9️⃣ VISUALIZATION (OPTIONAL)
    # ----------------------------------------------------------
    # TODO 15: Print a simple lane map using f-strings:
    #          Example:
    #          print(f"[1][2][3][4][5]")
    #          print(f"Rock in {rock_position} | Player in {player_position}")
    print(f"[1][2][3][4][5]")
    print(f"rock in {rock_position} / Player in {player_position}")
    # ----------------------------------------------------------
    # 🔟 DELAY BETWEEN ROUNDS
    # ----------------------------------------------------------
    time.sleep(speed)

# --------------------------------------------------------------
# 11️⃣ GAME OVER MESSAGE
# --------------------------------------------------------------
print(f"Game Over! Your final score was {score}")
print("Thanks for playing DODGE THE ROCKS!")