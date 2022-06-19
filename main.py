import shuma
import dazi
import hash
import datetime
import checkFile
import game
import pachong
import grammar

#由于在选择绘图程序显示进度条时使用双线程并行运行，所以导致重回菜单时无法回到主循环，再次画图将自动退出程序。
#若先进行除2以外选项则不会出现该问题。
def run():
    while(1):
        print(datetime.datetime.now().strftime('%Y年%m月%d日'))
        print('**************************************')
        print('现代编程技术课程作业')
        print('1.哈希函数')
        print('2.绘图程序')
        print('3.七段数码管显示')
        print('4.统计以上代码中各保留字个数')
        print('5.模拟游戏结果')
        print('6.爬取豆瓣电影前250名')
        print('7.检查文件中语法错误')
        print('8.结束')
        print('**************************************')
        choice=input('请选择->')
        if choice == '1':    
            hash.my_hash()
        elif choice == '2':
            dazi.dazi_main()
        elif choice == '3':
            shuma.pr()
        elif choice == '4':
            checkFile.getRetainword()
        elif choice == '5':
            game.game_main()
        elif choice == '6':
            pachong.main()
        elif choice == '7':
            grammar.grammarCheck()
        elif choice == '8':
            print("谢谢使用，下次再见")
            break
        else:
            print("输入无效，请重新选择")
            run()
run()

