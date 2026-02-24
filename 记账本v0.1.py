record=[]
balance=0
print('欢迎使用记账本！\n请告诉我你的需求！')
while True:
    choice=input('1.查看余额，2.变更余额，3.退出')
    if choice=='1':
         print(balance)
    elif choice=='2':
        a=float(input('请输入变化金额，收入用正数，支出用负数'))
        balance=balance+a
    elif choice=='3':
        print('谢谢使用！')
        break
    else:
        print('错误！请重新输入！')