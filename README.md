# Risa Discord Bot Template
Risa is a discord bot template that can be used readily to build a bot and deploy it.
Risa gives you a pretty good and ready to run template for the main discord bot program, which will save you time as you can directly jump into developing the unique features of your bot without having to code the main file yourself

The main file is ready to run and works with cogs, allowing you to add modules directly to it without modifing the main.py file responsible for running the bot

Risa comes with commands that allow you to hot load, unload and reload your extensions (discord cogs) to allow for speedy development. 
Just place your extensions' python file inside the "extensions" folder and you should be ready to go! (ofc given that there are no errors in your program)

Because of the work put into the template, you have no addition code to add to the main file for most use cases and only need to work on your bot specific cogs. Using Risa as the foundation for your bot will save a lot of development time and hassle.

Additionally the repository also has reference cogs for common discord commands like kick, ban, profile picture, ping, etc. which you can directly use or refer to incase it suits your bots' needs

# How to get started
» Clone the repository. (reference cogs are not necessary for this, they are optional)

» Have the required python libraries that are mentioned below

    discord.py
    python-decouple
    

» Make a file named ".env" (thats it, only ".env" nothing before or after it) and add your discord bot token in it as follows:

    token=[enter bot token here]
    
» Add your extensions (discord cogs) into "extensions" folder. (the extensions folder is in the same directory as main.py)

» Make sure there are no errors in the extensions that you have added.

» Run main.py in python version 3.6 or above, and your bot should be up and running.
