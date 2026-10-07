from reference_value import calculate_reference_value


def test_positive_adjustment() -> None:
    assert calculate_reference_value(100.0, 10.0) == 110.0


def test_full_reduction_reaches_zero() -> None:
    assert calculate_reference_value(100.0, -100.0) == 0.0
