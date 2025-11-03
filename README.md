<!-- Banner -->
<p align="center">
  <img src="banner.png" alt="ScayForce" width="600"/>
</p>

<h1 align="center">🚀 ScayForce</h1>
<p align="center">
  <b>The Ultimate Modern Password Cracker for ZIP/RAR Archives</b><br>
  <i>A powerful, feature-rich password recovery tool with beautiful CLI and advanced cracking capabilities</i>
</p>

<p align="center">
  <a href="https://scayar.com"><img src="https://img.shields.io/badge/website-scayar.com-blue?style=for-the-badge&logo=google-chrome"></a>
  <a href="https://t.me/im_scayar"><img src="https://img.shields.io/badge/telegram-@im_scayar-2CA5E0?style=for-the-badge&logo=telegram"></a>
  <a href="mailto:Scayar.exe@gmail.com"><img src="https://img.shields.io/badge/email-Scayar.exe@gmail.com-red?style=for-the-badge&logo=gmail"></a>
  <a href="https://buymeacoffee.com/scayar"><img src="https://img.shields.io/badge/buy%20me%20a%20coffee-support-yellow?style=for-the-badge&logo=buy-me-a-coffee"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.7+-blue.svg?style=flat-square&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-green.svg?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/status-active-success.svg?style=flat-square" alt="Status">
</p>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🏗️ Architecture](#️-architecture)
- [🔄 Workflow](#-workflow)
- [🚀 Quick Start](#-quick-start)
- [🧑‍💻 Usage Guide](#-usage-guide)
- [🛠️ Advanced Options](#️-advanced-options)
- [📊 Performance](#-performance)
- [🧪 Testing](#-testing)
- [🛡️ Security & Disclaimer](#️-security--disclaimer)
- [📞 Credits](#-credits)

---

## ✨ Features

### Core Capabilities
- 🎯 **Multi-format Support**: Crack both ZIP and RAR archives (AES encryption support)
- 🔀 **Dual Attack Modes**: Dictionary attacks and brute-force attacks
- ⚡ **Multi-threading**: Parallel password attempts for maximum speed
- 🧠 **Smart Pattern Intelligence**: Automatically tries common password patterns based on filename
- 🔄 **Auto-resume**: Resume interrupted sessions without losing progress
- ☁️ **Wordlist Downloader**: Automatically fetch popular wordlists (rockyou.txt)

### User Experience
- 🎨 **Beautiful CLI**: Rich terminal UI with hacker vibes, progress bars, and live updates
- 📊 **Real-time Feed**: See password attempts in real-time with verbose mode
- 📝 **Detailed Logging**: Comprehensive log files for all attempts and results
- 🔔 **Notifications**: Desktop and email notifications when password is found
- 🎬 **Animated Intro**: Matrix-style intro and typewriter banner effects

### Technical Excellence
- ✅ **Error Handling**: Robust error handling and graceful failures
- 📈 **Progress Tracking**: Real-time progress bars with time elapsed
- 💾 **State Persistence**: Save and restore cracking session state
- 🎯 **Smart Suggestions**: Pattern-based password suggestions before main attack

---

## 🏗️ Architecture

### System Architecture Diagram

```mermaid
graph TB
    A[User Input] --> B[ScayForce CLI]
    B --> C{File Type Detection}
    C -->|ZIP| D[ZipCracker Class]
    C -->|RAR| E[RarCracker Class]
    
    D --> F{Attack Mode}
    E --> F
    F -->|Dictionary| G[Dictionary Attack]
    F -->|Brute Force| H[Bruteforce Attack]
    
    G --> I[Wordlist Parser]
    H --> J[Password Generator]
    
    I --> K[Multi-threaded Workers]
    J --> K
    
    K --> L[Password Validator]
    L --> M{Password Found?}
    M -->|Yes| N[Success Handler]
    M -->|No| K
    
    N --> O[Notifications]
    N --> P[Logging]
    N --> Q[Result Output]
    
    style A fill:#4a90e2
    style B fill:#50c878
    style N fill:#ff6b6b
    style K fill:#ffd93d
```

### Component Overview

```mermaid
graph LR
    subgraph "Core Components"
        A[File Type Detector] --> B[ZipCracker]
        A --> C[RarCracker]
        B --> D[Worker Threads]
        C --> D
    end
    
    subgraph "Support Systems"
        E[Pattern Intelligence] --> F[Smart Suggestions]
        G[Resume Manager] --> H[State Persistence]
        I[Notification System] --> J[Desktop/Email]
        K[Logging System] --> L[Result Files]
    end
    
    subgraph "User Interface"
        M[Rich Console] --> N[Progress Bars]
        M --> O[Live Feed]
        M --> P[Beautiful Output]
    end
    
    D --> E
    D --> G
    D --> I
    D --> K
    D --> M
    
    style A fill:#4a90e2
    style D fill:#50c878
    style M fill:#ffd93d
```

---

## 🔄 Workflow

### Cracking Process Flow

```mermaid
flowchart TD
    Start([Start ScayForce]) --> Init[Initialize CLI & Banner]
    Init --> LoadFile[Load Target File]
    LoadFile --> Detect{Detect File Type}
    Detect -->|ZIP| CheckZip[Check pyzipper installed]
    Detect -->|RAR| CheckRar[Check rarfile installed]
    
    CheckZip --> Validate[Validate File Exists]
    CheckRar --> Validate
    
    Validate --> AttackMode{Select Attack Mode}
    AttackMode -->|Dictionary| DictMode[Dictionary Attack]
    AttackMode -->|Brute Force| BruteMode[Bruteforce Attack]
    
    DictMode --> LoadWordlist[Load Wordlist]
    BruteMode --> GeneratePasswords[Generate Password Combinations]
    
    LoadWordlist --> PatternCheck[Check Smart Patterns]
    GeneratePasswords --> PatternCheck
    
    PatternCheck --> TryPatterns{Try Smart Patterns First}
    TryPatterns -->|Found| Success[Password Found!]
    TryPatterns -->|Not Found| StartThreads[Start Worker Threads]
    
    StartThreads --> MultiThread[Multi-threaded Password Attempts]
    MultiThread --> TryPassword{Try Password}
    TryPassword -->|Valid| Success
    TryPassword -->|Invalid| UpdateProgress[Update Progress]
    UpdateProgress --> SaveState{Save State?}
    SaveState -->|Yes| PersistState[Persist to Resume File]
    SaveState -->|No| CheckMore{More Passwords?}
    PersistState --> CheckMore
    CheckMore -->|Yes| TryPassword
    CheckMore -->|No| Failure[Password Not Found]
    
    Success --> Notify[Send Notifications]
    Success --> Log[Log Results]
    Success --> Display[Display Success Message]
    
    Failure --> LogFailure[Log Failure]
    Failure --> Exit([Exit])
    
    Notify --> Exit
    Log --> Exit
    Display --> Exit
    LogFailure --> Exit
    
    style Start fill:#4a90e2
    style Success fill:#50c878
    style Failure fill:#ff6b6b
    style MultiThread fill:#ffd93d
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/scayar/ScayForce.git
cd ScayForce

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Download a wordlist
python ScayForce.py --fetch-wordlist rockyou.txt
```

### Basic Usage

```bash
# Dictionary attack on a ZIP file
python ScayForce.py --file archive.zip --dictionary --wordlist rockyou.txt

# Brute-force attack (numbers only, max length 4)
python ScayForce.py --file archive.zip --bruteforce --charset 0123456789 --max-length 4
```

---

## 🧑‍💻 Usage Guide

### 1️⃣ Dictionary Attack (Recommended)

Use a wordlist file to try common passwords:

```bash
python ScayForce.py --file encrypted.zip --dictionary --wordlist rockyou.txt
```

**Options:**
- `--file`: Path to your ZIP or RAR file
- `--dictionary`: Enable dictionary attack mode
- `--wordlist`: Path to your wordlist file

### 2️⃣ Brute-Force Attack

Try all possible combinations:

```bash
python ScayForce.py --file encrypted.zip --bruteforce --charset 0123456789abcdef --max-length 6
```

**Options:**
- `--bruteforce`: Enable brute-force attack mode
- `--charset`: Characters to use (default: alphanumeric)
- `--max-length`: Maximum password length to try

### 3️⃣ With Auto-Resume

Resume interrupted sessions:

```bash
python ScayForce.py --file encrypted.zip --dictionary --wordlist rockyou.txt --resume
```

### 4️⃣ Verbose Mode

See every password attempt in real-time:

```bash
python ScayForce.py --file encrypted.zip --dictionary --wordlist rockyou.txt --verbose
```

### 5️⃣ Multi-threading

Increase threads for faster cracking:

```bash
python ScayForce.py --file encrypted.zip --dictionary --wordlist rockyou.txt --threads 8
```

### 6️⃣ With Notifications

Get notified when password is found:

```bash
# Desktop notification (automatic)
python ScayForce.py --file encrypted.zip --dictionary --wordlist rockyou.txt --notify

# Email notification
python ScayForce.py --file encrypted.zip --dictionary --wordlist rockyou.txt --notify-email your@email.com
```

---

## 🛠️ Advanced Options

### Complete Option Reference

| Option | Description | Default | Example |
|--------|-------------|---------|---------|
| `--file` | Path to ZIP/RAR file | Required | `--file archive.zip` |
| `--dictionary` | Use dictionary attack | - | `--dictionary` |
| `--wordlist` | Path to wordlist file | Required with `--dictionary` | `--wordlist rockyou.txt` |
| `--bruteforce` | Use brute-force attack | - | `--bruteforce` |
| `--charset` | Characters for brute-force | alphanumeric | `--charset 0123456789` |
| `--max-length` | Max password length | 4 | `--max-length 6` |
| `--threads` | Number of threads | 4 | `--threads 8` |
| `--resume` | Resume from last session | Disabled | `--resume` |
| `--verbose` | Show all attempts | Disabled | `--verbose` |
| `--notify` | Desktop notification | Disabled | `--notify` |
| `--notify-email` | Email notification | - | `--notify-email user@mail.com` |
| `--fetch-wordlist` | Download wordlist | - | `--fetch-wordlist rockyou.txt` |
| `--log` | Log file path | `crack_results.log` | `--log mylog.log` |

### Performance Optimization Tips

```bash
# Use all CPU cores
python ScayForce.py --file archive.zip --dictionary --wordlist rockyou.txt --threads $(nproc)

# Optimize for specific charset
python ScayForce.py --file archive.zip --bruteforce --charset "0123456789" --max-length 4

# Combine resume with verbose for long sessions
python ScayForce.py --file archive.zip --dictionary --wordlist rockyou.txt --resume --verbose
```

---

## 📊 Performance

### Performance Characteristics

```mermaid
graph LR
    A[Password Attempt Speed] --> B{Attack Type}
    B -->|Dictionary| C[~100-1000/sec]
    B -->|Brute Force| D[~500-5000/sec]
    
    E[Thread Count] --> F{Performance Impact}
    F -->|4 threads| G[Standard]
    F -->|8 threads| H[Fast]
    F -->|16 threads| I[Very Fast]
    
    J[File Type] --> K{Encryption}
    K -->|AES-256 ZIP| L[Slower]
    K -->|Standard ZIP| M[Faster]
    K -->|RAR| N[Medium]
    
    style C fill:#50c878
    style D fill:#ffd93d
    style I fill:#ff6b6b
```

### Expected Performance

- **Dictionary Attack**: 100-1,000 passwords/second (depends on file size and encryption)
- **Brute-Force Attack**: 500-5,000 passwords/second
- **Multi-threading**: Linear scaling with thread count (up to CPU cores)
- **Memory Usage**: Low (<100MB for typical wordlists)

---

## 🧪 Testing

### Quick Test with Included Sample

A sample ZIP file (`test.zip`) is included for testing. The password is `123321`.

```bash
# 1. Download wordlist (if not already downloaded)
python ScayForce.py --fetch-wordlist rockyou.txt

# 2. Run dictionary attack
python ScayForce.py --file test.zip --dictionary --wordlist rockyou.txt

# 3. Or try brute-force (faster for this simple password)
python ScayForce.py --file test.zip --bruteforce --charset 0123456789 --max-length 6
```

### Creating Test Archives

```bash
# Create a test ZIP with password
zip -P password123 test.zip file1.txt file2.txt

# Create a test RAR with password
rar a -psecret456 test.rar file1.txt file2.txt
```

---

## 🛡️ Security & Disclaimer

### ⚠️ Legal Notice

**This tool is for educational and authorized security testing purposes only.**

- ✅ Use only on files you own or have explicit permission to test
- ✅ Use for legitimate password recovery (forgotten passwords)
- ✅ Use in authorized penetration testing environments
- ❌ Do NOT use on systems or archives without permission
- ❌ Do NOT use for illegal activities
- ❌ Do NOT violate any laws or regulations

### Security Best Practices

- Always keep wordlists and logs secure
- Use strong passwords for your archives
- Regularly update dependencies
- Review code before using in production environments

---

## 📞 Credits

### Author

**Scayar**

- 🌐 **Website**: [Scayar.com](https://scayar.com)
- 📧 **Email**: [Scayar.exe@gmail.com](mailto:Scayar.exe@gmail.com)
- 💬 **Telegram**: [@im_scayar](https://t.me/im_scayar)
- ☕ **Buy Me a Coffee**: [buymeacoffee.com/scayar](https://buymeacoffee.com/scayar)

### Acknowledgments

- Built with ❤️ by Scayar
- Uses [Rich](https://github.com/Textualize/rich) for beautiful terminal output
- Supports [pyzipper](https://github.com/danifus/pyzipper) for ZIP handling
- Uses [rarfile](https://github.com/markokr/rarfile) for RAR support

### License

All rights reserved © Scayar

---

## ⭐️ Support the Project

If you find ScayForce useful, please:

- ⭐ Star this repository
- 🐛 Report bugs and issues
- 💡 Suggest new features
- 📣 Share with your friends
- ☕ [Buy me a coffee](https://buymeacoffee.com/scayar)

---

<p align="center">
  <b>Made with ❤️ by Scayar</b><br>
  <i>Happy Cracking! 🔓</i>
</p>
