import datetime
balance=0   #余额
add_history=[]  #历史记录
def print_history():
    if not add_history:
        print('无历史记录！')
    else:
        print('历史记录：',add_history)
    return None
print('欢迎使用记账本！\n请告诉我你的需求！')
while True:
    choice=input('1.查看余额，2.变更余额，3.查询历史记录，4.退出')
    if choice=='1':
        print(balance)
    elif choice=='2':
        change_amount=float(input('请输入变化金额，收入用正数，支出用负数'))
        balance=balance+change_amount
        type=input("请输入收入/支出类别（如餐饮，工资）")
        note=input('请输入备注（可选）')
        record={'变动金额':change_amount,
                '类别':type,
                '备注':note,
                'time':datetime.datetime.now()}
        add_history.append(record)
    elif choice=='3':
        print_history()
    elif choice=='4':
        print('谢谢使用！')
        break
    else:
        print('错误！请重新输入！')