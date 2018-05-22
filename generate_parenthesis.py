def generateParenthesis(n):
    if n == 1:
        return ["()"]
    else:
        new = []
        array = generateParenthesis(n - 1)
        for i in array:
            for j in range(len(i)):
                a = i[:j]
                a += "()"
                a += i[j:]
                if a not in new:
                    new.append(a)
    return new

def generate(left,right,result,string):
    if left==0 and right==0:
        result.append(string)
        return
    if left:
        generate(left-1,right,result,string+"(")
    if left<right:
        generate(left,right-1,result,string+")")


def better_solution(n):
    left=n
    right=n
    result=[]
    generate(left,right,result,"")
    print(result)

# print(generateParenthesis(3))
better_solution(3)