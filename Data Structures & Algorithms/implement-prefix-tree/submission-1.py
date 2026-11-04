class PrefixTree:

    def __init__(self):
        self.root = [{}, False]
        

    def insert(self, word: str) -> None:
        root = self.root
        while word:
            char = word[0]
            word = word[1:]
            node = root[0].get(char)
            if node:
                root = node
                if len(word) == 0:
                    root[1] = True
            else:
                root[0][char] = [{}, len(word) == 0]
                root = root[0][char]


    def search(self, word: str) -> bool:
        root = self.root
        while word:
            char = word[0]
            word = word[1:]
            node = root[0].get(char)
            if node:
                root = node
            else:
                return False
        return root[1]
        

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        while prefix:
            char = prefix[0]
            prefix = prefix[1:]
            node = root[0].get(char)
            if node:
                root = node
            else:
                return False
        return True
        
        