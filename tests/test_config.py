import unittest
from django.conf import settings
settings.configure()
from jsxloader.config import load_config, Config

class ConfigTestCase(unittest.TestCase):
    def test_load_config_with_config_set(self):
        # Set the "JSX_LOADER_CONFIG" in Django's settings
        settings.JSX_LOADER_CONFIG = {
            "base_dir": "test_base_dir_value",
            "config_dir": "test_config_dir_value",
        }

        # Call the load_config function
        result = load_config()

        # Assert that the returned result is a Config object
        self.assertIsInstance(result, Config)

        # Assert that the Config object has the correct values
        self.assertEqual(result.base_dir, "test_base_dir_value")
        self.assertEqual(result.config_dir, "test_config_dir_value")

    def test_load_config_without_config_set(self):
        # Remove the "JSX_LOADER_CONFIG" from Django's settings
        if hasattr(settings, "JSX_LOADER_CONFIG"):
            del settings.JSX_LOADER_CONFIG

        # Call the load_config function
        result = load_config()

        # Assert that the returned result is a Config object
        self.assertIsInstance(result, Config, "load_config() should return a Config object")

        # Assert that the Config object is the default Config
        self.assertEqual(result, Config(), "Config object should be the default Config")


if __name__ == "__main__":
    unittest.main()