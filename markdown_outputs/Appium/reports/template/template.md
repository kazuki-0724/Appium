# ディレクトリ: Appium/reports/template

---

### ファイル: Appium/reports/template/report1.html

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
        a {
            color: #ffd600;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.2s;
        }
        a:hover {
            color: #00fff5;
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>スプラッシュ レポート</h1>
        <a href="summary.html">戻る</a>
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
                <td><img src="../screenshot/splash_005.png" width="200" alt="Splash Image"></td>
                <td><img src="../screenshot/splash_005.png" width="200" alt="Splash Image"></td>
            </tr>
        </table>
    </main>
    <footer class="footer">
        <p>&copy; 2023 プロジェクトチーム</p>
```

---

### ファイル: Appium/reports/template/report2.html

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
        a {
            color: #ffd600;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.2s;
        }
        a:hover {
            color: #00fff5;
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>未ログイントップ レポート</h1>
        <a href="summary.html">戻る</a>
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
                <td><img src="../screenshot/no_login_top_007.png" width="200" alt="未ログイントップ"></td>
                <td><img src="../screenshot/no_login_top_007.png" width="200" alt="未ログイントップ"></td>
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
                <td><img src="../screenshot/no_login_top_010.png" width="200" alt="未ログイントップ"></td>
                <td><img src="../screenshot/no_login_top_010.png" width="200" alt="未ログイントップ"></td>
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
                <td><img src="../screenshot/no_login_top_012.png" width="200" alt="未ログイントップ"></td>
                <td><img src="../screenshot/no_login_top_012.png" width="200" alt="未ログイントップ"></td>
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
                <td><img src="../screenshot/no_login_top_016.png" width="200" alt="未ログイントップ"></td>
                <td><img src="../screenshot/no_login_top_016.png" width="200" alt="未ログイントップ"></td>
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
                <td><img src="../screenshot/no_login_top_021.png" width="200" alt="未ログイントップ"></td>
                <td><img src="../screenshot/no_login_top_021.png" width="200" alt="未ログイントップ"></td>
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
                <td><img src="../screenshot/account_create_022.png" width="200" alt="アカウント作成"></td>
                <td><img src="../screenshot/account_create_022.png" width="200" alt="アカウント作成"></td>
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
                <td><img src="../screenshot/account_create_023.png" width="200" alt="アカウント作成"></td>
                <td><img src="../screenshot/account_create_023.png" width="200" alt="アカウント作成"></td>
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
                <td><img src="../screenshot/account_create_024.png" width="200" alt="アカウント作成"></td>
                <td><img src="../screenshot/account_create_024.png" width="200" alt="アカウント作成"></td>
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
                <td><img src="../screenshot/account_create_028.png" width="200" alt="アカウント作成"></td>
                <td><img src="../screenshot/account_create_028.png" width="200" alt="アカウント作成"></td>
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

### ファイル: Appium/reports/template/report3.html

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
        a {
            color: #ffd600;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.2s;
        }
        a:hover {
            color: #00fff5;
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>ログイン レポート</h1>
        <a href="summary.html">戻る</a>
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
                <td><img src="../screenshot/login_038.png" width="200" alt="Login Image"></td>
                <td><img src="../screenshot/login_038.png" width="200" alt="Login Image"></td>
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
                <td><img src="../screenshot/login_040.png" width="200" alt="Login Image"></td>
                <td><img src="../screenshot/login_040.png" width="200" alt="Login Image"></td>
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
                <td><img src="../screenshot/login_042.png" width="200" alt="Login Image"></td>
                <td><img src="../screenshot/login_042.png" width="200" alt="Login Image"></td>
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
                <td><img src="../screenshot/login_043.png" width="200" alt="Login Image"></td>
                <td><img src="../screenshot/login_043.png" width="200" alt="Login Image"></td>
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
                <td><img src="../screenshot/login_045.png" width="200" alt="Login Image"></td>
                <td><img src="../screenshot/login_045.png" width="200" alt="Login Image"></td>
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
                <td><img src="../screenshot/login_046.png" width="200" alt="Login Image"></td>
                <td><img src="../screenshot/login_046.png" width="200" alt="Login Image"></td>
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
                <td><img src="../screenshot/login_047.png" width="200" alt="Login Image"></td>
                <td><img src="../screenshot/login_047.png" width="200" alt="Login Image"></td>
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
                <td><img src="../screenshot/login_048.png" width="200" alt="Login Image"></td>
                <td><img src="../screenshot/login_048.png" width="200" alt="Login Image"></td>
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
                <td><img src="../screenshot/login_049.png" width="200" alt="Login Image"></td>
                <td><img src="../screenshot/login_049.png" width="200" alt="Login Image"></td>
            </tr>
        </table>
    </main>
    <footer class="footer">
        <p>&copy; 2023 プロジェクトチーム</p>
    </footer>
</body>
```

---

### ファイル: Appium/reports/template/report4.html

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
        a {
            color: #ffd600;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.2s;
        }
        a:hover {
            color: #00fff5;
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>企画回選択 レポート</h1>
        <a href="summary.html">戻る</a>
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
                <td><img src="../screenshot/select_product_catalog_058.png" width="200" alt="企画回選択"></td>
                <td><img src="../screenshot/select_product_catalog_058.png" width="200" alt="企画回選択"></td>
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
                <td><img src="../screenshot/select_product_catalog_062.png" width="200" alt="企画回選択"></td>
                <td><img src="../screenshot/select_product_catalog_062.png" width="200" alt="企画回選択"></td>
            </tr>
        </table>
    </main>
    <footer class="footer">
        <p>&copy; 2023 プロジェクトチーム</p>
    </footer>
</body>
```

---

### ファイル: Appium/reports/template/report5.html

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
        a {
            color: #ffd600;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.2s;
        }
        a:hover {
            color: #00fff5;
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>買い物タブ レポート</h1>
        <a href="summary.html">戻る</a>
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
                <td><img src="../screenshot/shopping_tab_062.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_062.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_066.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_066.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_070.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_070.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_071.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_071.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_073.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_073.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_075.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_075.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_078.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_078.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_079.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_079.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_081.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_081.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_082.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_082.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_083.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_083.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_084.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_084.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_085.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_085.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_086.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_086.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_090.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_090.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_091.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_091.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_092.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_092.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_093.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_093.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_094.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_094.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_095-1.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_095-1.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_095-2.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_095-2.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_096.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_096.png" width="200" alt="買い物タブ"></td>
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
                <td><img src="../screenshot/shopping_tab_097.png" width="200" alt="買い物タブ"></td>
                <td><img src="../screenshot/shopping_tab_097.png" width="200" alt="買い物タブ"></td>
            </tr>
        </table>
    </main>
    <footer class="footer">
        <p>&copy; 2023 プロジェクトチーム</p>
    </footer>
</body>
```

---

### ファイル: Appium/reports/template/report6.html

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
        a {
            color: #ffd600;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.2s;
        }
        a:hover {
            color: #00fff5;
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>Must Read Modal レポート</h1>
        <a href="summary.html">戻る</a>
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
                <td><img src="../screenshot/must_read_modal_112.png" width="200" alt="must_read_modal_112"></td>
                <td><img src="../screenshot/must_read_modal_112.png" width="200" alt="must_read_modal_112"></td>
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
                <td><img src="../screenshot/must_read_modal_113.png" width="200" alt="must_read_modal_113"></td>
                <td><img src="../screenshot/must_read_modal_113.png" width="200" alt="must_read_modal_113"></td>
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
                <td><img src="../screenshot/must_read_modal_117.png" width="200" alt="must_read_modal_117"></td>
                <td><img src="../screenshot/must_read_modal_117.png" width="200" alt="must_read_modal_117"></td>
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
                <td><img src="../screenshot/must_read_modal_118.png" width="200" alt="must_read_modal_118"></td>
                <td><img src="../screenshot/must_read_modal_118.png" width="200" alt="must_read_modal_118"></td>
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
                <td><img src="../screenshot/must_read_modal_119.png" width="200" alt="must_read_modal_119"></td>
                <td><img src="../screenshot/must_read_modal_119.png" width="200" alt="must_read_modal_119"></td>
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
                <td><img src="../screenshot/must_read_modal_121.png" width="200" alt="must_read_modal_121"></td>
                <td><img src="../screenshot/must_read_modal_121.png" width="200" alt="must_read_modal_121"></td>
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
                <td><img src="../screenshot/must_read_modal_123.png" width="200" alt="must_read_modal_123"></td>
                <td><img src="../screenshot/must_read_modal_123.png" width="200" alt="must_read_modal_123"></td>
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
                <td><img src="../screenshot/must_read_modal_124.png" width="200" alt="must_read_modal_124"></td>
                <td><img src="../screenshot/must_read_modal_124.png" width="200" alt="must_read_modal_124"></td>
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
                <td><img src="../screenshot/must_read_modal_125.png" width="200" alt="must_read_modal_125"></td>
                <td><img src="../screenshot/must_read_modal_125.png" width="200" alt="must_read_modal_125"></td>
            </tr>
        </table>
    </main>
    <footer class="footer">
        <p>&copy; 2023 プロジェクトチーム</p>
    </footer>
```

---

### ファイル: Appium/reports/template/report7.html

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
        a {
            color: #ffd600;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.2s;
        }
        a:hover {
            color: #00fff5;
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>パルくる便プロモーション レポート</h1>
        <a href="summary.html">戻る</a>
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
                <td><img src="../screenshot/pal_promo_130.png" width="200" alt="pal_promo_130"></td>
                <td><img src="../screenshot/pal_promo_130.png" width="200" alt="pal_promo_130"></td>
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
                <td><img src="../screenshot/pal_promo_132.png" width="200" alt="pal_promo_132"></td>
                <td><img src="../screenshot/pal_promo_132.png" width="200" alt="pal_promo_132"></td>
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
                <td><img src="../screenshot/pal_promo_134.png" width="200" alt="pal_promo_134"></td>
                <td><img src="../screenshot/pal_promo_134.png" width="200" alt="pal_promo_134"></td>
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
                <td><img src="../screenshot/pal_promo_136.png" width="200" alt="pal_promo_136"></td>
                <td><img src="../screenshot/pal_promo_136.png" width="200" alt="pal_promo_136"></td>
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
                <td><img src="../screenshot/pal_promo_137.png" width="200" alt="pal_promo_137"></td>
                <td><img src="../screenshot/pal_promo_137.png" width="200" alt="pal_promo_137"></td>
            </tr>
        </table>
    </main>
    <footer class="footer">
        <p>&copy; 2023 プロジェクトチーム</p>
    </footer>
</body>
```

---

### ファイル: Appium/reports/template/report8.html

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
        a {
            color: #ffd600;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.2s;
        }
        a:hover {
            color: #00fff5;
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>商品検索テスト レポート</h1>
        <a href="summary.html">戻る</a>
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
                <td><img src="../screenshot/item_search_139.png" width="200" alt="item_search_139"></td>
                <td><img src="../screenshot/item_search_139.png" width="200" alt="item_search_139"></td>
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
                <td><img src="../screenshot/item_search_140.png" width="200" alt="item_search_140"></td>
                <td><img src="../screenshot/item_search_140.png" width="200" alt="item_search_140"></td>
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
                <td><img src="../screenshot/item_search_141.png" width="200" alt="item_search_141"></td>
                <td><img src="../screenshot/item_search_141.png" width="200" alt="item_search_141"></td>
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
                <td><img src="../screenshot/item_search_142.png" width="200" alt="item_search_142"></td>
                <td><img src="../screenshot/item_search_142.png" width="200" alt="item_search_142"></td>
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
                <td><img src="../screenshot/item_search_143.png" width="200" alt="item_search_143"></td>
                <td><img src="../screenshot/item_search_143.png" width="200" alt="item_search_143"></td>
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
                <td><img src="../screenshot/item_search_146.png" width="200" alt="item_search_146"></td>
                <td><img src="../screenshot/item_search_146.png" width="200" alt="item_search_146"></td>
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
                <td><img src="../screenshot/item_search_147.png" width="200" alt="item_search_147"></td>
                <td><img src="../screenshot/item_search_147.png" width="200" alt="item_search_147"></td>
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
                <td><img src="../screenshot/item_search_148.png" width="200" alt="item_search_148"></td>
                <td><img src="../screenshot/item_search_148.png" width="200" alt="item_search_148"></td>
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
                <td><img src="../screenshot/item_search_150.png" width="200" alt="item_search_150"></td>
                <td><img src="../screenshot/item_search_150.png" width="200" alt="item_search_150"></td>
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
                <td><img src="../screenshot/item_search_151.png" width="200" alt="item_search_151"></td>
                <td><img src="../screenshot/item_search_151.png" width="200" alt="item_search_151"></td>
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
                <td><img src="../screenshot/item_search_152.png" width="200" alt="item_search_152"></td>
                <td><img src="../screenshot/item_search_152.png" width="200" alt="item_search_152"></td>
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
                <td><img src="../screenshot/item_search_154.png" width="200" alt="item_search_154"></td>
                <td><img src="../screenshot/item_search_154.png" width="200" alt="item_search_154"></td>
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
                <td><img src="../screenshot/item_search_155.png" width="200" alt="item_search_155"></td>
                <td><img src="../screenshot/item_search_155.png" width="200" alt="item_search_155"></td>
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
                <td><img src="../screenshot/item_search_158.png" width="200" alt="item_search_158"></td>
                <td><img src="../screenshot/item_search_158.png" width="200" alt="item_search_158"></td>
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
                <td><img src="../screenshot/item_search_159.png" width="200" alt="item_search_159"></td>
                <td><img src="../screenshot/item_search_159.png" width="200" alt="item_search_159"></td>
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
                <td><img src="../screenshot/item_search_161.png" width="200" alt="item_search_161"></td>
                <td><img src="../screenshot/item_search_161.png" width="200" alt="item_search_161"></td>
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
                <td><img src="../screenshot/item_search_164.png" width="200" alt="item_search_164"></td>
                <td><img src="../screenshot/item_search_164.png" width="200" alt="item_search_164"></td>
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
                <td><img src="../screenshot/item_search_165.png" width="200" alt="item_search_165"></td>
                <td><img src="../screenshot/item_search_165.png" width="200" alt="item_search_165"></td>
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
                <td><img src="../screenshot/item_search_166.png" width="200" alt="item_search_166"></td>
                <td><img src="../screenshot/item_search_166.png" width="200" alt="item_search_166"></td>
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

### ファイル: Appium/reports/template/report9.html

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
        a {
            color: #ffd600;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.2s;
        }
        a:hover {
            color: #00fff5;
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>カゴ画面テスト レポート</h1>
        <a href="summary.html">戻る</a>
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
                <td><img src="../screenshot/cart_168.png" width="200" alt="cart_168"></td>
                <td><img src="../screenshot/cart_168.png" width="200" alt="cart_168"></td>
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
                <td><img src="../screenshot/cart_171.png" width="200" alt="cart_171"></td>
                <td><img src="../screenshot/cart_171.png" width="200" alt="cart_171"></td>
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
                <td><img src="../screenshot/cart_174.png" width="200" alt="cart_174"></td>
                <td><img src="../screenshot/cart_174.png" width="200" alt="cart_174"></td>
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
                <td><img src="../screenshot/cart_177.png" width="200" alt="cart_177"></td>
                <td><img src="../screenshot/cart_177.png" width="200" alt="cart_177"></td>
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
                <td><img src="../screenshot/cart_194.png" width="200" alt="cart_194"></td>
                <td><img src="../screenshot/cart_194.png" width="200" alt="cart_194"></td>
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
                <td><img src="../screenshot/cart_195.png" width="200" alt="cart_195"></td>
                <td><img src="../screenshot/cart_195.png" width="200" alt="cart_195"></td>
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
                <td><img src="../screenshot/cart_196.png" width="200" alt="cart_196"></td>
                <td><img src="../screenshot/cart_196.png" width="200" alt="cart_196"></td>
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
                <td><img src="../screenshot/cart_198.png" width="200" alt="cart_198"></td>
                <td><img src="../screenshot/cart_198.png" width="200" alt="cart_198"></td>
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
                <td><img src="../screenshot/cart_199.png" width="200" alt="cart_199"></td>
                <td><img src="../screenshot/cart_199.png" width="200" alt="cart_199"></td>
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
                <td><img src="../screenshot/cart_201.png" width="200" alt="cart_201"></td>
                <td><img src="../screenshot/cart_201.png" width="200" alt="cart_201"></td>
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
                <td><img src="../screenshot/cart_203.png" width="200" alt="cart_203"></td>
                <td><img src="../screenshot/cart_203.png" width="200" alt="cart_203"></td>
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
                <td><img src="../screenshot/cart_207.png" width="200" alt="cart_207"></td>
                <td><img src="../screenshot/cart_207.png" width="200" alt="cart_207"></td>
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
                <td><img src="../screenshot/cart_209.png" width="200" alt="cart_209"></td>
                <td><img src="../screenshot/cart_209.png" width="200" alt="cart_209"></td>
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
                <td><img src="../screenshot/cart_213.png" width="200" alt="cart_213"></td>
                <td><img src="../screenshot/cart_213.png" width="200" alt="cart_213"></td>
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
                <td><img src="../screenshot/cart_214.png" width="200" alt="cart_214"></td>
                <td><img src="../screenshot/cart_214.png" width="200" alt="cart_214"></td>
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
                <td><img src="../screenshot/cart_229.png" width="200" alt="cart_229"></td>
                <td><img src="../screenshot/cart_229.png" width="200" alt="cart_229"></td>
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
                <td><img src="../screenshot/cart_230.png" width="200" alt="cart_230"></td>
                <td><img src="../screenshot/cart_230.png" width="200" alt="cart_230"></td>
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
                <td><img src="../screenshot/cart_231.png" width="200" alt="cart_231"></td>
                <td><img src="../screenshot/cart_231.png" width="200" alt="cart_231"></td>
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
                <td><img src="../screenshot/cart_234.png" width="200" alt="cart_234"></td>
                <td><img src="../screenshot/cart_234.png" width="200" alt="cart_234"></td>
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
                <td><img src="../screenshot/cart_235.png" width="200" alt="cart_235"></td>
                <td><img src="../screenshot/cart_235.png" width="200" alt="cart_235"></td>
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
                <td><img src="../screenshot/cart_236.png" width="200" alt="cart_236"></td>
                <td><img src="../screenshot/cart_236.png" width="200" alt="cart_236"></td>
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
                <td><img src="../screenshot/cart_237.png" width="200" alt="cart_237"></td>
                <td><img src="../screenshot/cart_237.png" width="200" alt="cart_237"></td>
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
                <td><img src="../screenshot/cart_239.png" width="200" alt="cart_239"></td>
                <td><img src="../screenshot/cart_239.png" width="200" alt="cart_239"></td>
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
                <td><img src="../screenshot/cart_241.png" width="200" alt="cart_241"></td>
                <td><img src="../screenshot/cart_241.png" width="200" alt="cart_241"></td>
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
                <td><img src="../screenshot/cart_242.png" width="200" alt="cart_242"></td>
                <td><img src="../screenshot/cart_242.png" width="200" alt="cart_242"></td>
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
                <td><img src="../screenshot/cart_244.png" width="200" alt="cart_244"></td>
                <td><img src="../screenshot/cart_244.png" width="200" alt="cart_244"></td>
            </tr>
        </table>
        <table>
            <caption>No245</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_245}</td>
                <td><img src="../screenshot/cart_245.png" width="200" alt="cart_245"></td>
                <td><img src="../screenshot/cart_245.png" width="200" alt="cart_245"></td>
            </tr>
        </table>
        <table>
            <caption>No247</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_247}</td>
                <td><img src="../screenshot/cart_247.png" width="200" alt="cart_247"></td>
                <td><img src="../screenshot/cart_247.png" width="200" alt="cart_247"></td>
            </tr>
        </table>
        <table>
            <caption>No251</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_251}</td>
                <td><img src="../screenshot/cart_251.png" width="200" alt="cart_251"></td>
                <td><img src="../screenshot/cart_251.png" width="200" alt="cart_251"></td>
            </tr>
        </table>
        <table>
            <caption>No253</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_253}</td>
                <td><img src="../screenshot/cart_253.png" width="200" alt="cart_253"></td>
                <td><img src="../screenshot/cart_253.png" width="200" alt="cart_253"></td>
            </tr>
        </table>
        <table>
            <caption>No257</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_257}</td>
                <td><img src="../screenshot/cart_257.png" width="200" alt="cart_257"></td>
                <td><img src="../screenshot/cart_257.png" width="200" alt="cart_257"></td>
            </tr>
        </table>
        <table>
            <caption>No259</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_259}</td>
                <td><img src="../screenshot/cart_259.png" width="200" alt="cart_259"></td>
                <td><img src="../screenshot/cart_259.png" width="200" alt="cart_259"></td>
            </tr>
        </table>
        <table>
            <caption>No263</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_263}</td>
                <td><img src="../screenshot/cart_263.png" width="200" alt="cart_263"></td>
                <td><img src="../screenshot/cart_263.png" width="200" alt="cart_263"></td>
            </tr>
        </table>
        <table>
            <caption>No264</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_264}</td>
                <td><img src="../screenshot/cart_264.png" width="200" alt="cart_264"></td>
                <td><img src="../screenshot/cart_264.png" width="200" alt="cart_264"></td>
            </tr>
        </table>
        <table>
            <caption>No266</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_266}</td>
                <td><img src="../screenshot/cart_266.png" width="200" alt="cart_266"></td>
                <td><img src="../screenshot/cart_266.png" width="200" alt="cart_266"></td>
            </tr>
        </table>
        <table>
            <caption>No267</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_267}</td>
                <td><img src="../screenshot/cart_267.png" width="200" alt="cart_267"></td>
                <td><img src="../screenshot/cart_267.png" width="200" alt="cart_267"></td>
            </tr>
        </table>
        <table>
            <caption>No268</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_268}</td>
                <td><img src="../screenshot/cart_268.png" width="200" alt="cart_268"></td>
                <td><img src="../screenshot/cart_268.png" width="200" alt="cart_268"></td>
            </tr>
        </table>
        <table>
            <caption>No269</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_269}</td>
                <td><img src="../screenshot/cart_269.png" width="200" alt="cart_269"></td>
                <td><img src="../screenshot/cart_269.png" width="200" alt="cart_269"></td>
            </tr>
        </table>
        <table>
            <caption>No272</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_272}</td>
                <td><img src="../screenshot/cart_272.png" width="200" alt="cart_272"></td>
                <td><img src="../screenshot/cart_272.png" width="200" alt="cart_272"></td>
            </tr>
        </table>
        <table>
            <caption>No273</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_273}</td>
                <td><img src="../screenshot/cart_273.png" width="200" alt="cart_273"></td>
                <td><img src="../screenshot/cart_273.png" width="200" alt="cart_273"></td>
            </tr>
        </table>
        <table>
            <caption>No274</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_274}</td>
                <td><img src="../screenshot/cart_274.png" width="200" alt="cart_274"></td>
                <td><img src="../screenshot/cart_274.png" width="200" alt="cart_274"></td>
            </tr>
        </table>
        <table>
            <caption>No275</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_275}</td>
                <td><img src="../screenshot/cart_275.png" width="200" alt="cart_275"></td>
                <td><img src="../screenshot/cart_275.png" width="200" alt="cart_275"></td>
            </tr>
        </table>
        <table>
            <caption>No277</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_277}</td>
                <td><img src="../screenshot/cart_277.png" width="200" alt="cart_277"></td>
                <td><img src="../screenshot/cart_277.png" width="200" alt="cart_277"></td>
            </tr>
        </table>
        <table>
            <caption>No279</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_279}</td>
                <td><img src="../screenshot/cart_279.png" width="200" alt="cart_279"></td>
                <td><img src="../screenshot/cart_279.png" width="200" alt="cart_279"></td>
            </tr>
        </table>
        <table>
            <caption>No280</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_280}</td>
                <td><img src="../screenshot/cart_280.png" width="200" alt="cart_280"></td>
                <td><img src="../screenshot/cart_280.png" width="200" alt="cart_280"></td>
            </tr>
        </table>
        <table>
            <caption>No282</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_282}</td>
                <td><img src="../screenshot/cart_282.png" width="200" alt="cart_282"></td>
                <td><img src="../screenshot/cart_282.png" width="200" alt="cart_282"></td>
            </tr>
        </table>
        <table>
            <caption>No283</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_283}</td>
                <td><img src="../screenshot/cart_283.png" width="200" alt="cart_283"></td>
                <td><img src="../screenshot/cart_283.png" width="200" alt="cart_283"></td>
            </tr>
        </table>
        <table>
            <caption>No284</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_284}</td>
                <td><img src="../screenshot/cart_284.png" width="200" alt="cart_284"></td>
                <td><img src="../screenshot/cart_284.png" width="200" alt="cart_284"></td>
            </tr>
        </table>
        <table>
            <caption>No286</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_286}</td>
                <td><img src="../screenshot/cart_286.png" width="200" alt="cart_286"></td>
                <td><img src="../screenshot/cart_286.png" width="200" alt="cart_286"></td>
            </tr>
        </table>
        <table>
            <caption>No289</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_289}</td>
                <td><img src="../screenshot/cart_289.png" width="200" alt="cart_289"></td>
                <td><img src="../screenshot/cart_289.png" width="200" alt="cart_289"></td>
            </tr>
        </table>
                <table>
            <caption>No291</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_291}</td>
                <td><img src="../screenshot/cart_291.png" width="200" alt="cart_291"></td>
                <td><img src="../screenshot/cart_291.png" width="200" alt="cart_291"></td>
            </tr>
        </table>
        <table>
            <caption>No292</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_292}</td>
                <td><img src="../screenshot/cart_292.png" width="200" alt="cart_292"></td>
                <td><img src="../screenshot/cart_292.png" width="200" alt="cart_292"></td>
            </tr>
        </table>
        <table>
            <caption>No293</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_293}</td>
                <td><img src="../screenshot/cart_293.png" width="200" alt="cart_293"></td>
                <td><img src="../screenshot/cart_293.png" width="200" alt="cart_293"></td>
            </tr>
        </table>
        <table>
            <caption>No294</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_294}</td>
                <td><img src="../screenshot/cart_294.png" width="200" alt="cart_294"></td>
                <td><img src="../screenshot/cart_294.png" width="200" alt="cart_294"></td>
            </tr>
        </table>
        <table>
            <caption>No296</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_296}</td>
                <td><img src="../screenshot/cart_296.png" width="200" alt="cart_296"></td>
                <td><img src="../screenshot/cart_296.png" width="200" alt="cart_296"></td>
            </tr>
        </table>
        <table>
            <caption>No297</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_297}</td>
                <td><img src="../screenshot/cart_297.png" width="200" alt="cart_297"></td>
                <td><img src="../screenshot/cart_297.png" width="200" alt="cart_297"></td>
            </tr>
        </table>
        <table>
            <caption>No298</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_298}</td>
                <td><img src="../screenshot/cart_298.png" width="200" alt="cart_298"></td>
                <td><img src="../screenshot/cart_298.png" width="200" alt="cart_298"></td>
            </tr>
        </table>
        <table>
            <caption>No299</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_299}</td>
                <td><img src="../screenshot/cart_299.png" width="200" alt="cart_299"></td>
                <td><img src="../screenshot/cart_299.png" width="200" alt="cart_299"></td>
            </tr>
        </table>
        <table>
            <caption>No302</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_302}</td>
                <td><img src="../screenshot/cart_302.png" width="200" alt="cart_302"></td>
                <td><img src="../screenshot/cart_302.png" width="200" alt="cart_302"></td>
            </tr>
        </table>
        <table>
            <caption>No303</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_303}</td>
                <td><img src="../screenshot/cart_303.png" width="200" alt="cart_303"></td>
                <td><img src="../screenshot/cart_303.png" width="200" alt="cart_303"></td>
            </tr>
        </table>
        <table>
            <caption>No306</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_306}</td>
                <td><img src="../screenshot/cart_306.png" width="200" alt="cart_306"></td>
                <td><img src="../screenshot/cart_306.png" width="200" alt="cart_306"></td>
            </tr>
        </table>
        <table>
            <caption>No307</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_307}</td>
                <td><img src="../screenshot/cart_307.png" width="200" alt="cart_307"></td>
                <td><img src="../screenshot/cart_307.png" width="200" alt="cart_307"></td>
            </tr>
        </table>
        <table>
            <caption>No308</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_308}</td>
                <td><img src="../screenshot/cart_308.png" width="200" alt="cart_308"></td>
                <td><img src="../screenshot/cart_308.png" width="200" alt="cart_308"></td>
            </tr>
        </table>
        <table>
            <caption>No313</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_313}</td>
                <td><img src="../screenshot/cart_313.png" width="200" alt="cart_313"></td>
                <td><img src="../screenshot/cart_313.png" width="200" alt="cart_313"></td>
            </tr>
        </table>
        <table>
            <caption>No314</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_314}</td>
                <td><img src="../screenshot/cart_314.png" width="200" alt="cart_314"></td>
                <td><img src="../screenshot/cart_314.png" width="200" alt="cart_314"></td>
            </tr>
        </table>
        <table>
            <caption>No315</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_315}</td>
                <td><img src="../screenshot/cart_315.png" width="200" alt="cart_315"></td>
                <td><img src="../screenshot/cart_315.png" width="200" alt="cart_315"></td>
            </tr>
        </table>
        <table>
            <caption>No320</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_320}</td>
                <td><img src="../screenshot/cart_320.png" width="200" alt="cart_320"></td>
                <td><img src="../screenshot/cart_320.png" width="200" alt="cart_320"></td>
            </tr>
        </table>
        <table>
            <caption>No321-1</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_321_1}</td>
                <td><img src="../screenshot/cart_321-1.png" width="200" alt="cart_321-1"></td>
                <td><img src="../screenshot/cart_321-1.png" width="200" alt="cart_321-1"></td>
            </tr>
        </table>
        <table>
            <caption>No321-2</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_321_2}</td>
                <td><img src="../screenshot/cart_321-2.png" width="200" alt="cart_321-2"></td>
                <td><img src="../screenshot/cart_321-2.png" width="200" alt="cart_321-2"></td>
            </tr>
        </table>
        <table>
            <caption>No336</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_336}</td>
                <td><img src="../screenshot/cart_336.png" width="200" alt="cart_336"></td>
                <td><img src="../screenshot/cart_336.png" width="200" alt="cart_336"></td>
            </tr>
        </table>
        <table>
            <caption>No337</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_337}</td>
                <td><img src="../screenshot/cart_337.png" width="200" alt="cart_337"></td>
                <td><img src="../screenshot/cart_337.png" width="200" alt="cart_337"></td>
            </tr>
        </table>
        <table>
            <caption>No342</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_342}</td>
                <td><img src="../screenshot/cart_342.png" width="200" alt="cart_342"></td>
                <td><img src="../screenshot/cart_342.png" width="200" alt="cart_342"></td>
            </tr>
        </table>
        <table>
            <caption>No343</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_343}</td>
                <td><img src="../screenshot/cart_343.png" width="200" alt="cart_343"></td>
                <td><img src="../screenshot/cart_343.png" width="200" alt="cart_343"></td>
            </tr>
        </table>
        <table>
            <caption>No345</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_345}</td>
                <td><img src="../screenshot/cart_345.png" width="200" alt="cart_345"></td>
                <td><img src="../screenshot/cart_345.png" width="200" alt="cart_345"></td>
            </tr>
        </table>
        <table>
            <caption>No346</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_346}</td>
                <td><img src="../screenshot/cart_346.png" width="200" alt="cart_346"></td>
                <td><img src="../screenshot/cart_346.png" width="200" alt="cart_346"></td>
            </tr>
        </table>
        <table>
            <caption>No348</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_348}</td>
                <td><img src="../screenshot/cart_348.png" width="200" alt="cart_348"></td>
                <td><img src="../screenshot/cart_348.png" width="200" alt="cart_348"></td>
            </tr>
        </table>
        <table>
            <caption>No349</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_349}</td>
                <td><img src="../screenshot/cart_349.png" width="200" alt="cart_349"></td>
                <td><img src="../screenshot/cart_349.png" width="200" alt="cart_349"></td>
            </tr>
        </table>
        <table>
            <caption>No350</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_350}</td>
                <td><img src="../screenshot/cart_350.png" width="200" alt="cart_350"></td>
                <td><img src="../screenshot/cart_350.png" width="200" alt="cart_350"></td>
            </tr>
        </table>
        <table>
            <caption>No351</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_351}</td>
                <td><img src="../screenshot/cart_351.png" width="200" alt="cart_351"></td>
                <td><img src="../screenshot/cart_351.png" width="200" alt="cart_351"></td>
            </tr>
        </table>
        <table>
            <caption>No353</caption>
            <tr>
                <th>類似率</th>
                <th>結果</th>
                <th>正解</th>
            </tr>
            <tr>
                <td class="similarity">{similarity_353}</td>
                <td><img src="../screenshot/cart_353.png" width="200" alt="cart_353"></td>
                <td><img src="../screenshot/cart_353.png" width="200" alt="cart_353"></td>
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

### ファイル: Appium/reports/template/summary.html

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
                        <td><a href="report1.html">詳細を見る</a></td>
                    </tr>
                    <tr>
                        <td>未ログイントップ画面</td>
                        <td class="status-fail">失敗</td>
                        <td><a href="report2.html">詳細を見る</a></td>
                    </tr>
                    <tr>
                        <td>ログイン画面</td>
                        <td class="status-success">成功</td>
                        <td><a href="report3.html">詳細を見る</a></td>
                    </tr>
                    <tr>
                        <td>企画回選択</td>
                        <td class="status-fail">失敗</td>
                        <td><a href="report4.html">詳細を見る</a></td>
                    </tr>
                    <tr>
                        <td>買い物タブ</td>
                        <td class="status-success">成功</td>
                        <td><a href="report5.html">詳細を見る</a></td>
                    </tr>
                    <tr>
                        <td>必読モーダル</td>
                        <td class="status-success">成功</td>
                        <td><a href="report6.html">詳細を見る</a></td>
                    </tr>
                    <tr>
                        <td>パルくる便プロモ</td>
                        <td class="status-success">成功</td>
                        <td><a href="report7.html">詳細を見る</a></td>
                    </tr>
                    <tr>
                        <td>商品検索画面</td>
                        <td class="status-success">成功</td>
                        <td><a href="report8.html">詳細を見る</a></td>
                    </tr>
                    <tr>
                        <td>カゴタブ</td>
                        <td class="status-success">成功</td>
                        <td><a href="report9.html">詳細を見る</a></td>
                    </tr>
                    <tr>
                        <td>注文内容確認</td>
                        <td class="status-success">成功</td>
                        <td><a href="report10.html">詳細を見る</a></td>
                    </tr>
                </tbody>
            </table>
        </section>
    </main>
</body>
```

