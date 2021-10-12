"""
Given a string path, which is an absolute path (starting with a slash '/') 
to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

Input: path = "/home/"
Output: "/home"

Input: path = "/../"
Output: "/"

Input: path = "/home//foo/"
Output: "/home/foo"

Input: path = "/a/./b/../../c/"
Output: "/c"

Idea: We can use stack to store the files and folders in path.
1. Split the string on the delimiter "/"
2. If the current component is a "..", then pop from stack if non-empty
3. A no-op for a "." or an empty string
4. If its a legitimate directory name, then add it to the stack.
5. Finally stitch together everything in the stack with delimiter.

O(n) time and space complexity.
"""
def simplifyPath(path: str) -> str:

    stack = []
    for s in path.split("/"):
        if s == "..":
            if stack:
                stack.pop()
        elif s == '.' or not s: # empty string is also a no-op
            continue
        else:
            stack.append(s)
    
    return "/" + "/".join(stack)