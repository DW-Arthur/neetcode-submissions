class Solution:
    def calPoints(self, operations: List[str]) -> int:
        array = []
        result = 0
        for i in operations:
            if i == "C":
                array.pop()
            elif i =="D":
                prev = array[-1]
                print(prev)
                prev = prev *2
                array.append(prev)
                print(prev)
                print(array)
            elif i =="+":
                total = 0
                array.append(array[-1] + array[-2])
            else:
                num = int(i)
                array.append(num)
        for i in array:
            result +=i
        return result