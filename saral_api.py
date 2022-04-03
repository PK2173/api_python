# import requests,json

# data= requests.get('http://saral.navgurukul.org/api/courses').json()
# with open('json_file.json','w') as f:
#     json.dump(data,f,indent=4)

# for i in data['availableCourses']:
#     print(i['id'],i['name'])
# res=int(input('enter cours id'))
# url1='http://saral.navgurukul.org/api/courses/'+str(res)+'/exercises'
# data1=requests.get(url1).json()
# with open('coreces.json','w') as f1:
#         json.dump(data1,f1,indent=4)

# x=0
# y=[]
# for i in data1['data']:
#     print(x,i['slug'])
#     y.append(i['slug'])
#     x+=1

# res1=int(input("enter your number"))
# url2='http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug='+str(y[res1])
# data2=requests.get(url2).json()
# with open('final.json','w') as f2:
#     json.dump(data2['slug'],f2,indent=4)


