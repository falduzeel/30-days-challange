scores = {
    "Alice": 95,
    "Bob": 82,
}

scores["Charlie"] = 88

print(scores["Alice"])

for student in scores:
    score = scores[student]
    print(f"{student} scored {score} points.")