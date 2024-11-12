import os.path
import unittest

from tiledb_cloud._common import trampoline


class TrampolineTest(unittest.TestCase):
    def test_trampoline(self):
        self.assertEqual(9765625, trampoline.run_python_function("builtins:pow", 5, 10))
        self.assertEqual(
            os.path.join("a", "b"),
            trampoline.run_python_function("os.path:join", "a", "b"),
        )

    def test_find_wrong_type(self):
        with self.assertRaises(TypeError):
            # This should find the module but raise a TypeError when it tries
            # to call a non-callable.
            trampoline.run_python_function("tiledb_cloud")
        with self.assertRaises(TypeError):
            # This should find the object but raise a TypeError when it tries
            # to call a non-callable.
            trampoline.run_python_function("tiledb_cloud.dag:Mode.LOCAL")

    def test_find_missing(self):
        # These will all fail prior to reaching the call.
        with self.assertRaises(ValueError):
            trampoline.run_python_function("")
        with self.assertRaises(ImportError):
            trampoline.run_python_function("tiledb_cloud.dag.Mode")
        with self.assertRaises(AttributeError):
            trampoline.run_python_function("os:invalid")
        with self.assertRaises(ValueError):
            trampoline.run_python_function(":no_module")
        with self.assertRaises(AttributeError):
            trampoline.run_python_function("builtins:")
        with self.assertRaises(AttributeError):
            trampoline.run_python_function("tiledb_cloud.dag:Mode.")
