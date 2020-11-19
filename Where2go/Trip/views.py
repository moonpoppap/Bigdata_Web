from django.shortcuts import render
import pandas as pd

def Home(request):
    return render(request,'index.html')
def Question(request):
    return render(request,'questionnaire.html')
#จิมทอมสันฟาร์ม
def Jim(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/Jim.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'จิมทอมสันฟาร์ม.html',{'ans':ans,'comment':comment})

#ข้าวโพดไร่สุวรรณ
def Corn(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/Corn.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'ข้าวโพดไร่สุวรรณ.html',{'ans':ans,'comment':comment})

#ฟาร์มโชคชัย
def Chokchai(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/Chokchai.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'ฟาร์มโชคชัย.html',{'ans':ans,'comment':comment})

#ศูนย์การเรียนรู้เศรษฐกิจพอเพียง
def Sufficiency(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/Sufficiency.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'ศูนย์การเรียนรู้เศรษฐกิจพอเพียง.html',{'ans':ans,'comment':comment})

#ดอยอินทนนท์
def Mountain(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/Mountain.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'Nดอยอินทนนท์.html',{'ans':ans,'comment':comment})

#น้ำตกห้วยแม่ขมิ้น
def Waterfall(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/Waterfall.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'Nน้ำตกห้วยแม่ขมิ้น.html',{'ans':ans,'comment':comment})

#อุทยานแห่งชาติภูเรือ
def Park(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/Park.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'Nอุทยานแห่งชาติภูเรือ.html',{'ans':ans,'comment':comment})

#สวนดอกไม้เมืองหนาวเบตง
def Garden(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/Garden.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'Nสวนดอกไม้เมืองหนาวเบตง.html',{'ans':ans,'comment':comment})

#เกาะขาม
def Island(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/Island.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'sเกาะขาม.html',{'ans':ans,'comment':comment})

#หาดชำอำ
def ChaAm(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/ChaAm.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'sหาดชำอำ.html',{'ans':ans,'comment':comment})

#หาดหัวหิน
def HuaHin(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/HuaHin.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'sหาดหัวหิน.html',{'ans':ans,'comment':comment})

#หาดเฉวง
def Chaweng(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/Chaweng.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'sหาดเฉวง.html',{'ans':ans,'comment':comment})

#นิทรรศน์รัตนโกสินทร์
def Rattanakosin(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/Rattanakosin.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'นิทรรศน์รัตนโกสินทร์.html',{'ans':ans,'comment':comment})

#มิวเซียมสยาม
def Siam(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/Siam.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'มิวเซียมสยาม.html',{'ans':ans,'comment':comment})

#วัดพระแก้ว
def Temple(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/Temple.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'วัดพระแก้ว.html',{'ans':ans,'comment':comment})

#อุทยานประวัติศาสตร์เมืองสิงห์
def Historic(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/Historic.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'อุทยานประวัติศาสตร์เมืองสิงห์.html',{'ans':ans,'comment':comment})

#สวนสัตว์เปิดเขาเขียว
def GreenHill(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/GreenHill.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'สวนสัตว์เปิดเขาเขียว.html',{'ans':ans,'comment':comment})

#สวนสนุกไลฟ์ปาร์ค
def LivePark(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/LivePark.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'สวนสนุกไลฟ์ปาร์ค @เขาใหญ่.html',{'ans':ans,'comment':comment})

#ดรีมเวิลด์
def DreamWorld(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/DreamWorld.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'ดรีมเวิลด์.html',{'ans':ans,'comment':comment})

#Safari World
def SafariWorld(request):
    #อ่านไฟล์ ภาษาไทย ด้วย encoding mbcs
    df=pd.read_csv("data/SafariWorld.csv",encoding="mbcs")
    comment = df['Comment'].values
    feeling = df['Feeling'].values
    p=0
    ne=0
    no=0
    for x in feeling:
        if(x=='positive'):
            p+=1
        elif(x=='negative'):
            ne+=1
        else:
            no+=1
    if(p>=no and p>ne):
        ans='positive'
    elif(ne>=no and ne>p):
        ans='negative'
    else:
        ans='normal'
    return render(request,'Safari World.html',{'ans':ans,'comment':comment})