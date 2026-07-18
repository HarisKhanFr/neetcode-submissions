class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token.isdigit() or token.startswith("-") and token[1:].isdigit():
                nums.append(int(token))
            else:
                num2 = nums.pop()
                num1 = nums.pop()

                match token:
                    case "*":
                        nums.append(num1 * num2)
                    case "-":
                        nums.append(num1 - num2)
                    case "+":
                        nums.append(num1 + num2)
                    case "/":
                        nums.append(int(num1 / num2))
        return nums[0]