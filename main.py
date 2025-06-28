from utilities.screenshot import shoot
from utilities.prompter import prompt

from dotenv import load_dotenv
from logging import log, INFO

if __name__ == '__main__':
    load_dotenv()
    
    ss = shoot()
    log(INFO, f"Screenshot saved @: {ss}")
    log(INFO, "Starting prompt for captured screenshot!")
    
    response = prompt(ss)
    print(response)
