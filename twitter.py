#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys, getopt, time
from selenium import webdriver
from selenium.webdriver.common import keys

def main():
	try:
		  opts, args = getopt.getopt(sys.argv[1:],"u:p:t:")
	except getopt.GetoptError:
		  print 'Usage: twitter.py -u USERNAME -p "PASSWORD" -t "your tweet"'
		  sys.exit()
	if(len(args)!=0):
		print 'Usage: twitter.py -u USERNAME -p "PASSWORD" -t "your tweet"'
		sys.exit()
	for opt, arg in opts:
		if opt == '-u':
			muser = arg
		elif opt == '-p':
			mpass = arg
		elif opt == '-t':
			mtweet = arg
	
	driver = webdriver.Chrome()
	driver.get("https://twitter.com/")
	driver.maximize_window()
	form = driver.find_element_by_xpath("//*[@id='front-container']/div[2]/div[2]/form")
	username = form.find_element_by_class_name("email-input")
	password = form.find_element_by_class_name("flex-table-input")
	username.send_keys(muser)
	password.send_keys(mpass)
	driver.find_element_by_css_selector("button.submit.btn.primary-btn").click()
	tweet = driver.find_element_by_xpath('//*[@id="global-new-tweet-button"]')
	tweet.click()
	driver.execute_script('document.evaluate( \'//*[@id="tweet-box-global"]/div\' ,document, null, XPathResult.ANY_TYPE, null ).iterateNext().innerHTML = "'+mtweet+'";')
	tweetbtn = driver.find_element_by_xpath('//*[@id="global-tweet-dialog-dialog"]/div[2]/div[4]/form/div[2]/div[2]/button')
	tweetbtn.click()
	while 1:
		time.sleep(1)
		try:
			b = driver.find_element_by_tag_name("body")
		except:
			sys.exit()
	
if __name__ == "__main__":
   main()
