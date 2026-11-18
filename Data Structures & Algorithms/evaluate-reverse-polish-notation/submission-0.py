class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        operators = {"+", "-", "*", "/"}

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                arr.append(int(tokens[i]))
            else:
                ele2 = arr.pop()
                ele1 = arr.pop()
                val = 0
                if tokens[i] == "+":
                    val = ele1 + ele2
                elif (tokens[i] == "-"):
                    val = ele1 - ele2
                elif (tokens[i] == "*"):
                    val = ele1 * ele2
                else:
                    val = ele1 / ele2
                    if (val >= 0):
                        val = math.floor(val)
                    else:
                        val = math.ceil(val)
                arr.append(val)
        
        return arr[0]
        
            