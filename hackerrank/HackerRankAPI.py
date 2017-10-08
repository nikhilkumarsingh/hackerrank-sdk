from __future__ import print_function 
import requests
import json
from hackerrank.settings import RUN_API_ENDPOINT
from hackerrank.settings import LANG_CODE


class HackerRankAPI():
	# initialize the API object
	def __init__(self, api_key):     
		self.params_dict = {}
		self.params_dict['api_key'] = api_key
		self.params_dict['format'] = 'json'

	# run given piece of code
	def run(self, code):
		self.manage_params(code)
		response = self.__request(RUN_API_ENDPOINT, self.params_dict)
		result = Result(response.json()['result'])    # create a result object of Result class
		return result

	# update params_dict with code data
	def manage_params(self, code):
		self.params_dict['source'] = code['source']
		self.params_dict['lang'] = self.getLangCode(code['lang'])
		if 'testcases' in code:
			self.params_dict['testcases'] = json.dumps(code['testcases'])
		else:
			self.params_dict['testcases'] = json.dumps([""])        # empty testcase
   
	# send API request
	def __request(self,url,params):
		try:
			response = requests.post(url, data=params)
			return response  
		except Exception as e:
			 print(e)

	# utility function to get language code to be passed as parameter to API
	def getLangCode(self, lang):
		try:
			return LANG_CODE[lang]
		except KeyError:
			print("%s language not recognized.Use function supportedlanguages() to see the list of proper names of allowed languages."%lang)
			return -1

	# get list of all supported languages
	def supportedlanguages(self):
		return LANG_CODE.keys()



# to convert json to a class object of Result
class Result():
	def __init__(self,result):
		self.error = result['stderr']
		self.output = result['stdout']
		self.memory = result['memory']
		self.time = result['time']
		self.message = result['compilemessage']
