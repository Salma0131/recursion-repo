def Fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)


def find_subsets(lst):
    if not lst:
        return [[]]

    smaller_subsets = find_subsets(lst[1:])

    subsets_with_current = []
    for subset in smaller_subsets:
        subsets_with_current.append([lst[0]] +subset)
    
    return smaller_subsets + subsets_with_current

# Example usage
print(find_subsets([1, 2]))
