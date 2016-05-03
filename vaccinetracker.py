#!/usr/bin/env python

"""
This program will list vaccinations required and milestones for a child at \
their current age according to CDC website.

Below are the references used to complete this project:
Credit URL:
http://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
(floating value roundup)
Credit usernames: mgilson and Rex Logan
Date accessed: April 21, 2016

Credit URL:
http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
Credit username: arcseldon
Date accessed: April 21, 2016

Credit pdf files from Dr. Brant Faircloth's class:
Lecture 9 and Lecture 14

Credit URL:
http://stackoverflow.com/questions/4576115/python-list-to-dictionary
Credit username: kindall
Date accessed: April 23, 2016
Note: Ended up not using dictionary for the project

Credit URL:
http://aparrish.neocities.org/lists-loops.html
Date accessed: April 23, 2016

Credit URL:
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#blockquotes
Date accessed: May 2, 2016

Created by Shraddha Shrestha on April 22, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""

import argparse
import datetime
import random


def parser():
    parser = argparse.ArgumentParser(description='takes date of birth of a \
    child and lists the vaccinations required and major developmental \
    milestones for that particular age range according to CDC website.')
    parser.add_argument(
            "-birthdate",
            required=True,
            type=str,
            help="""entering format: -birthdate 2014,3,21"""
            )
    args = parser.parse_args()
    return args


def calculating_current_age(birthdate):
    current_date = datetime.datetime.now()
    # print(date1)
    child_birthdate = birthdate
    age_in_days = abs(current_date - child_birthdate).days
    age_in_months = age_in_days/30
    return age_in_months


def quotes():
    quote = ["I may not be perfect, but when I look at my children I know that \
I got something in my life perfectly right.",
"In the eyes of a child, you will see the world as it should be.",
"The best toys a child can have is a parent who gets down on the floor and \
plays with them.",
"Happiness is...laughing with a toddler about something entirely nonsensical.",
"Happiness is...getting a kiss and a hug from a child.",
"Hakuna matata!",
"The littlest feet make the biggest footprints in our hearts.",
"People who say they sleep like a baby usually don't have one.",
"A baby makes love stronger, the days shorter, the nights longer, savings \
smaller, and a home happier.",
"Your first breath took ours away.",
"Children are heaven sent: A gift of love from up above.",
"Best things in life really do come in small tiny, cute packages.",
"Happiness is...hearing your baby fart.",
"When my baby is sleeping that is when I think...Wow! I made that.",
"Whatever you are, a good one."
]
    print("\nQuote of the day: " + random.choice(quote))

def vaccines_and_milestones(age, vaccinations):
    age = age
    no_vaccinations_applicable = True
    for vaccination in vaccinations:
        if vaccination['applicable'](age):
            print("\nRequired shots for your baby: " + vaccination['vaccination'])
            print("\nThese vaccines will protect your child from: pneumonia, \
measles, mumps, rubella, chickenpox, Hepatitis A and B viruses (inflammation \
of liver), polio, diphtheria, tetanus, whooping cough (pertusis), meningitis, \
genital warts, cervical cancer, diarrhea and vomitting.")
            print("\nDevelopmetal milestones according to CDC: " + vaccination['milestone'])
            print("\nPlease note that developmental milestones can vary from \
one child to the other. Let them grow at their own pace.")
            no_vaccinations_applicable = False
    if no_vaccinations_applicable:
        print("\nYAY! No shots until next visit! Weehooo!!!")


def main():
    args = parser()
    birthdate = datetime.datetime.strptime(args.birthdate, '%Y,%m,%d')
    age = calculating_current_age(birthdate)
    print("\nCurrent age of the child is: ")
    print("%0.2f" %age + " " + "months" )
    vaccinations = [
        {'vaccination':'Hepatitis B, Dose 1 of 3',
        'milestone': 'Recognizes caregivers voice, communicates through body \
language (crying or fussing)',
        'applicable':(lambda age:age<1)},
        {'vaccination':'DTaP, Dose 1 of 5, Hib Dose 1 of 4, Polio(IPV), Dose 1 \
of 4, Pneumococcal conjugate, Dose 1 of 4, Rotavirus, Dose 1 of 3',
        'milestone': 'starts to smile, raises head on tummy and calms down when\
 rocked, cradled or snug to',
        'applicable':(lambda age:2>age>=1)},
        {'vaccination':'DTaP, Dose 2 of 5, Hib, Dose 2 of 4, Polio, Dose 2 of \
4, Pneumococcal conjugate, Dose 2 of 4, Rotavirus, Dose 2 of 3',
        'milestone': 'begins to smile at other people, coos, makes gurgling \
sounds, begins to follow things with eyes and can hold head up',
        'applicable':(lambda age:4>age>=2)},
        {'vaccination': 'DTaP, Dose 2 of 5, Hib, Dose 2 of 4, Polio (IPV), \
Dose 2 of 4, Pneumococcal conjugate (PCV13), Dose 2 of 4, Rotavirus, Dose 2 \
of 3',
        'milestone': 'babbles with expression, likes to play with people, \
reaches for toy with one hand and brings hands to mouth',
        'applicable': (lambda age:2<age<=4)},
        {'vaccination':'DTap, Dose 3 of 5, Hib, Dose 3 of 4, , Pneumococcal \
conjugate (PCV13), Dose 3 of 4, Rotavirus, Dose 3 of 3, IPV, Dose 3 of 4, \
Hepatitis B, Dose 3 of 3',
        'milestone': 'knows familiar faces, responds to own name, brings things\
to mouth and rolls over in both directions',
        'applicable': (lambda age:4<age<=6)},
        {'vaccination': 'Hib, Dose 4 of 4, Pneumococcal conjugate (PCV13), Dose\
4 of 4, IPV, Dose 4 of 4, MMR, Dose 1 of 2, Varicella Dose 1 of 2, Hepatitis A,\
Dose 1 of 2, Influenza, 1st dose or 2nd dose if needed',
        'milestone': 'cries when mom or dad leaves, says "mama and dada", \
copies gestures and may be able to stand alone',
        'applicable': (lambda age:6<age<=12)},
        {'vaccination': 'Flu, booster shot of meningococcal conjugate vaccine \
MenACWY, optional: meningococcal conjugate vaccine MenB',
        'milestone': 'NOT AVAILABLE',
        'applicable': (lambda age:216<=age>=192)}
]
    vaccines_and_milestones(age, vaccinations)
    quotes()
    # quote = quotes()
    # print(quote)


if __name__ == '__main__':
    main()
