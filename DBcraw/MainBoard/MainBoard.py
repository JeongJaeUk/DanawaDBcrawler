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
driver.get('http://shop.danawa.com/main/?controller=goods&methods=index&productRegisterAreaGroupSeq=20&serviceSectionSeq=595#1')
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="limit"]/option[3]').click()
time.sleep(0.5)

for j in range(2,7):
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
		CPUSocket = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(2) > td:nth-of-type(2)')
		detailSocket = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(4) > td:nth-of-type(1)')
		formFactor = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(5) > td:nth-of-type(1)')
		memoryType = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(1)')
		numOfMemorySlot = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(3) > td:nth-of-type(1)')
		memoryCapacity = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(4) > td:nth-of-type(1)')
		multiVGADetail = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(3) > tr:nth-of-type(2) > td:nth-of-type(2)')
		VGAConnection1 = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(3) > tr:nth-of-type(3) > td:nth-of-type(1)')
		VGAConnection2 = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(3)) > tr:nth-of-type(3) > td:nth-of-type(2)')
		MPoint2 = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(4) > tr:nth-of-type(9) > td:nth-of-type(1)')
		D_SUB = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(8) > tr:nth-of-type(2) > td:nth-of-type(1)')
		DVI = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(8) > tr:nth-of-type(2) > td:nth-of-type(2)')
		HDMI = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(8) > tr:nth-of-type(3) > td:nth-of-type(1)')
		DisplayPort = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(8) > tr:nth-of-type(3) > td:nth-of-type(2)')
		bT_thunderBolt = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(9) > tr:nth-of-type(2) > td:nth-of-type(1)')
		bT_e_SATA = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(9) > tr:nth-of-type(2) > td:nth-of-type(2)')
		bT_IEEE1394 = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(9) > tr:nth-of-type(3) > td:nth-of-type(1)')
		bT_serialPort = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(9) > tr:nth-of-type(3) > td:nth-of-type(2)')
		bT_parallelPort = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(9) > tr:nth-of-type(4) > td:nth-of-type(1)')
		bT_USB3_0 = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(9) > tr:nth-of-type(4) > td:nth-of-type(2)')
		bT_USB3_1 = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(9) > tr:nth-of-type(5) > td:nth-of-type(1)')
		bT_PS_2 = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(9) > tr:nth-of-type(5) > td:nth-of-type(2)')
		nS_gigaBitLan = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(13) > tr:nth-of-type(2) > td:nth-of-type(1)')
		nS_10GigaBitLan = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(13) > tr:nth-of-type(2) > td:nth-of-type(2)')
		nS_wirelessLan = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(13) > tr:nth-of-type(3) > td:nth-of-type(1)')
		nS_bluetooth = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(13) > tr:nth-of-type(3) > td:nth-of-type(2)')
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
			sameroute.append(name[0].text.strip() + ',' + madeIn[0].text.strip() + ',' + productCategory[0].text.strip() + ',' + CPUSocket[0].text.strip() + ',' + detailSocket[0].text.strip() + ',' + formFactor[0].text.strip() + ',' + memoryType[0].text.strip() + ',' + numOfMemorySlot[0].text.strip() + ',' + memoryCapacity[0].text.strip() + ',' + multiVGADetail[0].text.strip() + ',' + VGAConnection1[0].text.strip() + ',' + VGAConnection2[0].text.strip() + ',' + MPoint2[0].text.strip() + ',' + D_SUB[0].text.strip() + ',' + DVI[0].text.strip() + ',' + HDMI[0].text.strip() + ',' + DisplayPort[0].text.strip() + ',' + bT_thunderBolt[0].text.strip() + ',' + bT_e_SATA[0].text.strip() + ',' + bT_IEEE1394[0].text.strip() + ',' + bT_serialPort[0].text.strip() + ',' + bT_parallelPort[0].text.strip() + ',' + bT_USB3_0[0].text.strip() + ',' + bT_USB3_1[0].text.strip() + ',' + bT_PS_2[0].text.strip() + ',' + nS_gigaBitLan[0].text.strip() + ',' + nS_10GigaBitLan[0].text.strip() + ',' + nS_wirelessLan[0].text.strip() + ',' + nS_bluetooth[0].text.strip() + ',' + realPrice + ',' + imageUrl)
		except IndexError:
			driver.execute_script("window.history.go(-1)")
		else:
			for title in sameroute:
				route = title
				with open('/Users/skstk/DBcraw/MainBoard/MainBoard.csv', 'a+') as csvfile:
					writer = csv.writer(csvfile, delimiter=',')
					writer.writerow([route])
					changeSlash = name[0].text.strip()
					afterChange = ''
					for i in range(0,len(changeSlash)):
						if (changeSlash[i] == '/'):
							afterChange = afterChange + '_'
						else:
							afterChange = afterChange + changeSlash[i]
					f = open('./MainBoardImage/' + afterChange + '.jpg', "wb")
					f.write(imageLink.read())
					f.close()
					im = Image.open('./MainBoardImage/' + afterChange + '.jpg')
					size = (200, 200)
					im.thumbnail(size)
					im.save('./MainBoardImage/' + afterChange + '.jpg')
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
		CPUSocket = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(2) > td:nth-of-type(2)')
		detailSocket = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(4) > td:nth-of-type(1)')
		formFactor = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(5) > td:nth-of-type(1)')
		memoryType = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(1)')
		numOfMemorySlot = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(3) > td:nth-of-type(1)')
		memoryCapacity = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(4) > td:nth-of-type(1)')
		multiVGADetail = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(3) > tr:nth-of-type(2) > td:nth-of-type(2)')
		VGAConnection1 = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(3) > tr:nth-of-type(3) > td:nth-of-type(1)')
		VGAConnection2 = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(3)) > tr:nth-of-type(3) > td:nth-of-type(2)')
		MPoint2 = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(4) > tr:nth-of-type(9) > td:nth-of-type(1)')
		D_SUB = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(8) > tr:nth-of-type(2) > td:nth-of-type(1)')
		DVI = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(8) > tr:nth-of-type(2) > td:nth-of-type(2)')
		HDMI = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(8) > tr:nth-of-type(3) > td:nth-of-type(1)')
		DisplayPort = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(8) > tr:nth-of-type(3) > td:nth-of-type(2)')
		bT_thunderBolt = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(9) > tr:nth-of-type(2) > td:nth-of-type(1)')
		bT_e_SATA = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(9) > tr:nth-of-type(2) > td:nth-of-type(2)')
		bT_IEEE1394 = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(9) > tr:nth-of-type(3) > td:nth-of-type(1)')
		bT_serialPort = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(9) > tr:nth-of-type(3) > td:nth-of-type(2)')
		bT_parallelPort = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(9) > tr:nth-of-type(4) > td:nth-of-type(1)')
		bT_USB3_0 = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(9) > tr:nth-of-type(4) > td:nth-of-type(2)')
		bT_USB3_1 = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(9) > tr:nth-of-type(5) > td:nth-of-type(1)')
		bT_PS_2 = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(9) > tr:nth-of-type(5) > td:nth-of-type(2)')
		nS_gigaBitLan = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(13) > tr:nth-of-type(2) > td:nth-of-type(1)')
		nS_10GigaBitLan = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(13) > tr:nth-of-type(2) > td:nth-of-type(2)')
		nS_wirelessLan = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(13) > tr:nth-of-type(3) > td:nth-of-type(1)')
		nS_bluetooth = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(13) > tr:nth-of-type(3) > td:nth-of-type(2)')
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
			sameroute.append(name[0].text.strip() + ',' + madeIn[0].text.strip() + ',' + productCategory[0].text.strip() + ',' + CPUSocket[0].text.strip() + ',' + detailSocket[0].text.strip() + ',' + formFactor[0].text.strip() + ',' + memoryType[0].text.strip() + ',' + numOfMemorySlot[0].text.strip() + ',' + memoryCapacity[0].text.strip() + ',' + multiVGADetail[0].text.strip() + ',' + VGAConnection1[0].text.strip() + ',' + VGAConnection2[0].text.strip() + ',' + MPoint2[0].text.strip() + ',' + D_SUB[0].text.strip() + ',' + DVI[0].text.strip() + ',' + HDMI[0].text.strip() + ',' + DisplayPort[0].text.strip() + ',' + bT_thunderBolt[0].text.strip() + ',' + bT_e_SATA[0].text.strip() + ',' + bT_IEEE1394[0].text.strip() + ',' + bT_serialPort[0].text.strip() + ',' + bT_parallelPort[0].text.strip() + ',' + bT_USB3_0[0].text.strip() + ',' + bT_USB3_1[0].text.strip() + ',' + bT_PS_2[0].text.strip() + ',' + nS_gigaBitLan[0].text.strip() + ',' + nS_10GigaBitLan[0].text.strip() + ',' + nS_wirelessLan[0].text.strip() + ',' + nS_bluetooth[0].text.strip() + ',' + realPrice + ',' + imageUrl)
		except IndexError:
			driver.execute_script("window.history.go(-1)")
		else:
			for title in sameroute:
				route = title
				with open('/Users/skstk/DBcraw/MainBoard/MainBoard.csv', 'a+') as csvfile:
					writer = csv.writer(csvfile, delimiter=',')
					writer.writerow([route])
					changeSlash = name[0].text.strip()
					afterChange = ''
					for i in range(0,len(changeSlash)):
						if (changeSlash[i] == '/'):
							afterChange = afterChange + '_'
						else:
							afterChange = afterChange + changeSlash[i]
					f = open('./MainBoardImage/' + afterChange + '.jpg', "wb")
					f.write(imageLink.read())
					f.close()
					im = Image.open('./MainBoardImage/' + afterChange + '.jpg')
					size = (200, 200)
					im.thumbnail(size)
					im.save('./MainBoardImage/' + afterChange + '.jpg')
			driver.execute_script("window.history.go(-1)")
	
	driver.find_element_by_xpath('//*[@id="productListPagingContainer"]/div/div/div/a[%d]' % j).click()
	time.sleep(2)