# Code Challenge – Hangman

[https://github.com/ask-t/Code-Challenge--Hangman](https://github.com/ask-t/Code-Challenge--Hangman)

## General info

### Language

Python3

I worked on it on ver3.8.5

### Time

3h20m (9:30am to 12:50pm)

## Purpose

Creating the Hangman game.

Hangman game is a word guessing game. player can guess a letter in a trying until knowing the word or after 6 missings. At this time I ignore this after 6times. Instead of it,  I put a system showing how many times the player try to do.

## Rules & Requirements
1. Greet the user welcoming them to the game

2. The program randomly selects a word from a list of 10 words with different lengths, you as the developer choose the words.

3. The program indicates to the user how many letters are in the word

4. The user is asked to guess a letter

a. If the letter is in the word, the letter is displayed in the correct position of the word with all previously guessed correct letters

b. If the letter is not in the word, display the letter indicating it is not in the word with all previously guessed letters that are not in the word

5. The program displays how many guesses have been made, with how many correct and incorrect guesses.

6. The program continues to ask the user for guesses until all the letters in the word are guessed correctly.

7. When all letters of the word are guessed correctly,

a. the program tells the user they have correctly guessed the word

b. and indicates the number of guesses it took

8. The program then asks the user if they would like to try again or quit

a. If the user indicates they want to continue, the program chooses a different word randomly and the play continues

b. If the user indicates they want to quit, the program thanks them for playing and quits.

9. You can choose to use a terminal interface or a web interface

Extra credit

10. Draw a gallows and person being hanged drawing a new body part each time a guess is wrong

## How to work it

### 1 prepare words for games.

we need to prepare the words and put these on the list.

One thing we need to care about is that we need to choose the word which does not include duplicate letters. 

⭕️ 'orange,’ 'lamb'

❌ ’cheese’, ‘beef’

```python
list_Original = ['orange','lamb', 'grape','cake','flour','milk','cream','bread','pork','pie']
```

### 2 Choose a word randomly

random.choice() can choose a word from the list randomly

```python
correct = random.choice(list_Original)
```

### 3 function

At this time, I prepared four functions, but these are almost the same functions. The only difference depends on word counts.

len() is showing the number of letters 

```python
def six_words():
def five_words():
def four_words():
def three_words():

l = len(correct)

if l == 3:
    three_words()
  elif l == 4:
    four_words()
  elif l == 5:
    five_words()
  elif l ==6:
    six_words()
```

```python
correct = 'orange'
l = len(correct)
>> 6

correct = 'lamb'
l = len(correct)
>> 4
```

### 4 show the letter in the correct position of the word.

In order to do it. First we need to change the string to the list by doing so, it is easy to change letters in specific positions.

```python
word = 'orange'
list(word)
>> ['o','r','a','n','g','e']
```

### 5 hiding the word

First, we need to hyde correct answer. this is also changed to list.

```python
secrets = "******"
secrets = list(secrets)
>> ['*', '*', '*', '*', '*']
```

### 6 changing the word

if the player can find the correct letter, we change * to the correct letter

```python
answer = o

word_l = ['o','r','a','n','g','e']
secrets =['*', '*', '*', '*', '*']

if answer == word_l[0]:
        secrets[0] = word_l[0]
>> ['o', '*', '*', '*', '*']
```

```python
answer = n

word_l = ['o','r','a','n','g','e']
secrets =['o', '*', '*', '*', '*']

if answer == word_l[3]:
        secrets[3] = word_l[3]
>> ['o', '*', '*', 'n', '*']
```

### 7 loop until finding out all letters

By using while, we can loop until finding out all letters. 

when secrets == word_l which means ['o','r','a','n','g','e'] == ['o','r','a','n','g','e'] 

the player can go out of this loop. Also, to show the number how many times the player tries it, it includes the count.

```python
count = 0
while True:
    if secrets == word_l:
      break
    count +=1
```
