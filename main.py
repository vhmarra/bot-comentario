# pip install selenium

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

username_element = (By.CSS_SELECTOR, "input[name='username']")
password_element = (By.CSS_SELECTOR, "input[name='password']")
string_username = ''
string_password = ''
string_test = ''
submit = (By.CSS_SELECTOR, "button[type='submit']")
save_information = (By.XPATH, "//div[contains(text(), 'Agora não') or contains(text(), 'Not now')]")
not_now_notification = (By.XPATH, "//button[contains(text(), 'Agora não') or contains(text(), 'Not now')]")
comment_box = (By.XPATH,
               "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/div/textarea")
submit_comment = (By.XPATH,
                  "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/div/div[2]/div")

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'  # trocar path do executavel do firefox
driver = webdriver.Firefox(executable_path=r"C:\Users\vhmar\Desktop\projects\botzin\geckodriver.exe",
                           options=options)  # trocarpath downalod do drive do firefox aqui -> https://www.selenium.dev/selenium/docs/api/javascript/module/selenium-webdriver/firefox.html
comment = "#DESAFIOTOMAESSA"
timeout = 10
post = "https://www.instagram.com/reel/Cq37_neICwH/?igshid=YmMyMTA2M2Y%3D" #colocar a url do post da sua atletica aqui


def login(string_username, string_password) -> None:
    driver.get("https://www.instagram.com/")

    username_field = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(username_element))
    password_field = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(password_element))
    username_field.clear()
    password_field.clear()

    username_field.send_keys(string_username)
    password_field.send_keys(string_password)

    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(submit)).click()

    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located(save_information)).click()
    except:
        pass

    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(not_now_notification)).click()
    except:
        pass


def do_comment():
    driver.get(post)
    comment_field = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(comment_box))
    comment_field.clear()
    comment_field.send_keys(comment)
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(submit_comment)).click()


def orchestrate():
    do_comment()


if __name__ == '__main__':
    login("", "") #colocar username e password aqui
    while True:
        orchestrate()
        time.sleep(25)  # espera 25 sec para comentar de novo
