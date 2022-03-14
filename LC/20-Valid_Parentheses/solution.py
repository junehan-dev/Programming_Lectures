class Solution:
    def isValid(self, s: str) -> bool:
        MAX_LEN = 10000;
        try:
            return check_valid(s);
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

def check_valid(s: str):
    stack = [];
    is_pushed = [False, False, False];
    for ch in s:
        if not is_paren(ch):
            raise TypeError("not paren");

        if ch in "()":
            if ch == '(':
                if is_pushed[0] is False:
                    is_pushed[0] = True;
                else: 
                    print(s);
                    raise ValueError("( not closed");
            else:
                if is_pushed[0] is True:
                    is_pushed[0] = False;
                else: 
                    print(s);
                    raise ValueError("( not opened");
        elif ch in "[]":
            if ch == '[':
                if is_pushed[1] is False:
                    is_pushed[1] = True;
                else: 
                    print(s);
                    raise ValueError("[ not closed");
            else:
                if is_pushed[1] is True:
                    is_pushed[1] = False;
                else: 
                    print(s);
                    raise ValueError("[ not opened");
        else:
            if ch == '{':
                if is_pushed[2] is False:
                    is_pushed[2] = True;
                else: 
                    print(s);
                    raise ValueError("{ not closed");
            else:
                if is_pushed[2] is True:
                    is_pushed[2] = False;
                else: 
                    print(s);
                    raise ValueError("{ not opened");
        stack.append(ch);

    if any(is_pushed):
        raise ValueError("somthing not closed");

    return True;

if __name__ == "__main__":
    tests = "(),()[]{},(},(){".split(',');
    a_sol = Solution();
    results = list(map(a_sol.isValid, tests));
    print(results);
    
