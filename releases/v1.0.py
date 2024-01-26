from time import sleep
from random import randint
"""
This is a rock paper scissors game
Made by:Jaiwant Morampudi
Download at https://github.com/MathdallasAlt/rock-paper-scissors/
Enjoy!
"""
#Defining variables
menu=["Rock","Paper","Scissors"]
#Rock-paper-scissors introduction
print("Hello! Welcome to rock paper scissors!")
sleep(1)
print("You will play against this computer which is your 'opponent'!")
sleep(1)
askI=input("Would you like an introduction of this game? Reply 1 for yes and 0 for no:")

if askI=="1":
    print("Rock paper scisccors is a multi-player, non-teamwork game in which you and your opponents choose rock,paper or scissor.")
    sleep(1)
    print("If you choose rock and your opponent chooses scissors,you win.If it's the other way around, you lose.")
    sleep(1)
    print("If you choose paper and your opponent chooses rock,you win again.If it's the other way around, you lose.")
    sleep(1)
    print("If you choose scissors and your opponent chooses paper you again win.If it's the other way around, you lose.")
    sleep(1)
    print("If you and your opponent both choose the same thing, no one wins.")
    sleep(1)
    print("So,you should be familiar with all of rock papaer scisssors!")
    sleep(2)
#Start of the game
print("Now let's play!")

pc=menu[randint(0,2)]
plyr=input("Choose 0 for rock,1 for paper or 2 for scissors:")
if plyr=="0":
    if pc=="Rock":
        print("Ooh!The computer chose Rock! It means it's a tie!:o")
    if pc=="Paper":
        print("Aw!The computer chose Paper! It means you lost!:(")
    if pc=="Scissors":
        print("Yay!The computer chose Scissors! It means you won!:D")
if plyr=="1":
    if pc=="Rock":
        print("Yay!The computer chose Rock! It means you won!:D")
    if pc=="Paper":
        print("Ooh!The computer chose! It means it's a tie!:o")
    if pc=="Scissors":
        print("Aw!The computer chose! It means you lost!:(")
if plyr=="2":
    if pc=="Rock":
        print("Aw!The computer chose Rock! It means you lost!:(")
    if pc=="Paper":
        print("Yay!The computer chose Paper! It means you won!:D")
    if pc=="Scissors":
         print("Ooh!The computer chose Scissor! It means it's a tie!:o")
