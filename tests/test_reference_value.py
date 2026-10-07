from reference_value import calculate_reference_value


def test_positive_adjustment() -> None:
    assert calculate_reference_value(100.0, 10.0) == 110.0


def test_full_reduction_reaches_zero() -> None:
    assert calculate_reference_value(100.0, -100.0) == 0.0


def test_adjustment_below_minus_one_hundred_percent_is_clamped_to_zero() -> None:
    assert calculate_reference_value(100.0, -150.0) == 0.0
