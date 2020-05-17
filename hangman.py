from datetime import datetime
import time
import random,os
#this library provides us with the terminal colors. to see supported colors use: print(termcolor.COLORS)
from termcolor import colored

#seret words will be loaded from wordList.txt file to this list
secret_word_list = []
#this is the list of letters entered by user
guess_list=[]
guessed=False
#the mistakes counter.. if it is 4 than all tries have been done
mistakes=0

#write BIG  Hangman text to the terminal screen for 2 seconds..
def intro():
   os.system('clear')
   print("| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
   print("| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
   print("|  _  | (_| | | | | (_| | | | | | | (_| | | | |")
   print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
   print("                   |___/                        ")
   time.sleep(2)

#according to number of mistakes this function draws the hangman
def draw_hangman(mistakes):
   print(colored("__________",'yellow'))
   print(colored("|        |",'yellow'))
   if mistakes >= 1:
      print(colored("|        @",'yellow'))
   else:
      print(colored("|        ",'yellow'))
   if mistakes >= 2:
      print(colored("|       /|\ ",'yellow'))
   else:
      print(colored("|        ",'yellow'))
   if mistakes >= 3:
      print(colored("|        |",'yellow'))
   else:
      print(colored("|        ",'yellow'))
   if mistakes >= 4:
      print(colored("|       / \\",'yellow'))
   else:
      print(colored("|        ",'yellow'))
   print("")

#this function prints secret word. it prints it bu dashes _ and guessed letters
def print_secret_word():
    guess=True
    print("KELIME: ",end='')
    for abc in secret_word:
        try:
            index_no = guess_list.index(abc)
        except ValueError:
            index_no = -1
        if  index_no>=0:
            print(abc,end='')
        else:
            print("-",end='')
            guess=False
        print(' ',end='')
    print("")
    print("")
    return guess

#this function prints guessed letters..
def print_guesses():
    print("yaptığınız tahminler: ")
    print(colored(guess_list,'green'))

#program starts here...
intro()
# we also measure how quickly user guessed or lost the game..
start_time=datetime.now()

f=open('wordList.txt')
secret_word_list=f.read().splitlines()
secret_word = random.choice(secret_word_list)
secret_word_len = len(secret_word)
#not guessed and not (mistakes >= 4):

while True:
   os.system('clear')
   harf="!"
   draw_hangman(mistakes)
   guessed=print_secret_word()
   print_guesses()
   if guessed == True:
       break

   if mistakes>=4:
       break

   print("harf giriniz: ",end='')
   harf = input()
   if secret_word.count(harf)==0:
      mistakes +=1
   guess_list.append(harf.upper())
   #print("guess:",str(guessed),"mistakes:",str(mistakes))

#this is the end time for game duration
end_time=datetime.now()
diff_time=end_time-start_time
print("\n gecen sure: ",diff_time.total_seconds())

if guessed==True:
    print("KAZANDINIZ.. TEBRİKLER..\n")
else:
    print("KAYBETTİNİZ.. TEKRAR DENEYİN..\n")
