# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json
from django.http import HttpResponse

from .models import user, article

from django.shortcuts import  get_object_or_404, render

import sys

# Create your views here.

#中文编码
default_encoding='utf-8'
if sys.getdefaultencoding()!=default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)



language_mapping = {'Chinese': 'zh-CHS', 'English': 'en', 'Japanese': 'ja', 'Korean': 'ko', 'Russian': 'ru'}

def getindex(request):
    return render(request,'translation/index.html')

def getspot(request):
    return render(request,'translation/spot.html')

def gethistory(request):
    return render(request,'translation/history.html')

def getlogin(request):
    return render(request,'translation/login.html')

def getregisger(request):
    return render(request,'translation/register.html')

def getcollection(request):
    return render(request,'translation/collection.html')


def getPersonCenter(request):
    return render(request,'translation/personCenter.html')



'''
class user(models.Model):
    user_name=models.CharField(max_length=10)
    user_email=models.CharField(max_length=20)
    user_password=models.CharField(max_length=20)
    user_city=models.CharField(max_length=10)
    user_state=models.CharField(max_length=10)
    user_country=models.CharField(max_length=10)
    user_phone=models.CharField(max_length=10)
    user_gender=models.CharField(max_length=10)
'''

def get_user_register(request):
    print("hello")
    name=request.GET.get('name')
    print(name)
    email=request.GET.get('email')
    password=request.GET.get('password')
    city=request.GET.get('city')
    state=request.GET.get('state')
    country=request.GET.get('country')
    phone=request.GET.get('phone')
    gender=request.GET.get('gender')
    q=user(user_name=name,user_email=email,user_password=password,
           user_city=city,user_state=state,user_country=country,
           user_phone=phone,user_gender=gender,user_level=1,user_count=0)
    print(q.user_name)
    q.save()
    return HttpResponse("SUCCESS")



def get_user_login(request):
    print("fuck")
    users=user.objects.all()
    name=request.GET.get('userName')
    password=request.GET.get('userPassword')
    print(name,password)
    for q in users:
        print(q.user_name,q.user_password)
        if name == q.user_name:
            if password == q.user_password:
                print '123'
                p = [q.user_name,q.user_password,q.user_email,q.user_country,q.user_state,q.user_city,q.user_phone,q.user_level]
                res = json.dumps({'user_info':p})
                print res
                return HttpResponse(res)
            else:
                print("passnot")
        else:
            print("usnot")
    print("not correct")
    return HttpResponse("False")




'''
	            url:"add_collection",
	            type:"GET",
	            data:{user_name:user_name,spotName:spotName,spotHot:spotHot,
	            spotRate:spotRate,spotIntroduce:spotIntroduce,
	            imageUrl:imageUrl,siteUrl:siteUrl},
	            success:function(data){
	            	alert("收藏成功!");
	            	    user=models.ForeignKey(user,on_delete=models.CASCADE)
    article_title=models.CharField(max_length=10)
    article_url=models.CharField(max_length=80)
    article_pic=models.CharField(max_length=80)
    article_briefcontent=models.CharField(max_length=40)
'''


def get_add_collection(request):
    print('add_collection')
    username=request.GET.get('user_name')
    users = user.objects.get(user_name=username)
    '''
     data:{user_name:user_name,spotName:spotName,spotHot:spotHot,
	            spotRate:spotRate,spotIntroduce:spotIntroduce,
	            imageUrl:imageUrl,siteUrl:siteUrl},
	'''

    spotname=request.GET.get('spotName')
    imageurl=request.GET.get('imageUrl')
    siteUrl=request.GET.get('siteUrl')
    spotIntroduce=request.GET.get('spotIntroduce')
    spotRate=request.GET.get('spotRate')
    spotHot=request.GET.get('spotHot')
    articles = article.objects.filter(user=users)
    for q in articles:
        if q.article_url == siteUrl:
            return HttpResponse("Failed")
    q = article(user=user.objects.get(user_name=username), article_title=spotname, article_pic=imageurl,
                article_url=siteUrl, article_briefcontent=spotIntroduce,article_hot=spotHot,
                article_star=spotRate)
    #加经验
    print(users.user_count)
    users.user_count=users.user_count+1
    print(users.user_count)
    users.user_level=1+(int)(users.user_count/6)
    print(users.user_level)

    q.save()
    users.save()
    return HttpResponse('SUCCESS')





'''-----------------展示收藏--------------------------------'''

def get_show_collection(request):
    print('ok')
    name=request.GET.get('username')
    articles=user.objects.get(user_name=name).article_set.all()
    if articles == None:
        print('no')
        return HttpResponse("Failed")
    else:
        message = []
        for q in articles:
            mes = [q.article_title, q.article_briefcontent, q.article_pic, q.article_url,q.article_hot,q.article_star]
            message.append(mes)
        print(message)
        res = json.dumps({'collect_info': message})
        print res
        return HttpResponse(res)











def get_text_translation(request):
    text = request.GET.get('text')
    myLanguage = request.GET.get('myLanguage')
    outputLanguage = request.GET.get('outputLanguage')

    if text:
        translated_text = text_translation(text, myLanguage, outputLanguage)
        return HttpResponse(translated_text)
    else:
        translated_text = 'no text'
        return HttpResponse('请输入您要翻译的内容')
    




def hello_world(request):
    return HttpResponse("Hello World")





def get_image_translation(request):
    import httplib
    import md5
    import urllib
    import urllib2
    import random
    import json
    import base64

    image_name = request.GET.get('pictureName')
    print(image_name)
    # 您的应用ID
    appKey = "4870db38ab0ba6b0"
    # 您的应用密钥，请勿把它和appKey泄露给他人
    appSecret = "8FHEFxfxPMGJ94KjZDhQ1QXNGIbETrM3"
    
    
    httpClient = None
    
    try:
        # 参数部分
        f=open('C:/Users/cctvxzw\Desktop/testImages/' + image_name,'rb') #二进制方式打开图文件
        q=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
        f.close()
        # 源语言
        fromLan = "en"
        # 目标语言
        to = "zh-CHS"
        # 上传类型
        type = "1"
        # 随机数，自己随机生成，建议时间戳
        salt = random.randint(1, 65536)
        # 签名
        sign = appKey+q+str(salt)+appSecret
        m1 = md5.new()
        m1.update(sign)
        sign = m1.hexdigest()
        
        data = {'appKey':appKey,'q':q,'from':fromLan,'to':to,'type':type,'salt':str(salt),'sign':sign}
        data = urllib.urlencode(data)
        req = urllib2.Request('http://openapi.youdao.com/ocrtransapi',data)
        #response是HTTPResponse对象
        response = urllib2.urlopen(req)
        content = json.loads(response.read())['resRegions'][0]['tranContent']
        return HttpResponse(content)
    finally:
        if httpClient:
            httpClient.close()







def text_translation(s, myLanguage, outputLanguage):    
    import sys
    import uuid
    import requests
    import hashlib
    import time
    import json
    global language_mapping
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    YOUDAO_URL = 'http://openapi.youdao.com/api'
    APP_KEY = '4870db38ab0ba6b0'
    APP_SECRET = '8FHEFxfxPMGJ94KjZDhQ1QXNGIbETrM3'

    def encrypt(signStr):
        hash_algorithm = hashlib.sha256()
        hash_algorithm.update(signStr.encode('utf-8'))
        return hash_algorithm.hexdigest()
        
        
    def truncate(q):
        if q is None:
            return None
        size = len(q)
        return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]
            
            
    def do_request(data):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        return requests.post(YOUDAO_URL, data=data, headers=headers)
    
    q = s

    data = {}
    data['from'] = language_mapping[myLanguage]
    data['to'] = language_mapping[outputLanguage]
    
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign
    
    response = do_request(data)
    content = json.loads(response.content)
    return content['translation'][0].decode()














#----------------SPOT-----------#
from django.template import loader
from django.http import  Http404
import time, urllib2, json, re
from lxml import etree
import pandas as pd

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def getPage(url):  # 获取链接中的网页内容
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    try:
        request = urllib2.Request(url=url, headers=headers)
        response = urllib2.urlopen(request, timeout=5)
        page = response.read().decode('utf-8')
        return page
    except (urllib2.URLError, Exception), e:
        if hasattr(e, 'reason'):
            print '抓取失败，具体原因：', e.reason
            request = urllib2.Request(url=url, headers=headers)
            response = urllib2.urlopen(request, timeout=5)
            page = response.read().decode('utf-8')
            return page


def getList(place):
    url = 'http://piao.qunar.com/ticket/list.htm?keyword=' + str(place) + '&region=&from=mpl_search_suggest&page={}'
    i = 1
    sightlist = []
    while i < 2:
        page = getPage(url.format(i))
        selector = etree.HTML(page)
        print '正在爬取第' + str(i) + '页景点信息'
        i += 1
        informations = selector.xpath('//div[@class="result_list"]/div')
        for inf in informations:  # 获取必要信息
            sight_name = inf.xpath('./div/div/h3/a/text()')[0]
            sight_level = inf.xpath('.//span[@class="level"]/text()')
            if len(sight_level):
                sight_level = sight_level[0].replace('景区', '')
            else:
                sight_level = 0
            sight_area = inf.xpath('.//span[@class="area"]/a/text()')[0]
            sight_hot = inf.xpath('.//span[@class="product_star_level"]//span/text()')[0].replace('热度 ', '')
            sight_add = inf.xpath('.//p[@class="address color999"]/span/text()')[0]
            sight_add = re.sub('地址：|（.*?）|\(.*?\)|，.*?$|\/.*?$', '', str(sight_add))
            sight_slogen = inf.xpath('.//div[@class="intro color999"]/text()')[0]
            sight_price = inf.xpath('.//span[@class="sight_item_price"]/em/text()')
            if len(sight_price):
                sight_price = sight_price[0]
            else:
                i = 0
                break
            sight_soldnum = inf.xpath('.//span[@class="hot_num"]/text()')[0]

            sight_point = inf.xpath('./@data-point')[0]

            sight_url = inf.xpath('.//h3/a[@class="name"]/@href')[0]
         #   print sight_url
            sight_picture = inf.xpath('.//img[@class="img_opacity load"]/@data-original')[0]

            sightlist.append(
                [sight_name, sight_level, sight_area, float(sight_price), int(sight_soldnum), float(sight_hot),
                 sight_add.replace('地址：', ''), sight_point, sight_slogen, sight_url,sight_picture])
        time.sleep(3)
    return sightlist, place

def get_sight_info(request):
    place = request.GET.get('cityName')[:-1]
    sightlist, place = getList(place)
    return HttpResponse(json.dumps({'message':sightlist}))







