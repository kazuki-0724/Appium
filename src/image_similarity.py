import os
from PIL import Image, ImageChops
import numpy as np
import re

folder1 = "../reports/screenshot"
folder2 = "../reports/screenshot"
# 添え字
html_files = [f"../reports/template/report{i}.html" for i in range(1, 10)]
output_dir = "../reports/generated"

# 1. 画像比較して類似率を辞書に格納
files1 = set(os.listdir(folder1))
files2 = set(os.listdir(folder2))
common_files = files1 & files2

similarity_dict = {}

for filename in common_files:
    path1 = os.path.join(folder1, filename)
    path2 = os.path.join(folder2, filename)
    try:
        img1 = Image.open(path1).convert("RGB")
        img2 = Image.open(path2).convert("RGB")
        if img1.size != img2.size:
            similarity = "サイズ不一致"
        else:
            diff = ImageChops.difference(img1, img2)
            diff_np = np.array(diff)
            if np.all(diff_np == 0):
                similarity = "1.0000"
            else:
                similarity = f"{1 - (np.count_nonzero(diff_np) / diff_np.size):.4f}"
        # ファイル名からXXX部分を取得（拡張子除去、数字部分や -1 なども対応）
        base = os.path.splitext(filename)[0]
        m = re.search(r'(\d{3}(?:-\d+)?)$', base)
        if m:
            key = m.group(1)
        else:
            key = base
        similarity_dict[key] = similarity
    except Exception as e:
        print(f"{filename}: 比較エラー {e}")

# 2. 各HTMLファイルを読み込み、{similarity_XXX}を置換してgeneratedに保存
os.makedirs(output_dir, exist_ok=True)

def replace_similarity(match):
    key = match.group(1)
    return similarity_dict.get(key, "N/A")

for html_path in html_files:
    if not os.path.exists(html_path):
        print(f"{html_path} が見つかりません。スキップします。")
        continue
    with open(html_path, encoding="utf-8") as f:
        html = f.read()
    html = re.sub(r"\{similarity_([0-9]{3}(?:-\d+)?)\}", replace_similarity, html)
    output_path = os.path.join(output_dir, os.path.basename(html_path))
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{output_path} に埋め込み済みHTMLを保存しました。")