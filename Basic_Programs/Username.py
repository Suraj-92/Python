'''
Author: Suraj N Temkar.
Date: 05/04/2021
Title: User Input and Replace String Template “Hello <<UserName>>, How are you?”
'''

import re    # import Regular Expression Library
import Logger  # import Logger Module 
import logging      # import logging library

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

formater = logging.Formatter('%(levelname)s : %(message)s')

file_handler = logging.FileHandler('sample2.log')
file_handler.setFormatter(formater)

logger.addHandler(file_handler)

# Function
def validation(username):
    try:                                                           # Try Block
        if re.match("^[A-Z][a-z]{2,}$", username):                 # Regex Pattern
            logger.debug("Username is valid",username)
            b = "Hello <<username>> How are you?"               
            c = b.replace("<<username>>", username)                # Replace method
            logger.debug(c)
        else:
            raise Exception
    except Exception:
        logger.debug("Invalid input Please Enter The Proper Username ")
    finally:                                                        # Finally block
        logger.debug("......................")

#Main Method
if __name__ == '__main__':
    username1 = input("Enter the Username: ")  # User Input
    validation(username1)                      # Function Call