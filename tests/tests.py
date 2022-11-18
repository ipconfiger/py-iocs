import unittest


class InnerClass(object):
    def __init__(self, msg):
        self.msg = msg

    def show(self):
        print("msg:", self.msg)


class OuterClass(object):
    def __init__(self):
        self.inner = None


class MyTestCase(unittest.TestCase):
    def test_something(self):
        from iocs import IocContainer
        container: IocContainer = IocContainer()
        msg = "哈哈哈"
        container.update_dependencies(inner=InnerClass(msg))

        def get_outer(deps):
            ins = OuterClass()
            ins.inner = deps.get('inner')
            return ins

        container.regist_classes(OuterClass, get_outer)

        ot: OuterClass = container(OuterClass)
        ot.inner.show()
        self.assertEqual(ot.inner.msg, msg)


if __name__ == '__main__':
    unittest.main()
