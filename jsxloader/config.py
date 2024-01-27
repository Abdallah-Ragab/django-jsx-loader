from dataclasses import dataclass
from django.conf import settings

@dataclass(kw_only=True)
class Config:
    base_dir: str = "jsx_modules"
    pre_bundle_dir: str = "prebundle"
    post_bundle_dir: str = "postbundle"
    config_dir: str = "config"

def load_config():
    # check if "JSX_LOADER_CONFIG" is set in django's settings
    if hasattr(settings, "JSX_LOADER_CONFIG"):
        config_dict = settings.JSX_LOADER_CONFIG
        return dict_to_config(config_dict)
    else:
        return Config()

def dict_to_config(config_dict: dict) -> Config:
    default_config = Config()
    config_dict = {key: value for key, value in config_dict.items() if hasattr(default_config, key)}
    return Config(**config_dict)