import os
import re

target_name = "SGT Patrian"
target_ig = "https://www.instagram.com/sargento_patrian?stkn=ZnFjb21jMzJvbWps"

count = 0
for root, dirs, files in os.walk("."):
    if any(p in root for p in ["node_modules", ".git", "android/app/build"]):
        continue
    for file in files:
        if file.endswith((".js", ".jsx", ".ts", ".tsx", ".html", ".json")):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                updated = False
                if "zoonoses" in content.lower():
                    content = content.replace("Zoonoses", target_name)
                    content = content.replace("zoonoses", target_name)
                    updated = True
                
                if "instagram.com" in content:
                    content = re.sub(r'https?://(?:www\.)?instagram\.com/[^\s"\'\?]+(\?[^\s"\']*)?', target_ig, content)
                    updated = True

                if updated:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"Atualizado: {path}")
                    count += 1
            except Exception:
                pass

print(f"Total de ficheiros atualizados: {count}")
