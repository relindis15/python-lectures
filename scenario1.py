# Deployment Script with Environment Selection:

# The idea is to for you to develop a Python script that allows users to select the #deployment environment(e.g., development, staging, or production) and performs different #actions based on their choice.

# Use conditionals to check the selected environment and execute specific deployment tasks accordingly.

# This exercise will allow you to practice conditionals, function calls that we studied in the last lecture and code organization to automate the deployment process based on user inputs.

# propose a function to deploy to development environment

def deploy_to_development():
    print("deploying to development environment")

# propose a function to deploy to staging environment


def deploy_to_staging():
    print("deploying to staging environment")

# Propose a function to deploy to production environment


def deploy_to_production():
    print("deploy to production environment")


def deploy(environment):
    if environment == "development":
        deploy_to_development()

    elif environment == "staging":
        deploy_to_staging()

    elif environment == "production":
        deploy_to_production()
    else:
        print("Its an invalid environment. Please choose either staging, production or development")


# Prompt the user for the deployment environment
user_environment = input(
    'enter the deployment environment(development, staging, production)')

# Call the function with user's choice
deploy(user_environment)


# Problem2
# Write a Python script that prompts the user to enter a password and then checks the strength of the password based on predefined criteria.
# The script should provide feedback on the strength of the password using a combination of conditions and loops.

user_password = input("prompt user to enter password : ")
count = 10
while (count <= 5):
    print("weak password strength :")
else:
    print("strong password strength :")


# Problem2
# Write a Python script that prompts the user to enter a password and then checks the strength of the password based on predefined criteria.
# The script should provide feedback on the strength of the password using a combination of conditions and loops.

def password_strength(n):
    if password_strength == 0:
        print("weak password strength :")
    elif password_strength == 4:
        print("Average password strength :")
    elif password_strength == 6:
        print("Good password strength :")
    else:
        print("Strong password strength :")


user_password = input("Enter a password : ")
