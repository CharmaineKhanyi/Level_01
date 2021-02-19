def test_number5(x, y):
    if x == 3 or y == 3 and (x+y) == 3:
        return True
    else:
        return False

print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))
