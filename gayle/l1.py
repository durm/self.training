import unittest


def t1(s):
    for i, c in enumerate(s):
        ss = s[:i]
        if c in ss:
            return False
    return True

        
def t2(s, c):
    return s[c:] + s[:c]
    

def t3(s1, s2):
    return len(set(s1) - set(s2)) == 0 and len(s1) == len(s2) and s1 != s2

    
def t4(s):
    return s.replace(" ", "%20")
    
    
def t5(s):
    curr = None
    n = 0
    result = ""
    for c in s:
        if curr == c:
            n += 1
        else:
            if curr is not None:
                result += curr + str(n)
            curr = c
            n = 1
    result += curr + str(n)
    return result if len(result) < len(s) else s

    
def t6(src):
    import copy
    trg = copy.deepcopy(src)
    ln = len(trg)
    trg = [[trg[j][i] for j in range(ln)] for i in range(ln)]
    trg = list(map(lambda l: list(reversed(l)), trg))
    return trg
    
    
def t7(src):
    trg = src.copy()
    nullrows = []
    nullcols = []
    for i, e in enumerate(src):
        if 0 in e:
            nullrows.append(i)
            for j, e2 in enumerate(e):
                if e2 == 0:
                    nullcols.append(j)
    return [[(0 if i in nullrows or j in nullcols else col) for j, col in enumerate(row)] for i, row in enumerate(src)]
    
    
def t8(src, trg):
    ln = len(src)
    if ln != len(trg):
        return False
    for i in range(1, ln-1):
        if src[i:] + src[:i] == trg:
            return True
    return False

    
class Tests(unittest.TestCase):
    
    
    def test_t1(self):
        self.assertFalse(t1("asdfsfgf"))
        self.assertTrue(t1("absdfgh"))

        
    def test_t2(self):    
        self.assertTrue(t2("asdfg", 2) == "dfgas")
    
    
    def test_t3(self):
        self.assertTrue(t3("zxc", "czx"))
        self.assertFalse(t3("zxc", "ccx"))
    
    
    def test_t4(self):
        self.assertEqual(t4("a b"), "a%20b")

        
    def test_t5(self):
        self.assertEqual(t5("aaabbnnnnn"), "a3b2n5")
        
        
    def test_t6(self):
        self.assertEqual(t6([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
        
        
    def test_t7(self):
        self.assertEqual(t7([[1, 2, 3], [4, 0, 6], [7, 8, 9]]), [[1, 0, 3], [0, 0, 0], [7, 0, 9]])
    
    
    def test_t8(self):
        self.assertTrue(t8("asb", "sba"))
    
    
if __name__ == "__main__":
    unittest.main()