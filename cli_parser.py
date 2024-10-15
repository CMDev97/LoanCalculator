import argparse

ANNUITY_VALUE = 'annuity'
DIFFERENTIAL_VALUE = 'diff'


def check_positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"Il valore deve essere maggiore di 0, ma è stato fornito: {value}")
    return ivalue


def check_positive_float(value):
    ivalue = float(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"Il valore deve essere maggiore di 0, ma è stato fornito: {value}")
    return ivalue


def init_arg_parse():
    parser = argparse.ArgumentParser(
        description='This program calculate the loan')

    parser.add_argument("--payment", type=check_positive_float, help="Monthly payment amount")
    parser.add_argument("--principal", type=check_positive_float, help="Loan principal (amount borrowed)")
    parser.add_argument('--periods', type=check_positive_int, help="Number of months to repay the loan")
    parser.add_argument(
        '--interest',
        type=check_positive_float,
        required=True,
        help="Annual interest rate (without percentage sign)"
    )
    parser.add_argument(
        '--type',
        choices=[ANNUITY_VALUE, DIFFERENTIAL_VALUE],
        required=True,
        help="Specifica il tipo di pagamento: 'annuity' per rate costanti o 'diff' per pagamento differenziato"
    )

    return parser.parse_args()
