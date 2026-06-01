names: list[str] = ["小明", "小红", "小刚"]
scores: list[int] = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"  {name}: {score}分")

print()
