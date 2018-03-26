import requests
import base64
import os
import matplotlib.pyplot as plt
import time

def getaccess_token():
    host='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=xS1EZjweQYY6URGWP49CvTXS&client_secret=xaWNIn8t9aOf8lo4y1sM5VwzAWpfG1aT'
    header_1 = {'Content-Type':'application/json; charset=UTF-8'}
    request=requests.post(host,headers =header_1)
    access_token=request.json()['access_token']
    return access_token

def open_pic(x):
    f = open('%s' % x , 'rb')
    img = base64.b64encode(f.read())
    return img

def go_api(img,access_token,nuaaid):
    data_1 = {"face_fields":"age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities","image":img,"max_face_num":5}
    params_1 = {'access_token':access_token}
    header_2 = {'Content-Type':'application/x-www-form-urlencoded'}
    pic_re=requests.post('https://aip.baidubce.com/rest/2.0/face/v1/detect',params=params_1,headers=header_2,data=data_1)
    print(pic_re.json()['result'][0]['beauty'],pic_re.json()['result'][0]['gender'],nuaaid)
    return(pic_re.json()['result'][0]['beauty'],pic_re.json()['result'][0]['gender'],nuaaid)

def average(rating):
    a=rating[0]/rating[1]
    b=rating[2]/rating[3]
    c=rating[4]/rating[5]
    return [a,b,c]

def picture(male,num_list):
    if male==1:
        plt.title("girl")
    if male==2 :
        plt.title("boy")
    if male==3 :
        plt.title("all")
    name_list = ['01','02','03','05','06','07','08','10','11','12','15','16']
    plt.bar(range(len(num_list)), num_list,color='rgb',tick_label=name_list)
    plt.show()

if __name__ == '__main__':
    sum_female=0
    sum_male=0
    sum_all=0
    count_female=0
    count_male=0
    count_all=0
    max_female=0
    max_male=0
    access_token=getaccess_token()
    list_path1 = os.listdir()
    for path1 in list_path1[:12]:
        os.chdir(path1)
        print(path1)
        list_pathx = os.listdir()
        for pathx in list_pathx:
            os.chdir(pathx)
            list_path3 = os.listdir()
            for path3 in list_path3:
                img=open_pic(path3)
                try:
                    xxx=go_api(img,access_token,path3)
                except :
                    print("Error")
                    pass
                else:
                    if xxx[1]=='female':
                        sum_female=sum_female+xxx[0]
                        count_female=count_female+1
                        if xxx[0]>max_female:
                            max_female=xxx[0]
                            max_female_nuaaid=xxx[2]
                    if xxx[1]=='male':
                        sum_male=sum_male+xxx[0]
                        count_male=count_male+1
                        if xxx[0]>max_male:
                            max_male=xxx[0]
                            max_male_nuaaid=xxx[2]
                    sum_all=xxx[0]+sum_all
                    count_all=count_all+1
            os.chdir('..')
        rating_average=average([sum_female,count_female,sum_male,count_male,sum_all,count_all])
        if path1 == '0116' :
            average_01=rating_average
            rating_average=[0]
        if path1 == '0216' :
            average_02=rating_average
            rating_average=[0]
        if path1 == '0316':
            average_03=rating_average
            rating_average=[0]
        if path1 == '0516':
            average_05=rating_average
            rating_average=[0]
        if path1 == '0616':
            average_06=rating_average
            rating_average=[0]
        if path1 == '0716':
            average_07=rating_average
            rating_average=[0]
        if path1 == '0816':
            average_08=rating_average
            rating_average=[0]
        if path1 == '1016':
            average_10=rating_average
            rating_average=[0]
        if path1 == '1116':
            average_11=rating_average
            rating_average=[0]
        if path1 == '1216':
            average_12=rating_average
            rating_average=[0]
        if path1 == '1516':
            average_15=rating_average
            rating_average=[0]
        if path1 == '1616':
            average_16=rating_average
            rating_average=[0]
        os.chdir('..')
    average_all_female=[average_01[0],average_02[0],average_03[0],average_05[0],average_06[0],average_07[0],average_08[0],average_10[0],average_11[0],average_12[0],average_15[0],average_16[0]]
    average_all_male=[average_01[1],average_02[1],average_03[1],average_05[1],average_06[1],average_07[1],average_08[1],average_10[1],average_11[1],average_12[1],average_15[1],average_16[1]]
    average_all=[average_01[2],average_02[2],average_03[2],average_05[2],average_06[2],average_07[2],average_08[2],average_10[2],average_11[2],average_12[2],average_15[2],average_16[2]]
    picture(1,average_all_female)
    picture(2,average_all_male)
    picture(3,average_all)
    print("女生中颜值最高的是:%s,男生中颜值最高的是:%s" % (max_female_nuaaid,max_male_nuaaid))
