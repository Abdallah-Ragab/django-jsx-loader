import hashlib
import re


def clean_js_variable_name(var_name: str) -> str:
    """
    Cleans a JavaScript variable name by removing any non-alphanumeric characters and ensuring it starts with a letter or underscore.

    Args:
        var_name (str): The variable name to be cleaned.

    Returns:
        str: The cleaned variable name.
    """
    while var_name[0].isdigit():
        var_name = "_" + var_name

    var_name = re.sub("[^0-9a-zA-Z_]+", "", var_name)

    if len(var_name) < 1:
        var_name = "_"

    return var_name


def hash_string(string: str) -> str:
    """
    Hashes a given string using SHA256 algorithm and returns the hash.

    Args:
        string (str): The string to be hashed.

    Returns:
        str: The alphanumeric characters of the hash.
    """
    hash_object = hashlib.sha256(string.encode())
    hex_digest = hash_object.hexdigest()
    hex_digest = str(hex_digest)

    # Keep only alphanumeric characters in the output
    result = "".join(char for char in hex_digest if char.isalnum())

    return result


def template_name_to_dotted_path(template_name: str) -> str:
    """
    Converts a template name to a dotted path.

    Args:
        template_name (str): The template name to convert.

    Returns:
        str: The converted dotted path.
    """
    template_name = template_name.strip("/.\\")
    template_name = template_name.split(".")[0]
    return template_name.replace("/", ".")
