from Main_App.Input_Pack import user_inputs as u
from Main_App.Operation_Pack import fetch_record as f
from Main_App.Operation_Pack import fetch_branch as fb
from Main_App.Operation_Pack import fetch_update as fu

while True:
    print("-----------MENU----------")
    print('''
    1. Enter Participants details 
    2. Fetch participants details
    3. Enter participants based on branch
    4. Update wrongly entered name change
    5. exist
    ''')
    print("choose any option from above menu:")
    ch = int(input())
    if ch == 1:
        u.input_data()
    elif ch == 2:
        f.fetch_data()
    elif ch == 3:
        input_branch = input("Enter branch to be fetched")
        fb.fetch_branch(input_branch)
    elif ch == 4:
        x = int(input("Enter ID : "))
        y = (input("Enter Name : "))
        fu.update_rec(x, y)
    else:
        break
