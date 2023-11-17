def get_summary(listOfTransactions):
    # Initialize an empty list to store the summary information
    summary_list = []

    # Iterate through each transaction in the input list
    for transaction in listOfTransactions:
        # Initialize variables to calculate the total cost for the transaction
        total_cost = 0

        # Iterate through each item in the transaction
        for item in transaction['Items']:
            # Calculate the cost for each item and add it to the total cost
            item_cost = item['Price'] * item['Qty']
            total_cost += item_cost

        # Create a summary dictionary for the transaction
        summary_dict = {
            "Cost": total_cost,
            "TID": transaction['TID']
        }

        # Add the summary dictionary to the list
        summary_list.append(summary_dict)

    # Return the final list of summary information for each transaction
    return summary_list


print(
    get_summary([
        {
            'TID': 'Gurunath_8528',
            'Items': [
                {'Name': 'Notebook', 'Price': 50, 'Qty': 4},
                {'Name': 'Pencil', 'Price': 10, 'Qty': 1},
                {'Name': 'Eraser', 'Price': 15, 'Qty': 1},
                {'Name': 'File', 'Price': 80, 'Qty': 1}
            ]
        }
    ])
)
