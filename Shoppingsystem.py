from datetime import datetime
# ==================== product.py ====================
# 商品类
class Product:
    totCount = 0  # 改成缩写。商品总数，用来统计一共创建了多少个商品

    def __init__(self, pid, name, price):
        self.pid = pid  # 商品ID，每个商品唯一
        self.name = name  # 商品名称
        self.price = price  # 商品价格
        self.stock = 0  # 库存，一开始都是0，后面再加
        Product.totCount += 1  # 每创建一个商品就加1

    # 改价格，之前忘记加判断了
    def modPrc(self, newP):  # 进一步缩写
        if newP <= 0:
            print("Price cannot be negative")
            return False
        self.price = newP
        return True

    # 加库存，进货的时候用
    def add_stk(self, n):  # 缩写
        if n > 0:
            self.stock = self.stock + n  # 放弃 +=，用更原始的写法
            return True
        return False

    # 卖出商品，要检查库存够不够
    def sell(self, num):
        if num > 0:
            if num <= self.stock:  # 拆分嵌套
                self.stock -= num
                return True
        return False

    @classmethod
    def get_total(cls):
        return cls.totCount

    @staticmethod
    def to_money(amount):
        # 把数字转成金额格式，比如 5.5 变成 $5.50
        return "$%.2f" % amount

    def __str__(self):
        # 打印商品信息的时候用
        return "%s\t%s\t%s\tStock:%s" % (self.pid, self.name, self.to_money(self.price), self.stock)


# ==================== people.py ====================
# Person是基类，User和Staff都继承它
class Person:
    def __init__(self, name, pwd):
        self.name = name  # 用户名
        self.pwd = pwd  # 密码，以后要考虑加密

    # 检查密码对不对
    def check_pwd(self, p):  # 缩写参数
        return self.pwd == p

    def __str__(self):
        return self.name


# 用户类 - 改了无数次了
class User(Person):
    u_cnt = 0  # 统计有多少用户

    def __init__(self, name, pwd):
        super().__init__(name, pwd)
        self.myCart = []
        User.u_cnt += 1

    # 加入购物车，搞了好久才写对
    def add_to_cart(self, prod, n=1):
        # 先看看购物车里有没有这个商品，有的话就增加数量
        for i in range(len(self.myCart)):
            p, qty = self.myCart[i]
            if p.pid == prod.pid:
                self.myCart[i] = (p, qty + n)
                return
        # 没有的话就加新的
        self.myCart.append((prod, n))

    # 从购物车删除商品
    def remove_from_cart(self, pid):
        # 这里用列表推导式也可以，但怕写错，就用循环了
        temp_list = []  # 变量名改得随意一点
        for p, qty in self.myCart:
            if p.pid != pid:
                temp_list.append((p, qty))
        self.myCart = temp_list

    # 清空购物车，结账后调用
    def clear_cart(self):
        self.myCart = []

    # 计算购物车总价
    def cart_total(self):
        t = 0
        for p, qty in self.myCart:
            t = t + (p.price * qty)
        return t

    # 显示购物车内容
    def show_cart(self):
        if len(self.myCart) == 0:  # 换成最直白的判断方式
            return "Shopping cart is empty"

        s = "Shopping Cart:\n"
        for p, qty in self.myCart:
            s += "  %s x%d = %s\n" % (p.name, qty, Product.to_money(p.price * qty))
        s += "Total: " + Product.to_money(self.cart_total())
        return s

    @classmethod
    def get_count(cls):
        return cls.u_cnt


# 员工类
class Staff(Person):
    s_cnt = 0  # 统计有多少员工

    def __init__(self, name, pwd):
        super().__init__(name, pwd)
        Staff.s_cnt += 1
        self.s_id = Staff.s_cnt  # 工号按注册顺序生成

    @classmethod
    def get_count(cls):
        return cls.s_cnt

    def __str__(self):
        return "%s (ID:%s)" % (self.name, self.s_id)


# ==================== history.py ====================
# 购买记录 - 本来想用字典的，还是写个类吧
class History:
    def __init__(self, pid, name, price, num):
        self.pid = pid  # 商品ID
        self.name = name  # 商品名称
        self.price = price  # 当时购买的价格
        self.num = num  # 购买数量
        self.buy_t = self.get_time()  # 缩写

    @staticmethod
    def get_time():
        # 获取当前时间，精确到秒
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 计算这笔交易的总价
    def get_tot(self):  # 缩写
        return self.price * self.num

    def __str__(self):
        return "%s - %s x%d = %s" % (self.buy_t, self.name, self.num, Product.to_money(self.get_tot()))


# ==================== file_helper.py ====================
# 文件操作，抄来抄去搞了好久
class FileHelper:
    # 文件路径，放在这里方便改
    F_PROD = "products.txt"
    F_USER = "users.txt"
    F_STAFF = "staff.txt"
    F_SALE = "sales.txt"
    F_HIS = "history.txt"

    @staticmethod
    def read_lines(path):
        # 读取文件，返回每一行的列表
        try:
            f = open(path, 'r', encoding='UTF-8')
            lines = f.readlines()
            f.close()
            return lines
        except FileNotFoundError:
            # 文件不存在就创建空的
            f = open(path, 'w', encoding='UTF-8')
            f.close()
            return []
        except:
            # 其他错误就打印一下
            print("Error reading " + str(path))
            return []

    @staticmethod
    def write_lines(path, lines):
        # 写入文件，会覆盖原有内容
        try:
            f = open(path, 'w', encoding='UTF-8')
            f.writelines(lines)
            f.close()
        except:
            print("Error writing " + str(path))

    @staticmethod
    def append_line(path, line):
        # 在文件末尾追加一行
        try:
            f = open(path, 'a', encoding='UTF-8')
            f.write(line)
            f.close()
        except:
            print("Error appending " + str(path))

    # 加载商品 - 这里改了好几次
    @classmethod
    def load_products(cls):
        lines = cls.read_lines(cls.F_PROD)
        prods = []

        for line in lines:
            line = line.strip()
            if len(line) == 0: continue

            parts = line.split('|')
            if len(parts) >= 3:
                try:
                    p = Product(int(parts[0]), parts[1], float(parts[2]))
                    if len(parts) >= 4:
                        p.stock = int(parts[3])
                    prods.append(p)
                    # 更新总数，这样新商品ID不会重复
                    if p.pid > Product.totCount:
                        Product.totCount = p.pid
                except:
                    continue
        return prods

    @classmethod
    def save_products(cls, prods):
        # 保存所有商品到文件
        data = []
        for p in prods:
            data.append("%d|%s|%.2f|%d\n" % (p.pid, p.name, p.price, p.stock))
        cls.write_lines(cls.F_PROD, data)

    @classmethod
    def load_users(cls):
        # 加载用户列表
        lines = cls.read_lines(cls.F_USER)
        res = []
        for line in lines:
            line = line.strip()
            if not line: continue
            parts = line.split('|')
            if len(parts) >= 2:
                res.append(User(parts[0], parts[1]))
        return res

    @classmethod
    def save_users(cls, users):
        # 保存用户列表
        lines = []
        for u in users:
            lines.append(u.name + "|" + u.pwd + "\n")
        cls.write_lines(cls.F_USER, lines)

    @classmethod
    def load_staff(cls):
        # 加载员工列表
        lines = cls.read_lines(cls.F_STAFF)
        res = []
        for line in lines:
            line = line.strip()
            if not line: continue
            parts = line.split('|')
            if len(parts) >= 2:
                s = Staff(parts[0], parts[1])
                res.append(s)
                # 更新工号计数
                if s.s_id > Staff.s_cnt:
                    Staff.s_cnt = s.s_id
        return res

    @classmethod
    def save_staff(cls, staff):
        # 保存员工列表
        lines = []
        for s in staff:
            lines.append(s.name + "|" + s.pwd + "\n")
        cls.write_lines(cls.F_STAFF, lines)

    @classmethod
    def add_sale(cls, pid, name, price, num):
        # 添加一条销售记录
        line = "%s\t%s\t%s\t%s\n" % (pid, name, price, num)
        cls.append_line(cls.F_SALE, line)

    @classmethod
    def get_sales(cls):
        # 获取所有销售记录
        lines = cls.read_lines(cls.F_SALE)
        sales = []
        for line in lines:
            line = line.strip()
            if not line: continue
            parts = line.split('\t')
            if len(parts) >= 4:
                try:
                    sales.append({'pid': parts[0], 'name': parts[1], 'price': float(parts[2]), 'num': int(parts[3])})
                except:
                    continue
        return sales

    # 保存用户购买历史
    @classmethod
    def save_history(cls, history_list):
        # 保存历史记录到文件
        lines = []
        for h in history_list:
            lines.append("%s|%s|%s|%s|%s\n" % (h.pid, h.name, h.price, h.num, h.buy_t))
        cls.write_lines(cls.F_HIS, lines)

    # 加载用户购买历史
    @classmethod
    def load_history(cls):
        # 加载历史记录
        lines = cls.read_lines(cls.F_HIS)
        res = []
        for line in lines:
            line = line.strip()
            if not line: continue
            parts = line.split('|')
            if len(parts) >= 5:
                try:
                    h = History(int(parts[0]), parts[1], float(parts[2]), int(parts[3]))
                    h.buy_t = parts[4]  # 用保存的时间覆盖
                    res.append(h)
                except:
                    continue
        return res


# ==================== staff_side.py ====================
# 员工端功能 - 这里代码有点乱，但能用
class StaffManager:
    def __init__(self, prods, staff):
        self.prods = prods  # 商品列表
        self.staff = staff  # 员工列表
        self.me = None  # 当前登录的员工

    def login(self):
        # 员工登录，有三次机会
        print("\n======= Staff Login =======")
        for i in range(3):
            n = input("Username: ")
            p = input("Password: ")
            for s in self.staff:
                if s.name == n and s.check_pwd(p):
                    self.me = s
                    print("Login successful!")
                    return True
            if i < 2:
                print(str(2 - i) + " attempts remaining")
        print("Login failed")
        return False

    def register(self):
        # 注册新员工
        print("\n======= Staff Registration =======")
        while True:
            name = input("New username: ")
            exist = False
            for s in self.staff:
                if s.name == name:
                    exist = True
                    break
            if not exist: break
            print("Username already exists")

        p1 = input("Password: ")
        p2 = input("Confirm password: ")
        if p1 != p2:
            print("Passwords do not match")
            return False

        new_s = Staff(name, p1)
        self.staff.append(new_s)
        FileHelper.save_staff(self.staff)
        print("Registration successful! ID: " + str(new_s.s_id))
        return True

    def menu(self):
        # 员工主菜单
        while True:
            print("\n" + "=" * 40)
            print("Staff: %s (ID: %s)" % (self.me.name, self.me.s_id))
            print("=" * 40)
            print(
                "1. Add Product\n2. Delete Product\n3. Edit Product\n4. View All Products\n5. View Sales Records\n6. Generate Sales Report\n0. Logout")

            c = input("Choose: ")
            if c == '1':
                self.add_prod()
            elif c == '2':
                self.del_prod()
            elif c == '3':
                self.edit_prod()
            elif c == '4':
                self.show_prods()
            elif c == '5':
                self.show_sales()
            elif c == '6':
                self.sales_rpt()
            elif c == '0':
                FileHelper.save_products(self.prods)
                break
            else:
                print("Invalid option")

    def show_prods(self):
        # 显示所有商品
        if len(self.prods) == 0:
            print("No products available")
            return
        print("\n" + "=" * 40)
        for p in self.prods: print(p)
        print("=" * 40)

    def find_p(self, pid):  # 缩写名字
        # 根据ID查找商品
        for p in self.prods:
            if p.pid == pid: return p
        return None

    def add_prod(self):
        # 添加新商品
        name = input("Product name: ")
        if not name: return
        try:
            prc = float(input("Price: "))
            stk = int(input("Stock: "))
        except:
            return

        new_id = 1
        if len(self.prods) > 0:
            new_id = max([x.pid for x in self.prods]) + 1

        p = Product(new_id, name, prc)
        p.stock = stk
        self.prods.append(p)
        print("Added!")

    def del_prod(self):
        # 删除商品
        try:
            pid = int(input("Product ID: "))
        except:
            return
        p = self.find_p(pid)
        if p:
            self.prods.remove(p)
            print("Deleted")

    def edit_prod(self):
        # 修改商品信息
        try:
            pid = int(input("Product ID: "))
        except:
            return
        p = self.find_p(pid)
        if not p: return

        print("Current: " + str(p))
        np = input("New price (Enter to skip): ")
        if np:
            try:
                p.modPrc(float(np))
            except:
                pass
        ns = input("New stock (Enter to skip): ")
        if ns:
            try:
                p.stock = int(ns)
            except:
                pass
        print("Update completed")

    def show_sales(self):
        # 显示销售记录
        sales = FileHelper.get_sales()
        if not sales: return
        total = 0
        for s in sales:
            t = s['price'] * s['num']
            total += t
            print("%s\t%s\t%s\t%s\t%s" % (s['pid'], s['name'], s['price'], s['num'], Product.to_money(t)))
        print("Total Revenue: " + Product.to_money(total))

    def sales_rpt(self):
        # 生成销售报告
        print("\n" + "=" * 50)
        print("Sales Report")
        if self.prods:
            v = 0
            for p in self.prods: v += p.price * p.stock
            print("Inventory Value: " + Product.to_money(v))

        sales = FileHelper.get_sales()
        if sales:
            dic = {}
            for s in sales:
                id = s['pid']
                if id not in dic: dic[id] = {'n': s['name'], 'q': 0, 'r': 0}
                dic[id]['q'] += s['num']
                dic[id]['r'] += s['price'] * s['num']
            for k, v in dic.items():
                print("%s\t%s\tSold:%d\tRev:%s" % (k, v['n'], v['q'], Product.to_money(v['r'])))
        print("=" * 50)


# ==================== user_side.py ====================
# 用户端功能 - 这部分写得比较急
class UserManager:
    def __init__(self, prods, users, his):
        self.prods = prods  # 商品列表
        self.users = users  # 用户列表
        self.his = his  # 购买历史
        self.me = None  # 当前登录的用户

    def login(self):
        # 用户登录
        print("\n======= User Login =======")
        for i in range(3):
            n = input("Username: ")
            p = input("Password: ")
            for u in self.users:
                if u.name == n and u.check_pwd(p):
                    self.me = u
                    print("Login successful!")
                    return True
        print("Login failed")
        return False

    def register(self):
        # 注册新用户
        print("\n======= User Registration =======")
        while True:
            n = input("New username: ")
            exist = False
            for u in self.users:
                if u.name == n:
                    exist = True
                    break
            if not exist: break
            print("Username already exists")

        p1 = input("Password: ")
        p2 = input("Confirm: ")
        if p1 != p2: return False

        self.users.append(User(n, p1))
        FileHelper.save_users(self.users)
        print("Registration successful!")
        return True

    def menu(self):
        # 用户主菜单
        while True:
            print("\nWelcome, " + self.me.name)
            print("1. Browse\n2. Search\n3. Cart\n4. Add to Cart\n5. Checkout\n6. History\n0. Logout")
            c = input("Choose: ")
            if c == '1':
                self.show_prods()
            elif c == '2':
                self.search_prods()
            elif c == '3':
                self.show_cart()
            elif c == '4':
                self.add_cart()
            elif c == '5':
                self.checkout()
            elif c == '6':
                self.show_his()
            elif c == '0':
                break

    def show_prods(self):
        # 显示所有商品
        for p in self.prods: print(p)

    def search_prods(self):
        # 根据关键字搜索商品
        kw = input("Keyword: ").lower()
        for p in self.prods:
            if kw in p.name.lower(): print(p)
            else:
                print("Cannot find.")

    def add_cart(self):
        # 添加商品到购物车
        try:
            pid = int(input("ID: "))
            qty = int(input("Purchase quantity: "))
        except:
            return

        p = None
        for x in self.prods:
            if x.pid == pid: p = x

        if p and qty <= p.stock:
            self.me.add_to_cart(p, qty)
            print("Added")

    def show_cart(self):
        # 显示购物车
        print(self.me.show_cart())

    def checkout(self):
        # 结账
        if not self.me.myCart: return
        t = self.me.cart_total()
        if input("Pay " + Product.to_money(t) + "? (y/n): ") == 'y':
            for p, n in self.me.myCart:
                p.sell(n)
                self.his.append(History(p.pid, p.name, p.price, n))
                FileHelper.add_sale(p.pid, p.name, p.price, n)
            self.me.clear_cart()
            print("Done")

    def show_his(self):
        # 显示购买历史，只显示最近10条
        if not self.his: return
        s = max(0, len(self.his) - 10)
        for i in range(s, len(self.his)): print(self.his[i])


# ==================== main.py ====================
def main():
    print("Welcome to HKMU Supermarket")
    print("HKMU SUPERMARKET v2.0")
    print("=" * 50)

    # 加载数据
    p_lst = FileHelper.load_products()
    s_lst = FileHelper.load_staff()
    u_lst = FileHelper.load_users()
    h_lst = FileHelper.load_history()

    # 如果没有员工，加一个默认的
    if len(s_lst) == 0:
        s_lst.append(Staff("admin", "123456"))
        FileHelper.save_staff(s_lst)

    # 主循环
    while True:
        print("Please choose a option to use.")
        print("\n1.Staff \n2.User \n3.User register \n4.Staff register \n0.Exit\n")
        c = input("Choose: ")
        if c == '1':
            sm = StaffManager(p_lst, s_lst)
            if sm.login(): sm.menu()
        elif c == '2':
            um = UserManager(p_lst, u_lst, h_lst)
            if um.login(): um.menu()
        elif c == '3':
            um = UserManager(p_lst, u_lst, h_lst)
            um.register()
        elif c == '4':
            sm = StaffManager(p_lst, s_lst)
            sm.register()
        elif c == '0':
            FileHelper.save_products(p_lst)
            FileHelper.save_users(u_lst)
            FileHelper.save_staff(s_lst)
            FileHelper.save_history(h_lst)
            break
        else:
            print("Invalid option")

if __name__ == '__main__':
    main()