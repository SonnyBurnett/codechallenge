import unittest
import euler54 as e

class TestEuler54(unittest.TestCase):
    def test_isConsecutiveFalse(self):
        self.assertFalse(e.isConsecutive(e.sortHand(["7C", "7H", "7D", "2D", "2S"])),False)
        self.assertFalse(e.isConsecutive(e.sortHand(["7D", "7S", "5D", "3S", "7C"])),False)
       

    def test_isConsecutiveTrue(self):
            self.assertTrue(e.isConsecutive(e.sortHand(["3S", "4C", "5H", "6D", "7C"])),True)
            self.assertTrue(e.isConsecutive(e.sortHand(["TC", "JC", "QC", "KC", "AC"])),True)


    def test_royalFlush(self):
        self.assertTrue(e.royalFlush(["TC", "JC", "QC", "KC", "AC"])[0],True)
        self.assertFalse(e.royalFlush(["8C", "JC", "QC", "KC", "AC"])[0],False)
        self.assertFalse(e.royalFlush(["9C", "TC", "JC", "QC", "KC"])[0],False)

    def test_whathand(self):
        #Test RoyaFlush hand
        self.assertEqual(e.whathand(["TC", "JC", "QC", "KC", "AC"])[0][0], 10)
        
        #Test Straight Flush. All cards are consecutive values of same suit.
        self.assertEqual(e.whathand(["8C", "9C", "TC", "JC", "QC"])[0][0], 9)
        
        #Test Four of a Kind: Four cards of the same value.
        self.assertEqual(e.whathand(["TH", "TD", "TS", "TC", "AC"])[0][0], 8)
        
        #Test Full House: Three of a kind and a pair.
        self.assertEqual(e.whathand(["TH", "TD", "TS", "KC", "KS"])[0][0], 7)
        
        #Test Flush: All cards of the same suit.
        self.assertEqual(e.whathand(["2C", "4C", "6C", "7C", "TC"])[0][0], 6)
        
        #Test Straight: All cards are consecutive values
        self.assertEqual(e.whathand(["2C", "3D", "4C", "5S", "6C"])[0][0], 5)
        
        #Test Three of a Kind: Three cards of the same value
        self.assertEqual(e.whathand(["TC", "TH", "TS", "KD", "AS"])[0][0], 4)
        
        #Test One Pair: Two cards of the same value.
        self.assertEqual(e.whathand(["TC", "TD", "2C", "4S", "6D"])[0][0], 2)
        
        #High Card: Highest value card.
        self.assertEqual(e.whathand(["2C", "4H", "6D", "8S", "AC"])[0][0], 1)


    def test_pair(self):
        #Test Two Pairs: Two different pairs.

        res = e.pair(["TH", "TD", "QC", "QS", "AC"])
        twoPairs = False
        print(str(id(res[0])) + " " + str(res[0]))
        print(str(id(len(res[1]))) + " " + str(res[1]))
        if res[0] and len(res[1]) == 2:
            twoPairs = True
        
        self.assertTrue(twoPairs,True)


    def test_compareHands(self):
        #Player 1 wins
        pl1 = ["TC", "JC", "QC", "KC", "AC"] #Royal Flush
        pl2 = ["8C", "9C", "TC", "JC", "QC"] #Straight Flush

        res = e.compareHands(pl1, pl2)
        self.assertEqual(res[0], 1) 

        #Player 2 wins
        pl1 = ["TC", "JC", "QC", "KC", "AC"] #Royal Flush
        pl2 = ["8C", "9C", "TC", "JC", "QC"] #Straight Flush

        res = e.compareHands(pl2, pl1)
        self.assertEqual(res[0], 2) 
        
        #Draw
        pl1 = ["TC", "JC", "QC", "KC", "AC"] #Royal Flush
        pl2 = ["TC", "JC", "QC", "KC", "AC"] #Royal Flush

        res = e.compareHands(pl1, pl2)
        self.assertEqual(res[0], 0) 
        

        #Draw with high card comparison
        pl1 = ["TC", "TH", "TS", "3D", "5S"] #Three of a kind. High card 5. 
        pl2 = ["TC", "TH", "TS", "6D", "4S"] #Three of a kind. Hight card 6. WINS!

        res = e.compareHands(pl1, pl2)
        self.assertEqual(res[0], 2)


if __name__ == "__main__":
    unittest.main()