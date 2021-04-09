import pickle

class db:
    def __init__(self):
        # try to open file, if no then create one?
        
        self.blk_chain_file = "blockchain.pckl"
        try:
            f = open("blockchain.pckl",'rb')
            self._blk_chain_data = pickle.load(f)
            f.close()
        except:
            self._blk_chain_data = None
        # print(self._blk_chain_data)
        # print(self._blk_data['Python']['C++'])

    def if_have_blk_chain(self):
        return self._blk_chain_data != None

    def get_blk_chain(self):
        return self._blk_chain_data

    def store_block_chain(self, blk_chain_data):
        self._blk_chain_data = blk_chain_data
        with open(self.blk_chain_file,'wb') as f:
            pickle.dump(blk_chain_data,f)
    
    def reset_block_chain(self):
        self._blk_chain_data
        with open(self.blk_chain_file,'wb') as f:
            pickle.dump(None,f)



# if __name__ == '__main__':
#     f = open("blockchain.json",'w')
#     data = {'Python' : {'C++' : '.cpp', 'Java' : '.java'}}
#     json_data = json.dumps(data)
#     f.write(json_data)
#     f.close()
#     d = db()