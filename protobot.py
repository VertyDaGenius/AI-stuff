#imports
import openai
from colorama import Fore
import os
import time
os.system('title: Protogen AI by vertydagenius!')
print('made by vertydagenius!')

while True:
    os.system(':newprotogen')
    
    print('Welcome to Protogen AI!')


    print('[1] red')
    print('[2] light black (grey)')
    print('[3] blue')
    print('[4] purple')
    color_choice = input('Choose a color: ')
    while color_choice not in ['1', '2', '3', '4']:
        color_choice = input('Enter 1, 2, 3, or 4: ')
    if color_choice == "1":
        color = Fore.RED
    elif color_choice == "2":
        color = Fore.LIGHTBLACK_EX
    elif color_choice == "3":
        color = Fore.BLUE
    elif color_choice == "4":
        color = Fore.MAGENTA
    break

while True:
    os.system(':choice')
    
    print(color + '''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠋⠀⠀⡀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⣼⡇⠀⣿⠀⠀⠀⠀⠀⠀⢀⣠⣴⠛⣷⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⢀⡼⣹⠁⠀⡟⠀⠀⣀⣤⠴⢾⠉⡟⠸⡇⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⢀⡞⢁⡟⠀⢠⡇⡖⢻⠁⢴⠀⢸⠀⡇⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⢀⡞⠀⡼⠁⠀⣼⢹⡆⢸⡀⢸⠀⢸⠀⣇⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⣼⢁⡼⠁⠀⣰⠻⡄⣇⠈⣇⠈⡇⢸⡄⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣰⣆⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⢉⣽⠞⠋⠉⠉⠙⠻⣽⡤⣿⠀⢷⣈⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⡏⠘⣦⡏⠀⠀⠀⠀⠀⠀⠀⣴⠏⠀⠀⠀⠀⢀⡴⠒⠻⡿⣿⣇⡼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⠇⠀⠘⠃⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⣴⠋⢀⡴⠚⢳⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⣼⠃⠀⠘⠧⠴⠟⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢠⡴⠞⠀⠰⣶⠖⠒⠋⠀⠀⢰⡇⣀⣀⣀⠀⡼⠁⠀⢀⣤⣶⣦⣄⠀⠀⠀⠙⢦⡀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠙⠦⣄⡀⢈⣹⢶⡟⠓⢲⡾⠋⠁⠀⠈⢻⠇⠀⢰⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠙⢦⡀⠀
    ⠀⠀⠀⠀⠀⣠⠴⢛⡽⠋⠁⣼⠀⢰⠏⠀⠀⠀⠀⠀⠈⢷⠀⢈⡻⠿⠿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠉⠳⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢀⡴⠞⠁⢶⡋⠀⠀⠀⠹⡄⢻⠀⠀⠀⠀⠀⠀⠀⢈⡇⠈⠿⢷⠀⠀⠀⠀⠁⠀⠀⠰⣦⣤⠀⣴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠐⠾⣏⡀⠀⠀⠀⠙⢦⡀⠀⠀⠙⢾⣧⡀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠘⣇⣀⡤⠖⢦⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢉⡷⠆⠀⠀⠀⠉⠓⠤⢤⣤⣬⠙⠳⠦⠴⠚⠉⠙⠒⠦⢤⣀⣀⠀⠀⠀⠈⠓⠶⠶⣤⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠰⣾⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢀⡤⠴⠒⠚⠛⠛⠃⠀⠀⣽⠉⠙⠓⠒⠒⠒⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠙⠳⢤⣀⣀⡀⠀⠀⠀⠀⠀⠘⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⠶⢺⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣴⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣾⣁⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠉⠉⣽⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣀⣈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠿⠞⠁⠘⠒⠦⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠦⢤⣀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠦⣄⡀⠀⠀⢻⡙⠓⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠦⣄⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⡙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')
    os.system(':choice')
    print('this is your protogen, what would you like to do?')
    print('[1] talk to it (AI)')
    print('[2] exit')
    choice = input('choose one: ')
    while choice not in ['1','2','3','4']:
        choice = input('enter 1, 2, 3, or 4: ')
    print(' ')
    print('apologies for the lack of choices, i ran out of ideas')
    if choice =="1":

        openai.api_key = 'replace with your openai api key'

        def generate_response(prompt, memory=""):
            system_message = "You are ProtoBot, a friendly and furry chatbot protogen. Your personality is a little bit shy and kind of dumb. You like making new friends. Your are enthusiastic and always ready to assist the user, don't break character, and talk as if you are a furry or kawaii.\n"
            prompt_with_memory = f"{system_message}{memory}{prompt}."

            response = openai.Completion.create(
                engine='text-davinci-003',
                
                prompt=prompt_with_memory + '.', #add a period to the end to avoid the bot generating an ending to the prompt
                max_tokens=100,
                n=1,
                stop=None,
                temperature=0.7
            )

            return response.choices[0].text.strip()

        def transform_response(response):
            # uwuify the response
            response = response.replace(".", " :3")
            response = response.replace("ai ", " me")
            response = response.replace("Sorry", "sowwyy")
            response = response.replace("sorry", "sowwyy")
            response = response.replace("bye", " bye :(")
            response = response.replace("Bye", " bye D;")
            response = response.replace("You", "u")
            response = response.replace("you", "u")
            response = response.replace("Your", "ur")
            response = response.replace("your", "ur")
            response = response.replace("You're", "ur")
            response = response.replace("you're", "ur")
            response = response.replace("love", "wuv")
            response = response.replace("Love", "wuv")
            response = response.replace("!", " :D")
            response = response.replace("hi ", "haii ")
            response = response.replace("Hi ", "haii ")
            response = response.replace("Hello", "hewoo")
            response = response.replace("hello", "hewwoo")
            response = response.replace("friend", "fwend")
            response = response.replace("Friend", "fwend")

            return response

        print('Before you use this, this has many bugs, sometimes it talks to itself and sometimes it finishes your responses or won\'t stop greeting you, or generates a completely random response.')
        print('Keep in mind this feature is still in beta and if you want to go back to the menu type in !return')
        print('also dont rely on this bot to do stuff like make food or write essays and i set the responses to be limited, you can edit the code and fix this yourself.')
        print(' ')
        memory = ""

        while True:
            user_input = input("Prompt: ")

            if user_input == "!return":
                break
                os.system('goto choice')


            response = generate_response(user_input, memory)
            transformed_response = transform_response(response)
            
            print(' ')
            print("ProtoBot: " + transformed_response)
            print(' ')

            
            memory = f"User: {user_input}\nProtoBot: {transformed_response}\n"

    if choice =="2":
        print('bye! come back soon :3')
        time.sleep(2)
        exit()


        

        







