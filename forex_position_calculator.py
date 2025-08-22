# forex_position_calculator.py

def calculate_position_size(account_balance, risk_per_trade, stop_loss_pips, pip_value):
    """
    Calculate position size for a Forex trade.

    :param account_balance: Total account balance in your trading account (float).
    :param risk_per_trade: Percentage of account balance you are willing to risk per trade (e.g., 1 for 1%).
    :param stop_loss_pips: Stop loss size in pips (float).
    :param pip_value: Value of 1 pip for the currency pair (float).
    :return: Position size (float).
    """
    risk_amount = account_balance * (risk_per_trade / 100)
    position_size = risk_amount / (stop_loss_pips * pip_value)
    return position_size


# Example usage
if __name__ == "__main__":
    balance = 1000        # Example: $1000 account
    risk = 1              # Risk 1%
    stop_loss = 20        # Stop loss = 20 pips
    pip_val = 1           # Each pip = $1
    
    size = calculate_position_size(balance, risk, stop_loss, pip_val)
    print(f"Recommended position size: {size:.2f} lots")
