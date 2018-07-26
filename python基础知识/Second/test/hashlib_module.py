'''
知识基础
>>>hash(zhangchuhan.json)
-3787897092370505053
不可逆

MD5算法
m.update(
m.hexdigest(

>>> m = hashlib.md5()
>>> m.update(zhangchuhan.json)
>>> m.hexdigest()
'bf7f2130d2dc6f6f2145ac20a26c756f'

>>> m1 = hashlib.sha1()
>>> m.update(zhangchuhan.json)
>>> m.hexdigest()
'fad98261fdf56cfd76be5d94d0231eb7'
'''
