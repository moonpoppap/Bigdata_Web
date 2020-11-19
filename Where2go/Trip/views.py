from django.shortcuts import render
import pandas as pd
from pythainlp.tokenize import word_tokenize
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from django.shortcuts import render
import pandas as pd
import numpy

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
    return render(request,'Safari World.html',{'ans':ans,'comment':comment})

#ทำนายคอมเม้น
def CommentPredict(request):
    comm = request.POST['comm']
    comment=word_tokenize(comm,engine='newmm')
    Test= numpy.zeros((1,123))
    for x in comment:
        if(x=="ดี"):
            Test[0][0]+=1
        if(x=="สบาย"):
            Test[0][1]+=1
        if(x=="สวย"):
            Test[0][2]+=1
        if(x=="คุ้มค่า"):
            Test[0][3]+=1
        if(x=="ประทับใจ"):
            Test[0][4]+=1
        if(x=="สดชื่น"):
            Test[0][5]+=1
        if(x=="ภูมิใจ"):
            Test[0][6]+=1
        if(x=="รัก"):
            Test[0][7]+=1
        if(x=="ชอบ"):
            Test[0][8]+=1
        if(x=="สมใจ"):
            Test[0][9]+=1
        if(x=="ฟิน"):
            Test[0][10]+=1
        if(x=="ตรึงตาตรึงใจ"):
            Test[0][11]+=1
        if(x=="ร่มรื่น"):
            Test[0][12]+=1
        if(x=="เงียบ"):
            Test[0][13]+=1
        if(x=="สงบ"):
            Test[0][14]+=1
        if(x=="สะดวก"):
            Test[0][15]+=1
        if(x=="สะอาด"):
            Test[0][16]+=1
        if(x=="สะใจ"):
            Test[0][17]+=1
        if(x=="สุดยอด"):
            Test[0][18]+=1
        if(x=="เยี่ยม"):
            Test[0][19]+=1
        if(x=="งดงาม"):
            Test[0][20]+=1
        if(x=="ว้าว"):
            Test[0][21]+=1
        if(x=="ขาว"):
            Test[0][22]+=1
        if(x=="สนุก"):
            Test[0][23]+=1
        if(x=="น่าสนใจ"):
            Test[0][24]+=1
        if(x=="ถูกใจ"):
            Test[0][25]+=1
        if(x=="ฟรี"):
            Test[0][26]+=1
        if(x=="สุภาพ"):
            Test[0][27]+=1
        if(x=="ให้ความรู้"):
            Test[0][28]+=1
        if(x=="ง่าย"):
            Test[0][29]+=1
        if(x=="ทันสมัย"):
            Test[0][30]+=1
        if(x=="ตื่นเต้น"):
            Test[0][31]+=1
        if(x=="ถูก"):
            Test[0][32]+=1
        if(x=="ลงตัว"):
            Test[0][33]+=1
        if(x=="แปลกตา"):
            Test[0][34]+=1
        if(x=="น่าชม"):
            Test[0][35]+=1
        if(x=="ร่ม"):
            Test[0][36]+=1
        if(x=="มีความสุข"):
            Test[0][37]+=1
        if(x=="ขอบคุณ"):
            Test[0][38]+=1
        if(x=="อลังการ"):
            Test[0][39]+=1
        if(x=="มีคุณค่า"):
            Test[0][40]+=1
        if(x=="สมบูรณ์"):
            Test[0][41]+=1
        if(x=="ระเบียบ"):
            Test[0][42]+=1
        if(x=="แนะนำ"):
            Test[0][43]+=1
        if(x=="สุขใจ"):
            Test[0][44]+=1
        if(x=="คุ้ม"):
            Test[0][45]+=1
        if(x=="เยอะ"):
            Test[0][46]+=1
        if(x=="กว้าง"):
            Test[0][47]+=1
        if(x=="ใหญ่"):
            Test[0][48]+=1
        if(x=="อร่อย"):
            Test[0][49]+=1
        if(x=="น่ารัก"):
            Test[0][50]+=1
        if(x=="เย็น"):
            Test[0][51]+=1
        if(x=="เหมาะ"):
            Test[0][52]+=1
        if(x=="รื่นรมย์"):
            Test[0][53]+=1
        if(x=="สมควร"):
            Test[0][54]+=1
        if(x=="หวาน"):
            Test[0][55]+=1
        if(x=="สด"):
            Test[0][56]+=1
        if(x=="ใหม่"):
            Test[0][57]+=1
        if(x=="คุณภาพ"):
            Test[0][58]+=1
        if(x=="เพียงพอ"):
            Test[0][59]+=1
        if(x=="อิ่ม"):
            Test[0][60]+=1
        if(x=="เพียบ"):
            Test[0][61]+=1
        if(x=="ให้"):
            Test[0][62]+=1
        if(x=="เสียเงิน"):
            Test[0][63]+=1
        if(x=="ปิด"):
            Test[0][64]+=1
        if(x=="รถติด"):
            Test[0][65]+=1
        if(x=="ร้อน"):
            Test[0][66]+=1
        if(x=="อด"):
            Test[0][67]+=1
        if(x=="ลด"):
            Test[0][68]+=1
        if(x=="น้อยลง"):
            Test[0][69]+=1
        if(x=="แพง"):
            Test[0][70]+=1
        if(x=="ไกล"):
            Test[0][71]+=1
        if(x=="ลำบาก"):
            Test[0][72]+=1
        if(x=="เสียดาย"):
            Test[0][73]+=1
        if(x=="สกปรก"):
            Test[0][74]+=1
        if(x=="ปรับปรุง"):
            Test[0][75]+=1
        if(x=="ยาก"):
            Test[0][76]+=1
        if(x=="ขยะ"):
            Test[0][77]+=1
        if(x=="พลุกพล่าน"):
            Test[0][78]+=1
        if(x=="เกินไป"):
            Test[0][79]+=1
        if(x=="แน่น"):
            Test[0][80]+=1
        if(x=="น่าเกลียด"):
            Test[0][81]+=1
        if(x=="ไม่ค่อย"):
            Test[0][82]+=1
        if(x=="สับสน"):
            Test[0][83]+=1
        if(x=="ผิดกฎหมาย"):
            Test[0][84]+=1
        if(x=="ผิดหวัง"):
            Test[0][85]+=1
        if(x=="เสียเวลา"):
            Test[0][86]+=1
        if(x=="เสีย"):
            Test[0][87]+=1
        if(x=="เบื่อ"):
            Test[0][88]+=1
        if(x=="ห่วย"):
            Test[0][89]+=1
        if(x=="รำคาญ"):
            Test[0][90]+=1
        if(x=="หลอก"):
            Test[0][91]+=1
        if(x=="แย่"):
            Test[0][92]+=1
        if(x=="เบียด"):
            Test[0][93]+=1
        if(x=="โกรธ"):
            Test[0][94]+=1
        if(x=="แออัด"):
            Test[0][95]+=1
        if(x=="น้อย"):
            Test[0][96]+=1
        if(x=="งง"):
            Test[0][97]+=1
        if(x=="นิดหน่อย"):
            Test[0][98]+=1
        if(x=="กลัว"):
            Test[0][99]+=1
        if(x=="เก่า"):
            Test[0][100]+=1
        if(x=="ธรรมดา"):
            Test[0][101]+=1
        if(x=="เมื่อย"):
            Test[0][102]+=1
        if(x=="นาน"):
            Test[0][103]+=1
        if(x=="ไม่"):
            Test[0][104]+=1
        if(x=="น่า"):
            Test[0][105]+=1
        if(x=="อยาก"):
            Test[0][106]+=1
        if(x=="ใส"):
            Test[0][107]+=1
        if(x=="ขุ่น"):
            Test[0][108]+=1
        if(x=="ไป"):
            Test[0][109]+=1
        if(x=="ควร"):
            Test[0][110]+=1
        if(x=="มา"):
            Test[0][111]+=1
        if(x=="ได้"):
            Test[0][112]+=1
        if(x=="ความรู้"):
            Test[0][113]+=1
        if(x=="พิจารณา"):
            Test[0][114]+=1
        if(x=="เย็นสบาย"):
            Test[0][115]+=1
        if(x=="น่าเบื่อ"):
            Test[0][116]+=1
        if(x=="เอกลักษณ์"):
            Test[0][117]+=1
        if(x=="เฉย"):
            Test[0][118]+=1
        if(x=="มี"):
            Test[0][119]+=1
        if(x=="ห่วยแตก"):
            Test[0][120]+=1
        if(x=="ดีมาก"):
            Test[0][121]+=1
        if(x=="แย่มาก"):
            Test[0][122]+=1
    #อ่านข้อมูล
    df=pd.read_csv("data/TrainData/Train.csv")

    x=df.drop("Feeling",axis=1).values

    y=df['Feeling'].values

    knn=KNeighborsClassifier(n_neighbors=1)

    knn.fit(x,y)

    pred=knn.predict(Test)

    trip = request.POST['comment']
    #เกษตร
    if(trip=="Jim"):
        readDF=pd.read_csv("data/Jim.csv",encoding="mbcs")
    elif(trip=="Corn"):
        readDF=pd.read_csv("data/Corn.csv",encoding="mbcs")
    elif(trip=="Chokchai"):
        readDF=pd.read_csv("data/Chokchai.csv",encoding="mbcs")
    elif(trip=="Sufficiency"):
        readDF=pd.read_csv("data/Sufficiency.csv",encoding="mbcs")
    #ธรรมชาติ
    elif(trip=="Mountain"):
        readDF=pd.read_csv("data/Mountain.csv",encoding="mbcs")
    elif(trip=="Waterfall"):
        readDF=pd.read_csv("data/Waterfall.csv",encoding="mbcs")
    elif(trip=="Park"):
        readDF=pd.read_csv("data/Park.csv",encoding="mbcs")
    elif(trip=="Garden"):
        readDF=pd.read_csv("data/Garden.csv",encoding="mbcs")
    #ทะเล
    elif(trip=="Island"):
        readDF=pd.read_csv("data/Island.csv",encoding="mbcs")
    elif(trip=="ChaAm"):
        readDF=pd.read_csv("data/ChaAm.csv",encoding="mbcs")
    elif(trip=="HuaHin"):
        readDF=pd.read_csv("data/HuaHin.csv",encoding="mbcs")
    elif(trip=="Chaweng"):
        readDF=pd.read_csv("data/Chaweng.csv",encoding="mbcs")
    #ประวัติศาสตร์
    elif(trip=="Rattanakosin"):
        readDF=pd.read_csv("data/Rattanakosin.csv",encoding="mbcs")
    elif(trip=="Siam"):
        readDF=pd.read_csv("data/Siam.csv",encoding="mbcs")
    elif(trip=="Temple"):
        readDF=pd.read_csv("data/Temple.csv",encoding="mbcs")
    elif(trip=="Historic"):
        readDF=pd.read_csv("data/Historic.csv",encoding="mbcs")
    #นันนาการ
    elif(trip=="GreenHill"):
        readDF=pd.read_csv("data/GreenHill.csv",encoding="mbcs")
    elif(trip=="LivePark"):
        readDF=pd.read_csv("data/LivePark.csv",encoding="mbcs")
    elif(trip=="DreamWorld"):
        readDF=pd.read_csv("data/DreamWorld.csv",encoding="mbcs")
    elif(trip=="SafariWorld"):
        readDF=pd.read_csv("data/SafariWorld.csv",encoding="mbcs")

    new = {'Comment': comm,
            'Feeling': pred
          }
    
    df = pd.DataFrame(new,columns= ['Comment', 'Feeling'])

    frame = [readDF,df]
    result = pd.concat(frame)
    #เกษตร
    if(trip=="Jim"):
        result.to_csv(r'data/Jim.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/Jim.csv",encoding="mbcs")
    elif(trip=="Corn"):
        result.to_csv(r'data/Corn.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/Corn.csv",encoding="mbcs")
    elif(trip=="Chokchai"):
        result.to_csv(r'data/Chokchai.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/Chokchai.csv",encoding="mbcs")
    elif(trip=="Sufficiency"):
        result.to_csv(r'data/Sufficiency.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/Sufficiency.csv",encoding="mbcs")
    #ธรรมชาติ
    elif(trip=="Mountain"):
        result.to_csv(r'data/Mountain.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/Mountain.csv",encoding="mbcs")
    elif(trip=="Waterfall"):
        result.to_csv(r'data/Waterfall.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/Waterfall.csv",encoding="mbcs")
    elif(trip=="Park"):
        result.to_csv(r'data/Park.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/Park.csv",encoding="mbcs")
    elif(trip=="Garden"):
        result.to_csv(r'data/Garden.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/Garden.csv",encoding="mbcs")
    #ทะเล
    elif(trip=="Island"):
        result.to_csv(r'data/Island.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/Island.csv",encoding="mbcs")
    elif(trip=="ChaAm"):
        result.to_csv(r'data/ChaAm.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/ChaAm.csv",encoding="mbcs")
    elif(trip=="HuaHin"):
        result.to_csv(r'data/HuaHin.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/HuaHin.csv",encoding="mbcs")
    elif(trip=="Chaweng"):
        result.to_csv(r'data/Chaweng.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/Chaweng.csv",encoding="mbcs")
    #ประวัติศาสตร์
    elif(trip=="Rattanakosin"):
        result.to_csv(r'data/Rattanakosin.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/Rattanakosin.csv",encoding="mbcs")
    elif(trip=="Siam"):
        result.to_csv(r'data/Siam.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/Siam.csv",encoding="mbcs")
    elif(trip=="Temple"):
        result.to_csv(r'data/Temple.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/Temple.csv",encoding="mbcs")
    elif(trip=="Historic"):
        result.to_csv(r'data/Historic.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/Historic.csv",encoding="mbcs")
    #นันนาการ
    elif(trip=="GreenHill"):
        result.to_csv(r'data/GreenHill.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/GreenHill.csv",encoding="mbcs")
    elif(trip=="LivePark"):
        result.to_csv(r'data/LivePark.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/LivePark.csv",encoding="mbcs")
    elif(trip=="DreamWorld"):
        result.to_csv(r'data/DreamWorld.csv', encoding="mbcs", index = False)
        df=pd.read_csv("data/DreamWorld.csv",encoding="mbcs")
    elif(trip=="SafariWorld"):
        result.to_csv(r'data/SafariWorld.csv', encoding="mbcs", index = False)
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
    #เกษตร
    if(trip=="Jim"):
        return render(request,'จิมทอมสันฟาร์ม.html',{'ans':ans,'comment':comment, 'feel':pred})
    elif(trip=="Corn"):
        return render(request,'ข้าวโพดไร่สุวรรณ.html',{'ans':ans,'comment':comment, 'feel':pred})
    elif(trip=="Chokchai"):
        return render(request,'ฟาร์มโชคชัย.html',{'ans':ans,'comment':comment, 'feel':pred})
    elif(trip=="Sufficiency"):
        return render(request,'ศูนย์การเรียนรู้เศรษฐกิจพอเพียง.html',{'ans':ans,'comment':comment, 'feel':pred})
    #ธรรมชาติ
    elif(trip=="Mountain"):
        return render(request,'Nดอยอินทนนท์.html',{'ans':ans,'comment':comment, 'feel':pred})
    elif(trip=="Waterfall"):
        return render(request,'Nน้ำตกห้วยแม่ขมิ้น.html',{'ans':ans,'comment':comment, 'feel':pred})
    elif(trip=="Park"):
        return render(request,'Nอุทยานแห่งชาติภูเรือ.html',{'ans':ans,'comment':comment, 'feel':pred})
    elif(trip=="Garden"):
        return render(request,'Nสวนดอกไม้เมืองหนาวเบตง.html',{'ans':ans,'comment':comment, 'feel':pred})
     #ทะเล
    elif(trip=="Island"):
        return render(request,'sเกาะขาม.html',{'ans':ans,'comment':comment, 'feel':pred})
    elif(trip=="ChaAm"):
        return render(request,'sหาดชำอำ.html',{'ans':ans,'comment':comment, 'feel':pred})
    elif(trip=="HuaHin"):
        return render(request,'sหาดหัวหิน.html',{'ans':ans,'comment':comment, 'feel':pred})
    elif(trip=="Chaweng"):
        return render(request,'sหาดเฉวง.html',{'ans':ans,'comment':comment, 'feel':pred})
     #ประวัติศาสตร์
    elif(trip=="Rattanakosin"):
        return render(request,'นิทรรศน์รัตนโกสินทร์.html',{'ans':ans,'comment':comment, 'feel':pred})
    elif(trip=="Siam"):
        return render(request,'มิวเซียมสยาม.html',{'ans':ans,'comment':comment, 'feel':pred})
    elif(trip=="Temple"):
        return render(request,'วัดพระแก้ว.html',{'ans':ans,'comment':comment, 'feel':pred})
    elif(trip=="Historic"):
        return render(request,'อุทยานประวัติศาสตร์เมืองสิงห์.html',{'ans':ans,'comment':comment, 'feel':pred})
     #นันนาการ
    elif(trip=="GreenHill"):
        return render(request,'สวนสัตว์เปิดเขาเขียว.html',{'ans':ans,'comment':comment, 'feel':pred})
    elif(trip=="LivePark"):
        return render(request,'สวนสนุกไลฟ์ปาร์ค @เขาใหญ่.html',{'ans':ans,'comment':comment, 'feel':pred})
    elif(trip=="DreamWorld"):
        return render(request,'ดรีมเวิลด์.html',{'ans':ans,'comment':comment, 'feel':pred})
    elif(trip=="SafariWorld"):
        return render(request,'Safari World.html',{'ans':ans,'comment':comment, 'feel':pred})

#ทำนายประเภทแหล่งท่องเที่ยว
def TripPredict(request):

    gender = request.POST['gender']
    age = request.POST['age']
    central = request.POST['central']
    plan = request.POST['plan']
    people = request.POST['people']
    travel = request.POST['travel']
    day = request.POST['day']
    cost = request.POST['cost']
    time = request.POST['time']
    busy = request.POST['busy']
    strain = request.POST['strain']
    photo = request.POST['photo']
    region = request.POST['region']
    help = request.POST['help']
    stay = request.POST['stay']
    like = request.POST['like']
    get = request.POST['get']

    Test= numpy.zeros((1,30))

    #เงื่อนไข gender
    if(gender=="female"):
        Test[0][0]=1
    elif(gender=="male"):
        Test[0][1]=1

    #เงื่อนไข age
    if(age=="young"):
        Test[0][2]=1
    elif(age=="half"):
        Test[0][2]=2
    else:
        Test[0][2]=3

    #เงื่อนไข central
    if(central=="yes"):
        Test[0][3]=1

    #เงื่อนไข plan
    if(plan=="1"):
        Test[0][4]=1
    elif(plan=="2"):
        Test[0][4]=2
    elif(plan=="3"):
        Test[0][4]=3
    elif(plan=="4"):
        Test[0][4]=4
    else:
        Test[0][4]=5

    #เงื่อนไข people
    if(people=="friends"):
        Test[0][5]=1
    elif(people=="alone"):
        Test[0][6]=1
    
    #เงื่อนไข travel
    if(travel=="private"):
        Test[0][7]=1
    elif(travel=="train"):
        Test[0][8]=1
    
    #เงื่อนไข day
    if(day=="1"):
        Test[0][9]=1
    elif(day=="2"):
        Test[0][9]=2
    else:
        Test[0][9]=3

    #เงื่อนไข cost
    if(cost=="1k"):
        Test[0][10]=1
    elif(cost=="3k"):
        Test[0][10]=2
    elif(cost=="5k"):
        Test[0][10]=3
    else:
        Test[0][10]=4
    
     #เงื่อนไข time
    if(time=="everytime"):
        Test[0][11]=1
    elif(time=="termend"):
        Test[0][12]=1
    elif(time=="holiday"):
        Test[0][13]=1
    
    #เงื่อนไข busy
    if(busy=="1"):
        Test[0][14]=1
    elif(busy=="2"):
        Test[0][14]=2
    elif(busy=="3"):
        Test[0][14]=3
    elif(busy=="4"):
        Test[0][14]=4
    else:
        Test[0][14]=5

    #เงื่อนไข strain
    if(strain=="1"):
        Test[0][15]=1
    elif(strain=="2"):
        Test[0][15]=2
    elif(strain=="3"):
        Test[0][15]=3
    elif(strain=="4"):
        Test[0][15]=4
    else:
        Test[0][15]=5
    
    #เงื่อนไข photo
    if(photo=="1"):
        Test[0][16]=1
    elif(photo=="2"):
        Test[0][16]=2
    elif(photo=="3"):
        Test[0][16]=3
    elif(photo=="4"):
        Test[0][16]=4
    else:
        Test[0][16]=5
    
    #เงื่อนไข region
    if(region=="in"):
        Test[0][17]=0
    
    #เงื่อนไข help
    if(help=="2"):
        Test[0][18]=2
    elif(help=="3"):
        Test[0][18]=3
    elif(help=="4"):
        Test[0][18]=4
    else:
        Test[0][18]=5

    #เงื่อนไข stay
    if(stay=="resort"):
        Test[0][19]=1
    elif(stay=="hotel"):
        Test[0][20]=1
    elif(stay=="homestay"):
        Test[0][21]=1
    elif(stay=="dailyroom"):
        Test[0][22]=1

    #เงื่อนไข like
    if(like=="n"):
        Test[0][23]=1
    elif(like=="c"):
        Test[0][24]=1
    elif(like=="e"):
        Test[0][25]=1
    elif(like=="s"):
        Test[0][26]=1
    
    #เงื่อนไข get
    if(get=="newexp"):
        Test[0][27]=1
    elif(get=="rest"):
        Test[0][28]=1
    elif(get=="relationship"):
        Test[0][29]=1

    df=pd.read_csv("data/TrainData/Train2.csv")

    x=df.drop("TouristAttraction",axis=1).values

    y=df['TouristAttraction'].values

    gbc = GradientBoostingClassifier()
    gbc.fit(x,y) 

    pred=gbc.predict(Test)

    if(pred=="farm"):
        return render(request,'ans01.html')
    elif(pred=="sea"):
        return render(request,'ans02.html')
    elif(pred=="nature"):
        return render(request,'ans03.html')
    elif(pred=="recreation"):
        return render(request,'ans04.html')
    else:
        return render(request,'ans05.html')