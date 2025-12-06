import requests, time

def fast_auth_whale():
    print("NEAR — FastAuth Whale Activated (> 10M NEAR moved via key-pump)")
    seen = set()
    while True:
        r = requests.get("https://api.nearblocks.io/v1/transactions?order=desc&per_page=40")
        for tx in r.json().get("txs", []):
            h = tx["transaction_hash"]
            if h in seen: continue
            seen.add(h)

            # FastAuth / key-pump = receiver creates account with huge balance in one action
            if not tx.get("receipts_outcome"): continue
            for outcome in tx["receipts_outcome"]:
                if "NewAccount := outcome.get("outcome", {}).get("logs"):
                    for log in ifNewAccount:
                        if "Account created with" in str(log) and "NEAR" in str(log):
                            try:
                                amount = float(log.split("with")[1].split("NEAR")[0].strip())
                                if amount >= 10_000_000:  # > 10M NEAR
                                    print(f"FASTAUTH WHALE BORN\n"
                                          f"{amount:,.0f} NEAR pumped into new account instantly\n"
                                          f"Parent: {tx['signer_id'][:16]}...\n"
                                          f"Child:  {outcome['outcome']['executor_id']}\n"
                                          f"Tx: https://nearblocks.io/tx/{h}\n"
                                          f"→ NEAR's account model just birthed a mega-whale in one click\n"
                                          f"→ No gasless, keyless, and terrifyingly efficient\n"
                                          f"{'-'*90}")
                            except:
                                continue
        time.sleep(1.7)

if __name__ == "__main__":
    fast_auth_whale()
