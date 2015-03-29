import glob
import logging
import os
from settings import solver_settings
import solver
import unittest


logging.disable(logging.CRITICAL)


class TestExecuteProblem(unittest.TestCase):
    """Make sure that solver.execute_problem works for
    """
    def setUp(self):
        self.module_name = 'solver'
        self.module_with_main = 'problems.problem_0001'
        self.module_not_exist = 'madeupmodule'
        self.module_without_main = 'math'
        self.logger = solver.logger

    def test_import_with_main(self):
        """Make sure that module with method main is able to be imported and
        main method can be executed. We use problems.problem_0001 to test
        that this works, i.e. that no errors are raised.
        """
        solver.execute_problem(self.module_with_main)

    def test_import_not_exist(self):
        """Make sure that if module that doesn't exist is passed, that function
        catches ImportError and returns None.
        """
        answer = solver.execute_problem(self.module_not_exist)
        self.assertEqual(answer, None)

    def test_import_without_main(self):
        """Make sure that if module that doesn't have method main is passed,
        that function catches AttributeError and returns None.
        """
        answer = solver.execute_problem(self.module_without_main)
        self.assertEqual(answer, None)


class TestGetModules(unittest.TestCase):
    """Make sure that solver.get_modules works for current settings. Test
    for when problems list is passed and when problems list is absent.
    """
    def setUp(self):
        self.current_settings = solver_settings.GET_MODULES_SETTINGS

        self.path_template = '.'.join([
            self.current_settings['package'],
            self.current_settings['module_template']
        ])

    def test_current_settings_glob(self):
        """Integration test to make sure that current settings for get_modules
        function returns every module that starts with problem_.
        """
        modules = solver.get_modules(problems=None, **self.current_settings)

        actual_modules = []

        files = glob.glob(self.current_settings['glob_pattern'])

        for path in files:
            directory, filename = os.path.split(path)
            base, ext = os.path.splitext(filename)
            actual_modules.append('.'.join([self.current_settings['package'],
                                            base]))

        actual_modules.sort()

        self.assertEqual(modules, actual_modules)

    def test_current_settings_problem(self):
        """Integration test to make sure that current settings for get_modules
        function returns modules for passed problems list.
        """
        problems = [1, 2]
        modules = solver.get_modules(problems=problems,
                                     **self.current_settings)

        correct_modules = [self.path_template.format(prb) for prb in problems]

        self.assertEqual(modules, correct_modules)

    def test_current_settings_problem_skip(self):
        """Make sure that get_modules does not add to modules variable
        problem numbers that are less than one or greater than upper bound
        in current_settings.
        """
        problems = [0, 1, solver_settings.UPPERBOUND + 1]
        modules = solver.get_modules(problems=problems,
                                     **self.current_settings)

        correct_modules = [self.path_template.format(1)]

        self.assertEqual(modules, correct_modules)


if __name__ == '__main__':
    unittest.main()
