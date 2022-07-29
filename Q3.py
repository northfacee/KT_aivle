#Q3

store = [2,3,7,8,9]
customer = [7,5,9]

target = list(set(store) & set(customer))

['yes' if customer[i] in target else 'no' for i in range(len(customer))]
