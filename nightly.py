#!/usr/bin/env python
import datetime
import os
from time import ctime
import csv
#import pandas as pd
from termcolor import colored
# possible colors: grey, red, green, yellow, blue, magenta, cyan, white


"""
add in did you do what you said you wanted to tomorrow
are you happier now than you thought you would be?
create seperate function that asks is this bedtime, or one activity you got done
ask what things at what time
add those things to calendar

ask about retainer!

habit checklist"""

File_object = "/Users/reed/Library/Mobile Documents/com~apple~CloudDocs/nightly.csv"


def get_input(question, color):
    answer = question + "||" + input(colored(question + "\n     ", color))
    print("")
    return answer

def questions(last_night_goals):
    return([
            get_input("What did you learn in RandoWiki?", "green"),
            get_input("How were you useful to others?", "magenta"),
            get_input("What are you missing?", "cyan"),
            get_input("Tell me 3 things from today you are greatful for", "green")
            ])

'''
PREVIOUS QUESTIONS
get_input("Document day in life goal for partnership, friendship, and wealth", "green")
get_input("Good or bad day? 0-1", "magenta"),
get_input("When and why did you not keep your word?", "magenta"),
get_input("Why are you pissed and will it matter when you die?", "red"),
get_input("What would you do if you couldn't fail?", "cyan"),
get_input("What would you accomplish if you couldn't fail?", "cyan"),
get_input("When and why did you not keep your word to yourself or others?", "magenta"),
get_input("Biggest failure today and what caused it", "magenta"),
get_input("Be a kid and write down a fucking dream (optional: risk and reward)", "cyan"),
get_input("Biggest failure today and what caused it", "purple"),
get_input("Why are you pissed and will it matter when you die?", "red"),
get_input("What is your purpose tomorrow?", "red"),
get_input("Be a kid and write down a fucking dream (optional: risk and reward)", "cyan"),
get_input("Affirm yourself or someone else", "green"),
get_input("How satisfied are you 1-3", "magenta"),
get_input("What are you grateful for?", "magenta"),
get_input("How did you act with courage or compassion today?", "green"),
get_input("What will you do tomorrow that actually matters?", "cyan"),
get_input("How were you compassionate today?", "green"),
get_input("How did you delay gratification today?", "blue"),
get_input("Reflect on your toggle track. Which actions aligned with your goals, and which didn't?", "green"),
get_input("How satisfied are you 1-10", "magenta"),
get_input("What did you do today that you're proud of?", "green"),
get_input("What are you happy about?", "red"),
get_input("What did you do today?", "green"),
get_input("What do you want to do tomorrow?", "cyan"),
get_input("What are you optimistic about?", "magenta"),
get_input("How could you have acted more in alignment with your goals today?", "red"),
get_input("How did you demonstrate learning from your past mistakes?", "blue"),
'''
            

def get_cell(infilepath, row, col):
    with open(infilepath) as infile:
        reader = csv.reader(infile, dialect ='excel')
       

def main():
    with open(File_object, 'a') as f:
        writer = csv.writer(f, dialect ='excel')
        os.system('clear')
        last_night =  get_cell(File_object, -1,-1)
        answers = questions(last_night)

        time = datetime.datetime.now()
        today = [time.minute, time.hour, time.day, time.month, time.year]
        readable = [ctime()]

        writer.writerow(readable + today + answers)

    print("\n\n\n", ctime())

if __name__ == "__main__":
    main()