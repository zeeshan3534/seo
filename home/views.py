from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from home.models import Data
import requests
from .forms import TrafficChecker
# import 
from bs4 import BeautifulSoup
# from home.apps.HomeConfig.models import Datas
from django.contrib.auth import logout,authenticate,login
from django.http import HttpResponse

global s
s = requests.session()
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
            # global response
            response = s.post("https://www.seoreviewtools.com/wp-login.php",data=payload)
            # print(response.content)
            # if request.method == "POST":
            # global search
            # search = request.POST.get('myvalue')
            
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

            m = { 'urls':data,
            'captcha': '',
            'cc': 68,
            'submit': ''
            }
            a = s.post('https://www.seoreviewtools.com/website-traffic-checker/',data=m)
            
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
            b = s.post("https://demo.atozseotools.com/mozrank-checker/output",d)
            soup1 = BeautifulSoup(b.content, 'lxml')
            # lst = []
            counter = 0
            for tagb in soup1.find_all("td"):
                if counter <= 5:
                    lst.append(tagb.text)
                else:
                    pass
            # print(lst2)

            return render(request, 'index.html', {'form': fm, 'variable':lst})

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

