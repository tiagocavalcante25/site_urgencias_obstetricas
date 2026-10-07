import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("assets/js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

html_ids = set(re.findall(r'id=["\']([^"\']+)["\']', html))
js_ids = set(re.findall(r'getElementById\(["\']([^"\']+)["\']\)', js))

print(f"Total HTML IDs: {len(html_ids)}")
print(f"Total JS getElementById IDs: {len(js_ids)}")

missing_in_html = js_ids - html_ids
print("\nIDs in JS but missing in HTML:")
for i in sorted(missing_in_html):
    print(f"  - {i}")

found_in_both = js_ids & html_ids
print(f"\nIDs matched in both JS and HTML: {len(found_in_both)} / {len(js_ids)}")
