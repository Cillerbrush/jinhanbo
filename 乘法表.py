# import random
# appetizer = ['话梅花生','拍黄瓜','凉拌三丝']
# def coupon(money):
#     if money < 5:
#         a = random.choice(appetizer)
#         return a
#     elif 5 <= money < 10:
#         b = random.choice (appetizer)
#         return b, '溏心蛋'
#
# result = coupon(6)
# print()
# a = '金汉博'
# b = '金十悦'
# print('我们家哥哥是:'+a,'我们家妹妹是'+b)
# print('我们家哥哥是{},我们家妹妹是{}'.format(a,b))bonus
import math


def estimated_time(size,number):
    time = size * 80 / number
    print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))


def estimated_number(size,time):
    number = math.ceil(size * 80 / time)
    print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number))


estimated_time(1.5,2)

estimated_number(1,60)