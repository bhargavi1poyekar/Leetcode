class Solution:
    def countSeniors(self, details: List[str]) -> int:

        passenger_60plus = 0

        for detail in details:
            age = int(detail[11:13])
            print(age)
            if age > 60:
                passenger_60plus += 1
        
        return passenger_60plus
