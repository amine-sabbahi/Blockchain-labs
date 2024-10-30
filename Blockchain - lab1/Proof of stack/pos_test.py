from pos_blockchain import PoSBlockchain, PosBlock
import time


def test_pos(min_stake):
    blockchain = PoSBlockchain(min_stake)

    # Add some blocks
    blockchain.add_block(PosBlock(1, "", int(time.time()), "Transaction Data 1", 100, "Validator A"))
    blockchain.add_block(PosBlock(2, "", int(time.time()), "Transaction Data 2", 150, "Validator B"))
    blockchain.add_block(PosBlock(3, "", int(time.time()), "Transaction Data 3", 75, "Validator C"))

    print(f"Minimum Stake: {min_stake}")
    print(f"Chain Valid: {blockchain.is_chain_valid()}")
    print("Blocks in the chain:")
    for block in blockchain.chain:
        print(f"Block #{block.index} - Hash: {block.hash}, Validator: {block.validator_address}, Stake: {block.stake_amount}")
    print("\n")

if __name__ == "__main__":
    test_pos(100)
    test_pos(50)