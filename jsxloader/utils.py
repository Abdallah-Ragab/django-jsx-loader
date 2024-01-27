import re


def clean_js_variable_name(var_name: str) -> str:
    """
    Cleans a JavaScript variable name by removing any non-alphanumeric characters and ensuring it starts with a letter or underscore.

    Args:
        var_name (str): The variable name to be cleaned.

    Returns:
        str: The cleaned variable name.
    """
    if var_name[0].isdigit():
        var_name = "_" + var_name

    var_name = re.sub("[^0-9a-zA-Z_]+", "", var_name)

    if len(var_name) < 1:
        var_name = "_"

    return var_name