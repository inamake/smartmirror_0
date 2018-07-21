#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import time
import Tkinter as tk

while True:
    # weather hack から取得
    location_id = 280010  # 神戸
    weather_data = requests.get(
        'http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'
                % location_id).json()

    # openweathermap から取得　神戸
    weather_data_o = requests.get(
        'http://api.openweathermap.org/data/2.5/forecast?id=1859171&APPID=5d40a8867f1d56216e171cc23e068fef'
                        ).json()

    # weather hack からの情報 タイトル
    print '********************'
    T = weather_data['title']
    print T
    print '********************'
    # openweathermap からの情報　気温
    weatherli = weather_data_o['list']
    # 3時間毎の最高気温を24時間ぶん取得する
    # Kから℃　
    i = 0
    list01 = list()
    for li in weatherli:
            celsius = (li['main']['temp_max'] - 273.15)
            list01.append(int(celsius))
            if i > 6:
                    break
            i = i + 1
    hi = max(list01)
    lo = min(list01)
    df = hi - lo

    print ("最高気温:{0:>5} ℃". format(hi))
    print ("最低気温:{0:>5} ℃". format(lo))
    print ("寒暖差　:{0:>5} ℃". format(df))

    # weather hack からの情報 テキスト
    for forecast in weather_data['forecasts']:
        print '********************'
        print forecast['dateLabel']+'('+forecast['date']+')'
        print forecast['telop']
    dd0 = weather_data['forecasts'][0]['dateLabel']+'('+weather_data['forecasts'][0]['date']+')'
    dd1 = weather_data['forecasts'][1]['dateLabel']+'('+weather_data['forecasts'][1]['date']+')'
    #dd2 = weather_data['forecasts'][2]['dateLabel']+'('+weather_data['forecasts'][2]['date']+')'
    telo0 = weather_data['forecasts'][0]['telop']
    telo1 = weather_data['forecasts'][1]['telop']

    crip = weather_data['description']['text']
    #print crip


    print '**************************************************************'
    print "今日の服装"
    # 一日の最高気温から服装の基準を表示する
    if hi > 26 or hi == 26:
        print "夏日、半袖で大丈夫だが、朝晩の冷え込みに注意。"
    elif 21 < hi < 26 or hi == 21:
        print "快適、半袖と薄めの物を羽織ると良い。冷房による冷えに注意。"
    elif 16 < hi < 21 or hi == 16:
        print "涼しい。カーディガンやジャケット等を重ね着する。"
    elif 12 < hi < 16 or hi == 12:
        print "少し寒い。薄めのコート、ニット、セーター等"
    elif 7 < hi < 12 or hi == 7:
        print "冬本番、冬服にコート。風にも気を付ける。"
    elif hi < 7:
        print "本格的に寒い。インナーを変える、マフラーも必要。"

    if df > 10:
        print "朝晩の冷え込みが強い。着脱可能な上着が必要。"
    print '**************************************************************'

    #　ここからGUI Tkinter　でウィジェット作成
　　
    root = tk.Tk()
    root.geometry("2000x1200")
    root.title(T)
    canvas = tk.Canvas(root, width =2000, height =1200, bg="black")
    canvas.place(x = 0, y = 0)

    canvas.create_line(0, 75, 300, 75, fill="white", width=3,)

    #気温
    canvas.create_text(100, 100, text="最高気温：", fill="white", font=("Helvetica", 18))
    canvas.create_text(180, 140, text=hi, fill="white", font=("Helvetica", 28))
    canvas.create_text(250, 145, text="℃", fill="white", font=("Helvetica", 18))
    canvas.create_text(100, 180, text="最低気温：", fill="white", font=("Helvetica", 18))
    canvas.create_text(180, 220, text=lo, fill="white", font=("Helvetica", 28))
    canvas.create_text(250, 225, text="℃", fill="white", font=("Helvetica", 18))
    canvas.create_text(100, 260, text="寒暖差　：", fill="white", font=("Helvetica", 18))
    canvas.create_text(180, 300, text=df, fill="white", font=("Helvetica", 28))
    canvas.create_text(250, 305, text="℃", fill="white", font=("Helvetica", 18))

    canvas.create_line(0, 330, 300, 330, fill="white", width=3,)

    #テキスト
    canvas.create_text(420, 650, text=crip, fill="white", font=("Helvetica", 18))

    canvas.create_line(330, 75, 330, 330, fill="white", width=3,)

    canvas.create_line(360, 75, 700, 75, fill="white", width=3,)
    canvas.create_line(360, 330, 700, 330, fill="white", width=3,)


    #天気
    canvas.create_text(450, 100, text=dd0, fill="white", font=("Helvetica", 18))
    canvas.create_text(450, 220, text=dd1, fill="white", font=("Helvetica", 18))
    #canvas.create_text(200, 260, text=dd2, fill="white", font=("Helvetica", 18))
    canvas.create_text(600, 160, text=telo0, fill="white", font=("Helvetica", 28))
    canvas.create_text(600, 280, text=telo1, fill="white", font=("Helvetica", 28))

    #画像

    imgSH = 'imgSH.gif'
    imgSHT = 'imgSHT.gif'
    imgBE = 'imgBE.gif'
    imgCO = 'imgCO.gif'
    imgJT = 'imgJT.gif'
    imgNI = 'imgNI.gif'
    imSH = tk.PhotoImage(file = imgSH)
    imSHT = tk.PhotoImage(file = imgSHT)
    imBE = tk.PhotoImage(file = imgBE)
    imCO = tk.PhotoImage(file = imgCO)
    imJT = tk.PhotoImage(file = imgJT)
    imNI = tk.PhotoImage(file = imgNI)

　　# 一日の最高気温から服の画像を表示する
    if hi > 26 or hi == 26:
        canvas.create_image(1000, 200, image=imSHT)
        canvas.create_image(1500, 200, image=imSH)
    elif 21 < hi < 26 or hi == 21:
        canvas.create_image(1000, 200, image=imSHT)
        canvas.create_image(1500, 200, image=imJT)
    elif 16 < hi < 21 or hi == 16:
        canvas.create_image(1000, 200, image=imSH)
        canvas.create_image(1500, 200, image=imJT)
    elif 12 < hi < 16 or hi == 12:
        canvas.create_image(1000, 200, image=imSHT)
        canvas.create_image(1500, 200, image=imNI)
    elif 7 < hi < 12 or hi == 7:
        canvas.create_image(1000, 200, image=imSH)
        canvas.create_image(1500, 200, image=imCO)
    elif hi < 7:
        canvas.create_image(1000, 200, image=imNI)
        canvas.create_image(1500, 200, image=imCO)

    if df > 10:
        canvas.create_image(1050, 700, image=imBE)


    root.mainloop()


    time.sleep(1080)
