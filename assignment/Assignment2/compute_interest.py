"""
File: compute_interest.py
-------------------------
Add your comments here.
"""


def compute(initial_balance, start_year, start_month, end_year, end_month, interest_rate):
    # tạo 2 biến tạm là temp_year và temp_month để tránh thay đổi giá trị của year và month
    temp_year = end_year + 1
    sum_balance = initial_balance
    for i in range(start_year, temp_year):
        temp_month = 13
        if(i == end_year):
            # Khi đến năm cuối sẽ chuyển tháng max là 12 về end_month
            temp_month = end_month + 1
        for j in range(start_month, temp_month):
            print("Year ", i, " month ", j, " balance: ", sum_balance)
            # tính số tiền lãi
            amount_of_interest = sum_balance * interest_rate
            # cập nhập số dư
            sum_balance = sum_balance + amount_of_interest
            if(j == 12):
                # chạy từ start_month đến t12 sẽ chuyển về t1 cho năm mới
                start_month = 1


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    initial_balance = input("Initial balance: ")
    initial_balance = float(initial_balance)
    start_year = input("Start year: ")
    start_month = input("Start month: ")
    end_year = input("End year: ")
    end_month = input("End month: ")
    start_year = int(start_year)
    start_month = int(start_month)
    end_year = int(end_year)
    end_month = int(end_month)
    if (start_year < end_year):
        while(True):
            interest_rate = input("Interest rate (0 to quit): ")
            # cho nhap vao ky tu de check
            interest_rate = str(interest_rate)
            if (interest_rate == '0'):
                break

            else:
                # ép kiểu từ str sang float để tính toán
                interest_rate = float(interest_rate)
                interest_rate = float(interest_rate)
                compute(initial_balance, start_year, start_month, end_year, end_month, interest_rate)
    else:
        print("Starting date needs to be before the ending date.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
