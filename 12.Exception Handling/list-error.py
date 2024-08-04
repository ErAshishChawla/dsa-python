try:
    my_list = [24274, 543, 353, 534, 534]
    print(my_list[12])
except Exception as e:
    print(e)
    print(type(e).__name__)
    print("Exception caught")
