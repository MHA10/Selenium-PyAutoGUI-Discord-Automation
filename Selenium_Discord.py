import time
from selenium import webdriver
import pyautogui
from selenium.webdriver.common.keys import Keys
import csv


def login(driver, email, password, url):
    try:
        # Opening the Discord web app page
        driver.get(url)
        driver.maximize_window()

        # Log in with credentials provided
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_class_name("sizeLarge-1vSeWK").click()

        # Time gap after login for DOM elements to load
        time.sleep(5)
    except:
        pass


# Send message to each member
def send_messages_individually(driver, name_tag, message):
    # Enter and type name tag in search bar
    driver.find_element_by_class_name("searchBar-6Kv8R2").click()
    driver.find_element_by_class_name("input-2VB9rf").send_keys(name_tag)
    time.sleep(2)
    # Click the searched member
    member_searched = driver.find_element_by_class_name("name-2NBmhj")
    member_searched.click()
    time.sleep(2)
    # Type and send the message
    driver.find_element_by_class_name("slateTextArea-1Mkdgw").send_keys(message)
    driver.find_element_by_class_name("slateTextArea-1Mkdgw").send_keys(Keys.ENTER)


# Send messages to the members
def send_messages(driver, members_dict, message):
    for name, tag in members_dict.items():
        try:
            name_tag = name + "#" + str(tag)
            send_messages_individually(driver, name_tag, message)
        except:
            # If a user is not found after search, need to hide the search box
            pyautogui.click(1200, 400)


def quitDriver(driver):
    driver.quit()


def printMembersDetails(members_dict):
    for id_key, name in members_dict.items():
        print(id_key + "---" + name)


def read_csv_members_file(file_name):
    with open(file_name, mode='r') as infile:
        reader = csv.reader(infile)
        # To ignore column names
        headings = next(reader)
        members_dict = {rows[0]: rows[1] for rows in reader}
        return members_dict


if __name__ == '__main__':
    executable_path = "/home/hamza/Downloads/chromedriver_linux64/chromedriver"

    # Getting the driver file from the path
    driver = webdriver.Chrome(executable_path=executable_path)

    # URL for the discord web app
    url = 'https://discord.com/channels/@me'
    email = "youremail@gmail.com"
    password = "yourpassword"
    file_name = "/home/hamza/Downloads/members-list-JobTests-675334770405933058.csv"
    message = "test message."

    members_dict = read_csv_members_file(file_name)
    login(driver, email, password, url)
    send_messages(driver, members_dict, message)

    quitDriver(driver)
