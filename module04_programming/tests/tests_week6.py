def test_accumulator():
    amounts = [500, 1500, 200]
    total = sum(a for a in amounts)
    assert total == 2200


def test_flag_filter():
    records = [{"amount": 500}, {"amount": 1500}, {"amount": 800}]
    flagged = [r for r in records if r["amount"] > 1000]
    assert len(flagged) == 1


def test_status_filter():
    records = [
        {"amount": 500, "status": "Pending"},
        {"amount": 1000, "status": "Approved"},
    ]
    pending = [r for r in records if r["status"] == "Pending"]
    assert len(pending) == 1


def test_dict_key_access():
    rec = {"id": 1, "amount": 750, "status": "Pending"}
    assert rec["amount"] == 750


def test_list_of_dicts_length():
    data = [{"x": 1}, {"x": 2}, {"x": 3}]
    assert len(data) == 3
