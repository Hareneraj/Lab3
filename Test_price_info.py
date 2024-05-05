import price_info


print("Test_price_info")

def test_bubble_sort_total_cost_shopping():
    shopping_list = {'orange' : 5}
    total = price_info.total_cost_shopping(shopping_list)
    assert( total == 7)

def test_bubble_sort_cost_of_fruits():
    quantity = 10
    price_list = {'apple' : 1.20}
    cost = price_info.cost_of_fruits('apple', 10)
    assert( cost == 12)

      