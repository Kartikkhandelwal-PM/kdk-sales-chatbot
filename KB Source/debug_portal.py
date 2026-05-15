import requests
import re

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
r = requests.get(
    "https://support.kdksoftware.com/portal/en/kb/kdk-softwares/express-gst",
    headers=headers,
    timeout=30,
)
html = r.text

# Script sources
scripts = re.findall(r"<script[^>]+src=[\"']([^\"']+)[\"']", html)
print("Script sources:")
for s in scripts[:15]:
    print(" ", s)

# Find portal/api call patterns
cdn_scripts = [s for s in scripts if "zoho" in s.lower() or "static" in s.lower()]
print("\nCDN scripts:", cdn_scripts[:5])

# Check for data embedded as window variables or __data
data_vars = re.findall(r"window\.__[A-Z_]+ ?=", html)
print("\nWindow vars:", data_vars[:10])

# Look for any JSON-like data with articles
article_matches = re.findall(r'"articles?":\s*\[', html)
print("\nArticle array patterns:", article_matches[:5])

# Find all URLs in the HTML
all_urls = re.findall(r"https?://[^\s\"'<>]+", html)
zoho_api_urls = [u for u in all_urls if "api" in u.lower() and "zoho" in u.lower()]
print("\nZoho API URLs:", zoho_api_urls[:10])

# Check what API the SPA might call - look for /portal/ paths used as API
portal_api = re.findall(r'"/portal/[^"]{5,80}"', html)
print("\nPortal paths:", portal_api[:10])

# Save HTML to check manually
with open("portal_debug.html", "w", encoding="utf-8") as f:
    f.write(html)
print(f"\nFull HTML saved to portal_debug.html ({len(html)} bytes)")
