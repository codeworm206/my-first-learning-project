balance=0
add_history=[]
def history_list(amount):
    global add_history
    add_history.append(amount)
    return add_history
print('欢迎使用记账本！\n请告诉我你的需求！')
while True:
    choice=input('1.查看余额，2.变更余额，3.查询历史记录，4.退出')
    if choice=='1':
        print(balance)
    elif choice=='2':
        ab=float(input('请输入变化金额，收入用正数，支出用负数'))
        balance=balance+ab
        add_history.append(ab)
    elif choice=='3':
        def print_history():
            global add_history
            if not add_history:
                print('无历史记录')
            else:
                print('历史记录：')
                for i, amount in enumerate(add_history, 1):
                    print(f'{i},{amount}')
            return None
        print_history()
    elif choice=='4':
        print('谢谢使用！')
        break
    else:
        print('错误！请重新输入！')