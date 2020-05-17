from datetime import datetime
import time
import random,os
import pygame

#secret_word_list = ["KOLTUK", "ARABA", "UÇAK", "TEPSİ", "SİHİRBAZ"]
secret_word_list = []
guess_list=[]
guessed=False
mistakes=0
def draw_hangman(mistakes):
   print("__________")
   print("|        |")
   if mistakes >= 1:
      print("|        @")
   else:
      print("|        ")
   if mistakes >= 2:
      print("|       /|\ ")
   else:
      print("|        ")
   if mistakes >= 3:
      print("|        |")
   else:
      print("|        ")
   if mistakes >= 4:
      print("|       / \\")
   else:
      print("|        ")
   print("")

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
    #print(guess)
    print("")
    print("")
    return guess


def print_guesses():
    print("yaptığınız tahminler: ")
    print(guess_list)

#program starts here...
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
end_time=datetime.now()
diff_time=end_time-start_time
print("\n gecen sure: ",diff_time.total_seconds())
if guessed==True:
    print("KAZANDINIZ.. TEBRİKLER..\n")
else:
    print("KAYBETTİNİZ.. TEKRAR DENEYİN..\n")
