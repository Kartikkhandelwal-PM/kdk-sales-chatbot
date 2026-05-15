import requests
import json

BASE_URL = "https://support.kdksoftware.com"
PORTAL_ID = "edbsne55ba7deb431da433c4ac3f11d62c1ef5bef37105f67d6f01f43b9cda906bdf4"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json, text/plain, */*",
    "Referer": f"{BASE_URL}/portal/en/kb/kdk-softwares/express-gst",
}

CAT_ID_GST = "202722000155513689"
CAT_ID_TDS = "202722000233618629"
CAT_ID_ITR = "202722000387498539"

def test(label, path, params):
    url = BASE_URL + path
    r = requests.get(url, headers=HEADERS, params=params, timeout=30)
    print(f"\n[{label}]")
    print(f"  URL: {r.url}")
    print(f"  Status: {r.status_code}")
    try:
        data = r.json()
        print(f"  Response: {json.dumps(data)[:500]}")
    except Exception:
        print(f"  Raw: {r.text[:300]}")

# Test 1: kbArticles with categoryId
test("articles by categoryId", "/portal/api/kbArticles", {
    "portalId": PORTAL_ID,
    "categoryId": CAT_ID_GST,
    "locale": "en",
    "from": 0,
    "limit": 10,
})

# Test 2: kbCategory articles endpoint
test("kbCategory/articles", f"/portal/api/kbCategory/{CAT_ID_GST}/articles", {
    "portalId": PORTAL_ID,
    "locale": "en",
})

# Test 3: article by permalink
test("article by permalink", "/portal/api/kbArticles/articleByPermalink", {
    "portalId": PORTAL_ID,
    "permalink": "expressgst-e-way-bill",
    "locale": "en",
})

# Test 4: search for articles
test("search articles", "/portal/api/kbArticles/search", {
    "portalId": PORTAL_ID,
    "searchStr": "GST",
    "locale": "en",
    "limit": 5,
})

# Test 5: check what category tree returns fully
r = requests.get(
    f"{BASE_URL}/portal/api/kbCategories/categoryTreeByPermalink",
    headers=HEADERS,
    params={"portalId": PORTAL_ID, "permalink": "express-gst", "locale": "en"},
    timeout=30,
)
print("\n[Full category tree response for express-gst]")
try:
    data = r.json()
    print(json.dumps(data, indent=2)[:2000])
except Exception:
    print(r.text[:500])
