import os
import random
from datetime import datetime
from bs4 import BeautifulSoup

# 设置根目录（自动使用脚本所在目录）
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TODAY = datetime.now().strftime("%Y-%m-%d")

# 更新 sitemap.xml 的 lastmod 字段
def update_sitemap():
    sitemap_path = os.path.join(ROOT_DIR, "sitemap.xml")
    if not os.path.exists(sitemap_path):
        print("❌ 未找到 sitemap.xml，跳过此步骤。")
        return
    with open(sitemap_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if "<loc>" in line and "<lastmod>" not in lines[lines.index(line)+1]:
            new_lines.append(f"  <lastmod>{TODAY}</lastmod>\n")
    
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print("✅ sitemap.xml 已添加 <lastmod> 字段")

# 对 HTML 页面内容区域打散结构
def shuffle_html_structure():
    html_files = [f for f in os.listdir(ROOT_DIR) if f.endswith(".html")]
    for file in html_files:
        path = os.path.join(ROOT_DIR, file)
        with open(path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        container = soup.find("div", class_="section")
        if container:
            children = container.find_all(recursive=False)
            random.shuffle(children)
            container.clear()
            for child in children:
                container.append(child)
            with open(path, "w", encoding="utf-8") as f:
                f.write(str(soup))
            print(f"✅ 页面已打散结构：{file}")
        else:
            print(f"⚠️ 未找到 section 区块，跳过：{file}")

if __name__ == "__main__":
    update_sitemap()
    shuffle_html_structure()
    print("\n🎉 所有处理完成。")
