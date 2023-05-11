# Copyright (C) 2012 Anaconda, Inc
# SPDX-License-Identifier: BSD-3-Clause
import unittest

from conda_env import env
from conda_env.specs.toml_file import TomlSpec

from .. import support_file


class TestTomlSpec(unittest.TestCase):
    def test_no_environment_file(self):
        spec = TomlSpec(name=None, filename="not-a-file")
        self.assertEqual(spec.can_handle(), False)

    def test_no_name(self):
        spec = TomlSpec(filename=support_file("pyproject.toml"))
        self.assertEqual(spec.can_handle(), False)

    def test_req_file_and_name(self):
        spec = TomlSpec(filename=support_file("pyproject.toml"), name="env")
        self.assertTrue(spec.can_handle())

    def test_environment(self):
        spec = TomlSpec(filename=support_file("pyproject.toml"), name="env")
        self.assertIsInstance(spec.environment, env.Environment)
        self.assertEqual(spec.environment.dependencies["conda"][0], "pip")
        self.assertEqual(spec.environment.dependencies["pip"][0], "flask ==1.1.1")