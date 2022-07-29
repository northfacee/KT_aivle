#Q3

store = [2,3,7,8,9]
customer = [7,5,9]

['yes' if customer[i] in list(set(store) & set(customer)) else 'no' for i in range(len(customer))]
