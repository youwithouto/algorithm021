class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for payment in bills:
            if payment == 5:
                five += 1
            elif payment == 10 and five:
                ten += 1
                five -= 1
            elif payment == 20 and five and ten:
                five -= 1
                ten -= 1
            elif payment == 20 and five >= 3:
                five -= 3
            else:
                return False
        return True
