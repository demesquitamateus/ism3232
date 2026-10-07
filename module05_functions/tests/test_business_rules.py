from business_rules import (
    apply_discount,
    calculate_total,
    get_approval_tier,
    requires_review,
)


def test_requires_review_over():
    assert requires_review(1500) is True


def test_requires_review_under():
    assert requires_review(500) is False


def test_boundary_limit():
    # Exactly 1000 should not require review (> not >=)
    assert requires_review(1000) is False


def test_total_includes_tax():
    assert round(calculate_total(100, 2), 2) == 214.00


def test_tier_auto():
    assert get_approval_tier(400) == "auto"


def test_tier_boundary():
    assert get_approval_tier(500) == "auto"


def test_tier_manager():
    assert get_approval_tier(750) == "manager"


def test_tier_director():
    assert get_approval_tier(1500) == "director"


def test_discount_ten():
    assert round(apply_discount(100, 10), 2) == 90.00
