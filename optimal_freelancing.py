# first iteration
def find_appropriate_slot(slots, current_slot, current_profit):
    minimum_profit_slot = 0
    minimum_profit = current_profit
    for slot_1, profit_1 in slots.items():
        if (slot_1 < current_slot) & (profit_1 < minimum_profit):
            minimum_profit = profit_1
            minimum_profit_slot = slot_1
    if minimum_profit_slot:
        slots[minimum_profit_slot] = current_profit
    return slots


def optimalFreelancing(jobs):
    # Write your code here.
    slots = {7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0}

    for job in jobs:
        for slot, profit in slots.items():
            if (job['deadline'] >= slot) & (job['payment'] > profit):
                current_profit = slots[slot]
                slots[slot] = job['payment']

                # moving the current profit to suitable previous slots
                if current_profit > 0:
                    slots = find_appropriate_slot(slots, slot, current_profit)
                break

    return sum(slots.values())


jobs = [
    {"deadline": 2, "payment": 1},
    {"deadline": 1, "payment": 4},
    {"deadline": 3, "payment": 2},
    {"deadline": 1, "payment": 3},
    {"deadline": 4, "payment": 3},
    {"deadline": 4, "payment": 2},
    {"deadline": 4, "payment": 1},
    {"deadline": 5, "payment": 4},
    {"deadline": 8, "payment": 1}
]

print(optimalFreelancing(jobs))
