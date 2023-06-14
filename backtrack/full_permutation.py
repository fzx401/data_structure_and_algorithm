def backtrack(nums, path: list, result):
    if len(path) == len(nums):
        result.append(path.copy())  # 注意这里不能直接append path本身，否则会传递引用进去
        return
    """
    应该如何去理解回溯的代码？
    首先，不要从入栈的好几个函数的角度去尝试逐层下沉和返回，否则很容易迷糊，这样去理解：
    循环nums时，对于每一个循环到的num，如果它不在当前的path里，就在path里加入它，然后调用backtrack函数
    最关键的是，不要去思考调用backtrack函数后新入栈的这个backtrack是怎么工作的
    只考虑我们当前层：backtrack后面紧跟着的，就是要把当前的num弹出，进入到下一个循环，这才是我们要考虑的
    """
    for num in nums:
        if num not in path:
            path.append(num)
            backtrack(nums, path, result)
            path.pop()

nums = [1, 2, 3]

def permute(num):
    result = []
    backtrack(num, [], result)
    return result
print(permute(nums))