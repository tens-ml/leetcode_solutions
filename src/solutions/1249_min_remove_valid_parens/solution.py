from src.runner import Runner

tests = [
    { 'args': { 's': 'lee(t(c)o)de)' }, 'expected': 'lee(t(c)o)de' },
    { 'args': { 's': 'a)b(c)d' }, 'expected': 'ab(c)d' },
    { 'args': { 's': '))((' }, 'expected': '' }
]


def solution(s: str) -> str:
    stack = []
    remove = []

    for idx, char in enumerate(list(s)):
        if char == '(':
            stack.append(idx)
        elif stack and char == ')':
            stack.pop()
        elif not stack and char == ')':
            remove.append(idx)
    
    remove_set = set(stack+remove)
    return ''.join([c for idx, c in enumerate(list(s)) if idx not in remove_set])

runner = Runner(tests=tests, solution=solution)
runner.run()