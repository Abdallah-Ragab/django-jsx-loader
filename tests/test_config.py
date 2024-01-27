import unittest
from django.conf import settings
from jsxloader.config import load_config, Config

class ConfigTestCase(unittest.TestCase):
    def test_load_config_with_config_set(self):
        # Set the "JSX_LOADER_CONFIG" in Django's settings
        settings.JSX_LOADER_CONFIG = {
            "key1": "value1",
            "key2": "value2",
        }

        # Call the load_config function
        result = load_config()

        # Assert that the returned result is a Config object
        self.assertIsInstance(result, Config)

        # Assert that the Config object has the correct values
        self.assertEqual(result.key1, "value1")
        self.assertEqual(result.key2, "value2")

    def test_load_config_without_config_set(self):
        # Remove the "JSX_LOADER_CONFIG" from Django's settings
        if hasattr(settings, "JSX_LOADER_CONFIG"):
            del settings.JSX_LOADER_CONFIG

        # Call the load_config function
        result = load_config()

        # Assert that the returned result is a Config object
        self.assertIsInstance(result, Config)

        # Assert that the Config object is empty
        self.assertEqual(len(result), 0)

if __name__ == "__main__":
    unittest.main()