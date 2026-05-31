from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

HTML_TEMPLATES = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CYBER ONX - TIKTOK DOWNLOADER</title>
    <style>
        body { background-color: #121212; color: #ffffff; font-family: 'Segoe UI', Arial, sans-serif; text-align: center; padding: 50px 20px; }
        .container { max-width: 500px; margin: 0 auto; background: #1e1e1e; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); border: 1px solid #ff4a4a; }
        h2 { color: #ff4a4a; margin-bottom: 5px; }
        p { color: #aaaaaa; font-size: 14px; margin-bottom: 25px; }
        input[type="text"] { width: 100%; padding: 12px; border: 1px solid #333; border-radius: 8px; background: #252525; color: #fff; box-sizing: border-box; margin-bottom: 15px; }
        button { width: 100%; padding: 12px; background: #ff4a4a; border: none; color: white; font-weight: bold; border-radius: 8px; cursor: pointer; transition: 0.3s; }
        button:hover { background: #e03e3e; }
        .result { margin-top: 25px; padding: 15px; background: #252525; border-radius: 8px; }
        .btn-download { display: inline-block; padding: 10px 20px; background: #00ec5b; color: #000; font-weight: bold; text-decoration: none; border-radius: 5px; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>📥 CYBER ONX DOWNLOADER</h2>
        <p>Bypass & Download Video TikTok Tanpa Watermark</p>
        
        <form method="POST">
            <input type="text" name="url" placeholder="Tempel link TikTok di sini..." required>
            <button type="submit">PROSES LINK</button>
        </form>

        {% if sukses %}
            <div class="result">
                <p style="color: #00ec5b; font-weight: bold;">🎉 Video Berhasil Diproses!</p>
                <p>Judul: {{ judul }}</p>
                <a href="{{ download_url }}" class="btn-download" target="_blank" download>KLIK UNTUK DOWNLOAD MP4</a>
            </div>
        {% elif error %}
            <div class="result" style="border: 1px solid #ff4a4a;">
                <p style="color: #ff4a4a;">❌ {{ error }}</p>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url'].strip()
        
        if "tiktok.com" in url:
            try:
                api_url = f"https://www.tikwm.com/api/?url={url}"
                respon = requests.get(api_url, timeout=15).json()
                if respon.get("code") == 0:
                    return render_template_string(HTML_TEMPLATES, sukses=True, judul=respon["data"]["title"][:50], download_url=respon["data"]["play"])
                else:
                    return render_template_string(HTML_TEMPLATES, error="Gagal mengambil data TikTok. Cek kembali link lu.")
            except Exception:
                return render_template_string(HTML_TEMPLATES, error="Gagal bypass proteksi. Coba lagi nanti.")
        else:
            return render_template_string(HTML_TEMPLATES, error="Hanya mendukung link TikTok di server ini, Man!")
            
    return render_template_string(HTML_TEMPLATES)
        
