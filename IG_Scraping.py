import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:

	def __init__(self, user, password):
		self.user = user
		self.password = password
		self.driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

	def closeDriver (self):
		self.driver.close()

	def login(self):
		self.driver.get("https://www.instagram.com/accounts/login/")
		time.sleep(2)
		username_ele = self.driver.find_element_by_xpath("//input[@name = 'username']")
		username_ele.clear()
		username_ele.send_keys(self.user)
		time.sleep(2)
		password_ele = self.driver.find_element_by_xpath("//input[@name = 'password']")
		password_ele.clear()
		password_ele.send_keys(self.password)
		time.sleep(2)

		# click login button 
		login_butt = self.driver.find_element_by_xpath("//button[@type = 'submit']")
		login_butt.click()
		time.sleep(2)

	def like_tag(self, hashtag):
		driver = self.driver
		driver.get("https://www.instagram.com/explore/tags/"+hashtag)
		time.sleep(2)
		# scroll Instagram website 3 pages to load contents
		for i in range(1,3):
			driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
		time.sleep(2)
		posts = driver.find_elements_by_tag_name("a")
		time.sleep(2)
		href_pics = []
		for ele in posts:
			href_pics.append(ele.get_attribute("href"))
		# print posts selected for the given hashtag
		print(hashtag + " : " + str(len(href_pics)))

		# for loop: like all photos 
		for link in href_pics:
			driver.get(link)
			driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
			try:
				driver.find_element_by_xpath("//button[@class ='dCJp8 afkep coreSpriteHeartOpen _0mzm-']").click()
				time.sleep(20)
			except Exception as e:
				time.sleep(2)



newBot = InstagramBot("alien199516","ljk123")
newBot.login()
newBot.like_tag("UBC")
newBot.closeDriver()


