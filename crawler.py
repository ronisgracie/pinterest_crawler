from splinter import Browser
import re

class PinterestCrawler(object):


	def __init__(self, url):
		self.navigator = Browser()
		self.url = url
		#self.profile = 'urldoprofileaqui'


	def login_to_pinterest(self, login, password):
		#variables to the account
		email_input = login
		password_input = password
		#variables to access input
		emailLogin = self.navigator.find_by_css('body > div > div.appContent > div.mainContainer > div > div > div > form > ul > li.loginUsername > input')[0]
		emailPassword = self.navigator.find_by_css('body > div > div.appContent > div.mainContainer > div > div > div > form > ul > li.loginPassword > input')[0]
		loginButton = self.navigator.find_by_css('body > div > div.appContent > div.mainContainer > div > div > div > form > div.formFooter > div > button')[0]
		
		#inputting the info
		emailLogin.fill(email_input)
		emailPassword.fill(password_input)
		return loginButton.click()

	def clickfollow(self, url):
		self.navigator.visit(url)
		css_path = 'div.App.AppBase.Module.full > div.appContent > div.mainContainer > div.Module.UserProfilePage > div.Module.UserProfileContent > div > div > child(1) > div > button'
		for child in css_path:
			number = re.findall('[0-9+]', css_path)
			child = number.pop(0)
			new_child = int(child)
			while new_child <= 50:
				self.navigator.find_by_css(css_path)[0].click()
				new_child +=1
				css_path.replace(child, str(new_child))
			else: break


#body > div.App.AppBase.Module.full > div.appContent > div.mainContainer > div.Module.UserProfilePage > div.Module.UserProfileContent > div > div >
