# 71. Simplify Path - med
class Solution:
    def simplifyPath(self, path: str) -> str: # O(n) time, O(n) space
        '''
            Given a string absolute path (Unix-style which always begins with with /')
            You must transform this absolute path into its simplified canonical path

            Rules of a Unix-style file system:
              .     -> current dir
              ..    -> parent dir
              // or /// ... -> should be treated as /
              any sequence of periods that doesn't match the rules above should be treated as a VALID directory or file name
                - For example, ... and .... are valid directory or file names

            Rules of simplified canonical path
              path must start with /
              dirs within path must be separately by one slash /
              path must not end with / UNLESS it's the root directory
              path must not have any single or double periods used to denote current or parent directories

            Return the simplified canonical path

            So pretty much convert the Unix style path to a simplified canonical path
        '''
        # stack = [] # stores directories
        # current = [] # current dir

        # for char in path:
        #     if char == '/':
        #         part = "".join(current)

        #         if part == "..": # Go up one directory
        #             if stack:
        #                 stack.pop()
        #         elif part != "" and part != ".": # Normal directory names
        #             stack.append(part)
                
        #         current = [] # reset 
        #     else:
        #         current.append(char)
        
        # # Path may not end with /
        # part = "".join(current) 
        # if part == "..":
        #     if stack:
        #         stack.pop()
        # elif part != "" and part != ".":
        #     stack.append(part)

        # return "/" + "/".join(stack)

        stack = [] # to hold directories

        for part in path.split('/'):
            if part == "" or part == ".": # Ignore / and .
                continue
            elif part == "..": # Go to parent directory
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        
        return "/" + "/".join(stack)
