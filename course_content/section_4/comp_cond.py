words1 = ["it", "was", "not", "easy", "to", "use", "python", "with", "WSL"]

words2 = [w for w in words1 if len(w) > 3] # 'if' acts as a filter for the for-loop
print(words2)
# ['easy', 'python', 'with']

words3 = [w.upper() if len(w) > 3 else w for w in words1] # the 'if-else' acts as a mapper for the for-loop
print(words3)
# ['it', 'was', 'not', 'EASY', 'to', 'use', 'PYTHON', 'WITH', 'WSL']