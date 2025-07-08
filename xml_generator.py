# * 是用來接收數量不定的參數
def func(*args):
    print(args)
a = 1
b = 2
c = 3
func(a, b, c) #(1, 2, 3)
# 可以看到個小缺點 : 看不到傳入參數的名稱 -> ** 可以解決 (dict 物件)
def func_v2(**kwargs):
    print(kwargs)
func_v2(a=1, b=2, c=3)

# xml generator
def myxml(tag, content = '', **kwargs):
    attr_list = []
    for key, value in kwargs.items():
        attr_list.append(f' {key}= "{value}"')
    attrs = ''.join(attr_list)
    return f'<{tag} {attrs}>{content}</{tag}>'
print(myxml('foo', 'bar', a = 1, b = 2, c = 3))
