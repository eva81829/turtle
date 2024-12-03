import turtle as t    # 匯入turtle套件，允許我們使用turtle指令

#畫筆速度(speed),畫筆粗細(pensize),畫筆顏色(color)
def pen_setting(speed,pensize,color):
    t.speed(speed) #1~10,1最慢
    t.pensize(pensize)
    t.pencolor(color)

def body():

    pen_setting(10,12,'black') 
    
    t.goto(0,0)
    t.penup()
    t.seth(90) #行走方向 
    t.fd(50) #行走距離
    t.seth(150)
    t.pendown()

    t.begin_fill()
    t.fillcolor('orange')

    #頭頂
    t.circle(120, 125) #半徑(像素),幾度
    
    #臉頰
    t.seth(220)
    t.circle(30,130)
    t.circle(200,15)
    #t.fd(30)

    #右手
    t.penup()
    t.seth(30)
    t.fd(50)
    t.pendown()
    t.seth(210)
    t.fd(20)
    t.seth(180)
    t.fd(20)
    t.circle(10,180)
    t.fd(10)
    t.circle(160,20)
    t.seth(30)
    t.circle(120,8)

    #肚子
    t.penup()
    t.seth(210)
    t.fd(15)
    t.pendown()
    t.seth(0)
    t.fd(120)
    
    #右腿
    t.penup()
    t.seth(120)
    t.fd(30)
    t.seth(270)
    t.pendown()
    t.circle(30,120)
    t.circle(-30,90)
    t.circle(10,180)
    t.fd(20)
    t.seth(135)
    t.fd(20)

    #屁股
    t.seth(80)
    t.circle(120,70)
    t.circle(100,50)

    #左手
    t.penup()
    t.goto(-195,-87)
    
    t.pendown()
    #t.done()
    t.fd(18)
    t.seth(200)

    t.circle(12,150)
    t.seth(15)
    t.fd(22)

    t.end_fill()


def spot1():
    #白點

    pen_setting(10,15,'white')

    t.penup()
    t.goto(-120,25)

    t.pendown()
    t.seth(30)
    t.fd(15)
    t.seth(215)
    t.fd(15)

    #白條
    pen_setting(10,12,'white')

    t.penup()
    t.goto(-75,40)
    t.seth(15)

    t.begin_fill()
    t.fillcolor('white')
    t.pendown()
    t.circle(-100,30)
    t.seth(325)
    t.circle(70,60)
    t.seth(200)
    pen_setting(10,18,'white')
    t.circle(-135,35)
    pen_setting(10,12,'white')
    t.seth(180)   
    t.circle(-135,20)
    t.end_fill()

def eye():
    pen_setting(10,15,'black') 

    t.penup()
    t.goto(-100,-45)

    t.pendown()
    t.seth(10)
    t.fd(10)
    t.seth(195)
    t.fd(10)

    t.penup()
    t.goto(-155,-65)
    t.pendown()
    t.seth(215)
    t.fd(10)
    t.seth(30)
    t.fd(10)

def mouse():
    pen_setting(10,10,'black')

    t.penup()
    t.goto(-145,-95)
    t.pendown()

    t.begin_fill()
    t.fillcolor('white')
    t.seth(20)
    t.fd(60)
    t.seth(132)
    t.circle(30,130)
    t.end_fill()

    t.penup()
    t.goto(-155,-87)
    t.seth(10)
    t.pendown()
    t.circle(-10,120)

def cloud():

    pen_setting(10,15,'black') 
    
    t.penup()
    t.goto(-180,-35)

    t.begin_fill()
    t.fillcolor('white')
    t.pendown()
    t.seth(180)
    t.circle(120, 40)
    t.circle(-80, 35)
    t.fd(60)
    t.seth(180)
    t.circle(90, 30)

    #最左
    t.circle(20, 140)
    t.seth(345)
    t.circle(150, 15)
    t.seth(353)
    t.fd(80)
    t.seth(345)
    t.circle(-40, 90)

    #最下
    t.circle(40, 90)
    t.seth(345)
    t.circle(200, 27)
    t.circle(200, 10)
    t.fd(130)

    #右半
    t.circle(-150, 40)
    t.circle(150, 50)
    t.circle(-150, 10)
    
    t.circle(-40, 43)
    t.seth(347)
    t.circle(90, 50)
    t.circle(30, 120)
    t.circle(80, 20)

    t.circle(-40, 70)
    t.circle(40, 40)
    #t.seth(347)
    t.circle(70, 10)
    t.circle(80, 30)
    t.circle(-100, 5)
    t.circle(-80, 20)
    t.circle(200, 20)
    
    t.end_fill()
    t.penup()

def spot2():
    pen_setting(10,10,'silver')

    #下面斑點
    t.penup()
    t.goto(-220,-180)
    t.pendown()

    t.begin_fill()
    t.fillcolor('silver')
    t.seth(270)
    t.circle(40, 90)
    t.seth(355)
    t.circle(200, 27)
    t.circle(200, 10)

    t.seth(170)
    t.circle(200, 30)

    t.seth(180)
    t.circle(-100, 30)
    t.goto(-220,-180)

    t.end_fill()

    #右邊斑點

    pen_setting(10,10,'silver')
    t.penup()

    t.begin_fill()
    t.goto(160,-165)
    t.pendown()
    
    t.seth(350)
    t.circle(100,40)

    t.fillcolor('silver')
    t.seth(40)
    pen_setting(10,10,'silver') 

    t.circle(-100,40)
    t.seth(340)
    t.circle(80,50)

    t.seth(160)
    t.circle(80,30)

    t.seth(175)
    t.circle(100,40)
  
    t.seth(228)
    t.circle(-100,60)
    t.goto(160,-165)    

    t.end_fill()

def main():
    t.hideturtle()
    t.setup(width=1.0, height=1.0) #畫布大小,全屏
    t.screensize(bg='dodgerblue') #畫布背景顏色

    #畫雲朵
    cloud()
    #畫身體
    body()
    #畫蛋黃光澤
    spot1()
    #畫眼睛
    eye()
    #畫嘴巴
    mouse()
    #畫蛋白光澤
    spot2()


    t.penup()
    t.goto(-450,165)   
    pen_setting(10,15,'black')
    t.write("不想上班   可是沒錢了...",font=("Arial", 65, "normal"))

    t.done()

if __name__ == '__main__':
    main()
