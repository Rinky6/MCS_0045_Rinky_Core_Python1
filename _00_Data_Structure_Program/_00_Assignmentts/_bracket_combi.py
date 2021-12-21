'''
lst=[]

def printParenthesis(str, n):
    if (n > 0):
        _printParenthesis(str, 0,
                          n, 0, 0);
    return;


def _printParenthesis(str, pos, n,
                      open, close):
    if (close == n):
        for i in str:
            print(i, end="");
        print();
        return;
    else:
        if (open > close):
            str[pos] = ')';
            _printParenthesis(str, pos + 1, n,
                              open, close + 1);
        if (open < n):
            str[pos] = '(';
            _printParenthesis(str, pos + 1, n,
                              open + 1, close);



n = int(input("Enter the no"))
str = [""] * 2 * n;
print("no are : ", str)
printParenthesis(str, n);

'''
lst = []
def printBracket(ob, cb, n, s = []):
    if cb == n:
        com= ''.join(s)
        lst.append(com)
        return
    if cb < ob:
        s.append(')')
        printBracket(ob, cb + 1, n, s)
        s.pop()
    if ob < n:
        s.append('(')
        printBracket(ob+1, cb, n, s)
        s.pop()
        return
n=int(input("Enter no"))
printBracket(0, 0, n)

print("All combinations are : ", lst)




