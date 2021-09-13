# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 18/07/21
# -----------------------------------------------

# ***** Simplify Directory Path *****
# Given a string A representing an absolute path for a file (Unix-style).
#
# Return the string A after simplifying the absolute path.
#
# Note:
#
# Absolute path always begin with '/' ( root directory ).
#
# Path will not have whitespace characters.
#
#
# Input Format
#
# The only argument given is string A.
# Output Format
#
# Return a string denoting the simplified absolue path for a file (Unix-style).
# For Example
#
# Input 1:
#     A = "/home/"
# Output 1:
#     "/home"
#
# Input 2:
#     A = "/a/./b/../../c/"
# Output 2:
#     "/c"

class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        # stack to store the file's names.
        st = []

        # temporary string which stores the extracted
        # directory name or commands("." / "..")
        # Eg. "/a/b/../."
        # dir will contain "a", "b", "..", ".";
        dir = ""

        # contains resultant simplifies string.
        res = ""

        # every string starts from root directory.
        res += "/"

        # stores length of input string.
        len_A = len(A)
        i = 0
        while i < len_A:

            # we will clear the temporary string
            # every time to accommodate new directory
            # name or command.
            dir_str = ""

            # skip all the multiple '/' Eg. "##/""
            while i < len_A and A[i] == '/':
                i += 1

            # stores directory's name("a", "b" etc.)
            # or commands("."/"..") into dir
            while i < len_A and A[i] != '/':
                dir_str += A[i]
                i += 1

            # if dir has ".." just pop the topmost
            # element if the stack is not empty
            # otherwise ignore.
            if dir_str == "..":
                if len(st):
                    st.pop()

            # if dir has "." then simply continue
            # with the process.
            elif dir_str == '.':
                continue

            # pushes if it encounters directory's
            # name("a", "b").
            elif len(dir_str) > 0:
                st.append(dir_str)

            i += 1

        # a temporary stack (st1) which will contain
        # the reverse of original stack(st).
        st1 = []
        while len(st):
            st1.append(st[-1])
            st.pop()

        # the st1 will contain the actual res.
        while len(st1):
            temp = st1[-1]

            # if it's the last element no need
            # to append "/"
            if len(st1) != 1:
                res += (temp + "/")
            else:
                res += temp
            st1.pop()

        return res


s = Solution()
# print(s.simplifyPath("/a/./b/../../c/"))
# print(s.simplifyPath("/.."))
# print(s.simplifyPath("/home/"))
# print(s.simplifyPath("/home//foo/"))
print(s.simplifyPath("/./.././ykt/xhp/nka/eyo/blr/emm/xxm/fuv/bjg/./qbd/./../pir/dhu/./../../wrm/grm/ach/jsy/dic/ggz/smq/mhl/./../yte/hou/ucd/vnn/fpf/cnb/ouf/hqq/upz/akr/./pzo/../llb/./tud/olc/zns/fiv/./eeu/fex/rhi/pnm/../../kke/./eng/bow/uvz/jmz/hwb/./././ids/dwj/aqu/erf/./koz/.."))
