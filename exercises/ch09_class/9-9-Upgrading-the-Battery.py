# Upgrading the Battery（电池升级示例）

# ---------------------------
# 基础类：Car（汽车）
# ---------------------------
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        # 以下属性属于“每一辆具体汽车”，因此使用 self 存储在对象内部
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 里程表初始为 0

    def get_descriptive_name(self):
        # 返回汽车的完整描述信息
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        # 输出当前里程
        print(f"This car has {self.odometer_reading} miles on it.")


# ---------------------------
# 子类：ElectricCar（电动车）
# ---------------------------
class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        # 先调用父类初始化方法，建立“汽车”的基础属性
        super().__init__(make, model, year)

        # 再添加电动车特有属性
        # 这里不是存一个数值，而是创建一个 Battery 对象
        # 表示“电动车包含一个电池”
        self.battery = Batterys(80)  # 初始电池容量设为 80


# ---------------------------
# 独立类：Batterys（电池）
# ---------------------------
class Batterys:
    def __init__(self, battery):
        # 电池容量（kWh）
        self.battery = battery

    def upgrade_battery(self):
        """
        将电池升级到 85（如果当前不是 85）
        """
        if self.battery != 85:
            self.battery = 85  # 升级
        # 如果已经是 85，则保持不变（这里省略 else）

        # 输出当前电池容量
        print(self.battery)


# ---------------------------
# 创建对象并调用方法
# ---------------------------

# 创建一辆电动车对象
my_tesla = ElectricCar("tesla", "model", 2016)

# 调用电池对象的方法（注意：battery 是对象，不是函数）
# 所以要通过 “对象.属性.方法” 的形式调用
my_tesla.battery.upgrade_battery()
