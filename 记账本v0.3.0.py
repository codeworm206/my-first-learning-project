import datetime
balance=0   #余额
add_history=[]  #历史记录
def print_history():
    if not add_history:
        print('无历史记录！')
    else:
        print('\n历史记录：')
        print('='*60)
        for i,record in enumerate(add_history,1):
            time=record['时间'].strftime('%Y-%m-%d %H-%M-%S')
            amount=record['变动金额']
            typee=record['类别']
            note=record['备注']
            print(f'时间：{time}\n变动金额：{amount}\n类别：{typee}\n备注：{note}')
            print('='*60)
    return None
def change_amount():
    while True:
        try:
            value=float(input('请输入变化金额，收入用正数，支出用负数'))
            return value
        except ValueError:
            print('请输入数字')
def typ():
    while True:
        verify=input('请输入类别').strip()
        if verify:
            return verify
        print('请输入有效的字符')
print('欢迎使用记账本！\n请告诉我你的需求！')
while True:
    choice=input('1.查看余额，2.变更余额，3.查询历史记录，4.退出')
    if choice=='1':
        print(balance)
    elif choice=='2':
        change_amo=change_amount()
        balance=balance+change_amo
        ty=typ()
        note=input('请输入备注（可选）')
        record={'变动金额':change_amo,
                '类别':ty,
                '备注':note,
                '时间':datetime.datetime.now()}
        add_history.append(record)
    elif choice=='3':
        print_history()
    elif choice=='4':
        print('谢谢使用！')
        break
    else:
        print('错误！请重新输入！')