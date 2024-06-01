import pytest
from water_flow import (
    water_column_height,
    pressure_gain_from_water_height,
    pressure_loss_from_pipe,
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction,
    kpa_to_psi
)

def test_water_column_height():
    assert water_column_height(10, 3) == 7
    assert water_column_height(5, 2) == 3
    assert water_column_height(8, 8) == 0

def test_pressure_gain_from_water_height():
    assert pytest.approx(pressure_gain_from_water_height(10), 0.01) == 98106.5
    assert pytest.approx(pressure_gain_from_water_height(5), 0.01) == 49053.25
    assert pytest.approx(pressure_gain_from_water_height(0), 0.01) == 0

def test_pressure_loss_from_pipe():
    assert pytest.approx(pressure_loss_from_pipe(100, 0.1, 0.01, 0.02), 0.01) == 19.64
    assert pytest.approx(pressure_loss_from_pipe(50, 0.1, 0.01, 0.02), 0.01) == 9.82
    assert pytest.approx(pressure_loss_from_pipe(100, 0.1, 0.02, 0.02), 0.01) == 78.46

def test_pressure_loss_from_fittings():
    assert pytest.approx(pressure_loss_from_fittings(0, 3), 0.001) == 0
    assert pytest.approx(pressure_loss_from_fittings(1.65, 0), 0.001) == 0
    assert pytest.approx(pressure_loss_from_fittings(1.65, 2), 0.001) == -0.109
    assert pytest.approx(pressure_loss_from_fittings(1.75, 2), 0.001) == -0.122
    assert pytest.approx(pressure_loss_from_fittings(1.75, 5), 0.001) == -0.306

def test_reynolds_number():
    assert pytest.approx(reynolds_number(0.048692, 0), 1) == 0
    assert pytest.approx(reynolds_number(0.048692, 1.65), 1) == 80069
    assert pytest.approx(reynolds_number(0.048692, 1.75), 1) == 84922
    assert pytest.approx(reynolds_number(0.28687, 1.65), 1) == 471729
    assert pytest.approx(reynolds_number(0.28687, 1.75), 1) == 500318

def test_pressure_loss_from_pipe_reduction():
    assert pytest.approx(pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692), 0.001) == 0
    assert pytest.approx(pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692), 0.001) == -163.744
    assert pytest.approx(pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692), 0.001) == -184.182

def test_kpa_to_psi():
    assert pytest.approx(kpa_to_psi(0), 0.001) == 0
    assert pytest.approx(kpa_to_psi(101.325), 0.001) == 14.6959
    assert pytest.approx(kpa_to_psi(100), 0.001) == 14.5038

if __name__ == "__main__":
    pytest.main()
