class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
       
        if len(sentence1) != len(sentence2):
            return False 
        
       
        pairs_set = set()
        for w1, w2 in similarPairs:
            pairs_set.add((w1, w2))
            pairs_set.add((w2, w1))
            
       
        for w1, w2 in zip(sentence1, sentence2):
           
            if w1 != w2 and (w1, w2) not in pairs_set:
                return False
                
        
        return True
        
        
