import pytest
from pathlib import Path


root_repository_path = Path(__file__).parent.parent.resolve()

pytest.main(
    [
        root_repository_path / "src/ciur",
        root_repository_path / "tests",
        f"--ignore={root_repository_path}/src/ciur/parse/parser_pdf.py"
    ]
)
