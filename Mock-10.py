def get_summary(listOfTransactions):
    return [{
        "Cost": sum(
            [item['Price'] * item['Qty'] for item in trans['Items']]
        ),
        "TID": trans['TID']
    } for trans in listOfTransactions]


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
