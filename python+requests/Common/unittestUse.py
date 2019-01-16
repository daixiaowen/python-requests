# encoding=utf-8
# __author__=zhangxiang


'''
使用unittest框架有3种方式
    1、通过unittest.main()来执行测试用例的方式；
    2、通过testsuit来执行测试用例的方式；
    3、通过测试类加载器testLoader方式；
'''

# 1、通过unittest.main()来执行测试用例的方式：
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        # 测试前需执行的操作
        pass

    def tearDown(self):
        # 测试用例执行完成后所需要执行的操作
        pass

    # 测试用例1
    def test01(self):
        # 具体的测试脚本
        pass

    # 测试用例02
    def test02(self):
        # 具体的测试脚本
        pass


if __name__ == "__main__":
    unittest.main()

# 2、通过testsuit来执行测试用例的方式；
import unittest


# 执行测试的类：以登录为例
class TestLogin(unittest.TestCase):
    def setUp(self):
        # 测试前需执行的操作
        pass

    def tearDown(self):
        # 测试用例执行完成后所需要执行的操作
        pass

    # 测试用例1
    def test01(self):
        # 具体的测试脚本
        pass

    # 测试用例02
    def test02(self):
        # 具体的测试脚本
        pass


if __name__ == "__main__":
    # 构造测试集,通过suit.addTest(类名("测试用例名"))添加测试用例,此种方式有弊端需要把所有测试用例都加到测试集里，如果测试用例过多1000条操作起来会很麻烦，可以优化；
    suit = unittest.TestSuite()
    suit.addTest(TestLogin("test01"))
    suit.addTest(TestLogin("test02"))
    # 初始化执行器，执行测试；
    runner = unittest.TextTestRunner()
    runner.run(suit)

# 3、通过testLoader测试类加载器的方式可以同时测试多各类：
import unittest


class TestCase01(unittest.TestCase):
    def setUp(self):
        # 测试前需执行的操作
        pass

    def tearDown(self):
        # 测试用例执行完成后所需要执行的操作
        pass

    # 测试用例1
    def test01(self):
        # 具体的测试脚本
        pass

    # 测试用例02
    def test02(self):
        # 具体的测试脚本
        pass


class TestCase02(unittest.TestCase):
    def setUp(self):
        # 测试前需执行的操作
        pass

    def tearDown(self):
        # 测试用例执行完成后所需要执行的操作
        pass

    # 测试用例1
    def test01(self):
        # 具体的测试脚本
        pass

    # 测试用例02
    def test02(self):
        # 具体的测试脚本
        pass


if __name__ == "__main__":
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCase01)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCase02)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
