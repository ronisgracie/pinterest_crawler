from crawler import PinterestCrawler

start = PinterestCrawler('http://www.pinterest.com/login/')

access_website = start.navigator.visit(start.url)

get_login = start.login_to_pinterest('', '')

start.clickfollow('https://www.pinterest.com/ntmcats/followers/')