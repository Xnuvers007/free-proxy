# Free Proxy

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![GitHub Workflow](https://img.shields.io/github/workflow/status/xnuvers007/free-proxy/Proxy%20Checker?label=CI)](https://github.com/xnuvers007/free-proxy/actions)
[![License](https://img.shields.io/github/license/xnuvers007/free-proxy)](LICENSE)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/xnuvers007/free-proxy)](https://github.com/xnuvers007/free-proxy)
[![GitHub Stars](https://img.shields.io/github/stars/xnuvers007/free-proxy?style=social)](https://github.com/xnuvers007/free-proxy/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/xnuvers007/free-proxy?style=social)](https://github.com/xnuvers007/free-proxy/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/xnuvers007/free-proxy)](https://github.com/xnuvers007/free-proxy/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/xnuvers007/free-proxy)](https://github.com/xnuvers007/free-proxy/pulls)
[![GitHub Contributors](https://img.shields.io/github/contributors/xnuvers007/free-proxy)](https://github.com/xnuvers007/free-proxy/graphs/contributors)
---

## 🔹 Overview

**Free Proxy Checker** adalah skrip Python profesional untuk **mengambil, memvalidasi, dan menyimpan daftar proxy gratis** dari situs [free-proxy-list.net](https://free-proxy-list.net/en/).

Fitur utama:

* Scrape proxy terbaru dari internet secara otomatis
* Cek **proxy aktif/hidup** menggunakan multithreading untuk kecepatan maksimal
* Simpan proxy dalam format **dengan skema** (`http://`/`https://`) dan **tanpa skema**
* Bisa dijalankan otomatis di **GitHub Actions** setiap 10 menit atau 30 menit
* Hasil proxy dapat di-upload sebagai artifact atau langsung di-commit ke repository

---

## 🔹 Features

* ✅ Mendukung **HTTP dan HTTPS proxies**
* ✅ **Multithreaded** untuk pengecekan cepat
* ✅ Timeout otomatis untuk proxy yang mati
* ✅ File output tersimpan dalam:

  * `proxy.txt` → daftar proxy tanpa skema
  * `proxy_scheme.txt` → daftar proxy dengan skema
  * `proxy_active.txt` → daftar proxy aktif tanpa skema
  * `proxy_scheme_active.txt` → daftar proxy aktif dengan skema
* ✅ Integrasi penuh dengan **GitHub Actions**

---

## 🔹 Installation

1. Clone repository:

```bash
git clone https://github.com/xnuvers007/free-proxy.git
cd free-proxy
```

2. Buat virtual environment (opsional tapi disarankan):

```bash
python -m venv venv
source venv/bin/activate   # Linux / MacOS
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> Atau langsung install secara manual:

```bash
pip install requests beautifulsoup4
```

---

## 🔹 Usage

Jalankan skrip Python untuk mengambil dan mengecek proxy:

```bash
python proxies.py
```

Output:

* `proxy.txt` → semua proxy yang diambil (tanpa skema)
* `proxy_scheme.txt` → semua proxy yang diambil (dengan skema)
* `proxy_active.txt` → proxy yang aktif (tanpa skema)
* `proxy_scheme_active.txt` → proxy yang aktif (dengan skema)

---

### 🔹 Contoh Integrasi GitHub Actions

Workflow otomatis untuk update proxy setiap 10 menit:

```yaml
on:
  schedule:
    - cron: "*/10 * * * *"
  workflow_dispatch:

jobs:
  check-proxies:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - run: pip install requests beautifulsoup4
      - run: python proxies.py
      - uses: actions/upload-artifact@v4
        with:
          name: proxy-files
          path: |
            proxy.txt
            proxy_scheme.txt
            proxy_active.txt
            proxy_scheme_active.txt
```

---

## 🔹 Contributing

Kontribusi sangat disambut!

1. Fork repository
2. Buat branch baru (`feature/nama-fitur`)
3. Commit perubahan (`git commit -m "Tambah fitur X"`)
4. Push ke branch (`git push origin feature/nama-fitur`)
5. Buat pull request

---

## 🔹 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 🔹 Author

* **Xnuvers007** – [GitHub Profile](https://github.com/Xnuvers007)

---

## 🔹 Acknowledgement
* Terima kasih kepada Allah SWT atas segala rahmat dan karunia-Nya.
* Terima kasih kepada nabi Muhammad SAW atas ajaran dan teladan yang luar biasa.
* Terima kasih kepada [free-proxy-list.net](https://free-proxy-list.net/en/) atas penyediaan daftar proxy gratis.
* Terima kasih kepada komunitas open-source Python atas pustaka hebat seperti `requests` dan `BeautifulSoup4`.
* Terima kasih kepada para kontributor yang telah membantu meningkatkan proyek ini.
* Terima kasih kepada pengguna yang memberikan masukan berharga untuk pengembangan proyek ini.
* Terima kasih kepada komunitas GitHub Actions atas dukungan integrasi CI/CD yang luar biasa.
* Terima kasih kepada semua yang telah mendukung proyek ini secara langsung maupun tidak langsung.

---
# Contributors
💡 Terima kasih kepada semua kontributor luar biasa
<table align="center">
      <tr>
        <td align="center">
          <a href="https://github.com/xnuvers007">
            <img
              src="https://github.com/xnuvers007.png"
              width="80px;"
              style="border-radius: 50%; border: 2px solid #444"
            />
            <br />
            <sub>
              <b>xnuvers007</b>
            </sub>
          </a>
          <br />
          <sub>🧠 Security Researcher • 🧩 Developer • 🔍 Penetration Tester</sub>
        </td>
        <td align="center">
          <a href="https://github.com/apps/github-actions">
            <img
              src="https://avatars.githubusercontent.com/in/15368?s=64&v=4"
              width="80px;"
              style="border-radius: 50%; border: 2px solid #444"
            />
            <br />
            <sub>
              <b>Github Bot</b>
            </sub>
          </a>
          <br />
          <sub>🤖 Automation Bot</sub>
        </td>
      </tr>
</table>
