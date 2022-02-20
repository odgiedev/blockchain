import hashlib, json

from datetime import datetime

blockchain = []

block1 = {
    "sender" : "Diego",
    "recipient" : "Leona",
    "amount" : "1 BTC",
}

block2 = {
    "sender" : "Lula",
    "recipient" : "Bolsonaro",
    "amount" : "2 BTC",
}

def getTime():
	return str(datetime.today())

def hashGen(string) :
    Hash = hashlib.sha512(string.encode())
    Hash = Hash.hexdigest()
    return Hash

def addBlock(block) :
    global blockchain

    if (not blockchain) :
        block["timestamp"] = getTime()
        
        block["hash"] = hashGen(json.dumps(block))
    else :
        last_block = blockchain[-1]
        
        block["timestamp"] = getTime()

        block["hash"] = last_block["hash"]
        block["hash"] = hashGen(json.dumps(block))

    blockchain.append(block)

addBlock(block1)

addBlock(block2)

for b in blockchain :
    print(f"\n{b}\n")
    print("=#" * 40)
