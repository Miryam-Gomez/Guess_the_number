# Guess the Number

A simple Python console game where the computer selects a random number between 1 and 100, and the player must guess it. After each attempt, the program gives a hint indicating whether the correct number is higher or lower. The game continues until the player guesses the number correctly.

---

## 🎮 Features

- Random number generation between 1 and 100  
- Input validation to prevent letters or invalid numbers  
- Hints: “higher” or “lower”  
- Counts the number of attempts  
- Simple and beginner‑friendly logic  

---

## 🧠 How It Works

1. The computer generates a random number.  
2. The player enters guesses through the console.  
3. The program checks the input:
   - If it's not a number → shows an error  
   - If it's a valid number → compares it with the secret number  
4. The game gives hints until the player finds the correct answer.  
5. When the player wins, the program displays the total number of attempts.

---

## ▶️ How to Run

Make sure you have **Python 3** installed.

Run the script from your terminal:
python guess_the_number.py

Follow the instructions shown on the screen.

---

## 📝 Example Gameplay

\\\Enter a number: 50
Higher
Enter a number: 75
Lower
Enter a number: 62
You guessed it!
Attempts: 3\\\

---

## 📚 What I Learned

- Using loops to repeat actions  
- Handling errors with `try/except`  
- Working with random number generation  
- Comparing values and giving feedback  
- Building a complete interactive console program  

---

## 🚀 Future Improvements

- Add difficulty levels (easy, medium, hard)  
- Limit the number of attempts  
- Add a scoring system  
- Create a graphical version using Tkinter  
- Make the computer guess the player's number  

---
