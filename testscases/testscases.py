from ConfigParser import ConfigParser
from nose.plugins.base import Plugin
from nose.util import tolist


class ExtendedTestsCases(Plugin):
    """Nose plugin to create different test cases
    """
    name = "extended_tests_case"

    def options(self, parser, env):
        super(ExtendedTestsCases, self).options(parser, env)
        parser.add_option(
            "--tests-cases",
            action="store",
            dest="tests_cases",
            help="You can specify the necessary test cases. ")
        parser.add_option(
            "--tests-cases-config",
            action="store",
            dest="cases_conf",
            default="cases.ini",
            help=("You can specify the configuration file cases. "
                  "Default config file: cases.cfg"))

    def configure(self, options, conf):
        """Configure plugin.
        """
        super(ExtendedTestsCases, self).configure(options, conf)
        self.conf = conf
        if options.tests_cases:
            self.cases = tolist(options.tests_cases)
            self.enabled = True
            try:
                self.cases_conf = ConfigParser()
                self.cases_conf.read(options.cases_conf)
                all_tests = []
                for case in self.cases:
                    tests = tolist(self.cases_conf.get(case, "tests"))
                    all_tests += tests
                self.conf.testNames += all_tests
            except IOError:
                raise IOError(
                    "configuration file %s is not found" % options.cases_conf)
