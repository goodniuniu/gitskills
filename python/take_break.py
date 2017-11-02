import webbrowser
import time
total_break_time = 3
break_time = 0
while break_time < total_break_time:
    print("the program starts at ", time.ctime())
    time.sleep(10)
    webbrowser.open("http://www.baidu.com")
    break_time = break_time+1
