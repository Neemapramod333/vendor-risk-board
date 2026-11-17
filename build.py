import json, os, html

with open("vendors.json") as f:
    vendors = json.load(f)

colours = {"Low": "#1f7a4d", "Medium": "#8a5a00", "High": "#b4312b"}
rows = ""
for v in sorted(vendors, key=lambda v: v["score"], reverse=True):
    c = colours[v["riskCategory"]]
    rows += (
        f"<tr><td>{html.escape(v['vendor'])}</td>"
        f"<td style='color:{c};font-weight:bold'>{v['riskCategory']}</td>"
        f"<td>{v['score']}</td></tr>\n"
    )

run = os.environ.get("GITHUB_RUN_NUMBER", "local")
commit = os.environ.get("GITHUB_SHA", "local")[:7]

page = f"""<!DOCTYPE html>
<html>
<head><title>Vendor Risk Board (practice)</title></head>
<body style="font-family: Arial; padding: 40px;">
  <h1>Vendor Risk Board</h1>
  <p>Practice data only.</p>
  <table border="1" cellpadding="8" style="border-collapse: collapse;">
    <tr><th>Vendor</th><th>Risk</th><th>Score</th></tr>
{rows}  </table>
  <p style="color: grey;">Deployment #{run} · commit {commit}</p>
</body>
</html>
"""

os.makedirs("site", exist_ok=True)
with open("site/index.html", "w") as f:
    f.write(page)
print(f"Built page with {len(vendors)} vendors")
