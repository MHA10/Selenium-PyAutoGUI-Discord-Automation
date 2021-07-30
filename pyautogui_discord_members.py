# To run puautogui
# sudo pip3 install python3-xlib
# sudo apt-get install scrot
# sudo apt-get install python3-tk
# sudo apt-get install python3-dev
# sudo pip install pyautogui #[If sudo is not added, there will be an error]

import time
import pyautogui
import webbrowser


# Navigate to server/channel on discord app
def navigate_to_server(base_url, server_id, channel_id):
    webbrowser.open(base_url + '/channels/' + server_id + '/' + channel_id)
    time.sleep(10)


# Operates the discord members extension
def operate_discord_extension():
    extension_button_location = pyautogui.locateOnScreen('/home/hamza/Pictures/discord_extension_icon.png')
    pyautogui.click(extension_button_location)
    time.sleep(3)
    csv_button_location = pyautogui.locateOnScreen('/home/hamza/Pictures/csv_button.png')
    pyautogui.click(csv_button_location)

    time.sleep(2)

    csv_button_location = pyautogui.locateOnScreen('/home/hamza/Pictures/go.png')
    pyautogui.click(csv_button_location)


if __name__ == '__main__':
    # pre-requisites required
    base_url = "https://discord.com"
    server_id = "722272427354357771"
    channel_id = "722273070995210360"

    navigate_to_server(base_url, server_id, channel_id)
    operate_discord_extension()
