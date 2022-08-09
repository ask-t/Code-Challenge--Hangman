import random


def six_words():
  word = correct
  word_l = list(word)
  secrets = "******"
  secrets = list(secrets)
  list_a =[]
  list_b =[]
  count = 0
  while True:
    if secrets == word_l:
      break
    count +=1
    answer = input(f'Round{count}: Please put word >> ')
    list_a.append(answer)
    if len(answer) <2:
      if answer == word_l[0]:
        secrets[0] = word_l[0]
        print(''.join(secrets))
      elif answer == word_l[1]:
        secrets[1] = word_l[1]
        print(''.join(secrets))
      elif answer == word_l[2]:
        secrets[2] = word_l[2]
        print(''.join(secrets))
      elif answer == word_l[3]:
        secrets[3] = word_l[3]
        print(''.join(secrets))
      elif answer == word_l[4]:
        secrets[4] = word_l[4]
        print(''.join(secrets))
      elif answer == word_l[5]:
        secrets[5] = word_l[5]
        print(''.join(secrets))
      else:
        print('it is not in the word.')
        print(''.join(secrets))
        list_b.append(answer)
      b = len(list_b)
      print(f'Now you have used {list_a}\n incorrect answer:{b}')
    else: print('Please put a letter')
  text = f'You take {count} tiems to try\ninccorect answer:{b}'
  print(text)

def five_words():
  word = correct
  word_l = list(word)
  secrets = "*****"
  secrets = list(secrets)
  list_a =[]
  list_b =[]
  count = 0
  while True:
    if secrets == word_l:
      break
    count +=1
    answer = input(f'Round{count}: Please put word >> ')
    list_a.append(answer)
    if len(answer) <2:
      if answer == word_l[0]:
        secrets[0] = word_l[0]
        print(''.join(secrets))
      elif answer == word_l[1]:
        secrets[1] = word_l[1]
        print(''.join(secrets))
      elif answer == word_l[2]:
        secrets[2] = word_l[2]
        print(''.join(secrets))
      elif answer == word_l[3]:
        secrets[3] = word_l[3]
        print(''.join(secrets))
      elif answer == word_l[4]:
        secrets[4] = word_l[4]
        print(''.join(secrets))
      else:
        print('it is not in the word.')
        print(''.join(secrets))
        list_b.append(answer)
      b = len(list_b)
      print(f'Now you have used {list_a}\n incorrect answer:{b}')
    else: print('Please put a letter')
  text = f'You take {count} tiems to try\ninccorect answer:{b}'
  print(text)

def four_words():
  word = correct
  word_l = list(word)
  secrets = "****"
  secrets = list(secrets)
  list_a =[]
  list_b =[]
  count = 0
  while True:
    if secrets == word_l:
      break
    count +=1
    answer = input(f'Round{count}: Please put word >> ')
    list_a.append(answer)
    if len(answer) <2:
      if answer == word_l[0]:
        secrets[0] = word_l[0]
        print(''.join(secrets))
      elif answer == word_l[1]:
        secrets[1] = word_l[1]
        print(''.join(secrets))
      elif answer == word_l[2]:
        secrets[2] = word_l[2]
        print(''.join(secrets))
      elif answer == word_l[3]:
        secrets[3] = word_l[3]
        print(''.join(secrets))
      else:
        print('it is not in the word.')
        print(''.join(secrets))
        list_b.append(answer)
      b = len(list_b)
      print(f'Now you have used {list_a}\n incorrect answer:{b}')
    else: print('Please put a letter')
  text = f'You take {count} tiems to try\ninccorect answer:{b}'
  print(text)

def three_words():
  word = correct
  word_l = list(word)
  secrets = "***"
  secrets = list(secrets)
  list_a =[]
  list_b =[]
  count = 0
  while True:
    if secrets == word_l:
      break
    count +=1
    answer = input(f'Round{count}: Please put word >> ')
    list_a.append(answer)
    if len(answer) <2:
      if answer == word_l[0]:
        secrets[0] = word_l[0]
        print(''.join(secrets))
      elif answer == word_l[1]:
        secrets[1] = word_l[1]
        print(''.join(secrets))
      elif answer == word_l[2]:
        secrets[2] = word_l[2]
        print(''.join(secrets))
      else:
        print('it is not in the word.')
        print(''.join(secrets))
        list_b.append(answer)
      b = len(list_b)
      print(f'Now you have used {list_a}\n incorrect answer:{b}')
    else: print('Please put a letter')
  text = f'You take {count} tiems to try\ninccorect answer:{b}'
  print(text)

list_Original = ['orange','lamb', 'grape','cake','flour','milk','cream','bread','pork','pie']
Try = True
Try_a ='y'
while True:
  correct = random.choice(list_Original)
  
  l = len(correct)
  print(f'word count is {l}')
  if l == 3:
    three_words()
  elif l == 4:
    four_words()
  elif l == 5:
    five_words()
  elif l ==6:
    six_words()
  Try_a = input('Do you want to play again? (y or n)>> ')
  if Try_a == 'n':
    Try_a = 1
  if Try_a == 1:
    break


