import os
from box.exceptions import BoxValueError
import yaml
from textSummarization.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yamL: Path) -> ConfigBox:
    """
    Read a yaml file and return a ConfigBox object
    """
    try:
        with open(path_to_yamL) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Reading yaml file from {path_to_yamL}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbrose=True):
    """
    Create directories
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbrose:
            logger.info(f"Directory created at {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size of a file in Kb
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} Kb"