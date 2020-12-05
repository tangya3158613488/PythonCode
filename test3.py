f = open("itheima.txt", "r")
str = f.read(4)
print("读取的数据是:", str)
position = f.tell()
print("当前文件位置:", position)
