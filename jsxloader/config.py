from dataclasses import dataclass

@dataclass
class Config:
    base_dir: str = "jsx_modules"
    pre_bundle_dir: str = "prebundle"
    post_bundle_dir: str = "postbundle"
    config_dir: str = "config"

