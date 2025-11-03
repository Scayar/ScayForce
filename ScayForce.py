#!/usr/bin/env python3
"""
ScayForce - Modern ZIP/RAR Password Cracker
Author: Scayar
Website: https://scayar.com
Email: Scayar.exe@gmail.com
Telegram: @im_scayar

A powerful, modern password cracking tool for ZIP and RAR archives
with beautiful CLI, smart pattern intelligence, and advanced features.
"""
import argparse
import os
import sys
import threading
import time
import random
from datetime import datetime
import json
import urllib.request

try:
    from rich.console import Console
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
    from rich.panel import Panel
    from rich.text import Text
    from rich.theme import Theme
    from rich.prompt import Prompt
    from rich.live import Live
    from rich.table import Table
    from rich.align import Align
    from rich.layout import Layout
except ImportError:
    print("[!] 'rich' library not installed. Please run: pip install rich")
    sys.exit(1)

try:
    import pyzipper
except ImportError:
    pyzipper = None
try:
    import rarfile
except ImportError:
    rarfile = None
try:
    from plyer import notification
except ImportError:
    notification = None
import smtplib
from email.mime.text import MIMEText

# ========== Custom Theme ========== #
hacker_theme = Theme({
    "banner": "bold green",
    "success": "bold bright_green",
    "fail": "bold red",
    "info": "bold cyan",
    "warning": "bold yellow",
    "prompt": "bold magenta",
    "quote": "italic bright_black",
    "log": "dim white"
})
console = Console(theme=hacker_theme)

# ========== Hacker Quotes ========== #
hacker_quotes = [
    "The quieter you become, the more you are able to hear.",
    "There is no patch for human stupidity.",
    "Hack the planet!",
    "Security is just an illusion.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "The best way to predict the future is to invent it.",
    "You are only as secure as your weakest password.",
    "In the world of bits and bytes, trust no one."
]

# ========== Matrix Intro ========== #
def matrix_intro(lines=10, width=60, delay=0.04):
    charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()'
    for _ in range(lines):
        line = ''.join(random.choice(charset) for _ in range(width))
        console.print(f'[green]{line}[/green]')
        time.sleep(delay)

# ========== Typewriter Banner ========== #
def typewriter_banner(banner):
    for line in banner.split('\n'):
        console.print(f'[banner]{line}[/banner]', end='\n', highlight=False)
        time.sleep(0.03)

# ========== Glitch Effect for Quotes ========== #
def glitch_text(text, color='green'):
    glitched = ''
    for c in text:
        if random.random() < 0.08:
            glitched += random.choice('!@#$%^&*()_+-=')
        else:
            glitched += c
    return f'[{color}]{glitched}[/{color}]'

# ========== Banner (unchanged) ========== #
def print_banner():
    banner = r'''
 ad8888888888ba
 dP'         `"8b,
 8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
 8  8' `8           "88baadP""""YbaaadP""""YbdP""Yb
 8  8   8              """        """      ""    8b
 8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
 8  `"""'       ,d8""
 Yb,         ,ad8"    Scayar
  "Y8888888888P"
    '''
    typewriter_banner(banner)
    quote = random.choice(hacker_quotes)
    console.print(Panel(glitch_text(quote, 'bright_green'), style="quote", title="[bold green]Hacker Tip"))
    console.print("[info]IHA089: Navigating the Digital Realm with Code and Security - Where Programming Insights Meet Cyber Vigilance.\n")

# ========== File Type Detection ========== #
def detect_file_type(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".zip":
        return "zip"
    elif ext == ".rar":
        return "rar"
    else:
        return None

# ========== Logging ========== #
def log_result(logfile, message):
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {message}\n")

# ========== Password Cracker Classes (add live feed for verbose) ========== #
class ZipCracker:
    def __init__(self, filename, wordlist=None, charset=None, max_length=None, threads=4, log=None, verbose=False):
        self.filename = filename
        self.wordlist = wordlist
        self.charset = charset
        self.max_length = max_length
        self.threads = threads
        self.log = log
        self.verbose = verbose
        self.found = threading.Event()
        self.password = None

    def try_password(self, password):
        """Try to extract the ZIP file with the given password."""
        try:
            with pyzipper.AESZipFile(self.filename) as zf:
                zf.pwd = password.encode("utf-8")
                # Try to read the first file without extracting
                zf.testzip()
            return True
        except (RuntimeError, pyzipper.BadZipFile, Exception):
            return False

    def worker(self, passwords, progress, task, feed, update_feed):
        for pwd in passwords:
            if self.found.is_set():
                return
            if self.try_password(pwd):
                self.password = pwd
                self.found.set()
                if self.log:
                    log_result(self.log, f"[ZIP] Password found: {pwd}")
                console.print(f"[success]\n[ZIP] ✓ Password found: [bold]{pwd}[/bold]")
                return
            if self.verbose and feed is not None:
                feed.append(pwd)
                if len(feed) > 10:
                    feed.pop(0)
                update_feed()
            progress.update(task, advance=1)

    def run_dictionary(self):
        with open(self.wordlist, "r", encoding="utf-8", errors="ignore") as f:
            passwords = [line.strip() for line in f if line.strip()]
        chunk_size = len(passwords) // self.threads + 1
        feed = []
        progress = Progress(SpinnerColumn(), BarColumn(), TextColumn("[progress.percentage]{task.percentage:>3.0f}%"), TimeElapsedColumn(), console=console)
        task = progress.add_task("[cyan]Cracking ZIP...", total=len(passwords))
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Last Attempts", style="cyan")
        layout = Layout()
        layout.split_column(
            Layout(progress, name="progress", size=3),
            Layout(table, name="feed")
        )
        def update_feed():
            table.rows = []
            for attempt in reversed(feed):
                table.add_row(attempt)
        with Live(layout, refresh_per_second=10, console=console):
            threads = []
            for i in range(self.threads):
                chunk = passwords[i*chunk_size:(i+1)*chunk_size]
                t = threading.Thread(target=self.worker, args=(chunk, progress, task, feed if self.verbose else None, update_feed if self.verbose else None))
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
        if not self.password:
            console.print("[fail]Password not found in wordlist.")
            if self.log:
                log_result(self.log, "[ZIP] Password not found.")

    def run_bruteforce(self):
        from itertools import product
        all_pwds = []
        for l in range(1, self.max_length+1):
            all_pwds.extend([''.join(x) for x in product(self.charset, repeat=l)])
        chunk_size = len(all_pwds) // self.threads + 1
        feed = []
        progress = Progress(SpinnerColumn(), BarColumn(), TextColumn("[progress.percentage]{task.percentage:>3.0f}%"), TimeElapsedColumn(), console=console)
        task = progress.add_task("[cyan]Bruteforcing ZIP...", total=len(all_pwds))
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Last Attempts", style="cyan")
        layout = Layout()
        layout.split_column(
            Layout(progress, name="progress", size=3),
            Layout(table, name="feed")
        )
        def update_feed():
            table.rows = []
            for attempt in reversed(feed):
                table.add_row(attempt)
        with Live(layout, refresh_per_second=10, console=console):
            threads = []
            for i in range(self.threads):
                chunk = all_pwds[i*chunk_size:(i+1)*chunk_size]
                t = threading.Thread(target=self.worker, args=(chunk, progress, task, feed if self.verbose else None, update_feed if self.verbose else None))
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
        if not self.password:
            console.print("[fail]Password not found with bruteforce.")
            if self.log:
                log_result(self.log, "[ZIP] Password not found (bruteforce).")

class RarCracker:
    def __init__(self, filename, wordlist=None, charset=None, max_length=None, threads=4, log=None, verbose=False):
        self.filename = filename
        self.wordlist = wordlist
        self.charset = charset
        self.max_length = max_length
        self.threads = threads
        self.log = log
        self.verbose = verbose
        self.found = threading.Event()
        self.password = None

    def try_password(self, password):
        """Try to open the RAR file with the given password."""
        try:
            rf = rarfile.RarFile(self.filename)
            rf.setpassword(password)
            # Try to read file info to verify password
            if rf.namelist():
                rf.getinfo(rf.namelist()[0])
            rf.close()
            return True
        except (rarfile.BadRarFile, rarfile.RarWrongPassword, rarfile.RarCannotExec, Exception):
            try:
                rf.close()
            except:
                pass
            return False

    def worker(self, passwords, progress, task, feed, update_feed):
        for pwd in passwords:
            if self.found.is_set():
                return
            if self.try_password(pwd):
                self.password = pwd
                self.found.set()
                if self.log:
                    log_result(self.log, f"[RAR] Password found: {pwd}")
                console.print(f"[success]\n[RAR] ✓ Password found: [bold]{pwd}[/bold]")
                return
            if self.verbose and feed is not None:
                feed.append(pwd)
                if len(feed) > 10:
                    feed.pop(0)
                update_feed()
            progress.update(task, advance=1)

    def run_dictionary(self):
        with open(self.wordlist, "r", encoding="utf-8", errors="ignore") as f:
            passwords = [line.strip() for line in f if line.strip()]
        chunk_size = len(passwords) // self.threads + 1
        feed = []
        progress = Progress(SpinnerColumn(), BarColumn(), TextColumn("[progress.percentage]{task.percentage:>3.0f}%"), TimeElapsedColumn(), console=console)
        task = progress.add_task("[cyan]Cracking RAR...", total=len(passwords))
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Last Attempts", style="cyan")
        layout = Layout()
        layout.split_column(
            Layout(progress, name="progress", size=3),
            Layout(table, name="feed")
        )
        def update_feed():
            table.rows = []
            for attempt in reversed(feed):
                table.add_row(attempt)
        with Live(layout, refresh_per_second=10, console=console):
            threads = []
            for i in range(self.threads):
                chunk = passwords[i*chunk_size:(i+1)*chunk_size]
                t = threading.Thread(target=self.worker, args=(chunk, progress, task, feed if self.verbose else None, update_feed if self.verbose else None))
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
        if not self.password:
            console.print("[fail]Password not found in wordlist.")
            if self.log:
                log_result(self.log, "[RAR] Password not found.")

    def run_bruteforce(self):
        from itertools import product
        all_pwds = []
        for l in range(1, self.max_length+1):
            all_pwds.extend([''.join(x) for x in product(self.charset, repeat=l)])
        chunk_size = len(all_pwds) // self.threads + 1
        feed = []
        progress = Progress(SpinnerColumn(), BarColumn(), TextColumn("[progress.percentage]{task.percentage:>3.0f}%"), TimeElapsedColumn(), console=console)
        task = progress.add_task("[cyan]Bruteforcing RAR...", total=len(all_pwds))
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Last Attempts", style="cyan")
        layout = Layout()
        layout.split_column(
            Layout(progress, name="progress", size=3),
            Layout(table, name="feed")
        )
        def update_feed():
            table.rows = []
            for attempt in reversed(feed):
                table.add_row(attempt)
        with Live(layout, refresh_per_second=10, console=console):
            threads = []
            for i in range(self.threads):
                chunk = all_pwds[i*chunk_size:(i+1)*chunk_size]
                t = threading.Thread(target=self.worker, args=(chunk, progress, task, feed if self.verbose else None, update_feed if self.verbose else None))
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
        if not self.password:
            console.print("[fail]Password not found with bruteforce.")
            if self.log:
                log_result(self.log, "[RAR] Password not found (bruteforce).")

# ========== Resume Helpers ========== #
RESUME_FILE = ".scayforce_resume.json"

def save_resume(state):
    with open(RESUME_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f)

def load_resume():
    try:
        with open(RESUME_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def clear_resume():
    if os.path.exists(RESUME_FILE):
        os.remove(RESUME_FILE)

COMMON_PATTERNS = [
    '{filename}', '{filename}123', '{filename}2024', '{filename}!', '{filename}@',
    '{filename}1', '{filename}12', '{filename}1234', '{filename}2023',
    '{filename.lower()}', '{filename.upper()}', '{filename.capitalize()}',
    'password', 'admin', '123456', 'qwerty', 'letmein', 'welcome', '0000', '1111', 'abc123',
]

CURRENT_YEAR = str(datetime.now().year)
PREV_YEAR = str(datetime.now().year - 1)

# ========== Pattern Intelligence Helper ========== #
def suggest_patterns(file_path):
    base = os.path.splitext(os.path.basename(file_path))[0]
    patterns = []
    for pat in COMMON_PATTERNS:
        try:
            val = pat.format(
                filename=base,
                filename_lower=base.lower(),
                filename_upper=base.upper(),
                filename_cap=base.capitalize(),
                year=CURRENT_YEAR,
                prev_year=PREV_YEAR
            )
            patterns.append(val)
        except Exception:
            pass
    # Add years
    for y in range(datetime.now().year, datetime.now().year-10, -1):
        patterns.append(str(y))
        patterns.append(base + str(y))
    # Remove duplicates, keep order
    seen = set()
    smart_patterns = []
    for p in patterns:
        if p not in seen:
            smart_patterns.append(p)
            seen.add(p)
    return smart_patterns

# ========== Patch Cracker Classes for Pattern Intelligence ========== #
def patch_pattern_intelligence(cls):
    orig_run_dictionary = cls.run_dictionary
    orig_run_bruteforce = cls.run_bruteforce
    def run_dictionary(self):
        # Suggest patterns
        patterns = suggest_patterns(self.filename)
        console.print("[info]Trying smart patterns first:")
        for p in patterns:
            console.print(f"[cyan]- {p}")
        # Ask user to skip or confirm
        try:
            from rich.prompt import Confirm
            if not Confirm.ask("[prompt]Try these patterns before main wordlist?", default=True):
                patterns = []
        except Exception:
            pass
        # Try patterns first
        for pwd in patterns:
            if self.found.is_set():
                return
            if self.try_password(pwd):
                self.password = pwd
                self.found.set()
                if self.log:
                    log_result(self.log, f"[PATTERN] Password found: {pwd}")
                console.print(f"[success]\n[PATTERN] Password found: [bold]{pwd}[/bold]")
                clear_resume()
                return
        # Then continue with original logic
        orig_run_dictionary(self)
    def run_bruteforce(self):
        # Suggest patterns
        patterns = suggest_patterns(self.filename)
        console.print("[info]Trying smart patterns first:")
        for p in patterns:
            console.print(f"[cyan]- {p}")
        try:
            from rich.prompt import Confirm
            if not Confirm.ask("[prompt]Try these patterns before main brute-force?", default=True):
                patterns = []
        except Exception:
            pass
        for pwd in patterns:
            if self.found.is_set():
                return
            if self.try_password(pwd):
                self.password = pwd
                self.found.set()
                if self.log:
                    log_result(self.log, f"[PATTERN] Password found: {pwd}")
                console.print(f"[success]\n[PATTERN] Password found: [bold]{pwd}[/bold]")
                clear_resume()
                return
        orig_run_bruteforce(self)
    cls.run_dictionary = run_dictionary
    cls.run_bruteforce = run_bruteforce

# ========== Wordlist Fetcher ========== #
WORDLIST_URLS = {
    'rockyou.txt': 'https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt'
}

def fetch_wordlist(name, dest):
    url = WORDLIST_URLS.get(name)
    if not url:
        console.print(f"[fail]No URL found for wordlist: {name}")
        return False
    try:
        with console.status(f"[info]Downloading {name}..."):
            urllib.request.urlretrieve(url, dest)
        console.print(f"[success]Downloaded {name} to {dest}")
        return True
    except Exception as e:
        console.print(f"[fail]Failed to download {name}: {e}")
        return False

# ========== Smart Notification Helpers ========== #
def send_desktop_notification(title, message):
    if notification:
        try:
            notification.notify(title=title, message=message, timeout=10)
        except Exception:
            pass
    else:
        console.print("[warning]plyer not installed: desktop notification not sent. Run: pip install plyer")

def send_email_notification(to_email, subject, body):
    try:
        # Simple SMTP: user must configure their SMTP server here
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_user = ''  # <-- User must fill
        smtp_pass = ''  # <-- User must fill
        if not smtp_user or not smtp_pass:
            console.print("[warning]Email notification not sent: SMTP credentials not set in script.")
            return
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = smtp_user
        msg['To'] = to_email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(smtp_user, [to_email], msg.as_string())
        server.quit()
        console.print(f"[success]Email notification sent to {to_email}")
    except Exception as e:
        console.print(f"[warning]Failed to send email notification: {e}")

# ========== Main ========== #
def main():
    parser = argparse.ArgumentParser(description="[Hacker Vibes] ZIP/RAR Password Cracker with Modern Features")
    parser.add_argument('--file', required=True, help='Target ZIP or RAR file')
    parser.add_argument('--bruteforce', action='store_true', help='Use brute-force attack')
    parser.add_argument('--dictionary', action='store_true', help='Use dictionary attack')
    parser.add_argument('--charset', default='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', help='Charset for brute-force')
    parser.add_argument('--max-length', type=int, default=4, help='Max password length for brute-force')
    parser.add_argument('--wordlist', help='Wordlist file for dictionary attack')
    parser.add_argument('--threads', type=int, default=4, help='Number of threads to use')
    parser.add_argument('--log', default='crack_results.log', help='Log file for results')
    parser.add_argument('--verbose', action='store_true', help='Show every attempt')
    parser.add_argument('--notify', action='store_true', help='Play sound/notification on success (Windows only)')
    parser.add_argument('--notify-email', help='Send email notification to this address when password is found')
    parser.add_argument('--resume', action='store_true', help='Resume from last progress if available')
    parser.add_argument('--fetch-wordlist', choices=WORDLIST_URLS.keys(), help='Download a popular wordlist and use it')
    args = parser.parse_args()

    if getattr(args, 'fetch_wordlist', None):
        wl_name = args.fetch_wordlist
        wl_path = os.path.join(os.getcwd(), wl_name)
        if not os.path.exists(wl_path):
            if not fetch_wordlist(wl_name, wl_path):
                sys.exit(1)
        args.wordlist = wl_path
        console.print(f"[info]Using downloaded wordlist: {wl_path}")

    matrix_intro()
    print_banner()

    if not os.path.isfile(args.file):
        console.print(f"[fail]File not found: {args.file}")
        sys.exit(1)

    ftype = detect_file_type(args.file)
    if ftype == "zip" and not pyzipper:
        console.print("[fail]pyzipper not installed. Please run: pip install pyzipper")
        sys.exit(1)
    if ftype == "rar" and not rarfile:
        console.print("[fail]rarfile not installed. Please run: pip install rarfile")
        sys.exit(1)
    if not ftype:
        console.print("[fail]Unsupported file type. Only .zip and .rar are supported.")
        sys.exit(1)

    if args.dictionary and not args.wordlist:
        console.print("[fail]You must specify --wordlist with --dictionary.")
        sys.exit(1)

    if args.bruteforce and not args.charset:
        console.print("[fail]You must specify --charset with --bruteforce.")
        sys.exit(1)

    # Resume logic
    resume_state = load_resume() if args.resume else None
    resume_idx = 0
    if resume_state and resume_state.get("file") == args.file:
        resume_idx = resume_state.get("index", 0)
        console.print(f"[info]Resuming from index {resume_idx} (previous session detected)")

    # Patch cracker classes to support resume
    def patch_run_dictionary(cls):
        orig_run_dictionary = cls.run_dictionary
        def run_dictionary(self):
            with open(self.wordlist, "r", encoding="utf-8", errors="ignore") as f:
                passwords = [line.strip() for line in f if line.strip()]
            chunk_size = len(passwords) // self.threads + 1
            feed = []
            progress = Progress(SpinnerColumn(), BarColumn(), TextColumn("[progress.percentage]{task.percentage:>3.0f}%"), TimeElapsedColumn(), console=console)
            task = progress.add_task("[cyan]Cracking ZIP..." if isinstance(self, ZipCracker) else "[cyan]Cracking RAR...", total=len(passwords))
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Last Attempts", style="cyan")
            layout = Layout()
            layout.split_column(
                Layout(progress, name="progress", size=3),
                Layout(table, name="feed")
            )
            def update_feed():
                table.rows = []
                for attempt in reversed(feed):
                    table.add_row(attempt)
            # Resume support
            start_idx = resume_idx if args.resume else 0
            def worker(passwords, progress, task, feed, update_feed, offset):
                for i, pwd in enumerate(passwords):
                    idx = offset + i
                    if idx < start_idx:
                        progress.update(task, advance=1)
                        continue
                    if self.found.is_set():
                        return
                    if self.try_password(pwd):
                        self.password = pwd
                        self.found.set()
                        if self.log:
                            log_result(self.log, f"[{ftype.upper()}] Password found: {pwd}")
                        console.print(f"[success]\n[{ftype.upper()}] Password found: [bold]{pwd}[/bold]")
                        msg = f"Password found for file {args.file}: {pwd}"
                        send_desktop_notification("ScayForce: Password Found!", msg)
                        if getattr(args, 'notify_email', None):
                            send_email_notification(args.notify_email, "ScayForce: Password Found!", msg)
                        clear_resume()
                        break
                    if args.resume:
                        save_resume({"file": args.file, "index": idx+1})
                    if self.verbose and feed is not None:
                        feed.append(pwd)
                        if len(feed) > 10:
                            feed.pop(0)
                        update_feed()
                    progress.update(task, advance=1)
            with Live(layout, refresh_per_second=10, console=console):
                threads = []
                for i in range(self.threads):
                    chunk = passwords[i*chunk_size:(i+1)*chunk_size]
                    offset = i*chunk_size
                    t = threading.Thread(target=worker, args=(chunk, progress, task, feed if self.verbose else None, update_feed if self.verbose else None, offset))
                    t.start()
                    threads.append(t)
                for t in threads:
                    t.join()
            if not self.password:
                console.print("[fail]Password not found in wordlist.")
                if self.log:
                    log_result(self.log, f"[{ftype.upper()}] Password not found.")
                clear_resume()
        cls.run_dictionary = run_dictionary
    def patch_run_bruteforce(cls):
        orig_run_bruteforce = cls.run_bruteforce
        def run_bruteforce(self):
            from itertools import product
            all_pwds = []
            for l in range(1, self.max_length+1):
                all_pwds.extend([''.join(x) for x in product(self.charset, repeat=l)])
            chunk_size = len(all_pwds) // self.threads + 1
            feed = []
            progress = Progress(SpinnerColumn(), BarColumn(), TextColumn("[progress.percentage]{task.percentage:>3.0f}%"), TimeElapsedColumn(), console=console)
            task = progress.add_task("[cyan]Bruteforcing ZIP..." if isinstance(self, ZipCracker) else "[cyan]Bruteforcing RAR...", total=len(all_pwds))
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Last Attempts", style="cyan")
            layout = Layout()
            layout.split_column(
                Layout(progress, name="progress", size=3),
                Layout(table, name="feed")
            )
            def update_feed():
                table.rows = []
                for attempt in reversed(feed):
                    table.add_row(attempt)
            # Resume support
            start_idx = resume_idx if args.resume else 0
            def worker(passwords, progress, task, feed, update_feed, offset):
                for i, pwd in enumerate(passwords):
                    idx = offset + i
                    if idx < start_idx:
                        progress.update(task, advance=1)
                        continue
                    if self.found.is_set():
                        return
                    if self.try_password(pwd):
                        self.password = pwd
                        self.found.set()
                        if self.log:
                            log_result(self.log, f"[{ftype.upper()}] Password found: {pwd}")
                        console.print(f"[success]\n[{ftype.upper()}] Password found: [bold]{pwd}[/bold]")
                        msg = f"Password found for file {args.file}: {pwd}"
                        send_desktop_notification("ScayForce: Password Found!", msg)
                        if getattr(args, 'notify_email', None):
                            send_email_notification(args.notify_email, "ScayForce: Password Found!", msg)
                        clear_resume()
                        break
                    if args.resume:
                        save_resume({"file": args.file, "index": idx+1})
                    if self.verbose and feed is not None:
                        feed.append(pwd)
                        if len(feed) > 10:
                            feed.pop(0)
                        update_feed()
                    progress.update(task, advance=1)
            with Live(layout, refresh_per_second=10, console=console):
                threads = []
                for i in range(self.threads):
                    chunk = all_pwds[i*chunk_size:(i+1)*chunk_size]
                    offset = i*chunk_size
                    t = threading.Thread(target=worker, args=(chunk, progress, task, feed if self.verbose else None, update_feed if self.verbose else None, offset))
                    t.start()
                    threads.append(t)
                for t in threads:
                    t.join()
            if not self.password:
                console.print("[fail]Password not found with bruteforce.")
                if self.log:
                    log_result(self.log, f"[{ftype.upper()}] Password not found (bruteforce).")
                clear_resume()
        cls.run_bruteforce = run_bruteforce
    patch_run_dictionary(ZipCracker)
    patch_run_dictionary(RarCracker)
    patch_run_bruteforce(ZipCracker)
    patch_run_bruteforce(RarCracker)

    # Patch for pattern intelligence
    patch_pattern_intelligence(ZipCracker)
    patch_pattern_intelligence(RarCracker)

    if args.dictionary:
        if ftype == "zip":
            cracker = ZipCracker(args.file, wordlist=args.wordlist, threads=args.threads, log=args.log, verbose=args.verbose)
        else:
            cracker = RarCracker(args.file, wordlist=args.wordlist, threads=args.threads, log=args.log, verbose=args.verbose)
        cracker.run_dictionary()
    elif args.bruteforce:
        if ftype == "zip":
            cracker = ZipCracker(args.file, charset=args.charset, max_length=args.max_length, threads=args.threads, log=args.log, verbose=args.verbose)
        else:
            cracker = RarCracker(args.file, charset=args.charset, max_length=args.max_length, threads=args.threads, log=args.log, verbose=args.verbose)
        cracker.run_bruteforce()
    else:
        console.print("[fail]You must specify either --dictionary or --bruteforce mode.")
        sys.exit(1)

    if (cracker.password or getattr(cracker, 'password', None)) and args.notify:
        try:
            if sys.platform.startswith('win'):
                import winsound
                winsound.Beep(1000, 500)
            else:
                print("\a")
        except Exception:
            pass

if __name__ == "__main__":
    main()
