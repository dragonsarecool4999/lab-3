import price_info as price
def test_total_cost_of_shopping():
    input = price.total_cost_shopping()
    answer = 46.75
    assert(answer==input)
def test_cost_of_fruit():
    input = price.cost_of_fruits('pomegranate',15)
    answer = 74.25
    assert(answer==input)
    