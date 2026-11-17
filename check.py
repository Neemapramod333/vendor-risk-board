import json, sys

with open("vendors.json") as f:
    vendors = json.load(f)   # fails here if the file is broken

problems = []
for v in vendors:
    name = v.get("vendor", "(no name)")
    score = v.get("score")
    category = v.get("riskCategory")

    if not isinstance(score, int) or not 0 <= score <= 100:
        problems.append(f"{name}: score must be a whole number from 0 to 100")
        continue

    # Business rule: 70 and above is High, 40 to 69 is Medium, below 40 is Low
    expected = "High" if score >= 70 else "Medium" if score >= 40 else "Low"
    if category != expected:
        problems.append(f"{name}: score {score} should be {expected}, not {category}")

if problems:
    print("Checks failed:")
    for p in problems:
        print(" -", p)
    sys.exit(1)

print(f"All {len(vendors)} vendors passed the checks")
