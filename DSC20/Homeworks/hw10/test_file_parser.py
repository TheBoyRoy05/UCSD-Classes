from File_Parser import File_Parser
import pytest

@pytest.fixture
def parser():
    return File_Parser()

def test_file_parser(parser):
    assert parser.path != ''