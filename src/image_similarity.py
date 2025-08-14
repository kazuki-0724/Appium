import os
from PIL import Image, ImageChops
import numpy as np
import re
from bs4 import BeautifulSoup
import threading
import sys
import time

# === スピナー表示 ===
def spinner_task(stop_event):
    spinner = ['|', '/', '-', '\\']
    idx = 0
    while not stop_event.is_set():
        sys.stdout.write('\r' + spinner[idx % len(spinner)] + ' 処理中...')
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
    sys.stdout.write('\rレポート生成が完了しました\n')


# === 画像比較処理 ===
def compare_images(current_folder, collect_folder):
    current_artifacts = set(os.listdir(current_folder))
    collect_artifacts = set(os.listdir(collect_folder))
    common_files = current_artifacts & collect_artifacts
    similarity_dict = {}

    for filename in common_files:
        path1 = os.path.join(current_folder, filename)
        path2 = os.path.join(collect_folder, filename)
        try:
            img1 = Image.open(path1).convert("RGB")
            img2 = Image.open(path2).convert("RGB")
            if img1.size != img2.size:
                similarity = "サイズ不一致"
            else:
                diff = ImageChops.difference(img1, img2)
                diff_np = np.array(diff)
                sim = 1 - (np.count_nonzero(diff_np) / diff_np.size)
                if np.all(diff_np == 0):
                    similarity = "OK"
                elif sim >= 0.970:
                    similarity = "OK"
                else:
                    similarity = f"NG：{sim:.5f}"
            base = os.path.splitext(filename)[0]
            m = re.search(r'(\d{3}(?:-\d+)?)$', base)
            if m:
                key = m.group(1)
            else:
                key = base
            similarity_dict[key] = similarity
        except Exception as e:
            print(f"{filename}: 比較エラー {e}")
    return similarity_dict


# === テンプレートHTMLの類似度埋め込み・保存 ===
def embed_similarity_and_save(html_files, similarity_dict, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    report_status = []

    def replace_similarity(match):
        key = match.group(1)
        return similarity_dict.get(key, "N/A")

    for idx, html_path in enumerate(html_files, 1):
        report_result = True
        if not os.path.exists(html_path):
            print(f"{html_path} が見つかりません。スキップします。")
            report_status.append("NG")
            continue
        with open(html_path, encoding="utf-8") as f:
            html = f.read()
        html = re.sub(r"\{similarity_([0-9]{3}(?:-\d+)?)\}", replace_similarity, html)
        # 判定: N/A, NG：, サイズ不一致が含まれていればNG
        if "N/A" in html or "NG：" in html or "サイズ不一致" in html:
            # print(f"{html_path} は要確認です")
            report_result = False
        
        if report_result:
            report_status.append("OK")
        else:
            report_status.append("NG")
        
        output_path = os.path.join(output_dir, os.path.basename(html_path))
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)
            
    return report_status


# === summary.htmlの「OK」「NG」書き換え ===
def update_summary_html(summary_path, report_status):
    if os.path.exists(summary_path):
        with open(summary_path, encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
        # report1はスプラッシュの確認のため除外
        for i, ng in enumerate(report_status, 2):
            tag = soup.find(id=f"report{i}")
            if tag:
                if ng == "NG":
                    tag.string = "要確認"
                    tag["class"] = "status-fail"
                else:
                    tag.string = "OK"
                    tag["class"] = "status-success"
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
    else:
        print("summary.htmlが見つかりません。更新をスキップします。")


# === メイン処理 ===
def main():
    # 各種パス・ファイルリストの準備
    current_folder = "../reports/screenshot"
    collect_folder = "../reports/evidence"
    html_files = [f"../reports/template/report{i}.html" for i in range(2, 12)]
    output_dir = "../reports/generated"
    summary_path = os.path.join(output_dir, "summary.html")

    # スピナー開始
    stop_event = threading.Event()
    spinner_thread = threading.Thread(target=spinner_task, args=(stop_event,))
    spinner_thread.start()

    # 画像比較
    similarity_dict = compare_images(current_folder, collect_folder)
    # 類似度埋め込み・保存
    report_status = embed_similarity_and_save(html_files, similarity_dict, output_dir)
    # summary.html更新
    update_summary_html(summary_path, report_status)

    # スピナー停止
    stop_event.set()
    spinner_thread.join()


if __name__ == "__main__":
    main()