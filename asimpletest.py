# @Time : 2020.10.14
# @Author : LeeWJ
# @Function  :  测试
# @Version  : 1.0

def do_test(param):
    #清除0，1
    if 0 in param:
        param.remove(0)
    if 1 in param:
        param.remove(1)
    #输入列表的长度
    param_length = len(param)
    #初始化输出字符串
    result_str = ''
    telephone_map = {
        0:'',
        1:'',
        2:'abc',
        3:'def',
        4:'ghi',
        5:'jkl',
        6:'mno',
        7:'pqrs',
        8:'tuv',
        9:'wxyz'
    }

    #递归组合字母
    def combine(param,combine_char='',flag=0):
        nonlocal result_str
        #如果标记等于list长度，则递归结束
        if flag == param_length:
            result_str = f'{result_str}{combine_char} '
            return 1
        character = telephone_map[param[flag]]
        #移动到用户输入的下一位数字
        flag += 1
        #遍历数字对应的字母
        for i in range(len(character)):
            combine(param,f'{combine_char}{character[i]}',flag)

    combine(param)

    return result_str

if __name__ == '__main__':
    user_input = [2,3]
    print(do_test(user_input))
    user_input = [9]
    print(do_test(user_input))
    user_input = [9,9]
    print(do_test(user_input))
    user_input = [5,7]
    print(do_test(user_input))
    user_input = [0,3]
    print(do_test(user_input))
    user_input = [1,3]
    print(do_test(user_input))
    user_input = [0,0]
    print(do_test(user_input))

# 运行结果：
# ad ae af bd be bf cd ce cf
# w x y z
# ww wx wy wz xw xx xy xz yw yx yy yz zw zx zy zz
# jp jq jr js kp kq kr ks lp lq lr ls
# d e f
# d e f
#