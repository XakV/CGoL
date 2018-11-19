import pytest
import gol

def test_create_cell():
    """ Testing if we can create a cell"""
    assert gol.create_cell

def test_check_if_alive():
    """Test if the cell is living"""
    assert gol.is_alive

def test_count_neighbors_should_return_3_for_three_neighbors():
    neighborhood = [
        [0, 1, 0,],
        [0, 0, 1,],
        [0, 1, 0,],
    ]

    assert gol.count_neighbors(neighborhood) == 3

def test_count_neighbors_should_return_4_for_four_neighbors():
    neighborhood = [
        [0, 1, 1,],
        [0, 0, 1,],
        [0, 1, 0,],
    ]

    assert gol.count_neighbors(neighborhood) == 4

def test_count_neighbors_should_return_0_for_zero_neighbors():
    neighborhood = [
        [0, 0, 0,],
        [0, 0, 0,],
        [0, 0, 0,],
    ]

    assert gol.count_neighbors(neighborhood) == 0
def test_count_neighbors_should_return_0_for_zero_neighbors():
    neighborhood = [
        [0, 0, 0,],
        [0, 1, 0,],
        [0, 0, 0,],
    ]

    assert gol.count_neighbors(neighborhood) == 0

def test_count_neighbors_should_return_1_for_one_neighbors():
    neighborhood = [
        [1, 0, 0,],
        [0, 1, 0,],
        [0, 0, 0,],
    ]
    
    assert gol.count_neighbors(neighborhood) == 1

def test_a_cell_with_one_neighbor_dies_after_1_tick():
    neighborhood = [
        [1, 0, 0,],
        [0, 1, 0,],
        [0, 0, 0,],
    ]
    gol.tick(neighborhood)
    assert neighborhood == [
        [1, 0, 0,],
        [0, 0, 0,],
        [0, 0, 0,],
    ]

def test_a_cell_with_two_neighbors_dies_after_1_tick():
    neighborhood = [
        [1, 1, 0,],
        [0, 1, 0,],
        [0, 0, 0,],
    ]
    gol.tick(neighborhood)
    assert neighborhood == [
        [1, 1, 0,],
        [0, 0, 0,],
        [0, 0, 0,],
    ]

