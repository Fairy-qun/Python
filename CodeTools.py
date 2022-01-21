#创建一个空列表记录信息
card_list = []
def showmeun():
    print("*" *50)
    print("欢迎使用名片管理系统 v1.0".center(50))
    print("*" *50)
    print("【1】新增名片")
    print("【2】显示全部名片")
    print("【3】查询名片")
    print("")
    print("【0】退出程序")
    print("*" *50)

def new_card():
    """新增名片"""
    print("-" *50)
    print("新增名片")
    print("-" *50)

    #1.提示用户输入名片的详细信息
    name = input("请输入姓名: ")
    phone = input("请输入电话号码: ")
    qq = input("请输入qq号码：")
    email = input("请输入邮箱：")
    #2.使用用户输入的信息建立一个名片字典
    card_dict = {
        "name": name,
        "phone": phone,
        "QQ": qq,
        "email": email
    }
    #3.将名片字典添加到列表中
    card_list.append(card_dict)
    #4.提示用户添加成功
    print("添加用户名片信息成功！")

def show_all():
    """显示所有名片"""
    print("-" *50)
    print("显示所有名片")
    print("-" *50)

    #判断列表是否有数据
    if len(card_list) == 0:
        print("当前没有任何数据，请使用新增功能！")
        return
    #打印表头
    for table in ["姓名","电话","QQ","邮箱"]:
        print(table,end="\t\t")
    print("")
    print("=" *50)
    for card_lists in card_list:
        print("{}\t{}\t{}\t{}".format(card_lists["name"],card_lists["phone"],
                                            card_lists["QQ"],card_lists["email"]))
        print("=" *50)
def search_card():
    """搜索名片"""
    print("-" *50)
    print("搜索名片")
    print("-" *50)

    #1.提示用户输入需要搜索的姓名
    search_name = input("请输入需要查询的姓名：")
    #2.遍历名片列表，查询要搜索的姓名，若没有找到，需要提示用户
    for card_dict in card_list:
        # print(card_dict)
        if card_dict["name"] == search_name:
            print("查找成功！信息如下：")

            #打印表头
            print("-" *50)
            for table in ["姓名","电话","QQ","邮箱"]:
                print(table,end="\t\t")
            print("")
            print("=" *50)
            print("{}\t{}\t{}\t{}".format(card_dict["name"],card_dict["phone"],
                                          card_dict["QQ"],card_dict["email"]))
            print("=" *50)

            #针对找到的名片记录作修改和删除操作
            deal_card(card_dict)

            return

    else:
        print("抱歉，该系统中没有{}的信息!".format(search_name))


def deal_card(find_card):
    """
    处理用户查找的名片
    :param find_card:   用户查找的名片信息
    """
    # print(find_card)
    action_str = input("请选择需要执行的操作 "
                       "[1]/修改 [2]/删除 [0]/返回上级菜单: ")

    if action_str == "1":
        print("*" *50)
        print("请输入更改信息".center(50))
        print("*" *50)
        find_card["name"] = input_card_info(find_card["name"],"姓名【若回车即为不修改】：")
        find_card["phone"] = input_card_info(find_card["phone"],"电话号码【若回车即为不修改】：")
        find_card["QQ"] = input_card_info(find_card["QQ"],"QQ【若回车即为不修改】: ")
        find_card["email"] = input_card_info(find_card["email"],"邮箱【若回车即为不修改】：")
        print("修改名片名片成功！")
    elif action_str == "2":
        card_list.remove(find_card)
        print("删除名片成功！")


def input_card_info(dict_value,tip_message):
    """
    处理用户修改的名片信息
    :param dict_value: 字典原有的值
    :param tip_message: 用户输入的信息
    :return: 如果用户输入有数据，则直接返回用户输入的数据，若用户没有输入数据，则返回字典中原有的数据
    """
    #1.提示用户输入信息
    reslut_str = input(tip_message)

    #2.针对用户输入进行判断，如果用户输入了内容，直接返回结果
    if len(reslut_str) > 0:
        return reslut_str
    #3.如果用户没有输入信息，则返回字典中原有的数据
    else:
        return dict_value