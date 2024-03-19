my_list = []

if not my_list:
    print("The list is empty.")
else:
    print("The list is not empty.")


my_list = None

if my_list is not None:
    print("The list is not None.")
else:
    print("The list is None.")