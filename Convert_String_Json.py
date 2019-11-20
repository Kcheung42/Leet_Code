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

    delim = set(['[' ,',', ']', '}'])

    def jsonArray(self, s, index):
        array = []
        while s[index] != ']':
            index += 1
            if s[index] == '{':
                val , index = self.strToJsonHelper(s, index)
            else:
                start = index
                while s[index] not in self.delim:
                    index += 1
                val = s[start:index]
                if all(x.isdigit() for x in val):
                    val = int(val)
            array.append(val)
        index += 1
        return (array, index)

    def strToJsonHelper(self, s, index):
        if s[index] != '{':
            return
        d = {}
        while s[index] != '}':
            key = ''
            val = ''
            index += 1

            start = index
            while s[index] != ':':
                if s[index] != '"':
                    key += s[index]
                index +=1
            while s[index] not in self.delim:
                index += 1
            # start of a new json map
            if s[index] == '{':
                val, index = self.strToJsonHelper(s, index)
            # start of a new json array
            elif s[index] == '[':
                val, index = self.jsonArray(s, index)
            # get regular value
            else:
                while(s[index] not in self.delim):
                    if s[index] != ' ':
                        val += s[index]
                    index += 1
            # print(f'\nkey: {key} , val: {val}')
            d[key] = val
        index += 1
        return (d, index)

    def strToJson(self, string):
        result = self.strToJsonHelper(string, 0)
        return(result[0])


    def JsonToString(self, json):
        result = ''
        result += '{'
        result = ['{']
        for key,val in json.items():
            result.append(''.join([key, ':', str(val)]))
        result.append('}')
        return ",".join(result)

    def prettyPrintJson(self, json):
        i = 0
        result = []
        multiplier = 0
        indent = "   "
        while i  < len(json):
            if json[i] in ['{', '[']:
                result.append(indent * multiplier + json[i])
                multiplier += 1
                i += 1
            elif json[i] in ['}', ']']:
                multiplier -= 1
                result.append(indent * multiplier + json[i])
                i += 1
            elif json[i] == ',':
                result[-1] += ','
                i += 1
            else:
                start = i
                while i < len(json) and json[i] not in ['[', ']', '{', '}', ',' ]:
                    i += 1
                result.append(indent * multiplier + json[start:i])

        for r in result:
            print(r)


s = Converter()
# json = '{id: 0001,type: donut,name: Cake,ppu: 0.55, batters:{batter:[{ id: 1001, type: Regular },{ id: 1002, type: Chocolate }]}, nums: [1,2,3,4,5],topping:[{ id: 5001, type: None },{ id: 5002, type: Glazed }]}'
json = '{"id": "0001","type": "donut","name": "Cake","ppu": 0.55,"batters":{"batter":[{ "id": "1001", "type": "Regular" },{ "id": "1002", "type": "Chocolate" }]},"topping":[{ "id": "5001", "type": "None" },{ "id": "5002", "type": "Glazed" }]}'
# print(s.JsonToString(s.strToJson(json)))
# json = '{nums: [1,2,3,4]}'
# print(s.strToJson(json))
print(s.prettyPrintJson(json))
