#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unirest
import requests

def UrlShortener(link):
	dict_code = {
		"400":"Bad Requests",
		"401":"Unauthorized",
		"403":"Forbidden",
		"404":"Not Found",
		"500":"Internal Server Error",
		"503":"Service Unavailable"
		}

	code = requests.get(link).status_code
	if code != 200:
		code = str(code)
		if code in dict_code:
			print(" Error "+code+" : "+dict_code[code])
			exit()
	else:
		try:
			response = unirest.post("https://url-shortener-service.p.rapidapi.com/shorten",
			  headers={
			    "X-RapidAPI-Host": "url-shortener-service.p.rapidapi.com",
			    "X-RapidAPI-Key": "9ad14197e0mshb760b7991e634fcp11f307jsnbc7ca7452483",
			    "Content-Type": "application/x-www-form-urlencoded"
			  },
			  params={
			    "url": str(link)
			  }
			)
		except:
			return("Error")
			exit()
		else:
			return(response.body["result_url"])

link = raw_input("   Your link: ")
result = UrlShortener(link)
while result == "Error":
	result = UrlShortener(link)
	if "goolnk.com" in result:
		print(result)
		break