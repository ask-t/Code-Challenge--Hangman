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

Hangman game is a word guessing game. player can guess a letter in a trying until knowing the word or after 6 missings. 

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

# Version2

The previous program has some problems, and this code is long, so I tried to simplify it more.

## step1 (remove the constraint of the word’s length)

In the previous version, we can use only words whose length is between 3 to 6. By using for loop, I fixed to be able to deal with any words.

### Previous

```python
secrets = ''
word = 'apple'
l = len(word)
if l == 3:
    secrets = '***'
elif l == 4:
  secrets = '****'
elif l == 5:
  secrets = '*****'
elif l ==6:
  secrets = '******'

print(secrets)

# *****
```

### After

```python
secrets = ''
word = 'apple'
l = len(word)
for _ in range(l):
  secrets += '*'

print(secrets)
	
# *****

```

## Use list comprehension

At this time, I will try to change letters with list, so it is better to use list comprehenshion.

```python
word = 'apple'
length = len(word)
print(length)
l_a = [ '*' for i in range(length)]

#5
#['*', '*', '*', '*', '*']
```

## step2 ( remove constraint of index number)

By using for loop, you do not have to write all index number.

### Previous

```python
word_l = list('apple')
secrets = ['*', '*', '*', '*', '*']
answer = 'p'

if answer == word_l[0]:
  secrets[0] = word_l[0]
if answer == word_l[1]:
  secrets[1] = word_l[1]
if answer == word_l[2]:
  secrets[2] = word_l[2]
if answer == word_l[3]:
  secrets[3] = word_l[3]
if answer == word_l[4]:
  secrets[4] = word_l[4]

print(secrets)

# ['*', 'p', 'p', '*', '*']
```

### After

```python
word_l = list('apple')
secrets = ['*', '*', '*', '*', '*']
answer = 'p'

num = 0

for _ in range(len(word_l)):
  if answer == word_l[num]:
    secrets[num] = word_l[num]
  num += 1

print(secrets)

# ['*', 'p', 'p', '*', '*']
```
