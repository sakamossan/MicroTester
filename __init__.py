class MicroTester(object):

    OK = "<span style='color:green;'>OK</span>"
    NG = "<span style='color:red;'>NG</span>"

    @classmethod
    def run(cls, *args, **kw):
        tester = cls(*args, **kw)
        tester.set_up()
        tester._run()
        tester.tear_down()
        return tester._get_results()

    def __init__(self, *args, **kw):
        raise NotImplementedError

    def set_up(self): 
        pass

    def tear_down(self): 
        pass

    def test000(self):
        """test.run() is runable """
        return True

    def _run(self):
        self.results = [self._is_ok(fn) for fn in self._get_tests()]

    def _is_ok(self, fn):
        result = self.OK if fn() else self.NG
        return "%s %s" % (result, fn.__doc__)

    def _get_tests(self):
        v = re.compile(r'^test')
        return (getattr(self, attr) for attr in sorted(dir(self)) if v.match(attr))

    def _get_results(self):
        header = "<h3>%s</h3>" % self.__class__.__name__
        return  header + "<br />".join(self.results) + "<hr />"