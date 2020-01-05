#!/usr/bin/env python
# coding: utf-8

# # Twitter Sentiment Analysis
# ## Dean Thoms
# ### 11-14-2019


# Import necessary dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

# # Step 1 - Scraping
def get_browser():
	# Using Firefox instead of Chrome, Chrome on my PC has limitation set by IT
	executable_path = {'executable_path': 'geckodriver.exe'}
	return Browser('firefox', **executable_path, headless=False)
	
	# Change browser to chrome if you have it on your PC
    #executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    #return Browser('chrome', headless=False)

def scrape():
	account_list = [
		'realDonaldTrump',
		'BarackObama',
		'jimmykimmel',
		'Oprah',
		'atlnewsnow',
		'elonmusk',
		'iamcardib',
		'm_ryan02',
		'KimKardashian'
	]

	# Dictionary to store tweets
	dict = {}

	try:
		# Use splinter to establish browswer route
		browser = get_browser()
	
		# Loop through requested accounts urls and scrape each for most recent tweet
		for account in account_list:
	
			#for url in url_list:
			browser.visit(f"https://twitter.com/{account}")

			# Create BeautifulSoup object; parse with 'html.parser'
			soup = bs(browser.html, 'html.parser')
			time.sleep(1.5)
			
			tweet = soup.find('p',class_= 'js-tweet-text').get_text()
			dict[account] = tweet
		
	except:
		print("Error during scraping tweets")
	finally:
		browser.quit()	

	return dict






