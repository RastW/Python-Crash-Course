# ·检查两个字符串相等和不等。·使用函数lower()的测试。·检查两个数字相等、不等、大于、小于、大于等于和小于等于。·使用关键字and和or的测试。·测试特定的值是否包含在列表中。·测试特定的值是否未包含在列表中。
var = "true"
if var == "ture":
    print("A YES")

if var.lower() == "ture":
    print("B YES")

number = 10

if number > 5:
    print("C YES")
if number < 15:
    print("D YES")
if number == 10:
    print("E YES")
if number != 10:
    print("F YES")

if number == 11 or number ==10:
    print("1")

if number == 10 and number < 11:
    print("1")



list = {"1", "2", "3", "4"}

if "1" in list:
    print("111")

if "9" not in list:
    print("222")
