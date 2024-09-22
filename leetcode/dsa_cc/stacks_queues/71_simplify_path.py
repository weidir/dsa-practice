class Solution:
    def simplifyPath(self, path: str) -> str:

        # Initialize stack
        stack = path.split('/')

        # Initialize the final answer
        simple_path = ["/"]
        
        # Loop through stack and look for the following:
        for idx, item in enumerate(stack):
            print(f"Pass {idx} - Item: '{item}'")
            if item == "..":
                # Protect against edge case where user tries to go above root directory
                if ''.join(simple_path) != "/":
                    last = simple_path.pop()
            elif item != "" and item != ".":
                simple_path.append(item + "/")
            
            print(f"Simple path: '{''.join(simple_path)}'\n")
        
        # Convert stack back into string
        simple_path = "".join(simple_path)

        # Remove trailing "/" if the final answer is not just the root directory "/"
        if len(simple_path) > 1:
            simple_path = simple_path[:-1]

        return simple_path


if __name__ == "__main__":
    sol = Solution()

    # path1 = "/home/"
    # ans1 = sol.simplifyPath(path1)
    # print(f"Answer 1: {ans1}")
    # assert ans1 == "/home"

    # path2 = "/home//foo/"
    # ans2 = sol.simplifyPath(path2)
    # print(f"Answer 2: {ans2}")
    # assert ans2 == "/home/foo"

    # path3 = "/home/user/Documents/../Pictures"
    # ans3 = sol.simplifyPath(path3)
    # print(f"Answer 3: {ans3}")
    # assert ans3 == "/home/user/Pictures"

    # path4 = "/../"
    # ans4 = sol.simplifyPath(path4)
    # print(f"Answer 4: {ans4}")
    # assert ans4 == "/"

    # path5 = "/.../a/../b/c/../d/./"
    # ans5 = sol.simplifyPath(path5)
    # print(f"Answer 5: {ans5}")
    # assert ans5 == "/.../b/d"

    path6 = "/a/../../b/../c//.//"
    ans6 = sol.simplifyPath(path6)
    print(f"Answer 6: {ans6}")
    # assert ans6 == "/c"