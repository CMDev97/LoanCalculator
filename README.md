
# Loan Calculator Program

This is a command-line loan calculator program that calculates various aspects of a loan based on user input. It supports two types of loan repayments: annuity payments (fixed payments over time) and differentiated payments (decreasing payments over time).

## Features:
- **Annuity payments**: Calculate the monthly payment or the number of months to repay the loan.
- **Differentiated payments**: Calculate monthly payments that decrease over time, showing each month's payment and the total overpayment.
- **Overpayment calculation**: Calculates how much extra the borrower will pay based on the loan type and other parameters.

## Command-line Arguments:

The program accepts the following command-line arguments:

- `--payment`: Monthly payment amount (required for specific modes)
- `--principal`: Loan principal (the amount borrowed)
- `--periods`: Number of months to repay the loan
- `--interest`: **Required**. Annual interest rate as a float (without the percentage sign)
- `--type`: **Required**. Type of payment - either 'annuity' for fixed payments or 'diff' for differentiated payments.

### Example usage:

To calculate the loan principal given the number of months, interest, and monthly payment:

```
python loan_calculator.py --type=annuity --payment=8722.5 --periods=120 --interest=5.6
```

To calculate differentiated payments for a loan:

```
python loan_calculator.py --type=diff --principal=1000000 --periods=10 --interest=10
```

## Modes:
The program supports three modes depending on the input parameters:

- **Monthly Payment Mode**: Calculates the monthly payment based on loan principal, periods, and interest rate.
- **Loan Principal Mode**: Calculates the loan principal based on monthly payments, periods, and interest rate.
- **Number of Payments Mode**: Calculates the number of months required to repay the loan given the loan principal, monthly payment, and interest rate.

## Functions:
- `get_program_mode(cli_type, payment, principal, periods)`: Determines which mode the program should run based on user input.
- `calculate_monthly_payments(principal, periods, interest)`: Calculates the monthly payment for annuity loans.
- `calculate_months(principal, payment, interest)`: Determines how many months it will take to repay the loan.
- `calculate_monthly_diff_payment(principal, periods, interest)`: Calculates monthly payments for differentiated loans.
- `calculate_loan_payments(payment, periods, interest)`: Calculates the loan principal for a given monthly payment.
- `calculate_overpayment(a, b, total)`: Calculates the overpayment made during the loan period.

## How to Run the Program:

1. Clone or download the repository.
2. Ensure you have Python installed (Python 3.7+).
3. Install any required libraries (if necessary).
4. Run the program with the required arguments as shown in the examples.

## Dependencies:

The program does not require any external libraries beyond the Python Standard Library.

## License:

This program is free to use and modify under the MIT license.
