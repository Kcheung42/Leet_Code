# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Convert_String_Json.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/14 16:37:27 by kcheung           #+#    #+#              #
#    Updated: 2018/02/10 14:32:07 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
Convert a string to Json
Convert a Json to string
'''

class Converter:
	def jsonArray(self, s, index):
		array = []
		while s[index] != ']':
			index += 1
			json , index = self.strToJsonHelper(s, index)
			array.append(json)
		index += 1
		return (array, index)

	def strToJsonHelper(self, s, index):
		if s[index] != '{':
			return
		d = {}
		delim = set([',', ']', '}'])
		key = ''
		while s[index] != '}':
			key = ''
			val = ''
			index += 1
			while(s[index] != ':' and s[index] not in delim):
				key += s[index]
				index +=1
			index += 1
            # start of a new json map
			if s[index] == '{':
				val, index = self.strToJsonHelper(s, index)
            # start of a new json array
			elif s[index] == '[':
				val, index = self.jsonArray(s, index)
            # get regular value
			else:
				while(s[index] not in delim):
					val += s[index]
					index += 1
			# print('key is:%s ,val is: %s' % (key, val))
			d[key] = val
		index += 1
		return (d, index)

	def strToJson(self, string):
		result = self.strToJsonHelper(string, 0)
		return(result[0])

	def JsonToString(self, json):
		result = ''
		result += '{'
		for key in json:
			result += key + ':' + str(json[key])
			result += ','
		result += '}'
		return result

s = Converter()
json = '{id: 0001,type: donut,name: Cake,ppu: 0.55, batters:{batter:[{ id: 1001, type: Regular },{ id: 1002, type: Chocolate }]},topping:[{ id: 5001, type: None },{ id: 5002, type: Glazed }]}'
print(s.JsonToString(s.strToJson(json)))
