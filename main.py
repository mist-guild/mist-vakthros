import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


# create webdriver instance
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

# navigate to the URL
driver.get(
    "https://www.raidbots.com/simbot/quick?region=us&realm=malganis&name=seriallos")

# wait for the Convert to SimC input button to be visible
wait = WebDriverWait(driver, float('inf'))
convert_button = wait.until(EC.visibility_of_element_located(
    (By.ID, "ArmoryInput-convertToSimcInput")))

# click the Convert to SimC input button
convert_button.click()

# find the text area with the id "SimcUserInput-input"
textarea = wait.until(EC.visibility_of_element_located(
    (By.ID, "SimcUserInput-input")))

# wait 5 seconds
time.sleep(2)

# edit the text in the textarea such that the line that starts with 'talent=' is changed to 'epicgmaingmoment'
text = textarea.text
lines = text.split("\n")
new_lines = []
for line in lines:
    if line.startswith("talents="):
        new_lines.append(
            "talents=BYGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAgkICSChkkIJSBaJSSSolgI5AJ0SKRCRSDgA" + "\n")
    else:
        new_lines.append(line + "\n")
textarea.clear()
textarea.send_keys(new_lines)

time.sleep(5)

# click the run quick sim button
run_sim_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/section/div[2]/section/div[6]/div/div/button')
run_sim_button.click()

time.sleep(5)

# store the URL of the page that the button takes us to in a variable
target_url = driver.current_url
print(target_url)
