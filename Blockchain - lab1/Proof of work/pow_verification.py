from pow_blockchain import Pow_Blockchain, Block
import time

def test_pow(difficulty):
    blockchain = Pow_Blockchain()
    blockchain.set_difficulty(difficulty)

    start_time = time.time()

    # Ajouter quelques blocs
    blockchain.add_block(Block(1, "", int(time.time()), "Transaction Data 1"))
    blockchain.add_block(Block(2, "", int(time.time()), "Transaction Data 2"))
    blockchain.add_block(Block(3, "", int(time.time()), "Transaction Data 3"))

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Difficulty: {difficulty}")
    print(f"Time taken: {execution_time:.2f} seconds")
    print(f"Chain valid: {blockchain.is_chain_valid()}")
    print("Blocks in the chain:")
    for block in blockchain.chain:
        print(f"Block #{block.index} - Hash: {block.hash}")
    print("\n")

if __name__ == "__main__":
    for difficulty in range(4, 7):
        test_pow(difficulty)