class Solution:
    def isValid(self, s: str):
        return check_valid(s);

def check_valid(s: str):
    stack = [];
    is_pushed = [0, 0, 0];

    for ch in s:
        if ch in "({[":
            if ch == '(':
                is_pushed[0] += 1;
            elif ch == '[':
                is_pushed[1] += 1;
            else:
                is_pushed[2] += 1;

            if len(stack) > 10000:
                return False;
            stack.append(ch);

        elif ch in ")]}":
            if ch == ')':
                if is_pushed[0] and stack[-1] == '(':
                    is_pushed[0] -= 1;
                    stack.pop();
                else: 
                    return False;
            elif ch == ']':
                if is_pushed[1] and stack[-1] == '[':
                    is_pushed[1] -= 1;
                    stack.pop();
                else: 
                    return False;
            else:
                if is_pushed[2] and stack[-1] == '{':
                    is_pushed[2] -= 1;
                    stack.pop();
                else: 
                    return False;
        else:
            return False;
    return (False if any(is_pushed) else True);



if __name__ == "__main__":
    #tests = "(),()[]{},(},(){".split(',');
    a_sol = Solution();
    #results = list(map(a_sol.isValid, tests));
    #print(results, end="\n\n");
    #test = "({)}";
    #print(a_sol.isValid(test), end="\n\n");
    #test = "({})";
    #print(a_sol.isValid(test));
    test = "(([]))";
    print(a_sol.isValid(test));




