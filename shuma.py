
from cProfile import run
import turtle as t
import datetime as d
def drawgap(): #绘制数码管的间距
    t.penup()
    t.fd(95)
    t.right(90)
    t.fd(8)
def drawline(draw): #绘制单段数码管
    if draw:
        t.pendown()
        t.begin_fill()
        t.fd(83)
        t.right(45)
        t.fd(6)
        t.right(90)
        t.fd(6)
        t.right(45)
        t.fd(83)
        t.right(45)
        t.fd(6)
        t.right(90)
        t.fd(6)
        t.right(45)
        t.end_fill()
        drawgap()
    else:
        t.pendown()
        t.fd(83)
        t.right(45)
        t.fd(6)
        t.right(90)
        t.fd(6)
        t.right(45)
        t.fd(83)
        t.right(45)
        t.fd(6)
        t.right(90)
        t.fd(6)
        t.right(45)
        drawgap() 
def drawdigit(d): #根据数字绘制七段数码管
    drawline(True) if d in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if d in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if d in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if d in [0,2,6,8] else drawline(False)
    t.right(180)
    t.fd(8)
    t.right(90)
    t.fd(3)
    drawline(True) if d in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if d in[0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if d in[0,1,2,3,4,7,8,9] else drawline(False)
    t.right(180)
    t.fd(40)
    t.left(90)
    t.fd(4.5)
    t.right(90)
def drawdata(data):
    for x in data:
        drawdigit(eval(x))
def drawdate(date):
    t.color("black","black")
    for i in date:
        if i == '-':
            t.write('年',font=("Arial",18,"normal"))
            t.color("black","black")
            t.fd(40)
        elif i =='=':
            t.write('月',font=("Arial",18,"normal"))
            t.color("black","black")
            t.fd(40)
        elif i=='+':
            t.write('日',font=("Arial",18,"normal"))
        else:
            drawdigit(eval(i))
def pr():
    print("请选择以下功能")
    print("1.当前日期")
    print("2.显示输入的数据")
    print("3.返回上一级")
    try:
        a=eval(input("请选择："))
        if a==1:
            t.setup(1000.1000,0,0)
            t.speed(50)
            t.penup()
            t.bk(500)
            drawdate(d.datetime.now().strftime('%Y-%m=%d+'))
        elif a==2:
            b=input ("请输入数据：")
            t.setup(1000.1000,0,0)
            t.speed(50)
            t.penup()
            t.bk(500)
            drawdata(b)
        elif a==3:
            return()
    except:
        print("输入异常")
        pr()
def shuma_main():
    pr()
    t.done()
if __name__ == '__main__':
    shuma_main()





            




