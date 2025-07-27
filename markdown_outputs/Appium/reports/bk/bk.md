# ディレクトリ: Appium/reports/bk

---

### ファイル: Appium/reports/bk/report1.html

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=800, initial-scale=1.0">
    <title>スプラッシュ レポート</title>
    <style>
        body {
            background: linear-gradient(120deg, #232526 0%, #414345 100%);
            color: #f5f5f5;
            font-family: 'Meiryo', 'Yu Gothic', 'Segoe UI', sans-serif;
            margin: 0;
            padding: 0;
        }
        .header {
            background: #00adb5;
            color: #fff;
            padding: 28px 0 12px 0;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .header h1 {
            margin: 0;
            font-size: 2.1rem;
            letter-spacing: 0.08em;
        }
        .main {
            max-width: 700px;
            margin: 32px auto 0 auto;
            background: rgba(34, 40, 49, 0.97);
            border-radius: 14px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.12);
            padding: 32px 32px 24px 32px;
        }
        .main h2 {
            color: #ffd600;
            border-left: 6px solid #00adb5;
            padding-left: 12px;
            margin-top: 16px;
            margin-bottom: 18px;
            font-size: 1.3rem;
        }
        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            background: #393e46;
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        caption {
            caption-side: top;
            color: #00adb5;
            font-size: 1.1rem;
            font-weight: bold;
            margin-bottom: 6px;
            letter-spacing: 0.04em;
        }
        th, td {
            padding: 14px 10px;
            text-align: center;
        }
        th {
            background: #00adb5;
            color: #fff;
            font-size: 1.08rem;
            letter-spacing: 0.04em;
        }
        tr:nth-child(even) td {
            background: #232931;
        }
        tr:nth-child(odd) td {
            background: #393e46;
        }
        td {
            font-size: 1.05rem;
        }
        td img {
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.10);
            border: 1.5px solid #222831;
            background: #232931;
        }
        .similarity {
            color: #ffd600;
            font-weight: bold;
            font-size: 1.08rem;
        }
        .footer {
            text-align: center;
            color: #888;
            margin-top: 40px;
            font-size: 0.95rem;
        }
        @media (max-width: 800px) {
            .main {
                padding: 16px 2vw;
            }
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>スプラッシュ レポート</h1>
    </header>
    <main class="main">
        <h2>テストケース: スプラッシュ</h2>
        <table>
            <caption>No5</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_005}</td>
                <td><img src="../20250604/splash_005.png" width="200" alt="Splash Image"></td>
                <td><img src="../20250604/splash_005.png" width="200" alt="Splash Image"></td>
            </tr>
        </table>
    </main>
    <footer class="footer">
        <p>&copy; 2023 プロジェクトチーム</p>
    </footer>
</body>
</html>
```

---

### ファイル: Appium/reports/bk/report2.html

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=800, initial-scale=1.0">
    <title>未ログイントップ レポート</title>
    <style>
        body {
            background: linear-gradient(120deg, #232526 0%, #414345 100%);
            color: #f5f5f5;
            font-family: 'Meiryo', 'Yu Gothic', 'Segoe UI', sans-serif;
            margin: 0;
            padding: 0;
        }
        .header {
            background: #00adb5;
            color: #fff;
            padding: 28px 0 12px 0;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .header h1 {
            margin: 0;
            font-size: 2.1rem;
            letter-spacing: 0.08em;
        }
        .main {
            max-width: 800px;
            margin: 32px auto 0 auto;
            background: rgba(34, 40, 49, 0.97);
            border-radius: 14px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.12);
            padding: 32px 32px 24px 32px;
        }
        .main h2 {
            color: #ffd600;
            border-left: 6px solid #00adb5;
            padding-left: 12px;
            margin-top: 16px;
            margin-bottom: 18px;
            font-size: 1.3rem;
        }
        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            background: #393e46;
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        caption {
            caption-side: top;
            color: #00adb5;
            font-size: 1.1rem;
            font-weight: bold;
            margin-bottom: 6px;
            letter-spacing: 0.04em;
        }
        th, td {
            padding: 14px 10px;
            text-align: center;
        }
        th {
            background: #00adb5;
            color: #fff;
            font-size: 1.08rem;
            letter-spacing: 0.04em;
        }
        tr:nth-child(even) td {
            background: #232931;
        }
        tr:nth-child(odd) td {
            background: #393e46;
        }
        td {
            font-size: 1.05rem;
        }
        td img {
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.10);
            border: 1.5px solid #222831;
            background: #232931;
        }
        .similarity {
            color: #ffd600;
            font-weight: bold;
            font-size: 1.08rem;
        }
        .footer {
            text-align: center;
            color: #888;
            margin-top: 40px;
            font-size: 0.95rem;
        }
        @media (max-width: 900px) {
            .main {
                padding: 16px 2vw;
            }
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>未ログイントップ レポート</h1>
    </header>
    <main class="main">
        <h2>テストケース: 未ログイントップ</h2>
        <table>
            <caption>No7</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_007}</td>
                <td><img src="../20250604/no_login_top_007.png" width="200" alt="未ログイントップ"></td>
                <td><img src="../20250604/no_login_top_007.png" width="200" alt="未ログイントップ"></td>
            </tr>
        </table>
        <table>
            <caption>No10</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_010}</td>
                <td><img src="../20250604/no_login_top_010.png" width="200" alt="未ログイントップ"></td>
                <td><img src="../20250604/no_login_top_010.png" width="200" alt="未ログイントップ"></td>
            </tr>
        </table>
        <table>
            <caption>No12</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_012}</td>
                <td><img src="../20250604/no_login_top_012.png" width="200" alt="未ログイントップ"></td>
                <td><img src="../20250604/no_login_top_012.png" width="200" alt="未ログイントップ"></td>
            </tr>
        </table>
        <table>
            <caption>No16</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_016}</td>
                <td><img src="../20250604/no_login_top_016.png" width="200" alt="未ログイントップ"></td>
                <td><img src="../20250604/no_login_top_016.png" width="200" alt="未ログイントップ"></td>
            </tr>
        </table>
        <table>
            <caption>No21</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_021}</td>
                <td><img src="../20250604/no_login_top_021.png" width="200" alt="未ログイントップ"></td>
                <td><img src="../20250604/no_login_top_021.png" width="200" alt="未ログイントップ"></td>
            </tr>
        </table>
        <table>
            <caption>No22</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_022}</td>
                <td><img src="../20250604/account_create_022.png" width="200" alt="アカウント作成"></td>
                <td><img src="../20250604/account_create_022.png" width="200" alt="アカウント作成"></td>
            </tr>
        </table>
        <table>
            <caption>No23</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_023}</td>
                <td><img src="../20250604/account_create_023.png" width="200" alt="アカウント作成"></td>
                <td><img src="../20250604/account_create_023.png" width="200" alt="アカウント作成"></td>
            </tr>
        </table>
        <table>
            <caption>No24</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_024}</td>
                <td><img src="../20250604/account_create_024.png" width="200" alt="アカウント作成"></td>
                <td><img src="../20250604/account_create_024.png" width="200" alt="アカウント作成"></td>
            </tr>
        </table>
        <table>
            <caption>No28</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_028}</td>
                <td><img src="../20250604/account_create_028.png" width="200" alt="アカウント作成"></td>
                <td><img src="../20250604/account_create_028.png" width="200" alt="アカウント作成"></td>
            </tr>
        </table>
    </main>
    <footer class="footer">
        <p>&copy; 2023 プロジェクトチーム</p>
    </footer>
</body>
</html>
```

---

### ファイル: Appium/reports/bk/report3.html

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=800, initial-scale=1.0">
    <title>ログイン レポート</title>
    <style>
        body {
            background: linear-gradient(120deg, #232526 0%, #414345 100%);
            color: #f5f5f5;
            font-family: 'Meiryo', 'Yu Gothic', 'Segoe UI', sans-serif;
            margin: 0;
            padding: 0;
        }
        .header {
            background: #00adb5;
            color: #fff;
            padding: 28px 0 12px 0;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .header h1 {
            margin: 0;
            font-size: 2.1rem;
            letter-spacing: 0.08em;
        }
        .main {
            max-width: 800px;
            margin: 32px auto 0 auto;
            background: rgba(34, 40, 49, 0.97);
            border-radius: 14px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.12);
            padding: 32px 32px 24px 32px;
        }
        .main h2 {
            color: #ffd600;
            border-left: 6px solid #00adb5;
            padding-left: 12px;
            margin-top: 16px;
            margin-bottom: 18px;
            font-size: 1.3rem;
        }
        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            background: #393e46;
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        caption {
            caption-side: top;
            color: #00adb5;
            font-size: 1.1rem;
            font-weight: bold;
            margin-bottom: 6px;
            letter-spacing: 0.04em;
        }
        th, td {
            padding: 14px 10px;
            text-align: center;
        }
        th {
            background: #00adb5;
            color: #fff;
            font-size: 1.08rem;
            letter-spacing: 0.04em;
        }
        tr:nth-child(even) td {
            background: #232931;
        }
        tr:nth-child(odd) td {
            background: #393e46;
        }
        td {
            font-size: 1.05rem;
        }
        td img {
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.10);
            border: 1.5px solid #222831;
            background: #232931;
        }
        .similarity {
            color: #ffd600;
            font-weight: bold;
            font-size: 1.08rem;
        }
        .footer {
            text-align: center;
            color: #888;
            margin-top: 40px;
            font-size: 0.95rem;
        }
        @media (max-width: 900px) {
            .main {
                padding: 16px 2vw;
            }
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>ログイン レポート</h1>
    </header>
    <main class="main">
        <h2>テストケース: ログイン</h2>
        <table>
            <caption>No38</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_038}</td>
                <td><img src="../20250604/login_038.png" width="200" alt="Login Image"></td>
                <td><img src="../20250604/login_038.png" width="200" alt="Login Image"></td>
            </tr>
        </table>
        <table>
            <caption>No40</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_040}</td>
                <td><img src="../20250604/login_040.png" width="200" alt="Login Image"></td>
                <td><img src="../20250604/login_040.png" width="200" alt="Login Image"></td>
            </tr>
        </table>
        <table>
            <caption>No42</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_042}</td>
                <td><img src="../20250604/login_042.png" width="200" alt="Login Image"></td>
                <td><img src="../20250604/login_042.png" width="200" alt="Login Image"></td>
            </tr>
        </table>
        <table>
            <caption>No43</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_043}</td>
                <td><img src="../20250604/login_043.png" width="200" alt="Login Image"></td>
                <td><img src="../20250604/login_043.png" width="200" alt="Login Image"></td>
            </tr>
        </table>
        <table>
            <caption>No45</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_045}</td>
                <td><img src="../20250604/login_045.png" width="200" alt="Login Image"></td>
                <td><img src="../20250604/login_045.png" width="200" alt="Login Image"></td>
            </tr>
        </table>
        <table>
            <caption>No46</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_046}</td>
                <td><img src="../20250604/login_046.png" width="200" alt="Login Image"></td>
                <td><img src="../20250604/login_046.png" width="200" alt="Login Image"></td>
            </tr>
        </table>
        <table>
            <caption>No47</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_047}</td>
                <td><img src="../20250604/login_047.png" width="200" alt="Login Image"></td>
                <td><img src="../20250604/login_047.png" width="200" alt="Login Image"></td>
            </tr>
        </table>
        <table>
            <caption>No48</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_048}</td>
                <td><img src="../20250604/login_048.png" width="200" alt="Login Image"></td>
                <td><img src="../20250604/login_048.png" width="200" alt="Login Image"></td>
            </tr>
        </table>
        <table>
            <caption>No49</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_049}</td>
                <td><img src="../20250604/login_049.png" width="200" alt="Login Image"></td>
                <td><img src="../20250604/login_049.png" width="200" alt="Login Image"></td>
            </tr>
        </table>
    </main>
    <footer class="footer">
```

---

### ファイル: Appium/reports/bk/report4.html

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=800, initial-scale=1.0">
    <title>企画回選択 レポート</title>
    <style>
        body {
            background: linear-gradient(120deg, #232526 0%, #414345 100%);
            color: #f5f5f5;
            font-family: 'Meiryo', 'Yu Gothic', 'Segoe UI', sans-serif;
            margin: 0;
            padding: 0;
        }
        .header {
            background: #00adb5;
            color: #fff;
            padding: 28px 0 12px 0;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .header h1 {
            margin: 0;
            font-size: 2.1rem;
            letter-spacing: 0.08em;
        }
        .main {
            max-width: 800px;
            margin: 32px auto 0 auto;
            background: rgba(34, 40, 49, 0.97);
            border-radius: 14px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.12);
            padding: 32px 32px 24px 32px;
        }
        .main h2 {
            color: #ffd600;
            border-left: 6px solid #00adb5;
            padding-left: 12px;
            margin-top: 16px;
            margin-bottom: 18px;
            font-size: 1.3rem;
        }
        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            background: #393e46;
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        caption {
            caption-side: top;
            color: #00adb5;
            font-size: 1.1rem;
            font-weight: bold;
            margin-bottom: 6px;
            letter-spacing: 0.04em;
        }
        th, td {
            padding: 14px 10px;
            text-align: center;
        }
        th {
            background: #00adb5;
            color: #fff;
            font-size: 1.08rem;
            letter-spacing: 0.04em;
        }
        tr:nth-child(even) td {
            background: #232931;
        }
        tr:nth-child(odd) td {
            background: #393e46;
        }
        td {
            font-size: 1.05rem;
        }
        td img {
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.10);
            border: 1.5px solid #222831;
            background: #232931;
        }
        .similarity {
            color: #ffd600;
            font-weight: bold;
            font-size: 1.08rem;
        }
        .footer {
            text-align: center;
            color: #888;
            margin-top: 40px;
            font-size: 0.95rem;
        }
        @media (max-width: 900px) {
            .main {
                padding: 16px 2vw;
            }
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>企画回選択 レポート</h1>
    </header>
    <main class="main">
        <h2>テストケース: 企画回選択</h2>
        <table>
            <caption>No58</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_058}</td>
                <td><img src="../20250604/select_product_catalog_058.png" width="200" alt="企画回選択"></td>
                <td><img src="../20250604/select_product_catalog_058.png" width="200" alt="企画回選択"></td>
            </tr>
        </table>
        <table>
            <caption>No62</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_062}</td>
                <td><img src="../20250604/select_product_catalog_062.png" width="200" alt="企画回選択"></td>
                <td><img src="../20250604/select_product_catalog_062.png" width="200" alt="企画回選択"></td>
            </tr>
        </table>
    </main>
    <footer class="footer">
        <p>&copy; 2023 プロジェクトチーム</p>
    </footer>
```

---

### ファイル: Appium/reports/bk/report5.html

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=800, initial-scale=1.0">
    <title>買い物タブ レポート</title>
    <style>
        body {
            background: linear-gradient(120deg, #232526 0%, #414345 100%);
            color: #f5f5f5;
            font-family: 'Meiryo', 'Yu Gothic', 'Segoe UI', sans-serif;
            margin: 0;
            padding: 0;
        }
        .header {
            background: #00adb5;
            color: #fff;
            padding: 28px 0 12px 0;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .header h1 {
            margin: 0;
            font-size: 2.1rem;
            letter-spacing: 0.08em;
        }
        .main {
            max-width: 800px;
            margin: 32px auto 0 auto;
            background: rgba(34, 40, 49, 0.97);
            border-radius: 14px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.12);
            padding: 32px 32px 24px 32px;
        }
        .main h2 {
            color: #ffd600;
            border-left: 6px solid #00adb5;
            padding-left: 12px;
            margin-top: 16px;
            margin-bottom: 18px;
            font-size: 1.3rem;
        }
        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            background: #393e46;
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        caption {
            caption-side: top;
            color: #00adb5;
            font-size: 1.1rem;
            font-weight: bold;
            margin-bottom: 6px;
            letter-spacing: 0.04em;
        }
        th, td {
            padding: 14px 10px;
            text-align: center;
        }
        th {
            background: #00adb5;
            color: #fff;
            font-size: 1.08rem;
            letter-spacing: 0.04em;
        }
        tr:nth-child(even) td {
            background: #232931;
        }
        tr:nth-child(odd) td {
            background: #393e46;
        }
        td {
            font-size: 1.05rem;
        }
        td img {
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.10);
            border: 1.5px solid #222831;
            background: #232931;
        }
        .similarity {
            color: #ffd600;
            font-weight: bold;
            font-size: 1.08rem;
        }
        .footer {
            text-align: center;
            color: #888;
            margin-top: 40px;
            font-size: 0.95rem;
        }
        @media (max-width: 900px) {
            .main {
                padding: 16px 2vw;
            }
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>買い物タブ レポート</h1>
    </header>
    <main class="main">
        <h2>テストケース: 買い物タブ</h2>
        <table>
            <caption>No62</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_062}</td>
                <td><img src="../20250604/shopping_tab_062.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_062.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No66</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_066}</td>
                <td><img src="../20250604/shopping_tab_066.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_066.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No70</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_070}</td>
                <td><img src="../20250604/shopping_tab_070.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_070.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No71</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_071}</td>
                <td><img src="../20250604/shopping_tab_071.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_071.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No73</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_073}</td>
                <td><img src="../20250604/shopping_tab_073.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_073.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No75</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_075}</td>
                <td><img src="../20250604/shopping_tab_075.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_075.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No78</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_078}</td>
                <td><img src="../20250604/shopping_tab_078.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_078.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No79</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_079}</td>
                <td><img src="../20250604/shopping_tab_079.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_079.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No81</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_081}</td>
                <td><img src="../20250604/shopping_tab_081.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_081.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No82</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_082}</td>
                <td><img src="../20250604/shopping_tab_082.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_082.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No83</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_083}</td>
                <td><img src="../20250604/shopping_tab_083.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_083.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No84</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_084}</td>
                <td><img src="../20250604/shopping_tab_084.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_084.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No85</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_085}</td>
                <td><img src="../20250604/shopping_tab_085.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_085.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No86</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_086}</td>
                <td><img src="../20250604/shopping_tab_086.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_086.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No90</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_090}</td>
                <td><img src="../20250604/shopping_tab_090.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_090.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No91</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_091}</td>
                <td><img src="../20250604/shopping_tab_091.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_091.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No92</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_092}</td>
                <td><img src="../20250604/shopping_tab_092.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_092.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No93</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_093}</td>
                <td><img src="../20250604/shopping_tab_093.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_093.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No94</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_094}</td>
                <td><img src="../20250604/shopping_tab_094.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_094.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No95-1</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_095}</td>
                <td><img src="../20250604/shopping_tab_095-1.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_095-1.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No95-2</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_095}</td>
                <td><img src="../20250604/shopping_tab_095-2.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_095-2.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No96</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_096}</td>
                <td><img src="../20250604/shopping_tab_096.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_096.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
        <table>
            <caption>No97</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_097}</td>
                <td><img src="../20250604/shopping_tab_097.png" width="200" alt="買い物タブ"></td>
                <td><img src="../20250604/shopping_tab_097.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
    </main>
    <footer class="footer">
        <p>&copy; 2023 プロジェクトチーム</p>
    </footer>
</body>
</html>
```

---

### ファイル: Appium/reports/bk/report6.html

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=800, initial-scale=1.0">
    <title>Must Read Modal レポート</title>
    <style>
        body {
            background: linear-gradient(120deg, #232526 0%, #414345 100%);
            color: #f5f5f5;
            font-family: 'Meiryo', 'Yu Gothic', 'Segoe UI', sans-serif;
            margin: 0;
            padding: 0;
        }
        .header {
            background: #00adb5;
            color: #fff;
            padding: 28px 0 12px 0;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .header h1 {
            margin: 0;
            font-size: 2.1rem;
            letter-spacing: 0.08em;
        }
        .main {
            max-width: 800px;
            margin: 32px auto 0 auto;
            background: rgba(34, 40, 49, 0.97);
            border-radius: 14px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.12);
            padding: 32px 32px 24px 32px;
        }
        .main h2 {
            color: #ffd600;
            border-left: 6px solid #00adb5;
            padding-left: 12px;
            margin-top: 16px;
            margin-bottom: 18px;
            font-size: 1.3rem;
        }
        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            background: #393e46;
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        caption {
            caption-side: top;
            color: #00adb5;
            font-size: 1.1rem;
            font-weight: bold;
            margin-bottom: 6px;
            letter-spacing: 0.04em;
        }
        th, td {
            padding: 14px 10px;
            text-align: center;
        }
        th {
            background: #00adb5;
            color: #fff;
            font-size: 1.08rem;
            letter-spacing: 0.04em;
        }
        tr:nth-child(even) td {
            background: #232931;
        }
        tr:nth-child(odd) td {
            background: #393e46;
        }
        td {
            font-size: 1.05rem;
        }
        td img {
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.10);
            border: 1.5px solid #222831;
            background: #232931;
        }
        .similarity {
            color: #ffd600;
            font-weight: bold;
            font-size: 1.08rem;
        }
        .footer {
            text-align: center;
            color: #888;
            margin-top: 40px;
            font-size: 0.95rem;
        }
        @media (max-width: 900px) {
            .main {
                padding: 16px 2vw;
            }
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>Must Read Modal レポート</h1>
    </header>
    <main class="main">
        <h2>テストケース: 必読モーダル</h2>
        <table>
            <caption>No112</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_112}</td>
                <td><img src="../20250604/must_read_modal_112.png" width="200" alt="must_read_modal_112"></td>
                <td><img src="../20250604/must_read_modal_112.png" width="200" alt="must_read_modal_112"></td>
            </tr>
        </table>
        <table>
            <caption>No113</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_113}</td>
                <td><img src="../20250604/must_read_modal_113.png" width="200" alt="must_read_modal_113"></td>
                <td><img src="../20250604/must_read_modal_113.png" width="200" alt="must_read_modal_113"></td>
            </tr>
        </table>
        <table>
            <caption>No117</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_117}</td>
                <td><img src="../20250604/must_read_modal_117.png" width="200" alt="must_read_modal_117"></td>
                <td><img src="../20250604/must_read_modal_117.png" width="200" alt="must_read_modal_117"></td>
            </tr>
        </table>
        <table>
            <caption>No118</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_118}</td>
                <td><img src="../20250604/must_read_modal_118.png" width="200" alt="must_read_modal_118"></td>
                <td><img src="../20250604/must_read_modal_118.png" width="200" alt="must_read_modal_118"></td>
            </tr>
        </table>
        <table>
            <caption>No119</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_119}</td>
                <td><img src="../20250604/must_read_modal_119.png" width="200" alt="must_read_modal_119"></td>
                <td><img src="../20250604/must_read_modal_119.png" width="200" alt="must_read_modal_119"></td>
            </tr>
        </table>
        <table>
            <caption>No121</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_121}</td>
                <td><img src="../20250604/must_read_modal_121.png" width="200" alt="must_read_modal_121"></td>
                <td><img src="../20250604/must_read_modal_121.png" width="200" alt="must_read_modal_121"></td>
            </tr>
        </table>
        <table>
            <caption>No123</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_123}</td>
                <td><img src="../20250604/must_read_modal_123.png" width="200" alt="must_read_modal_123"></td>
                <td><img src="../20250604/must_read_modal_123.png" width="200" alt="must_read_modal_123"></td>
            </tr>
        </table>
        <table>
            <caption>No124</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_124}</td>
                <td><img src="../20250604/must_read_modal_124.png" width="200" alt="must_read_modal_124"></td>
                <td><img src="../20250604/must_read_modal_124.png" width="200" alt="must_read_modal_124"></td>
            </tr>
        </table>
        <table>
            <caption>No125</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_125}</td>
                <td><img src="../20250604/must_read_modal_125.png" width="200" alt="must_read_modal_125"></td>
                <td><img src="../20250604/must_read_modal_125.png" width="200" alt="must_read_modal_125"></td>
            </tr>
        </table>
    </main>
    <footer class="footer">
        <p>&copy; 2023 プロジェクトチーム</p>
    </footer>
</body>
</html>
```

---

### ファイル: Appium/reports/bk/report7.html

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=800, initial-scale=1.0">
    <title>パルくる便プロモーション レポート</title>
    <style>
        body {
            background: linear-gradient(120deg, #232526 0%, #414345 100%);
            color: #f5f5f5;
            font-family: 'Meiryo', 'Yu Gothic', 'Segoe UI', sans-serif;
            margin: 0;
            padding: 0;
        }
        .header {
            background: #00adb5;
            color: #fff;
            padding: 28px 0 12px 0;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .header h1 {
            margin: 0;
            font-size: 2.1rem;
            letter-spacing: 0.08em;
        }
        .main {
            max-width: 800px;
            margin: 32px auto 0 auto;
            background: rgba(34, 40, 49, 0.97);
            border-radius: 14px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.12);
            padding: 32px 32px 24px 32px;
        }
        .main h2 {
            color: #ffd600;
            border-left: 6px solid #00adb5;
            padding-left: 12px;
            margin-top: 16px;
            margin-bottom: 18px;
            font-size: 1.3rem;
        }
        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            background: #393e46;
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        caption {
            caption-side: top;
            color: #00adb5;
            font-size: 1.1rem;
            font-weight: bold;
            margin-bottom: 6px;
            letter-spacing: 0.04em;
        }
        th, td {
            padding: 14px 10px;
            text-align: center;
        }
        th {
            background: #00adb5;
            color: #fff;
            font-size: 1.08rem;
            letter-spacing: 0.04em;
        }
        tr:nth-child(even) td {
            background: #232931;
        }
        tr:nth-child(odd) td {
            background: #393e46;
        }
        td {
            font-size: 1.05rem;
        }
        td img {
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.10);
            border: 1.5px solid #222831;
            background: #232931;
        }
        .similarity {
            color: #ffd600;
            font-weight: bold;
            font-size: 1.08rem;
        }
        .footer {
            text-align: center;
            color: #888;
            margin-top: 40px;
            font-size: 0.95rem;
        }
        @media (max-width: 900px) {
            .main {
                padding: 16px 2vw;
            }
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>パルくる便プロモーション レポート</h1>
    </header>
    <main class="main">
        <h2>テストケース: パルくる便プロモーション</h2>
        <table>
            <caption>No130</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_130}</td>
                <td><img src="../20250604/pal_promo_130.png" width="200" alt="pal_promo_130"></td>
                <td><img src="../20250604/pal_promo_130.png" width="200" alt="pal_promo_130"></td>
            </tr>
        </table>
        <!--
        <table>
            <caption>No132</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_132}</td>
                <td><img src="../20250604/pal_promo_132.png" width="200" alt="pal_promo_132"></td>
                <td><img src="../20250604/pal_promo_132.png" width="200" alt="pal_promo_132"></td>
            </tr>
        </table>
        <table>
            <caption>No134</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_134}</td>
                <td><img src="../20250604/pal_promo_134.png" width="200" alt="pal_promo_134"></td>
                <td><img src="../20250604/pal_promo_134.png" width="200" alt="pal_promo_134"></td>
            </tr>
        </table>
        -->
        <table>
            <caption>No136</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_136}</td>
                <td><img src="../20250604/pal_promo_136.png" width="200" alt="pal_promo_136"></td>
                <td><img src="../20250604/pal_promo_136.png" width="200" alt="pal_promo_136"></td>
            </tr>
        </table>
        <table>
            <caption>No137</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_137}</td>
                <td><img src="../20250604/pal_promo_137.png" width="200" alt="pal_promo_137"></td>
                <td><img src="../20250604/pal_promo_137.png" width="200" alt="pal_promo_137"></td>
            </tr>
        </table>
    </main>
    <footer class="footer">
        <p>&copy; 2023 プロジェクトチーム</p>
    </footer>
</body>
</html>
```

---

### ファイル: Appium/reports/bk/report8.html

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=800, initial-scale=1.0">
    <title>商品検索テスト レポート</title>
    <style>
        body {
            background: linear-gradient(120deg, #232526 0%, #414345 100%);
            color: #f5f5f5;
            font-family: 'Meiryo', 'Yu Gothic', 'Segoe UI', sans-serif;
            margin: 0;
            padding: 0;
        }
        .header {
            background: #00adb5;
            color: #fff;
            padding: 28px 0 12px 0;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .header h1 {
            margin: 0;
            font-size: 2.1rem;
            letter-spacing: 0.08em;
        }
        .main {
            max-width: 900px;
            margin: 32px auto 0 auto;
            background: rgba(34, 40, 49, 0.97);
            border-radius: 14px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.12);
            padding: 32px 32px 24px 32px;
        }
        .main h2 {
            color: #ffd600;
            border-left: 6px solid #00adb5;
            padding-left: 12px;
            margin-top: 16px;
            margin-bottom: 18px;
            font-size: 1.3rem;
        }
        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            background: #393e46;
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        caption {
            caption-side: top;
            color: #00adb5;
            font-size: 1.1rem;
            font-weight: bold;
            margin-bottom: 6px;
            letter-spacing: 0.04em;
        }
        th, td {
            padding: 14px 10px;
            text-align: center;
        }
        th {
            background: #00adb5;
            color: #fff;
            font-size: 1.08rem;
            letter-spacing: 0.04em;
        }
        tr:nth-child(even) td {
            background: #232931;
        }
        tr:nth-child(odd) td {
            background: #393e46;
        }
        td {
            font-size: 1.05rem;
        }
        td img {
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.10);
            border: 1.5px solid #222831;
            background: #232931;
        }
        .similarity {
            color: #ffd600;
            font-weight: bold;
            font-size: 1.08rem;
        }
        .footer {
            text-align: center;
            color: #888;
            margin-top: 40px;
            font-size: 0.95rem;
        }
        @media (max-width: 900px) {
            .main {
                padding: 16px 2vw;
            }
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>商品検索テスト レポート</h1>
    </header>
    <main class="main">
        <h2>テストケース: 商品検索</h2>
        <table>
            <caption>No139</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_139}</td>
                <td><img src="../20250604/item_search_139.png" width="200" alt="item_search_139"></td>
                <td><img src="../20250604/item_search_139.png" width="200" alt="item_search_139"></td>
            </tr>
        </table>
        <table>
            <caption>No140</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_140}</td>
                <td><img src="../20250604/item_search_140.png" width="200" alt="item_search_140"></td>
                <td><img src="../20250604/item_search_140.png" width="200" alt="item_search_140"></td>
            </tr>
        </table>
        <table>
            <caption>No141</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_141}</td>
                <td><img src="../20250604/item_search_141.png" width="200" alt="item_search_141"></td>
                <td><img src="../20250604/item_search_141.png" width="200" alt="item_search_141"></td>
            </tr>
        </table>
        <table>
            <caption>No142</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_142}</td>
                <td><img src="../20250604/item_search_142.png" width="200" alt="item_search_142"></td>
                <td><img src="../20250604/item_search_142.png" width="200" alt="item_search_142"></td>
            </tr>
        </table>
        <table>
            <caption>No143</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_143}</td>
                <td><img src="../20250604/item_search_143.png" width="200" alt="item_search_143"></td>
                <td><img src="../20250604/item_search_143.png" width="200" alt="item_search_143"></td>
            </tr>
        </table>
        <table>
            <caption>No146</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_146}</td>
                <td><img src="../20250604/item_search_146.png" width="200" alt="item_search_146"></td>
                <td><img src="../20250604/item_search_146.png" width="200" alt="item_search_146"></td>
            </tr>
        </table>
        <table>
            <caption>No147</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_147}</td>
                <td><img src="../20250604/item_search_147.png" width="200" alt="item_search_147"></td>
                <td><img src="../20250604/item_search_147.png" width="200" alt="item_search_147"></td>
            </tr>
        </table>
        <table>
            <caption>No148</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_148}</td>
                <td><img src="../20250604/item_search_148.png" width="200" alt="item_search_148"></td>
                <td><img src="../20250604/item_search_148.png" width="200" alt="item_search_148"></td>
            </tr>
        </table>
        <table>
            <caption>No150</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_150}</td>
                <td><img src="../20250604/item_search_150.png" width="200" alt="item_search_150"></td>
                <td><img src="../20250604/item_search_150.png" width="200" alt="item_search_150"></td>
            </tr>
        </table>
        <table>
            <caption>No151</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_151}</td>
                <td><img src="../20250604/item_search_151.png" width="200" alt="item_search_151"></td>
                <td><img src="../20250604/item_search_151.png" width="200" alt="item_search_151"></td>
            </tr>
        </table>
        <table>
            <caption>No152</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_152}</td>
                <td><img src="../20250604/item_search_152.png" width="200" alt="item_search_152"></td>
                <td><img src="../20250604/item_search_152.png" width="200" alt="item_search_152"></td>
            </tr>
        </table>
        <table>
            <caption>No154</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_154}</td>
                <td><img src="../20250604/item_search_154.png" width="200" alt="item_search_154"></td>
                <td><img src="../20250604/item_search_154.png" width="200" alt="item_search_154"></td>
            </tr>
        </table>
        <table>
            <caption>No155</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_155}</td>
                <td><img src="../20250604/item_search_155.png" width="200" alt="item_search_155"></td>
                <td><img src="../20250604/item_search_155.png" width="200" alt="item_search_155"></td>
            </tr>
        </table>
        <table>
            <caption>No158</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_158}</td>
                <td><img src="../20250604/item_search_158.png" width="200" alt="item_search_158"></td>
                <td><img src="../20250604/item_search_158.png" width="200" alt="item_search_158"></td>
            </tr>
        </table>
        <table>
            <caption>No159</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_159}</td>
                <td><img src="../20250604/item_search_159.png" width="200" alt="item_search_159"></td>
                <td><img src="../20250604/item_search_159.png" width="200" alt="item_search_159"></td>
            </tr>
        </table>
        <table>
            <caption>No161</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_161}</td>
                <td><img src="../20250604/item_search_161.png" width="200" alt="item_search_161"></td>
                <td><img src="../20250604/item_search_161.png" width="200" alt="item_search_161"></td>
            </tr>
        </table>
        <table>
            <caption>No164</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_164}</td>
                <td><img src="../20250604/item_search_164.png" width="200" alt="item_search_164"></td>
                <td><img src="../20250604/item_search_164.png" width="200" alt="item_search_164"></td>
            </tr>
        </table>
        <table>
            <caption>No165</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_165}</td>
                <td><img src="../20250604/item_search_165.png" width="200" alt="item_search_165"></td>
                <td><img src="../20250604/item_search_165.png" width="200" alt="item_search_165"></td>
            </tr>
        </table>
        <table>
            <caption>No166</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_166}</td>
                <td><img src="../20250604/item_search_166.png" width="200" alt="item_search_166"></td>
                <td><img src="../20250604/item_search_166.png" width="200" alt="item_search_166"></td>
            </tr>
        </table>
    </main>
    <footer class="footer">
        <p>&copy; 2023 プロジェクトチーム</p>
```

---

### ファイル: Appium/reports/bk/report9.html

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=800, initial-scale=1.0">
    <title>カゴ画面テスト レポート</title>
    <style>
        body {
            background: linear-gradient(120deg, #232526 0%, #414345 100%);
            color: #f5f5f5;
            font-family: 'Meiryo', 'Yu Gothic', 'Segoe UI', sans-serif;
            margin: 0;
            padding: 0;
        }
        .header {
            background: #00adb5;
            color: #fff;
            padding: 28px 0 12px 0;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .header h1 {
            margin: 0;
            font-size: 2.1rem;
            letter-spacing: 0.08em;
        }
        .main {
            max-width: 900px;
            margin: 32px auto 0 auto;
            background: rgba(34, 40, 49, 0.97);
            border-radius: 14px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.12);
            padding: 32px 32px 24px 32px;
        }
        .main h2 {
            color: #ffd600;
            border-left: 6px solid #00adb5;
            padding-left: 12px;
            margin-top: 16px;
            margin-bottom: 18px;
            font-size: 1.3rem;
        }
        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            background: #393e46;
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        caption {
            caption-side: top;
            color: #00adb5;
            font-size: 1.1rem;
            font-weight: bold;
            margin-bottom: 6px;
            letter-spacing: 0.04em;
        }
        th, td {
            padding: 14px 10px;
            text-align: center;
        }
        th {
            background: #00adb5;
            color: #fff;
            font-size: 1.08rem;
            letter-spacing: 0.04em;
        }
        tr:nth-child(even) td {
            background: #232931;
        }
        tr:nth-child(odd) td {
            background: #393e46;
        }
        td {
            font-size: 1.05rem;
        }
        td img {
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.10);
            border: 1.5px solid #222831;
            background: #232931;
        }
        .similarity {
            color: #ffd600;
            font-weight: bold;
            font-size: 1.08rem;
        }
        .footer {
            text-align: center;
            color: #888;
            margin-top: 40px;
            font-size: 0.95rem;
        }
        @media (max-width: 900px) {
            .main {
                padding: 16px 2vw;
            }
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>カゴ画面テスト レポート</h1>
    </header>
    <main class="main">
        <h2>テストケース: カゴ画面</h2>
        <table>
            <caption>No168</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_168}</td>
                <td><img src="../20250608/cart_168.png" width="200" alt="cart_168"></td>
                <td><img src="../20250608/cart_168.png" width="200" alt="cart_168"></td>
            </tr>
        </table>
        <table>
            <caption>No171</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_171}</td>
                <td><img src="../20250608/cart_171.png" width="200" alt="cart_171"></td>
                <td><img src="../20250608/cart_171.png" width="200" alt="cart_171"></td>
            </tr>
        </table>
        <table>
            <caption>No174</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_174}</td>
                <td><img src="../20250608/cart_174.png" width="200" alt="cart_174"></td>
                <td><img src="../20250608/cart_174.png" width="200" alt="cart_174"></td>
            </tr>
        </table>
        <table>
            <caption>No177</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_177}</td>
                <td><img src="../20250608/cart_177.png" width="200" alt="cart_177"></td>
                <td><img src="../20250608/cart_177.png" width="200" alt="cart_177"></td>
            </tr>
        </table>
        <table>
            <caption>No194</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_194}</td>
                <td><img src="../20250608/cart_194.png" width="200" alt="cart_194"></td>
                <td><img src="../20250608/cart_194.png" width="200" alt="cart_194"></td>
            </tr>
        </table>
        <table>
            <caption>No195</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_195}</td>
                <td><img src="../20250608/cart_195.png" width="200" alt="cart_195"></td>
                <td><img src="../20250608/cart_195.png" width="200" alt="cart_195"></td>
            </tr>
        </table>
        <table>
            <caption>No196</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_196}</td>
                <td><img src="../20250608/cart_196.png" width="200" alt="cart_196"></td>
                <td><img src="../20250608/cart_196.png" width="200" alt="cart_196"></td>
            </tr>
        </table>
        <table>
            <caption>No198</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_198}</td>
                <td><img src="../20250608/cart_198.png" width="200" alt="cart_198"></td>
                <td><img src="../20250608/cart_198.png" width="200" alt="cart_198"></td>
            </tr>
        </table>
        <table>
            <caption>No199</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_199}</td>
                <td><img src="../20250608/cart_199.png" width="200" alt="cart_199"></td>
                <td><img src="../20250608/cart_199.png" width="200" alt="cart_199"></td>
            </tr>
        </table>
        <table>
            <caption>No201</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_201}</td>
                <td><img src="../20250608/cart_201.png" width="200" alt="cart_201"></td>
                <td><img src="../20250608/cart_201.png" width="200" alt="cart_201"></td>
            </tr>
        </table>
        <table>
            <caption>No203</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_203}</td>
                <td><img src="../20250608/cart_203.png" width="200" alt="cart_203"></td>
                <td><img src="../20250608/cart_203.png" width="200" alt="cart_203"></td>
            </tr>
        </table>
        <table>
            <caption>No207</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_207}</td>
                <td><img src="../20250608/cart_207.png" width="200" alt="cart_207"></td>
                <td><img src="../20250608/cart_207.png" width="200" alt="cart_207"></td>
            </tr>
        </table>
        <table>
            <caption>No209</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_209}</td>
                <td><img src="../20250608/cart_209.png" width="200" alt="cart_209"></td>
                <td><img src="../20250608/cart_209.png" width="200" alt="cart_209"></td>
            </tr>
        </table>
        <table>
            <caption>No213</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_213}</td>
                <td><img src="../20250608/cart_213.png" width="200" alt="cart_213"></td>
                <td><img src="../20250608/cart_213.png" width="200" alt="cart_213"></td>
            </tr>
        </table>
        <table>
            <caption>No214</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_214}</td>
                <td><img src="../20250608/cart_214.png" width="200" alt="cart_214"></td>
                <td><img src="../20250608/cart_214.png" width="200" alt="cart_214"></td>
            </tr>
        </table>
        <table>
            <caption>No229</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_229}</td>
                <td><img src="../20250608/cart_229.png" width="200" alt="cart_229"></td>
                <td><img src="../20250608/cart_229.png" width="200" alt="cart_229"></td>
            </tr>
        </table>
        <table>
            <caption>No230</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_230}</td>
                <td><img src="../20250608/cart_230.png" width="200" alt="cart_230"></td>
                <td><img src="../20250608/cart_230.png" width="200" alt="cart_230"></td>
            </tr>
        </table>
        <table>
            <caption>No231</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_231}</td>
                <td><img src="../20250608/cart_231.png" width="200" alt="cart_231"></td>
                <td><img src="../20250608/cart_231.png" width="200" alt="cart_231"></td>
            </tr>
        </table>
        <table>
            <caption>No234</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_234}</td>
                <td><img src="../20250608/cart_234.png" width="200" alt="cart_234"></td>
                <td><img src="../20250608/cart_234.png" width="200" alt="cart_234"></td>
            </tr>
        </table>
        <table>
            <caption>No235</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_235}</td>
                <td><img src="../20250608/cart_235.png" width="200" alt="cart_235"></td>
                <td><img src="../20250608/cart_235.png" width="200" alt="cart_235"></td>
            </tr>
        </table>
        <table>
            <caption>No236</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_236}</td>
                <td><img src="../20250608/cart_236.png" width="200" alt="cart_236"></td>
                <td><img src="../20250608/cart_236.png" width="200" alt="cart_236"></td>
            </tr>
        </table>
        <table>
            <caption>No237</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_237}</td>
                <td><img src="../20250608/cart_237.png" width="200" alt="cart_237"></td>
                <td><img src="../20250608/cart_237.png" width="200" alt="cart_237"></td>
            </tr>
        </table>
        <table>
            <caption>No239</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_239}</td>
                <td><img src="../20250608/cart_239.png" width="200" alt="cart_239"></td>
                <td><img src="../20250608/cart_239.png" width="200" alt="cart_239"></td>
            </tr>
        </table>
        <table>
            <caption>No241</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_241}</td>
                <td><img src="../20250608/cart_241.png" width="200" alt="cart_241"></td>
                <td><img src="../20250608/cart_241.png" width="200" alt="cart_241"></td>
            </tr>
        </table>
        <table>
            <caption>No242</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_242}</td>
                <td><img src="../20250608/cart_242.png" width="200" alt="cart_242"></td>
                <td><img src="../20250608/cart_242.png" width="200" alt="cart_242"></td>
            </tr>
        </table>
        <table>
            <caption>No244</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_244}</td>
                <td><img src="../20250608/cart_244.png" width="200" alt="cart_244"></td>
                <td><img src="../20250608/cart_244.png" width="200" alt="cart_244"></td>
            </tr>
        </table>
    </main>
    <footer class="footer">
        <p>&copy; 2023
```

---

### ファイル: Appium/reports/bk/summary.html

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=800, initial-scale=1.0">
    <title>レポートの概要</title>
    <link rel="stylesheet" href="../css/style.css">
    <style>
        body {
            background: linear-gradient(120deg, #232526 0%, #414345 100%);
            color: #f5f5f5;
            font-family: 'Meiryo', 'Yu Gothic', 'Segoe UI', sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background: #00adb5;
            color: #fff;
            padding: 32px 0 16px 0;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        header h1 {
            margin: 0;
            font-size: 2.4rem;
            letter-spacing: 0.1em;
        }
        main {
            max-width: 900px;
            margin: 32px auto 0 auto;
            background: rgba(34, 40, 49, 0.95);
            border-radius: 16px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.12);
            padding: 32px 40px 24px 40px;
        }
        h2 {
            color: #ffd600;
            border-left: 6px solid #00adb5;
            padding-left: 12px;
            margin-top: 32px;
            margin-bottom: 16px;
            font-size: 1.4rem;
        }
        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            background: #393e46;
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        th, td {
            padding: 14px 10px;
            text-align: center;
        }
        th {
            background: #00adb5;
            color: #fff;
            font-size: 1.1rem;
            letter-spacing: 0.05em;
        }
        tr:nth-child(even) td {
            background: #232931;
        }
        tr:nth-child(odd) td {
            background: #393e46;
        }
        td {
            font-size: 1.05rem;
        }
        td a {
            color: #ffd600;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.2s;
        }
        td a:hover {
            color: #00fff5;
            text-decoration: underline;
        }
        .status-success {
            color: #00ff99;
            font-weight: bold;
        }
        .status-fail {
            color: #ff5252;
            font-weight: bold;
        }
        section {
            margin-bottom: 32px;
        }
        footer {
            text-align: center;
            color: #888;
            margin-top: 40px;
            font-size: 0.95rem;
        }
        @media (max-width: 900px) {
            main {
                padding: 16px 4vw;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>標準テストレポート</h1>
    </header>
    <main>
        <section>
            <h2>最終実行結果</h2>
            <p>最終実行</p>
            <p>テスト成功率：<span style="color:#ffd600;font-weight:bold;">hogehoge%</span></p>
        </section>
        <section>
            <h2>各ケース</h2>
            <table>
                <thead>
                    <tr>
                        <th>ケース名</th>
                        <th>結果</th>
                        <th>詳細</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>スプラッシュ画面</td>
                        <td class="status-success">成功</td>
                        <td><a href="generated/report1.html">詳細を見る</a></td>
                    </tr>
                    <tr>
                        <td>未ログイントップ画面</td>
                        <td class="status-fail">失敗</td>
                        <td><a href="generated/report2.html">詳細を見る</a></td>
                    </tr>
                    <tr>
                        <td>ログイン画面</td>
                        <td class="status-success">成功</td>
                        <td><a href="generated/report3.html">詳細を見る</a></td>
                    </tr>
                    <tr>
                        <td>企画回選択</td>
                        <td class="status-fail">失敗</td>
                        <td><a href="generated/report4.html">詳細を見る</a></td>
                    </tr>
                    <tr>
                        <td>買い物タブ</td>
                        <td class="status-success">成功</td>
                        <td><a href="generated/report5.html">詳細を見る</a></td>
                    </tr>
                    <tr>
                        <td>必読モーダル</td>
                        <td class="status-success">成功</td>
                        <td><a href="generated/report6.html">詳細を見る</a></td>
                    </tr>
                    <tr>
                        <td>パルくる便プロモ</td>
                        <td class="status-success">成功</td>
                        <td><a href="generated/report7.html">詳細を見る</a></td>
                    </tr>
                    <tr>
                        <td>商品検索画面</td>
                        <td class="status-success">成功</td>
                        <td><a href="generated/report8.html">詳細を見る</a></td>
                    </tr>
                    <tr>
                        <td>カゴタブ</td>
                        <td class="status-success">成功</td>
                        <td><a href="generated/report9.html">詳細を見る</a></td>
                    </tr>
                    <tr>
                        <td>注文内容確認</td>
                        <td class="status-success">成功</td>
                        <td><a href="generated/report10.html">詳細を見る</a></td>
                    </tr>
                </tbody>
            </table>
        </section>
        <section>
            <h2>使い方</h2>
            <p>各セクションの詳細な分析は、個別のレポートで確認できます。</p>
        </section>
        <footer>
            <p>&copy; 2023 プロジェクトチーム</p>
        </footer>
    </main>
</body>
```

