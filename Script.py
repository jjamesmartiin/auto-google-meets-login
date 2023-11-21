import schedule
import time
import webbrowser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import date
import keyboard
import pyautogui

today = date.today()
date = date.weekday(today)

def gov(date):
	driver = webdriver.Chrome(ChromeDriverManager().install())
	if date == 1:
		driver.get('https://meet.google.com/kcy-hufv-cjt')
		input("Press any key to terminate process.")

	elif date == 5:
		driver.get('https://meet.google.com/ivp-fvvu-mug')
		returnhome = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/span/span')))
		returnhome.click()
		#signup = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-content"]/section[1]/div/div[1]/div[2]/div/a/button')))
		time.sleep(.05)
		signup = driver.find_element_by_xpath('//*[@id="page-content"]/section[1]/div/div[1]/div[2]/div/a/button')
		signup.click()
		email = driver.find_element_by_xpath('//*[@id="identifierId"]')
		email.send_keys('fakeemail@gmail.com ')
		next1 = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
		next1.click()
		password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
		#password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
		password.send_keys('Jj176209')
		next2 = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
		next2.click()
		return2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/span/span')))
		return2.click()
		meetingcode = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]/div')))
		meetingcode.click()
		codebox = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input')
		codebox.send_keys('ivp-fvvu-mug')
		enter = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[4]/div[2]/div/span')
		enter.click()
		time.sleep(1)

		# Hitting esc to back out of a menu
		num = 3
		while num != 0:
			keyboard.press('esc')
			time.sleep(.05)
			keyboard.release('esc')
			num = num - 1
			time.sleep(2)
		joinnow = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]')
		joinnow.click()
		input("Press any key to terminate process.")
		

	else:
		print('It is not a class day today.')
		input("Press any key to terminate process.")


gov(date)
	

	



