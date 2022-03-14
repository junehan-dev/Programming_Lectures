class Solution:
    def isValid(self, s: str) -> bool:
        try:
            return check_valid_2(s);
        except ValueError as e:
            print(e.args);
#            raise e;
            return False;
        except TypeError as e:
            print(e.args);
#            raise e;
            return False;
        return True;
    
def is_paren(ch: str):
    if ch in "()[]{}":
        return True
    raise ValueError();

def check_valid_2(s: str):
    MAXLEN = 10000;
    stack = [];
    is_pushed = [False, False, False];
    print(s); 
    for ch in s:
        if not is_paren(ch):
            raise TypeError("not paren");

        if ch in "({[":
            if ch == '(':
                if is_pushed[0] is False:
                    is_pushed[0] = True;
                else: 
                    print(s);
                    raise ValueError("( not closed");
            elif ch == '[':
                if is_pushed[1] is False:
                    is_pushed[1] = True;
                else: 
                    print(s);
                    raise ValueError("[ not closed");
            else:
                if ch == '{':
                    if is_pushed[2] is False:
                        is_pushed[2] = True;
                else: 
                    print(s);
                    raise ValueError("{ not closed");
            stack.append(ch);

        else:
            if ch == ')':
                if is_pushed[0] is True and stack[-1] == '(':
                    is_pushed[0] = False;
                    stack.pop();
                else: 
                    print("close with", ch, ". stack:", stack);
                    raise ValueError(")close order error");
            elif ch == ']':
                if is_pushed[1] is True and stack[-1] == '[':
                    is_pushed[1] = False;
                    stack.pop();
                else: 
                    print("close with", ch, ". stack:", stack);
                    raise ValueError("]close order error");
            else:
                if is_pushed[2] is True and stack[-1] == '{':
                    is_pushed[2] = False;
                    stack.pop();
                else: 
                    print("close with", ch, ". stack:", stack);
                    raise ValueError("}close order error");

        if len(stack) > MAXLEN:
            return IndexError("over limit");

    if any(is_pushed):
        raise ValueError("somthing not closed");

    return True;

if __name__ == "__main__":
    tests = "(),()[]{},(},(){".split(',');
    a_sol = Solution();
    results = list(map(a_sol.isValid, tests));
    print(results, end="\n\n");
    test = "({)}";
    print(a_sol.isValid(test), end="\n\n");
    test = "({})";
    print(a_sol.isValid(test));
