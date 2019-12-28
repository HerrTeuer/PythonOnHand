# 小结
# 正则表达式非常强大，要在短短的一节里讲完是不可能的。要讲清楚正则的所有内容，可以写一本厚厚的书了。如果你经常遇到正则表达式的问题，你可能需要一本正则表达式的参考书。

# 练习
# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：

# someone@gmail.com
# bill.gates@microsoft.com

# -*- coding: utf-8 -*-
import re

def is_valid_email(addr):
    if re.match(r'[a-zA-Z]+[.]*[a-zA-Z]*@(gmail|microsoft).com$',addr):
        return True
    else:
        return False
		


# 版本二可以提取出带名字的Email地址：

# <Tom Paris> tom@voyager.org => Tom Paris
# bob@example.com => bob

		
# -*- coding: utf-8 -*-
import re
def name_of_email(addr):
    n = re.match(r'([\s\S]+)@',addr)
    if n:
        m = re.match(r'<([\s\S]+)>',n.group(0))
        if m:
            return m.group(1)
        else:
            return n.group(1)
    else:
        return None