#!/usr/bin/python
# unicode: utf-8

import time
import random
from splinter import Browser


class PinterestCrawler(object):

    def __init__(self, url):
        self.navigator = Browser()
        self.url = url

    def login_to_pinterest(self, login, password):
        email_input = login
        password_input = password
        emaillogin = self.navigator.find_by_css(
            'body > div > div.appContent > div.mainContainer > div > div > div > form > ul > li.loginUsername > input')[0]
        emailpassword = self.navigator.find_by_css('body > div > div.appContent > div.mainContainer > div > div > div > form > ul > li.loginPassword > input')[0]
        loginbutton = self.navigator.find_by_css('body > div > div.appContent > div.mainContainer > div > div > div > form > div.formFooter > div > button')[0]

        emaillogin.fill(email_input)
        emailpassword.fill(password_input)
        time.sleep(random.randint(2, 6))
        return loginbutton.click()

    def clickfollow(self, url):
        self.navigator.visit(url)
        time.sleep(6)
        self.navigator.execute_script(
            'window.scrollTo(50,document.body.scrollHeight);')

        css_path = 'body > div.App.AppBase.Module.full > div.appContent > div.mainContainer > div.Module.UserProfilePage > div.Module.UserProfileContent > div > div > div:nth-child({0}) > div > button'
        new_child = 1
        while new_child <= 50:
            css_path2 = css_path.format(new_child)
            time.sleep(2)
            self.navigator.find_by_css(css_path2)[0].click()
            new_child += 1
            time.sleep(random.randint(3, 12))

    def main(self):
        self.navigator.visit(self.url)
        self.login_to_pinterest('graciewestwood@gmail.com', 'blackhouse123')

        self.clickfollow('https://www.pinterest.com/PaleoLivingMag/followers/')

start = PinterestCrawler('http://www.pinterest.com/login/')

if __name__ == '__main__':
    print 'ok'
    start.main()
else:
    print dir(start.navigator)
    start.navigator.quit()
