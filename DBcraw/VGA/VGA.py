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
driver.get('http://shop.danawa.com/main/?controller=goods&methods=index&productRegisterAreaGroupSeq=20&serviceSectionSeq=597#1')
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="limit"]/option[3]').click()
time.sleep(0.5)

for j in range(2,5):
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
		chipsetManufacturer = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(2) > td:nth-of-type(1)')
		chipset = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(2) > td:nth-of-type(2)')
		interfaceVGA = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(5) > td:nth-of-type(1)')
		memoryType = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(1)')
		memoryCapacity = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(3) > td:nth-of-type(1)')
		memoryBus = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(3) > td:nth-of-type(2)')
		HDMI = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(3) > tr:nth-of-type(2) > td:nth-of-type(2)')
		DisplayPort = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(3) > tr:nth-of-type(3) > td:nth-of-type(1)')
		add_multiVGA = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(4)) > tr:nth-of-type(2) > td:nth-of-type(1)')
		add_DualLink = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(4) > tr:nth-of-type(2) > td:nth-of-type(2)')
		add_4kResolution = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(4) > tr:nth-of-type(3) > td:nth-of-type(1)')
		add_VRReady = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(4) > tr:nth-of-type(3) > td:nth-of-type(2)')
		add_HDMOI2_0 = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(4) > tr:nth-of-type(4) > td:nth-of-type(1)')
		add_Dp1_4 = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(4) > tr:nth-of-type(4) > td:nth-of-type(2)')
		add_HDCP = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(4) > tr:nth-of-type(5) > td:nth-of-type(1)')
		add_DualBIOS = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(4) > tr:nth-of-type(5) > td:nth-of-type(2)')
		coreCoolingSystem = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(2) > td:nth-of-type(1)')
		VGASize_horizontal = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(3) > td:nth-of-type(1)')
		VGASize_vertical = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(3) > td:nth-of-type(2)')
		designPower = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(5) > tr:nth-of-type(2) > td:nth-of-type(1)')
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
			sameroute.append(name[0].text.strip() + ',' + madeIn[0].text.strip() + ',' + chipsetManufacturer[0].text.strip() + ',' + chipset[0].text.strip() + ',' + interfaceVGA[0].text.strip() + ',' + memoryType[0].text.strip() + ',' + memoryCapacity[0].text.strip() + ',' + memoryBus[0].text.strip() + ',' + HDMI[0].text.strip() + ',' + DisplayPort[0].text.strip() + ',' + add_multiVGA[0].text.strip() + ',' + add_DualLink[0].text.strip() + ',' + add_4kResolution[0].text.strip() + ',' + add_VRReady[0].text.strip() + ',' + add_HDMOI2_0[0].text.strip() + ',' + add_Dp1_4[0].text.strip() + ',' + add_HDCP[0].text.strip() + ',' + add_DualBIOS[0].text.strip() + ',' + coreCoolingSystem[0].text.strip() + ',' + VGASize_horizontal[0].text.strip() + ',' + VGASize_vertical[0].text.strip() + ',' + designPower[0].text.strip() + ',' + realPrice + ',' + imageUrl)
		except IndexError:
			driver.execute_script("window.history.go(-1)")
		else:
			for title in sameroute:
				route = title
				with open('/Users/skstk/DBcraw/VGA/VGA.csv', 'a+') as csvfile:
					writer = csv.writer(csvfile, delimiter=',')
					writer.writerow([route])
					changeSlash = name[0].text.strip()
					afterChange = ''
					for i in range(0,len(changeSlash)):
						if (changeSlash[i] == '/'):
							afterChange = afterChange + '_'
						else:
							afterChange = afterChange + changeSlash[i]
					f = open('./VGAImage/' + afterChange + '.jpg', "wb")
					f.write(imageLink.read())
					f.close()
					im = Image.open('./VGAImage/' + afterChange + '.jpg')
					size = (200, 200)
					im.thumbnail(size)
					im.save('./VGAImage/' + afterChange + '.jpg')
			driver.execute_script("window.history.go(-1)")

	for temp in range(1,81):
		driver.find_element_by_xpath('//*[@id="productListContainer"]/div/ul[2]/li[%d]/div/div[2]/div[1]/a/strong' % temp).click()
		time.sleep(0.5)
		sameroute = []
		html = driver.page_source
		soup = BeautifulSoup(html, 'html.parser')
		name = soup.select('div.prod_view_head > div > p > strong')
		madeIn = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(1) > td:nth-of-type(1)')
		chipsetManufacturer = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(2) > td:nth-of-type(1)')
		chipset = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(2) > td:nth-of-type(2)')
		interfaceVGA = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(5) > td:nth-of-type(1)')
		memoryType = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(1)')
		memoryCapacity = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(3) > td:nth-of-type(1)')
		memoryBus = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(3) > td:nth-of-type(2)')
		HDMI = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(3) > tr:nth-of-type(2) > td:nth-of-type(2)')
		DisplayPort = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(3) > tr:nth-of-type(3) > td:nth-of-type(1)')
		add_multiVGA = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(4)) > tr:nth-of-type(2) > td:nth-of-type(1)')
		add_DualLink = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(4) > tr:nth-of-type(2) > td:nth-of-type(2)')
		add_4kResolution = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(4) > tr:nth-of-type(3) > td:nth-of-type(1)')
		add_VRReady = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(4) > tr:nth-of-type(3) > td:nth-of-type(2)')
		add_HDMOI2_0 = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(4) > tr:nth-of-type(4) > td:nth-of-type(1)')
		add_Dp1_4 = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(4) > tr:nth-of-type(4) > td:nth-of-type(2)')
		add_HDCP = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(4) > tr:nth-of-type(5) > td:nth-of-type(1)')
		add_DualBIOS = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(4) > tr:nth-of-type(5) > td:nth-of-type(2)')
		coreCoolingSystem = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(2) > td:nth-of-type(1)')
		VGASize_horizontal = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(3) > td:nth-of-type(1)')
		VGASize_vertical = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(3) > td:nth-of-type(2)')
		designPower = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(5) > tr:nth-of-type(2) > td:nth-of-type(1)')
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
			sameroute.append(name[0].text.strip() + ',' + madeIn[0].text.strip() + ',' + chipsetManufacturer[0].text.strip() + ',' + chipset[0].text.strip() + ',' + interfaceVGA[0].text.strip() + ',' + memoryType[0].text.strip() + ',' + memoryCapacity[0].text.strip() + ',' + memoryBus[0].text.strip() + ',' + HDMI[0].text.strip() + ',' + DisplayPort[0].text.strip() + ',' + add_multiVGA[0].text.strip() + ',' + add_DualLink[0].text.strip() + ',' + add_4kResolution[0].text.strip() + ',' + add_VRReady[0].text.strip() + ',' + add_HDMOI2_0[0].text.strip() + ',' + add_Dp1_4[0].text.strip() + ',' + add_HDCP[0].text.strip() + ',' + add_DualBIOS[0].text.strip() + ',' + coreCoolingSystem[0].text.strip() + ',' + VGASize_horizontal[0].text.strip() + ',' + VGASize_vertical[0].text.strip() + ',' + designPower[0].text.strip() + ',' + realPrice + ',' + imageUrl)
		except IndexError:
			driver.execute_script("window.history.go(-1)")
		else:
			for title in sameroute:
				route = title
				with open('/Users/skstk/DBcraw/VGA/VGA.csv', 'a+') as csvfile:
					writer = csv.writer(csvfile, delimiter=',')
					writer.writerow([route])
					changeSlash = name[0].text.strip()
					afterChange = ''
					for i in range(0,len(changeSlash)):
						if (changeSlash[i] == '/'):
							afterChange = afterChange + '_'
						else:
							afterChange = afterChange + changeSlash[i]
					f = open('./VGAImage/' + afterChange + '.jpg', "wb")
					f.write(imageLink.read())
					f.close()
					im = Image.open('./VGAImage/' + afterChange + '.jpg')
					size = (200, 200)
					im.thumbnail(size)
					im.save('./VGAImage/' + afterChange + '.jpg')
			driver.execute_script("window.history.go(-1)")
	
	driver.find_element_by_xpath('//*[@id="productListPagingContainer"]/div/div/div/a[%d]' % j).click()
	time.sleep(2)