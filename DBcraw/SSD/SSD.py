#-*- coding: utf-8 -*-

import urllib2
from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import codecs
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.Chrome('/Users/skstk/DBcraw/chromedriver')
driver.implicitly_wait(1)
driver.get('http://shop.danawa.com/main/?controller=goods&methods=index&productRegisterAreaGroupSeq=20&serviceSectionSeq=604#1')
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="limit"]/option[3]').click()
time.sleep(0.5)

for j in range(2,6):
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')
	
	for temp in range(1,11):
		driver.find_element_by_xpath('//*[@id="productListContainer"]/div/ul[1]/li[%d]/div/div[2]/div[1]/a/strong' % temp).click()
		time.sleep(0.5)
		sameroute = []
		html = driver.page_source
		soup = BeautifulSoup(html, 'html.parser')
		name = soup.select('div.prod_view_head > div > p > strong')
		madeIn = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(1) > td:nth-of-type(1)')
		productCategory = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(2) > td:nth-of-type(1)')
		diskType = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(2) > td:nth-of-type(2)')
		interfaceSSD = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(3) > td:nth-of-type(1)')
		diskCapacity = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(4) > td:nth-of-type(1)')
		memoryType = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(1)')
		nandStructure = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(2)')
		nmProcess = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(3) > td:nth-of-type(1)')
		controller = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(3) > td:nth-of-type(2)')
		writeSpeed = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(3)) > tr:nth-of-type(2) > td:nth-of-type(2)')
		tempWriteSpeed = writeSpeed[0].text.strip()
		realWriteSpeed = ''
		for i in range(0,len(tempWriteSpeed)):
			if (tempWriteSpeed[i] != ','):
				realWriteSpeed = realWriteSpeed + tempWriteSpeed[i]
		readSpeed = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(3) > tr:nth-of-type(2) > td:nth-of-type(1)')
		tempReadSpeed = readSpeed[0].text.strip()
		realReadSpeed = ''
		for i in range(0,len(tempReadSpeed)):
			if (tempReadSpeed[i] != ','):
				realReadSpeed = realReadSpeed + tempReadSpeed[i]
		add_UASP = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(2) > td:nth-of-type(1)')
		add_AES = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(2) > td:nth-of-type(2)')
		add_WiFi = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(3) > td:nth-of-type(1)')
		add_USB = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(3) > td:nth-of-type(2)')
		add_3_5Bracket = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(4) > td:nth-of-type(1)')
		add_forMacBookUpgrade = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(4) > td:nth-of-type(2)')
		add_ONFI = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(5) > td:nth-of-type(1)')
		price = soup.select('div.prod_view_top > div.prod_view_info > div.prod_info_list.list_line > div:nth-of-type(2) > strong > span')
		tempPrice = price[0].text.strip()
		realPrice = ''
		for i in range(0,len(tempPrice)):
			if (tempPrice[i] != ','):
				realPrice = realPrice + tempPrice[i]
		imageUrltemp = soup.select('div.prod_view_top > div.prod_view_thumb > div > img')
		imageUrl = 'http:' + imageUrltemp[0].get('src')
		hdr = {'User-Agent': 'Mozilla/5.0', 'referer':'http://m.naver.com'}
		req = urllib2.Request(imageUrl, headers=hdr)
		imageLink = urllib2.urlopen(req)
		try:
			sameroute.append(name[0].text.strip() + ',' + madeIn[0].text.strip() + ',' + productCategory[0].text.strip() + ',' + diskType[0].text.strip() + ',' + interfaceSSD[0].text.strip() + ',' + diskCapacity[0].text.strip() + ',' + memoryType[0].text.strip() + ',' + nandStructure[0].text.strip() + ',' + nmProcess[0].text.strip() + ',' + controller[0].text.strip() + ',' + realWriteSpeed + ',' + realReadSpeed + ',' + add_UASP[0].text.strip() + ',' + add_AES[0].text.strip() + ',' + add_WiFi[0].text.strip() + ',' + add_USB[0].text.strip() + ',' + add_3_5Bracket[0].text.strip() + ',' + add_forMacBookUpgrade[0].text.strip() + ',' + add_ONFI[0].text.strip() + ',' + realPrice + ',' + imageUrl)
		except IndexError:
			driver.execute_script("window.history.go(-1)")
		else:
			for title in sameroute:
				route = title
				with open('/Users/skstk/DBcraw/SSD/SSD.csv', 'a+') as csvfile:
					writer = csv.writer(csvfile, delimiter=',')
					writer.writerow([route])
					changeSlash = name[0].text.strip()
					afterChange = ''
					for i in range(0,len(changeSlash)):
						if (changeSlash[i] == '/'):
							afterChange = afterChange + '_'
						else:
							afterChange = afterChange + changeSlash[i]
					f = open('./SSDImage/' + afterChange + '.jpg', "wb")
					f.write(imageLink.read())
					f.close()
					im = Image.open('./SSDImage/' + afterChange + '.jpg')
					size = (200, 200)
					im.thumbnail(size)
					im.save('./SSDImage/' + afterChange + '.jpg')
			driver.execute_script("window.history.go(-1)")

	for temp in range(1,81):
		driver.find_element_by_xpath('//*[@id="productListContainer"]/div/ul[2]/li[%d]/div/div[2]/div[1]/a/strong' % temp).click()
		time.sleep(0.5)
		sameroute = []
		html = driver.page_source
		soup = BeautifulSoup(html, 'html.parser')
		name = soup.select('div.prod_view_head > div > p > strong')
		madeIn = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(1) > td:nth-of-type(1)')
		productCategory = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(2) > td:nth-of-type(1)')
		diskType = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(2) > td:nth-of-type(2)')
		interfaceSSD = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(3) > td:nth-of-type(1)')
		diskCapacity = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(4) > td:nth-of-type(1)')
		memoryType = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(1)')
		nandStructure = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(2)')
		nmProcess = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(3) > td:nth-of-type(1)')
		controller = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(3) > td:nth-of-type(2)')
		writeSpeed = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(3)) > tr:nth-of-type(2) > td:nth-of-type(2)')
		tempWriteSpeed = writeSpeed[0].text.strip()
		realWriteSpeed = ''
		for i in range(0,len(tempWriteSpeed)):
			if (tempWriteSpeed[i] != ','):
				realWriteSpeed = realWriteSpeed + tempWriteSpeed[i]
		readSpeed = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(3) > tr:nth-of-type(2) > td:nth-of-type(1)')
		tempReadSpeed = readSpeed[0].text.strip()
		realReadSpeed = ''
		for i in range(0,len(tempReadSpeed)):
			if (tempReadSpeed[i] != ','):
				realReadSpeed = realReadSpeed + tempReadSpeed[i]
		add_UASP = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(2) > td:nth-of-type(1)')
		add_AES = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(2) > td:nth-of-type(2)')
		add_WiFi = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(3) > td:nth-of-type(1)')
		add_USB = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(3) > td:nth-of-type(2)')
		add_3_5Bracket = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(4) > td:nth-of-type(1)')
		add_forMacBookUpgrade = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(4) > td:nth-of-type(2)')
		add_ONFI = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(5) > td:nth-of-type(1)')
		price = soup.select('div.prod_view_top > div.prod_view_info > div.prod_info_list.list_line > div:nth-of-type(2) > strong > span')
		tempPrice = price[0].text.strip()
		realPrice = ''
		for i in range(0,len(tempPrice)):
			if (tempPrice[i] != ','):
				realPrice = realPrice + tempPrice[i]
		imageUrltemp = soup.select('div.prod_view_top > div.prod_view_thumb > div > img')
		imageUrl = 'http:' + imageUrltemp[0].get('src')
		hdr = {'User-Agent': 'Mozilla/5.0', 'referer':'http://m.naver.com'}
		req = urllib2.Request(imageUrl, headers=hdr)
		imageLink = urllib2.urlopen(req)
		try:
			sameroute.append(name[0].text.strip() + ',' + madeIn[0].text.strip() + ',' + productCategory[0].text.strip() + ',' + diskType[0].text.strip() + ',' + interfaceSSD[0].text.strip() + ',' + diskCapacity[0].text.strip() + ',' + memoryType[0].text.strip() + ',' + nandStructure[0].text.strip() + ',' + nmProcess[0].text.strip() + ',' + controller[0].text.strip() + ',' + realWriteSpeed + ',' + realReadSpeed + ',' + add_UASP[0].text.strip() + ',' + add_AES[0].text.strip() + ',' + add_WiFi[0].text.strip() + ',' + add_USB[0].text.strip() + ',' + add_3_5Bracket[0].text.strip() + ',' + add_forMacBookUpgrade[0].text.strip() + ',' + add_ONFI[0].text.strip() + ',' + realPrice + ',' + imageUrl)
		except IndexError:
			driver.execute_script("window.history.go(-1)")
		else:
			for title in sameroute:
				route = title
				with open('/Users/skstk/DBcraw/SSD/SSD.csv', 'a+') as csvfile:
					writer = csv.writer(csvfile, delimiter=',')
					writer.writerow([route])
					changeSlash = name[0].text.strip()
					afterChange = ''
					for i in range(0,len(changeSlash)):
						if (changeSlash[i] == '/'):
							afterChange = afterChange + '_'
						else:
							afterChange = afterChange + changeSlash[i]
					f = open('./SSDImage/' + afterChange + '.jpg', "wb")
					f.write(imageLink.read())
					f.close()
					im = Image.open('./SSDImage/' + afterChange + '.jpg')
					size = (200, 200)
					im.thumbnail(size)
					im.save('./SSDImage/' + afterChange + '.jpg')
			driver.execute_script("window.history.go(-1)")
	
	driver.find_element_by_xpath('//*[@id="productListPagingContainer"]/div/div/div/a[%d]' % j).click()
	time.sleep(2)