"""
Given a string s, return true if s is a valid number.

Input: s = "e"
Output: false

Input: s = "."
Output: false

Input: s = ".1"
Output: true

Idea: A number is a valid number if it has a digit, sign, dot and exponent in their valid order.
The valid permutations are:

With digits and dots and exponents

digit, sign, dot
digit, dot, exponent
digit, dot

digits and exponents
digit
digit, exponent

sign and digits
sign, digit
digit

We can create a list with this combinations which is essentially a DFA (Deterministic Finite Automata)
With this DFA, the valid end state would be whenever we end with digits.
We will maintain a current state and keep going to the next state using the DFA and we should eventully land at the valid state. 
Otherwise its not a number.

Constructing DFA:

O = start
    1 = digit
        digit can be on its own since more digits could be added so that node is circular
    2 = sign
        digit node to 1
        can also go to dot 3
    3 = dot
        needs to go to a digit, let's say state 4

    1 = digit
        Can also go to digit state 4 via a dot
        Can go to another state with an exponent, call it 5
    
    5 = exponent
        Can come from digit state 1 or 4
        exponent can be followed by a sign or a digit which can lead to 2 more states let's say 6 for one followed by sign and 7 for one followed by digit
    6 = sign
        needs a digit to go to state 7
    7 = digit
        digit here can be on its own since more digits could be added


Time Complexity: O(n), space: O(1)

s = .1, state = 0
for c in s:
    1. c = .
    group = dot
    state = dfa[0][dot] = 3
    2. c = 1
    group = digit
    state = dfa[3][digit] = 4
    since 4 is a valid end state, return True
"""

def isNumber(s: str) -> bool:
    # 0 is the start state of the DFA
    dfa = [
        {"digit": 1, "sign": 2, "dot": 3},
        {"digit": 1, "dot": 4, "exponent": 5},
        {"digit": 1, "dot": 3},
        {"digit": 4},
        {"digit": 4, "exponent": 5},
        {"sign": 6, "digit": 7},
        {"digit": 7},
        {"digit": 7}, # Why 2 digit: 7 ? Because we want to make sure that the DFA has an index for all possible states. Otherwise you would get an index out of bounds.
    ]

    state = 0
    for c in s:
        if c.isdigit():
            group = "digit"
        elif c in ['+', '-']:
            group = "sign"
        elif c in ['e', 'E']:
            group = "exponent"
        elif c == '.':
            group = "dot"
        else:
            return False
        
        if group not in dfa[state]:
            return False
        
        state = dfa[state][group]

    return state in [1, 4, 7]