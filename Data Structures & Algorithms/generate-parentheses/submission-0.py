class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        op_pr = 0
        cl_pr = 0

        string = ""

        res = []

        def dbs(op_pr, cl_pr, cur):
            if (op_pr == n and cl_pr == n):
                res.append(cur)
                return
            if (cl_pr > op_pr):
                return
            
            if (op_pr == n):
                with_closed = cur + ")"
                dbs(n, cl_pr + 1, with_closed)
            else:   
                with_open = cur + "("
                with_closed = cur + ")"
                dbs(op_pr + 1, cl_pr, with_open)
                dbs(op_pr, cl_pr + 1, with_closed)
        
        dbs(1, 0, "(")
        return res