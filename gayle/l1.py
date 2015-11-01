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

        
if __name__ == "__main__":
    unittest.main()