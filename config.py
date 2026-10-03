"""
Configuration module for Hotel Automation & RPA Ecosystem.
Loads configuration securely from .env or environment variables with sensible defaults.
"""

import os
from pathlib import Path

# Base Directory
BASE_DIR = Path(__file__).resolve().parent

# Optional .env loading
try:
    from dotenv import load_dotenv
    load_dotenv(BASE_DIR / ".env")
except ImportError:
    pass

# Hotel Identity
HOTEL_NAME = os.getenv("HOTEL_NAME", "Grand Nusantara Hotel & Resort")
APP_ENV = os.getenv("APP_ENV", "development")

# Database (Sybase SQL Anywhere 17 / ODBC)
DB_CONFIG = {
    "driver": os.getenv("DB_DRIVER", "{SQL Anywhere 17}"),
    "server": os.getenv("DB_SERVER", "db_demo_server"),
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "port": int(os.getenv("DB_PORT", "2639")),
    "uid": os.getenv("DB_USER", "demo_dba"),
    "pwd": os.getenv("DB_PASSWORD", "demo_password_123"),
}

def get_connection_string():
    """Generates the ODBC connection string for Sybase SQL Anywhere."""
    return (
        f"Driver={DB_CONFIG['driver']};"
        f"ServerName={DB_CONFIG['server']};"
        f"LINKS=tcpip(Host={DB_CONFIG['host']}:{DB_CONFIG['port']});"
        f"UID={DB_CONFIG['uid']};"
        f"PWD={DB_CONFIG['pwd']}"
    )

# Cloud PMS Scraper Credentials
CLOUD_PMS = {
    "login_url": os.getenv("CLOUD_PMS_LOGIN_URL", "https://pms.hotel-cloud-provider.example/login"),
    "username": os.getenv("CLOUD_PMS_USERNAME", "demo_operator@example.com"),
    "password": os.getenv("CLOUD_PMS_PASSWORD", "mock_demo_pass"),
    "headless": os.getenv("SCRAPER_HEADLESS", "true").lower() == "true",
    "interval": int(os.getenv("SCRAPER_SYNC_INTERVAL_SECONDS", "600")),
}

# Directories & Storage
MAILBOX_DIR = Path(os.getenv("MAILBOX_DIRECTORY", str(BASE_DIR / "data" / "dummy_vouchers")))
STORAGE_PROCESSED = Path(os.getenv("VOUCHER_STORAGE_DIR", str(BASE_DIR / "data" / "processed")))
STORAGE_QUARANTINE = Path(os.getenv("QUARANTINE_STORAGE_DIR", str(BASE_DIR / "data" / "quarantine")))

# Micro-Server
SERVER_HOST = os.getenv("SERVER_HOST", "127.0.0.1")
SERVER_PORT = int(os.getenv("SERVER_PORT", "8085"))
