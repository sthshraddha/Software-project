# vaccinetracker.py 

## Introduction:
This is a Python based program that helps parents get a quick list of vaccinations needed for their children until 18 years of age. It also lists the milestones for children under 6 years of age. When the user runs this program, it will ask for child's date of birth and based on the user's input, it will calculate child's current age. It will then list the aforementioned information according to Center for Disease and Control (CDC) website. Additionally, it will also print a friendly note to parents reminding them to let their kids grow and develop at their own pace and a "Quote of the day".

## Structure of the program:
The program has five separate functions. They are as following:
**Function 1:** _parser_
```
def parser():
    parser = argparse.ArgumentParser(description='takes date of birth of a \
    child and lists the vaccinations required and major developmental \
    milestones for that particular age range according to CDC website.')
    parser.add_argument(
            "-birthdate",
            required=True,
            type=str,
            help="""entering format: --birthdate 2014,3,21"""
            )
    args = parser.parse_args()
    return args
```
This function enables the user to enter his/her child's date of birth so that the input information can be passed on to the second function.

**Function 2:" *calculating_current_age*
```
def calculating_current_age(birthdate):
    current_date = datetime.datetime.now()
    # print(date1)
    child_birthdate = birthdate
    age_in_days = abs(current_date - child_birthdate).days
    age_in_months = age_in_days/30
    return age_in_months
```
This function calls the user's input and calculates the current age of child in months.


