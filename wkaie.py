# Author: dare_devil_ex

try:
    import requests
    import time
    from io import BytesIO
    from os import system as wkaie
    from PIL import Image, ImageTk
    import tkinter as tk
except:
    wkaie("pip install PILLOW")
    wkaie("pip install requests")
    wkaie("pip install tkinter")

root = tk.Tk()
root.title("Text2Img")
root.geometry("1080x720")
API_URL = "https://ai-api.magicstudio.com/api/ai-art-generator"

HEADERS = {
    "sec-ch-ua-platform": "\"Android\"",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "accept": "application/json, text/plain, */*",
    "sec-ch-ua": "\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "origin": "https://magicstudio.com",
    "x-requested-with": "mark.via.gq",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://magicstudio.com/ai-art-generator/",
    "accept-language": "en-US,en;q=0.9",
}
def Ai(prompt):
    data = {
        "prompt": prompt,
        "output_format": "bytes",
        "user_profile_id": "null",
        "anonymous_user_id": "12392865-ff1f-4ef7-a67d-00f058fbe6cf",
        "request_timestamp": "1734701568.295",
        "user_is_subscribed": "false",
        "client_id": "pSgX7WgjukXCBoYwDM8G8GLnRRkvAoJlqa5eAVvj95o",
    }
    for attempt in range(3):
        try:
            response = requests.post(API_URL, headers=HEADERS, data=data, timeout=10)
            if response.status_code == 200:
                return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}. Attempt {attempt + 1} of 3.")
            time.sleep(5)
    return None

def output():
    prompt = entry.get()
    image_data = Ai(prompt)
    image_data = BytesIO(image_data)
    image = Image.open(image_data)
    image_tk = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=image_tk)
    label.pack()
    tk.mainloop()


label = tk.Label(root, text="TEXT2IMG", font=("Arial", 14))
label.pack(pady=5)
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=7)
button = tk.Button(root, text="Submit", command=output)
button.pack(pady=1)

root.mainloop()
