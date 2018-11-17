import pytest
import gol

def test_create_cell():
    assert gol.create_cell() == "CELL"
