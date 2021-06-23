from crypto import Block, Blockchain, Transaction

blockchain = Blockchain()
blockchain.create_transaction(Transaction("address1", "address2", 20))
blockchain.create_transaction(Transaction("address2", "address3", 10))
blockchain.mine_pending_transactions("address3")
print("The balance of address3 is: ", blockchain.get_balance_of_address("address3"))
blockchain.mine_pending_transactions("address3")
print("The balance of address3 is: ", blockchain.get_balance_of_address("address3"))
print("The balance of address2 is: ", blockchain.get_balance_of_address("address2"))
print("The balance of address1 is: ", blockchain.get_balance_of_address("address1"))

#blockchain.print_block_chain()