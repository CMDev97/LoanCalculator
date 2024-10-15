import cli_parser
import math

MONTHLY_PAYMENT_MODE = 1
LOAN_PRINCIPAL_MODE = 2
NUMBER_PAYMENTS_MODE = 3
INVALID_MODE = -1

ANNUITY_TYPE = 'annuity'
DIFFERENTIAL_TYPE = 'diff'
OVERPAY_KEY = "overpay"

TOTAL_MONTH = 12


def get_program_mode(cli_type, payment, principal, periods):
    if payment and principal  and cli_type == ANNUITY_TYPE:
        return NUMBER_PAYMENTS_MODE
    elif payment and periods and cli_type == ANNUITY_TYPE:
        return LOAN_PRINCIPAL_MODE
    elif periods and principal and (cli_type == ANNUITY_TYPE or cli_type == DIFFERENTIAL_TYPE):
        return MONTHLY_PAYMENT_MODE
    else:
        return INVALID_MODE


def get_monthly_interest(interest):
    return interest / (TOTAL_MONTH * 100)


def calculate_months(principal, payment, interest):
    monthly_interest = get_monthly_interest(interest)
    arg_log = payment / (payment - monthly_interest * principal)
    base_log = 1 + monthly_interest
    log_value = math.log(arg_log, base_log)
    return int(math.ceil(log_value))


def calculate_monthly_payments(principal, periods, interest):
    monthly_interest = get_monthly_interest(interest)
    first_argument = principal * monthly_interest
    second_argument = 1 - math.pow(1 + monthly_interest, -periods)
    return int(math.ceil(first_argument / second_argument))


def calculate_monthly_diff_payment(principal, periods, interest):
    monthly_interest = get_monthly_interest(interest)
    monthly_rate_lock = principal / periods
    dictionary = {}
    sum_rate = 0
    for i in range(1, periods+1):
        interest = monthly_interest * (principal - (principal * (i-1))/periods)
        payment = int(math.ceil(monthly_rate_lock + interest))
        dictionary[str(i)] = payment
        sum_rate += payment
    overpayment = sum_rate - principal
    dictionary[OVERPAY_KEY] = overpayment
    return dictionary


def print_monthly_diff_payments(monthly_diff_payments):
    for key in monthly_diff_payments:
        if key == OVERPAY_KEY:
            print(f"Overpayment = {monthly_diff_payments[OVERPAY_KEY]}")
        else:
            print(f"Month {key}: payment is {monthly_diff_payments[key]}")


def calculate_loan_payments(payment, periods, interest):
    monthly_interest = get_monthly_interest(interest)
    first_argument = payment * (1 - math.pow(1 + monthly_interest, -periods))
    return int(first_argument / monthly_interest)


def calculate_overpayment(a, b, total):
    product = a * b
    return int(product - total)


def print_months_and_years(months):
    if months > TOTAL_MONTH:
        years = months // TOTAL_MONTH
        month = months - (years * TOTAL_MONTH)
        print(f"It will take {years} years and {month} months to repay this loan!")
    else:
        print(f"It will take {months} months to repay this loan!")


def main(mode, loan_type, payment, principal, periods, interest):
    if mode == MONTHLY_PAYMENT_MODE:
        if loan_type == ANNUITY_TYPE:
            monthly_payment = calculate_monthly_payments(principal, periods, interest)
            print(f"Your monthly payment = {monthly_payment}!")
        elif loan_type == DIFFERENTIAL_TYPE:
            dictionary_monthly = calculate_monthly_diff_payment(principal, periods, interest)
            print_monthly_diff_payments(dictionary_monthly)
    elif mode == LOAN_PRINCIPAL_MODE:
        loan_payments = calculate_loan_payments(payment, periods, interest)
        overpayment = calculate_overpayment(payment, periods, loan_payments)
        print(f"Your loan principal = {loan_payments}!")
        print(f"Overpayment = {overpayment}")
    elif mode == NUMBER_PAYMENTS_MODE:
        months = calculate_months(principal, payment, interest)
        overpayment = calculate_overpayment(months, payment, principal)
        print_months_and_years(months)
        print(f"Overpayment = {overpayment}")


def run_program():
    args = cli_parser.init_arg_parse()
    mode = get_program_mode(args.type, args.payment, args.principal, args.periods)
    if mode == INVALID_MODE:
        print("Invalid parameters")
    else:
        main(mode, args.type, args.payment, args.principal, args.periods, args.interest)


if __name__ == '__main__':
    run_program()


