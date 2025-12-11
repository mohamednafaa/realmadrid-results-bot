import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
url = "https://native-stats.org/team/86"
driver.get(url)

wait = WebDriverWait(driver, 10)
time.sleep(3)

all_data = []

# Page 1
rows = driver.find_elements(By.XPATH, '(//table[@class="table table-xs"])[2]//tr')
for row in rows:
    data = [item.text for item in row.find_elements(By.XPATH, './/*[self::td or self::th]')]
    if data and '«' not in str(data):
        all_data.append(data)

# Page 2
try:
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@phx-value-page="next"]')))
    driver.execute_script("arguments[0].click();", next_button)
    time.sleep(2)
    
    rows = driver.find_elements(By.XPATH, '(//table[@class="table table-xs"])[2]//tr')
    for row in rows[1:]:
        data = [item.text for item in row.find_elements(By.XPATH, './/*[self::td or self::th]')]
        if data and '«' not in str(data):
            all_data.append(data)
except Exception as e:
    pass

driver.quit()

# Create and output the dataframe
df = pd.DataFrame(all_data[1:], columns=all_data[0])
print(df)