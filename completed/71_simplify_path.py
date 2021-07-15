class Solution:
    def simplifyPath(self, path: str) -> str:
        simplify_path_str = "/"

        directory_info = path.strip("/").split("/")
        stack: list = []

        pass_str = [".", "", ".."]
        for current_path in directory_info:
            if current_path == ".." and len(stack) != 0:
                stack.pop()
            elif current_path not in pass_str:
                stack.append(current_path)

        simplify_path_str += "/".join(stack)
        return simplify_path_str

path = "/a/./b/../../c/"
path = "/home//foo/"
path = "/../"
print(Solution().simplifyPath(path))