import random

def six_words():
  word = collect
  length = len(word)
  word_l = list(word)
  secrets = []
  for _ in range(length):
    secrets.append('_')
  list_a =[]
  list_b =[]
  count = 0
  while True:
    if secrets == word_l:
      break
    count +=1
    print(''.join(secrets))
    answer = input(f'Round{count}: Please put word >> ')
    list_a.append(answer)
    if len(answer) <2:
      num =0
      if answer in word_l:
        for i in word_l:
          if answer == i:
            secrets[num] = word_l[num]
          num += 1
      else:
        print('it is not in the word.')
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
  collect = random.choice(list_Original)
  print(collect)
  l = len(collect)
  print(f'word count is {l}')
  six_words()
  Try_a = input('Do you want to play again? (y or n)>> ')
  if Try_a == 'n':
    Try_a = 1
  if Try_a == 1:
    break


