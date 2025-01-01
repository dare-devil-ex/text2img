# Author: dare_devil_ex
# Remainder: Changing credits doesn't make you a programmer 

try:
    import requests
    import time
    from io import BytesIO
    from os import system
    from datetime import datetime as dt
    from PIL import Image, ImageTk
    import tkinter as tk
except:
    system("pip install PILLOW")
    system("pip install requests")
    system("pip install tkinter")

root = tk.Tk()
root.title("Text2Img")
root.geometry("1080x1090")
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
    global imglabel, imagex
    prompt = entry.get()
    image_data = Ai(prompt)
    image_data = BytesIO(image_data)
    image = Image.open(image_data)
    imagex = image.resize((1440, 1440))
    ShowImg = image.resize((800, 800))
    image_tk = ImageTk.PhotoImage(ShowImg)
    imglabel = tk.Label(root, image=image_tk)
    imglabel.pack()
    try:
        root.mainloop()
    except KeyboardInterrupt:
        pass
    
def saveAct():
    win2 = tk.Tk()
    win2.title("Save Activity")
    win2.geometry("250x250")
    tk.Label(win2, text="Entering file name is optional", font=("Arial", 8)).pack()
    entry = tk.Entry(win2, width=30)
    entry.pack(pady=4)
    def fetch():
        if entry.get():
            inp = entry.get()
        else:
            inp = str(dt.now().date())
        try:
            imagex.save("{}.jpg".format(inp))
        except Exception as e:
            print("Error:", e)
            root.destroy()
            win2.destroy()
            
    buttonSave = tk.Button(win2, text="SAVE", command=fetch)
    buttonSave.pack(pady=5)
    tk.Label(win2, text="wkaie").pack(pady=99)

def refresh():
    global imglabel
    try:
        imglabel.forget()
    except:
        pass

label = tk.Label(root, text="TEXT2IMG", font=("Arial", 14))
label.pack(pady=5)
entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=7)
button = tk.Button(root, text="GENERATE IMAGE", command=output)
button.pack(pady=1)
button = tk.Button(root, text="REFRESH", command=refresh)
button.pack(pady=1)
button = tk.Button(root, text="SAVE", command=saveAct)
button.pack(pady=1)

try:
    root.mainloop()
except KeyboardInterrupt:
    print("This  program was developed by dare-devil-ex\nThank you!")
