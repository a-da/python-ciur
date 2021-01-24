from pathlib import Path
import os

import pytest


@pytest.fixture(
    # scope="session", 
    autouse=True
)
def ensure_working_dir_test_dir():
    os.chdir(Path(__file__).parent)
