from splinter import Browser


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

