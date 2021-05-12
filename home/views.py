from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from home.models import Data
import requests
from requests.exceptions import ConnectionError
from requests.packages.urllib3.exceptions import MaxRetryError
from requests.packages.urllib3.exceptions import ProxyError as urllib3_ProxyError
from .forms import TrafficChecker
# import 
from bs4 import BeautifulSoup
# from home.apps.HomeConfig.models import Datas
from django.contrib.auth import logout,authenticate,login
from django.http import HttpResponse

# global s
s = requests.session()
headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
            }
# print(s)
# Create your views here.
def loginUser(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
       
        if user is not None:
            login(request,user)
            
            # s = requests.session()
            payload={
            "log":username,
            'pwd': password,    
                }
            try:

            # global response
                response = s.post("https://www.seoreviewtools.com/wp-login.php",data=payload,headers = headers)
                print("mai login hoagaya seoreview tools mai",response)
            # print(response.content)
            # if request.method == "POST":
            # global search
            # search = request.POST.get('myvalue')
            except ConnectionError as ce:
                if (isinstance(ce.args[0], MaxRetryError) and
                        isinstance(ce.args[0].reason, urllib3_ProxyError)):
                    # oops, requests should have handled this, but didn't.
                    # see https://github.com/kennethreitz/requests/issues/3050
                    pass
            
            # print(search)
            return redirect('/')
            
            
        else:
        # No backend authenticated the credentials
            return render(request,'login.html')
        
    return render(request,'login.html')

def index(request):
    # global context
    if request.user.is_anonymous:
        return redirect('/login')
    # context = {
    #     'variable':abc(request)
    # }


    
    # return render(request,'index.html',context)
    
    if request.method == 'POST':
        fm = TrafficChecker(request.POST)
        if fm.is_valid:
            data = request.POST['data']
            z = data
            # print(z)
            try:
                m = { 'urls':data,
                'captcha': '',
                'cc': 68,
                'submit': ''
                }

                a = s.post('https://www.seoreviewtools.com/website-traffic-checker/',data=m,headers=headers)
                print("search hoagaya")
                x = a.content
                soup = BeautifulSoup(x, 'lxml')
                # print("\nFind and print all li tags:\n")
                lst = []
                counter = 0
                for tag in soup.find_all("td"):
                    if counter <=5:
                        lst.append(tag.text)
                    else:
                        pass
                # print(lst)
                # FOR DA PA MOZ RANK
                d = {
                    "url": data,
                    "submit": "Submit"
                }
                b = s.post("https://demo.atozseotools.com/mozrank-checker/output",d,headers=headers)
                soup1 = BeautifulSoup(b.content, 'lxml')
                # lst = []
                counter = 0
                for tagb in soup1.find_all("td"):
                    if counter <= 5:
                        lst.append(tagb.text)
                    else:
                        pass
                return render(request, 'index.html', {'form': fm, 'variable': lst})
            except ConnectionError as ce:
                if (isinstance(ce.args[0], MaxRetryError) and
                        isinstance(ce.args[0].reason, urllib3_ProxyError)):
                    # oops, requests should have handled this, but didn't.
                    # see https://github.com/kennethreitz/requests/issues/3050
                    pass
            # print(lst2)
    else:
        fm = TrafficChecker()

    return render(request,'index.html',{'form':fm})


# def abc(request):
    # search = request.POST.get('myvalue')
    # m = { 'urls':search,
    # 'captcha': '',
    # 'cc': 68,
    # 'submit': ''
    # }
    # a = s.post('https://www.seoreviewtools.com/website-traffic-checker/',data=m)
    
    # x = a.content
    # return x




def logoutUser(request):
    logout(request)
    return redirect('/login')

