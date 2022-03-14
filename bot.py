from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests


driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(20)

def bot():
    try:
        ball = driver.find_element_by_class_name('aumms1qt')
        ball = driver.find_elements_by_class_name('aumms1qt')
        click_ball = ball[-1]
        action_ball = webdriver.common.action_chains.ActionChains(driver)
        action_ball.move_to_element_with_offset(click_ball, 0, -20) # movimenta o click certo na bolinha
        # clique duplo
        action_ball.click()
        action_ball.perform()
        action_ball.click()
        action_ball.perform()

        # número do cliente
        client_number = driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span')
        final_number = client_number.text
        print(final_number)

        # última msg
        all_msg = driver.find_elements_by_class_name('_1Gy50')
        all_msg_text = [e.text for e in all_msg]
        msg = all_msg_text[-1]
        print(msg)

        # resp msg
        text_field = driver.find_element_by_xpath(('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'))
        text_field.click()
        answer = requests.get("http://localhost/bot/", params={'msg': {msg}, 'number': {final_number},})
        bot_answer = answer.text
        time.sleep(3)
        text_field.send_keys(bot_answer, Keys.ENTER)

        # volta ao padrão
        default_contact = driver.find_element_by_class_name('_2XH9R')
        action_contact = webdriver.common.action_chains.ActionChains(driver)
        action_contact.move_to_element_with_offset(default_contact, 0, -20) # movimenta o click certo
        # clique duplo
        action_contact.click()
        action_contact.perform()
        action_contact.click()
        action_contact.perform()

    except:
        print('Search new messages')
        time.sleep(3)

while True:
    bot()