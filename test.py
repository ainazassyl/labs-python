from collections import defaultdict
transactions = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2), (1001, 1)]

stats = defaultdict(lambda: {1: 0, 2: 0, 3: 0, 'mft': None, 'lft': None})

for user_id, transaction_type in transactions:
    stats[user_id][transaction_type] += 1

for user, transactions_info in stats.items():
    max_trans = max(transactions_info, key=lambda k: transactions_info[k] if k in (1, 2, 3) else -1)
    min_trans = min(transactions_info, key=lambda k: transactions_info[k] if k in (1, 2, 3) else float('inf'))
    transactions_info['mft'] = max_trans
    transactions_info['lft'] = min_trans

stats = dict(stats)
print("stats = ", stats)