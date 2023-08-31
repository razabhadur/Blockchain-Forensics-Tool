import random

def simulate_transaction_tracing(transaction_count):
    transactions = []
    for _ in range(transaction_count):
        sender = f'0x{random.randint(1000,9999):04x}'
        receiver = f'0x{random.randint(1000,9999):04x}'
        amount = random.randint(1, 100)
        transactions.append((sender, receiver, amount))
    return transactions

def simulate_address_profiling(address):
    high_risk_addresses = [f'0x{random.randint(1000,1999):04x}' for _ in range(5)]
    return address in high_risk_addresses

def analyze_transaction_value(amount):
    high_value_threshold = 80
    return amount > high_value_threshold

def visualize_transactions(transactions):
    for sender, receiver, amount in transactions:
        print(f'{sender} --({amount} ETH)--> {receiver}')

def generate_report(transactions):
    report = 'Blockchain Forensics Report\n'
    report += '=' * 30 + '\n'
    for sender, receiver, amount in transactions:
        report += f'Transaction: {sender} sent {amount} ETH to {receiver}\n'
        if simulate_address_profiling(receiver):
            report += f'WARNING: {receiver} is a potential high-risk address!\n'
        if analyze_transaction_value(amount):
            report += f'WARNING: High transaction value of {amount} ETH detected!\n'
    return report

if __name__ == '__main__':
    transaction_count = 5
    transactions = simulate_transaction_tracing(transaction_count)
    print('Visualizing Transactions:\n')
    visualize_transactions(transactions)
    report = generate_report(transactions)
    print('\n' + report)
