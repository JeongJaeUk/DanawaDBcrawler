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
driver.get('http://shop.danawa.com/main/?controller=goods&methods=index&productRegisterAreaGroupSeq=20&serviceSectionSeq=600#1')
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="limit"]/option[3]').click()
time.sleep(0.5)

for j in range(2,15):
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
		caseSize = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(2) > td:nth-of-type(2)')
		supportPowerSpecification = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(3) > td:nth-of-type(2)')
		sBS_Extended_ATX = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(1)')
		sBS_Standard_ATX = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(2)')
		sBS_Micro_ATX = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(3) > td:nth-of-type(1)')
		sBS_Flex_ATX = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(3) > td:nth-of-type(2)')
		sBS_Standard_BTX = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(4) > td:nth-of-type(1)')
		sBS_Micro_BTX = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(4) > td:nth-of-type(2)')
		sBS_Standard_ITX = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(5) > td:nth-of-type(1)')
		sBS_Mini_ITX = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(5) > td:nth-of-type(2)')
		sddOnlyBay = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(3) > tr:nth-of-type(4) > td:nth-of-type(1)')
		VGASize = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(4) > td:nth-of-type(1)')
		CPUCoolerSize = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(4) > td:nth-of-type(2)')
		IntegralWaterCooler = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(5) > td:nth-of-type(1)')
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
			sameroute.append(name[0].text.strip() + ',' + madeIn[0].text.strip() + ',' + productCategory[0].text.strip() + ',' + caseSize[0].text.strip() + ',' + supportPowerSpecification[0].text.strip() + ',' + sBS_Extended_ATX[0].text.strip() + ',' + sBS_Standard_ATX[0].text.strip() + ',' + sBS_Micro_ATX[0].text.strip() + ',' + sBS_Flex_ATX[0].text.strip() + ',' + sBS_Standard_BTX[0].text.strip() + ',' + sBS_Micro_BTX[0].text.strip() + ',' + sBS_Standard_ITX[0].text.strip() + ',' + sBS_Mini_ITX[0].text.strip() + ',' + sddOnlyBay[0].text.strip() + ',' + VGASize[0].text.strip() + ',' + CPUCoolerSize[0].text.strip() + ',' + IntegralWaterCooler[0].text.strip() + ',' + realPrice + ',' + imageUrl)
		except IndexError:
			driver.execute_script("window.history.go(-1)")
		else:
			for title in sameroute:
				route = title
				with open('/Users/skstk/DBcraw/Case/Case.csv', 'a+') as csvfile:
					writer = csv.writer(csvfile, delimiter=',')
					writer.writerow([route])
					changeSlash = name[0].text.strip()
					afterChange = ''
					for i in range(0,len(changeSlash)):
						if (changeSlash[i] == '/'):
							afterChange = afterChange + '_'
						else:
							afterChange = afterChange + changeSlash[i]
					f = open('./CaseImage/' + afterChange + '.jpg', "wb")
					f.write(imageLink.read())
					f.close()
					im = Image.open('./CaseImage/' + afterChange + '.jpg')
					size = (200, 200)
					im.thumbnail(size)
					im.save('./CaseImage/' + afterChange + '.jpg')
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
		caseSize = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(2) > td:nth-of-type(2)')
		supportPowerSpecification = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody.main_info > tr:nth-of-type(3) > td:nth-of-type(2)')
		sBS_Extended_ATX = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(1)')
		sBS_Standard_ATX = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(2)')
		sBS_Micro_ATX = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(3) > td:nth-of-type(1)')
		sBS_Flex_ATX = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(3) > td:nth-of-type(2)')
		sBS_Standard_BTX = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(4) > td:nth-of-type(1)')
		sBS_Micro_BTX = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(4) > td:nth-of-type(2)')
		sBS_Standard_ITX = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(5) > td:nth-of-type(1)')
		sBS_Mini_ITX = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(2) > tr:nth-of-type(5) > td:nth-of-type(2)')
		sddOnlyBay = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(3) > tr:nth-of-type(4) > td:nth-of-type(1)')
		VGASize = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(4) > td:nth-of-type(1)')
		CPUCoolerSize = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(4) > td:nth-of-type(2)')
		IntegralWaterCooler = soup.select('div.prod_view_con > div.prod_specs_wrap > table > tbody:nth-of-type(6) > tr:nth-of-type(5) > td:nth-of-type(1)')
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
			sameroute.append(name[0].text.strip() + ',' + madeIn[0].text.strip() + ',' + productCategory[0].text.strip() + ',' + caseSize[0].text.strip() + ',' + supportPowerSpecification[0].text.strip() + ',' + sBS_Extended_ATX[0].text.strip() + ',' + sBS_Standard_ATX[0].text.strip() + ',' + sBS_Micro_ATX[0].text.strip() + ',' + sBS_Flex_ATX[0].text.strip() + ',' + sBS_Standard_BTX[0].text.strip() + ',' + sBS_Micro_BTX[0].text.strip() + ',' + sBS_Standard_ITX[0].text.strip() + ',' + sBS_Mini_ITX[0].text.strip() + ',' + sddOnlyBay[0].text.strip() + ',' + VGASize[0].text.strip() + ',' + CPUCoolerSize[0].text.strip() + ',' + IntegralWaterCooler[0].text.strip() + ',' + realPrice + ',' + imageUrl)
		except IndexError:
			driver.execute_script("window.history.go(-1)")
		else:
			for title in sameroute:
				route = title
				with open('/Users/skstk/DBcraw/Case/Case.csv', 'a+') as csvfile:
					writer = csv.writer(csvfile, delimiter=',')
					writer.writerow([route])
					changeSlash = name[0].text.strip()
					afterChange = ''
					for i in range(0,len(changeSlash)):
						if (changeSlash[i] == '/'):
							afterChange = afterChange + '_'
						else:
							afterChange = afterChange + changeSlash[i]
					f = open('./CaseImage/' + afterChange + '.jpg', "wb")
					f.write(imageLink.read())
					f.close()
					im = Image.open('./CaseImage/' + afterChange + '.jpg')
					size = (200, 200)
					im.thumbnail(size)
					im.save('./CaseImage/' + afterChange + '.jpg')
			driver.execute_script("window.history.go(-1)")
	
	driver.find_element_by_xpath('//*[@id="productListPagingContainer"]/div/div/div/a[%d]' % j).click()
	time.sleep(2)