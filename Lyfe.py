import tweepy
from datetime import date

##Defines a function for printing out the menu and taking user input
def menu():
    print("For daily calorie goal, enter 1")
    print("")
    print("For daily quote, enter 2")
    print("")
    print("For the date, enter 3")
    print("")
    print("To quit, enter 0")
    print("")
    opt = int(input('Which option do you want?'))
    print("")
    return(opt)


#Collects user info and returns their basal metabolic rate
def user_info():
    age = int(input('What is your age: '))
    gender = input('What is your gender: ')
    weight = int(input('What is your weight: '))
    height = int(input('What is your height in inches: '))

    if gender == 'male':
        c1 = 66.47
        wm = 6.24 * weight
        hm = 12.7 * height
        am = 6.76 * age
    elif gender == 'female':
        c1 = 65.51
        wm = 4.35 * weight
        hm = 4.7 * height
        am = 4.7 * age

    #https://www.omnicalculator.com/health/bmr-harris-benedict-equation#:~:text=How%20do%20I%20calculate%20BMR,(4.7%20*%20age%20in%20years)
    bmr_result = c1 + hm + wm - am
    return(int(bmr_result))


#Calculates activity level in order to scale BMR
def calculate_activity(bmr_result): 
    activity_level = input('What is your activity level (none, light, moderate, heavy, or extreme): ')
    print("")

    if activity_level == 'none':
        activity_level = 1.2 * bmr_result
    elif activity_level == 'light':
        activity_level = 1.375 * bmr_result
    elif activity_level == 'moderate':
        activity_level = 1.55 * bmr_result
    elif activity_level == 'heavy':
        activity_level = 1.725 * bmr_result
    elif activity_level == 'extreme':
        activity_level = 1.9 * bmr_result

    return(int(activity_level))

#Uses calculated activity level with BMR to determine calories for desired effect
def gain_or_lose(activity_level):
    goals = input('Do you want to lose, maintain, or gain weight: ')

    if goals == 'lose':
        calories = activity_level - 500
    elif goals == 'maintain':
        calories = activity_level
    elif goals == 'gain':
        gain = int(input('Gain 1 or 2 pounds per week? Enter 1 or 2: '))
        if gain == 1: 
            calories = activity_level + 500
        elif gain == 2:
            calories = activity_level + 1000

    print('In order to', goals, 'weight, your daily caloric goals should be', int(calories), '!')
    print("")

#Utilizes Tweepy with Twitter API to GET most recent tweet from @quotepage and print it
def getDailyQuote():
    client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAIqOcgEAAAAACUGq2H0Yc8wD7%2F0HU1oOgXe9bDc%3DU0qrN7OUhZ48cn3wUlSelR9xwk7t1wyXvThz7Uoj6tBkWazvcl')

    #@quotepage id
    client_id = "23245396"

    tweets = client.get_users_tweets(id = client_id)
    print(tweets.data[0])
    print("")

#Utilizes datetime in order to print out the current date and weekday
def getDate():
    now = date.today()
    print('Date: ' + now.strftime('%m-%d-%y'))
    print('Day of Week: ' + now.strftime('%A'))
    print("")

option = -1

print("")
print("Welcome to LYFE!")
print("")

while option != 0:
    option = menu()
    if option == 1:
        gain_or_lose(calculate_activity(user_info()))
    elif option == 2:
        getDailyQuote()
    elif option == 3:
        getDate()
    elif option == 0:
        print("Quitting...")
    else:
        print("Please input valid option")