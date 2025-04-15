import os
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--remote-debugging-port=9222')

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=chrome_options)

def login():
    try:
        driver.get("https://thecircleads.com/login")
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys(os.getenv("USER_EMAIL"))
        driver.find_element(By.NAME, "password").send_keys(os.getenv("USER_PASSWORD"))
        driver.find_element(By.XPATH, "//button[contains(text(), 'Acceso')]").click()
        time.sleep(5)
        return True
    except Exception as e:
        print(f"Error en login: {e}")
        return False

def buscar_videos():
    try:
        driver.get("https://thecircleads.com")
        time.sleep(4)
        enlaces = driver.find_elements(By.XPATH, "//a[contains(@href, '/watch-video/')]")
        return list({e.get_attribute("href") for e in enlaces})
    except Exception as e:
        print(f"Error buscando videos: {e}")
        return []

def ver_video(url):
    try:
        driver.get(url)
        time.sleep(random.uniform(3, 6))
        driver.execute_script("window.scrollBy(0, window.innerHeight/2);")
        time.sleep(random.uniform(1, 2))
        driver.find_element(By.CSS_SELECTOR, "button[class*='play']").click()
        time.sleep(random.randint(65, 85))
    except Exception as e:
        print(f"Error en video {url}: {e}")

def iniciar():
    if login():
        while True:
            videos = buscar_videos()
            for video in videos:
                ver_video(video)
                time.sleep(random.randint(10, 25))

def detener():
    driver.quit()







