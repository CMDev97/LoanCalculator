import unittest
from io import StringIO
from unittest.mock import patch, MagicMock
import main


class LoanCalculatorTest(unittest.TestCase):

    def test_get_program_mode_annuity_monthly_mode(self):
        # Arrange
        periods = 10
        principal = 10000
        payment = None
        type = main.ANNUITY_TYPE

        # Act
        result = main.get_program_mode(type, payment, principal, periods)

        # Assert
        self.assertEqual(result, main.MONTHLY_PAYMENT_MODE)

    def test_get_program_mode_differential_monthly_mode(self):
        # Arrange
        periods = 10
        principal = 10000
        payment = None
        type = main.DIFFERENTIAL_TYPE

        # Act
        result = main.get_program_mode(type, payment, principal, periods)

        # Assert
        self.assertEqual(result, main.MONTHLY_PAYMENT_MODE)

    def test_get_program_mode_differential_number_payments_mode_should_invalid_mode(self):
        # Arrange
        periods = None
        principal = 10000
        payment = 1233
        type = main.DIFFERENTIAL_TYPE

        # Act
        result = main.get_program_mode(type, payment, principal, periods)

        # Assert
        self.assertEqual(result, main.INVALID_MODE)

    def test_get_program_mode_annuity_number_payments_mode(self):
        # Arrange
        periods = None
        principal = 10000
        payment = 1233
        type = main.ANNUITY_TYPE

        # Act
        result = main.get_program_mode(type, payment, principal, periods)

        # Assert
        self.assertEqual(result, main.NUMBER_PAYMENTS_MODE)

    def test_get_program_mode_annuity_loan_principal_mode(self):
        # Arrange
        periods = 10
        principal = None
        payment = 1233
        type = main.ANNUITY_TYPE

        # Act
        result = main.get_program_mode(type, payment, principal, periods)

        # Assert
        self.assertEqual(result, main.LOAN_PRINCIPAL_MODE)

    def test_get_program_mode_differential_loan_principal_mode_should_invalid_mode(self):
        # Arrange
        periods = 10
        principal = None
        payment = 1233
        type = main.DIFFERENTIAL_TYPE

        # Act
        result = main.get_program_mode(type, payment, principal, periods)

        # Assert
        self.assertEqual(result, main.INVALID_MODE)

    def test_get_monthly_interest(self):
        # Arrange
        interest = 10

        # Act
        result = main.get_monthly_interest(interest)

        # Assert
        self.assertAlmostEqual(result, 0.00833, places=5)

    def test_calculate_months(self):
        # Arrange
        interest = 10
        principal = 1000000
        payment = 15000

        # Act
        result = main.calculate_months(principal, payment, interest)

        # Assert
        self.assertEqual(result, 98)

    def test_calculate_monthly_payments(self):
        # Arrange
        principal = 1000000
        periods = 60
        interest_year = 10

        # Act
        result = main.calculate_monthly_payments(principal, periods, interest_year)

        # Assert
        self.assertEqual(result, 21248)

    def test_calculate_monthly_diff_payment(self):
        # Arrange
        principal = 500000
        periods = 8
        interest = 7.8
        assert_dictionary = {'1': 65750, '2': 65344, '3': 64938, '4': 64532, '5': 64125, '6': 63719, '7': 63313, '8': 62907, 'overpay': 14628}

        # Act
        result = main.calculate_monthly_diff_payment(principal, periods, interest)

        # Arrange
        self.assertEqual(result, assert_dictionary)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_monthly_diff_payment_when_8_months(self, mock_stdout):
        # Arrange
        dictionary = {'1': 65750, '2': 65344, '3': 64938, '4': 64532, '5': 64125, '6': 63719, '7': 63313, '8': 62907,
                      'overpay': 14628}
        assert_array = ['Month 1: payment is 65750', 'Month 2: payment is 65344', 'Month 3: payment is 64938',
                        'Month 4: payment is 64532', 'Month 5: payment is 64125', 'Month 6: payment is 63719',
                        'Month 7: payment is 63313', 'Month 8: payment is 62907', 'Overpayment = 14628', '']

        # Act
        main.print_monthly_diff_payments(dictionary)

        # Assert
        self.assertEqual(mock_stdout.getvalue().split("\n"), assert_array)

    def test_calculate_loan_payments(self):
        # Arrange
        payment = 8721.8
        periods = 120
        interest_year = 5.6

        # Act
        result = main.calculate_loan_payments(payment, periods, interest_year)

        # Assert
        self.assertEqual(result, 800000)

    def test_calculate_overpayment(self):
        # Arrange
        a, b, total = 12, 10, 50

        # Act
        result = main.calculate_overpayment(a, b, total)

        # Assert
        self.assertEqual(result, 70)

    def test_calculate_overpayment_should_return_less_then_0(self):
        # Arrange
        a, b, total = 12, 10, 140

        # Act
        result = main.calculate_overpayment(a, b, total)

        # Assert
        self.assertEqual(result, -20)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_month_and_years_when_10_months(self, mock_stdout):
        # Arrange
        months = 10

        # Act
        main.print_months_and_years(months)

        # Assert
        self.assertEqual(mock_stdout.getvalue(), 'It will take 10 months to repay this loan!\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_months_and_years_when_98_months(self, mock_stdout):
        # Arrange
        months = 98

        # Act
        main.print_months_and_years(months)

        # Assert
        self.assertEqual(mock_stdout.getvalue(), 'It will take 8 years and 2 months to repay this loan!\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_months_and_years_when_48_months(self, mock_stdout):
        # Arrange
        months = 48

        # Act
        main.print_months_and_years(months)

        # Assert
        self.assertEqual(mock_stdout.getvalue(), 'It will take 4 years and 0 months to repay this loan!\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_with_diff_principal_period_interest_should_return_monthly_payment(self, mock_stdout):
        # Arrange
        principal, periods, interest = 500000, 8, 7.8
        assert_array = ['Month 1: payment is 65750', 'Month 2: payment is 65344', 'Month 3: payment is 64938',
                        'Month 4: payment is 64532', 'Month 5: payment is 64125', 'Month 6: payment is 63719',
                        'Month 7: payment is 63313', 'Month 8: payment is 62907', 'Overpayment = 14628', '']

        # Act
        main.main(main.MONTHLY_PAYMENT_MODE, main.DIFFERENTIAL_TYPE,None, principal, periods, interest)

        # Assert
        self.assertEqual(mock_stdout.getvalue().split("\n"), assert_array)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_with_annuity_principal_period_interest_should_return_monthly_payment(self, mock_stdout):
        # Arrange
        principal, periods, interest = 1000000, 60, 10
        string_assert = "Your monthly payment = 21248!\n"

        # Act
        main.main(main.MONTHLY_PAYMENT_MODE, main.ANNUITY_TYPE, None, principal, periods, interest)

        # Assert
        self.assertEqual(mock_stdout.getvalue(), string_assert)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_with_annuity_payment_period_interest_should_return_loan_payment(self, mock_stdout):
        # Arrange
        payment, periods, interest = 8721.8, 120, 5.6
        string_assert = ["Your loan principal = 800000!", "Overpayment = 246615", '']

        # Act
        main.main(main.LOAN_PRINCIPAL_MODE, main.ANNUITY_TYPE, payment, None, periods, interest)

        # Assert
        self.assertEqual(mock_stdout.getvalue().split("\n"), string_assert)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_with_annuity_principal_payment_interest_should_return_number_of_years(self, mock_stdout):
        # Arrange
        principal, payment, interest = 1000000, 15000, 10
        string_assert = ["It will take 8 years and 2 months to repay this loan!", "Overpayment = 470000", '']

        # Act
        main.main(main.NUMBER_PAYMENTS_MODE, main.ANNUITY_TYPE, payment, principal, None, interest)

        # Assert
        self.assertEqual(mock_stdout.getvalue().split("\n"), string_assert)

    @patch('cli_parser.init_arg_parse')
    @patch('main.main')
    def test_run_program_valid_mode(self, mock_main, mock_init_arg_parse):
        # Arrange
        mock_args = MagicMock()
        mock_args.type = main.DIFFERENTIAL_TYPE
        mock_args.payment = None
        mock_args.principal = 50000
        mock_args.periods = 12
        mock_args.interest = 5.5
        mock_init_arg_parse.return_value = mock_args

        # Act
        main.run_program()

        # Assert
        mock_main.assert_called_once_with(main.MONTHLY_PAYMENT_MODE, main.DIFFERENTIAL_TYPE, None, 50000, 12, 5.5)

    @patch('cli_parser.init_arg_parse')
    @patch('main.main')
    @patch('sys.stdout', new_callable=StringIO)
    def test_run_program_valid_mode(self, mock_stdout, mock_main, mock_init_arg_parse):
        # Arrange
        mock_args = MagicMock()
        mock_args.type = main.DIFFERENTIAL_TYPE
        mock_args.payment = None
        mock_args.principal = None
        mock_args.periods = 12
        mock_args.interest = 5.5
        mock_init_arg_parse.return_value = mock_args

        # Act
        main.run_program()

        # Assert
        self.assertEqual("Invalid parameters\n", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
