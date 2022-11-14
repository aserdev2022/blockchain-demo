import time



class Block:
    """
    Block: a unit of storage.
    store transactions in a blockchain that supports a cryptocurrency.
    """

    def __init__(self, timestamp, hash, last_hash, data, ):
        self.data = data
        self.timestamp = timestamp
        self.hash = hash
        self.last_hash = last_hash

    def __repr__(self):
        return (
            'Block('
            f'data: {self.data},'
            f'hash: {self.hash},'
            f'last_hash: {self.last_hash},'
            f'timestamp: {self.timestamp})'
        )

    @staticmethod
    def mine_block(last_block, data):
        """
        Mine a block based on the given last_block and data.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        hash = f'{timestamp}-{last_hash}'
        return Block(timestamp, last_hash, hash, data)

    @staticmethod
    def genesis():
        """
        Generate the genesis block.
        """
        return Block(1, 'genesis_last_hash', 'genesis_hash', [])



def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'foo')
    print(block)


if __name__ == '__main__':
    main()
