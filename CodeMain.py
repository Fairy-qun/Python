#导入工具包
import CodeTools
while True:
    # 显示系统菜单
    #导入方法
    CodeTools.showmeun()
    action_str = input("请输入你选择的选项：")
    print("你选择的是【{}】".format(action_str))

    if action_str in ["1","2","3"]:
        #增加名片
        if action_str == "1":
            CodeTools.new_card()
        #显示所有名片
        elif action_str == "2":
            CodeTools.show_all()
        #查询名片
        elif action_str == "3":
            CodeTools.search_card()
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print("输入有错误，请重新输入！")