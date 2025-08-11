import os
from PIL import Image, ImageChops
import numpy as np
import re
from bs4 import BeautifulSoup

# === 各種パス・ファイルリストの準備 ===

# テスト実行時のスクリーンショット格納フォルダ
current_folder = "../reports/screenshot"
# 正解（期待値）スクリーンショット格納フォルダ
collect_folder = "../reports/evidence"
# テンプレートHTML（各テストケースごと）のリスト
html_files = [f"../reports/template/report{i}.html" for i in range(1, 11)]
# 出力先ディレクトリ
output_dir = "../reports/generated"
# summary.htmlのパス
summary_path = os.path.join(output_dir, "summary.html")

# スクリーンショットファイル名の集合を取得
current_artifacts = set(os.listdir(current_folder))
collect_artifacts = set(os.listdir(collect_folder))
# 両方に存在するファイルのみ比較対象とする
common_files = current_artifacts & collect_artifacts

# 類似度結果を格納する辞書
similarity_dict = {}

# === 画像比較処理 ===
for filename in common_files:
    # path1: テスト実行時の画像, path2: 正解画像
    path1 = os.path.join(current_folder, filename)
    path2 = os.path.join(collect_folder, filename)
    
    try:
        # 画像をRGBで開く
        img1 = Image.open(path1).convert("RGB")
        img2 = Image.open(path2).convert("RGB")
        # 画像サイズが異なる場合は「サイズ不一致」とする
        if img1.size != img2.size:
            similarity = "サイズ不一致"
        else:
            # 差分画像を計算
            diff = ImageChops.difference(img1, img2)
            diff_np = np.array(diff)
            # 完全一致なら1.0000
            if np.all(diff_np == 0):
                similarity = "1.0000"
            else:
                # 一致率を計算し、1.0未満ならNG表記
                sim = 1 - (np.count_nonzero(diff_np) / diff_np.size)
                if sim == 1.0:
                    similarity = "1.0000"
                else:
                    similarity = f"NG：{sim*100:.2f}%"
        # ファイル名からキー（例: 123や123-1など）を抽出
        base = os.path.splitext(filename)[0]
        m = re.search(r'(\d{3}(?:-\d+)?)$', base)
        if m:
            key = m.group(1)
        else:
            key = base
        # 類似度を辞書に格納
        similarity_dict[key] = similarity
    except Exception as e:
        print(f"{filename}: 比較エラー {e}")

# === テンプレートHTMLの類似度埋め込み・保存 ===

# 出力ディレクトリがなければ作成
os.makedirs(output_dir, exist_ok=True)

# {similarity_XXX} を対応する値で置換する関数
def replace_similarity(match):
    key = match.group(1)
    return similarity_dict.get(key, "N/A")

# 各レポートのNG判定リスト
report_ng = []

for idx, html_path in enumerate(html_files, 1):
    if not os.path.exists(html_path):
        print(f"{html_path} が見つかりません。スキップします。")
        report_ng.append(True)  # ファイルがなければ失敗扱い
        continue
    with open(html_path, encoding="utf-8") as f:
        html = f.read()
    # {similarity_XXX} を実際の値で置換
    html = re.sub(r"\{similarity_([0-9]{3}(?:-\d+)?)\}", replace_similarity, html)
    # 埋め込んだ後のHTMLから類似度値を抽出し、1.0000以外があればNG
    similarities = re.findall(r'>(1\.0000|NG：[\d\.]+%|サイズ不一致)<', html)
    has_ng = any(s != "1.0000" for s in similarities)
    report_ng.append(has_ng)
    # 埋め込み済みHTMLをgeneratedディレクトリに保存
    output_path = os.path.join(output_dir, os.path.basename(html_path))
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{output_path} に埋め込み済みHTMLを保存しました。")

# === summary.htmlの「成功」「失敗」書き換え ===
if os.path.exists(summary_path):
    with open(summary_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    # 各reportXのidを「失敗」または「成功」に書き換え
    for i, ng in enumerate(report_ng, 1):
        tag = soup.find(id=f"report{i}")
        if tag:
            if ng:
                tag.string = "失敗"
                tag["class"] = "status-fail"
            else:
                tag.string = "成功"
                tag["class"] = "status-success"
    # summary.htmlを上書き保存
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("summary.htmlを更新しました。")
else:
    print("summary.htmlが見つかりません。更新をスキップします。")