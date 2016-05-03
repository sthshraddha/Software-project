# vaccinetracker.py 

## Introduction:
This is a Python based program that helps parents get a quick list of vaccinations needed for their children until 18 years of age. It also lists the milestones for children under 6 years of age. When the user runs this program, it will ask for child's date of birth and based on the user's input, it will calculate child's current age. It will then list the aforementioned information according to Center for Disease and Control (CDC) website. Additionally, it will also print a friendly note to parents reminding them to let their kids grow and develop at their own pace and a "Quote of the day".

## Usage:
_For Windows OS users:_**
There are few things to do prior to running this program. They are:
##### 1. Download Python version 3.5.1 or above for Windows OS.
##### 2. Download Anaconda <https://www.continuum.io/downloads> 
After downloading these two programs, the user can download vaccinetracker.py in a specified folder. To run the program, the user needs to go that folder and type the following command: *NOTE: Notice the format of date of birthdate of the child.*
For example:
```
[Anaconda3] C:\Users\Shraddha>cd Desktop

[Anaconda3] C:\Users\Shraddha\Desktop>python vaccinetracker.py -birthdate 2016,1,10
```

## Structure of the program:
The program has five separate functions. They are as following:
**Function 1:** _parser_
```
def parser():
    parser = argparse.ArgumentParser(description='takes date of birth of a child and lists the vaccinations required and major developmental milestones for that particular age range according to CDC website.')
    parser.add_argument(
            "-birthdate",
            required=True,
            type=str,
            help="""entering format: -birthdate 2014,2,20"""
            )
    args = parser.parse_args()
    return args
```
This function enables the user to enter his/her child's date of birth so that the input information can be passed on to the second function. 

**Function 2:** *calculating_current_age*
```
def calculating_current_age(birthdate):
    current_date = datetime.datetime.now()
    child_birthdate = birthdate
    age_in_days = abs(current_date - child_birthdate).days
    age_in_months = age_in_days/30
    return age_in_months
```
This function calls the user's input and calculates the current age of child in months.

**Function 3:** _quotes_
```
def quotes():
    quote = ["I may not be perfect, but when I look at my children I know that I got something in my life perfectly right.",
            "In the eyes of a child, you will see the world as it should be.",
            
            ...truncated
            
            ]
    print("\nQuote of the day: " + random.choice(quote))
```
This function shuffles the listed quotes and prints out a different quote when run at different times. The user can add as many quotes as he/she wants.

**Function 4:** *vaccines_and_milestones*
```
def vaccines_and_milestones(age, vaccinations):
    age = age
    no_vaccinations_applicable = True
    for vaccination in vaccinations:
        if vaccination['applicable'](age):
            print("\nRequired shots for your baby: " + vaccination['vaccination'])
            print("\nThese vaccines will protect your child from: pneumonia, measles, mumps, rubella, chickenpox, Hepatitis A and B viruses (inflammation of liver), polio, diphtheria, tetanus, whooping cough (pertusis), meningitis, genital warts, cervical cancer, diarrhea and vomitting.")
            print("\nDevelopmetal milestones according to CDC: " + vaccination['milestone'])
            print("\nPlease note that developmental milestones can vary from one child to the other. Let them grow at their own pace.")
            no_vaccinations_applicable = False
    if no_vaccinations_applicable:
        print("\nYAY! No shots until next visit! Weehooo!!!")
```
This function loops through the vaccine and milestone list according to the age of the child and then checks whether vaccination/s is/are required for current age or not. If no vaccine is required then the program will inform the user that no vaccine is required.

**Function 5:** *main*
```
def main():
    args = parser()
    birthdate = datetime.datetime.strptime(args.birthdate, '%Y,%m,%d')
    age = calculating_current_age(birthdate)
    print("\nCurrent age of the child is: ")
    print("%0.2f" %age + " " + "months" )
    vaccinations = [
        {'vaccination':'Hepatitis B, Dose 1 of 3',
        'milestone': 'Recognizes caregivers voice, communicates through body language (crying or fussing)',
        'applicable':(lambda age:age<1)},
        
        ...truncated
        
    vaccines_and_milestones(age, vaccinations)
    quotes()

if __name__ == '__main__':
    main()
```
This function ties up the above four functions and tells the program which function to run in what order. 

## Output example:
```
[Anaconda3] C:\Users\Shraddha\Desktop>python vaccinetracker.py -birthdate 2016,3,20

Current age of the child is:
1.47 months

Required shots for your baby: DTaP, Dose 1 of 5, Hib Dose 1 of 4, Polio(IPV), Dose 1 of 4, Pneumococcal conjugate, Dose 1 of 4, Rotavirus, Dose 1 of 3

These vaccines will protect your child from: pneumonia, measles, mumps, rubella, chickenpox, Hepatitis A and B viruses (inflammation of liver), polio, diphtheria, tetanus, whooping cough (pertusis), meningitis, genital warts, cervical cancer, diarrhea and vomitting.

Developmetal milestones according to CDC: starts to smile, raises head on tummy and calms down when rocked, cradled or snug to

Please note that developmental milestones can vary from one child to the other. Let them grow at their own pace.

Quote of the day: Your first breath took ours away.
```
