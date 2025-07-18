<!-- Banner -->
<p align="center">
  <img src="https://scayar.com/assets/scayforce-banner.png" alt="ScayForce" width="600"/>
</p>

<h1 align="center">🚀 ScayForce</h1>
<p align="center">
  <b>The Ultimate Modern Password Cracker for ZIP/RAR Archives</b><br>
  <i>All rights reserved © <a href="https://scayar.com">Scayar</a></i>
</p>

<p align="center">
  <a href="https://scayar.com"><img src="https://img.shields.io/badge/website-scayar.com-blue?style=flat-square&logo=google-chrome"></a>
  <a href="https://t.me/im_scayar"><img src="https://img.shields.io/badge/telegram-@im_scayar-2CA5E0?style=flat-square&logo=telegram"></a>
  <a href="mailto:Scayar.exe@gmail.com"><img src="https://img.shields.io/badge/email-Scayar.exe@gmail.com-red?style=flat-square&logo=gmail"></a>
  <a href="https://buymeacoffee.com/scayar"><img src="https://img.shields.io/badge/buy%20me%20a%20coffee-support-yellow?style=flat-square&logo=buy-me-a-coffee"></a>
</p>

---

## ✨ Features

- ⚡️ Ultra-modern CLI with hacker vibes
- 🧠 Smart password pattern intelligence
- 🔄 Auto-resume for interrupted sessions
- ☁️ Download popular wordlists automatically
- 🔔 Desktop/email notifications on success
- 📊 Beautiful progress bars and live attempt feed
- 📝 Detailed logging and reporting

---

## 🧪 Quick Test: Try ScayForce Instantly!

> **No setup needed!**
>
> - A sample ZIP file (`test.zip`) is already included in this folder.
> - The password for `test.zip` is **123321**.
> - You need to download the wordlist `rockyou.txt` (not included due to GitHub file size limits).

### ▶️ **How to Download rockyou.txt:**

Run this command in your ScayForce folder:
```bash
python ScayForce.py --fetch-wordlist rockyou.txt
```

Or download it manually from [here](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) and place it in the tool folder.

### ▶️ **How to Test:**

```bash
python ScayForce.py --file test.zip --dictionary --wordlist rockyou.txt
```

- The tool will try passwords from `rockyou.txt` and should find the password `123321` for `test.zip`.
- You can also try brute-force or other options as shown below.

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/scayar/ScayForce.git
cd ScayForce

# 2. Install requirements
pip install -r requirements.txt

# 3. Download the wordlist (if you haven't already)
python ScayForce.py --fetch-wordlist rockyou.txt
```

---

## 🧑‍💻 How to Use ScayForce

> **Super Easy! Just follow these steps:**

### 1️⃣ Crack a ZIP/RAR file with a wordlist (Dictionary Attack)
```bash
python ScayForce.py --file test.zip --dictionary --wordlist rockyou.txt
```
- `--file` : Path to your ZIP or RAR file
- `--dictionary` : Use a wordlist to try passwords
- `--wordlist` : Path to your wordlist file (e.g. rockyou.txt)

### 2️⃣ Brute-force Attack (Try all combinations)
```bash
python ScayForce.py --file test.zip --bruteforce --charset 0123456789 --max-length 4
```
- `--bruteforce` : Try all possible combinations
- `--charset` : Characters to use (e.g. numbers only)
- `--max-length` : Maximum password length to try

### 3️⃣ Auto-resume (Continue after interruption)
```bash
python ScayForce.py --file test.zip --dictionary --wordlist rockyou.txt --resume
```
- `--resume` : Continue from where you left off if the process was interrupted

### 4️⃣ Download a popular wordlist automatically
```bash
python ScayForce.py --file test.zip --dictionary --fetch-wordlist rockyou.txt
```
- `--fetch-wordlist` : Download and use a popular wordlist (like rockyou.txt)

### 5️⃣ Get notified by email when password is found
```bash
python ScayForce.py --file test.zip --dictionary --wordlist rockyou.txt --notify-email you@email.com
```
- `--notify-email` : Send an email notification when the password is found

---

## 🛠️ All Options Explained

| Option              | Description                                      |
|---------------------|--------------------------------------------------|
| `--file`            | Path to the ZIP or RAR file                      |
| `--dictionary`      | Use a wordlist for password attempts             |
| `--wordlist`        | Path to the wordlist file                        |
| `--bruteforce`      | Use brute-force attack                           |
| `--charset`         | Characters to use in brute-force                 |
| `--max-length`      | Max password length for brute-force              |
| `--resume`          | Resume from last progress                        |
| `--fetch-wordlist`  | Download a popular wordlist automatically        |
| `--notify-email`    | Email to notify when password is found           |
| `--threads`         | Number of threads to use (default: 4)            |
| `--verbose`         | Show every password attempt                      |
| `--log`             | Log file for results (default: crack_results.log)|

---

## 💡 Pro Tips

- 🏷️ **Use strong wordlists** for better results (try `rockyou.txt` or your own custom list).
- 🚦 **Verbose mode** (`--verbose`) lets you see every password attempt in real time.
- 🧩 **Multi-threading** (`--threads 8`) can speed up cracking on modern CPUs.
- 💾 **Auto-resume** is a lifesaver for long sessions—never lose your progress!
- 📈 **Check `crack_results.log`** for a summary of all attempts and results.

---

## 👤 Author & Rights

- **Tool Name:** ScayForce  
- **Author:** [Scayar](https://scayar.com)  
- **All rights reserved © Scayar**

---

## 🌐 Official Channels

- 🌍 **Website:** [scayar.com](https://scayar.com)
- 💬 **Telegram Group:** [@im_scayar](https://t.me/im_scayar)
- 📧 **Email:** [Scayar.exe@gmail.com](mailto:Scayar.exe@gmail.com)
- ☕ **Buy Me a Coffee:** [buymeacoffee.com/scayar](https://buymeacoffee.com/scayar)

---

## 🛡️ Disclaimer

> This tool is for educational and authorized security testing purposes only.  
> **Do not** use it on systems or archives you do not own or have explicit permission to test.

---

## ⭐️ Show your support

If you like ScayForce, star the repo and share it with your friends!

<p align="center">
  <img src="https://img.shields.io/github/stars/scayar/ScayForce?style=social" alt="GitHub stars"/>
</p> 