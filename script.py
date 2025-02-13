import requests

url = "https://noor.moe.gov.sa/Noor/EduWaveDashBoard/StudentProgress.aspx"
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en,en-US;q=0.9,ar-AE;q=0.8,ar;q=0.7,bn;q=0.6",
    "cache-control": "max-age=0",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "",
    "Referer": "https://noor.moe.gov.sa/Noor/EduWavek12Portal/HomePage.aspx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

try:
    r = requests.get(url, headers=headers)
    print("Request sent, status code:", r.status_code)
except Exception as e:
    print("Error:", e)
