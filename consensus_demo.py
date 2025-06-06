import random
from collections import Counter

# ----------- Proof of Work (PoW) -----------
# In PoW, the validator (miner) with the highest computational power is selected.
list_of_miner_ids = [{'id': 'Miner1','power': random.randint(10, 100)},{'id': 'Miner2','power': random.randint(10, 100)},{'id': 'Miner3','power': random.randint(10, 100)}]
print("PoW Miners:")
# Generate a list of miners with random computational power
for miner in list_of_miner_ids:
    print(f"Miner ID: {miner['id']}, Power: {miner['power']}")

print("PoW Logic: The miner with the highest computational power gets to validate the block.")

for miner in list_of_miner_ids:
    # Select the miner with the maximum power
    if 'max_power' not in locals() or miner['power'] > max_power:
        max_power = miner['power']
        selected_miner = miner

print(f"Selected Validator (PoW): {selected_miner['id']}\n")


# ----------- Proof of Stake (PoS) -----------
# In PoS, the validator with the highest amount of coins staked is selected.

stakers = [
    {'id': 'Staker1', 'stake': random.randint(10, 100)},
    {'id': 'Staker2', 'stake': random.randint(10, 100)},
    {'id': 'Staker3', 'stake': random.randint(10, 100)},
]

print("PoS Stakers:")
for s in stakers:
    print(f"{s['id']} has staked {s['stake']} coins")

# Select the staker with the maximum stake
pos_winner = max(stakers, key=lambda x: x['stake'])

print("\nPoS Logic: The staker with the highest stake is chosen to validate the block.")
print(f"Selected Validator (PoS): {pos_winner['id']}\n")


# ----------- Delegated Proof of Stake (DPoS) -----------
# In DPoS, stakeholders vote for delegates, and the delegate with most votes is selected.

delegates = ['Delegate1', 'Delegate2', 'Delegate3']

voters = [
    {'id': 'VoterA', 'vote': 'Delegate1'},
    {'id': 'VoterB', 'vote': 'Delegate2'},
    {'id': 'VoterC', 'vote': 'Delegate1'},  # Delegate1 gets 2 votes
]

print(" DPoS Voters:")
for v in voters:
    print(f"{v['id']} voted for {v['vote']}")

# Count the number of votes for each delegate
vote_counts = Counter(v['vote'] for v in voters)
top_delegate = vote_counts.most_common(1)[0][0]

print("\nDPoS Logic: Delegates are voted by stakeholders. The one with most votes is selected.")
print(f" Selected Validator (DPoS): {top_delegate}")
