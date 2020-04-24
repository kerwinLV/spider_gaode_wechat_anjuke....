import sys

class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger(r"C:\kerwin\workspace\requestpro\log.txt")
a = "['所属小区', '巨杨小区', '房屋户型', '2室', '1厅', '1卫', '房屋单价', '73108', '元/m²', '所在位置', '浦东新区－', '洋泾－', '沈家弄路901弄', '\ue003', '建筑面积', '54平方米'"
print(a.encode("gb18030"))
