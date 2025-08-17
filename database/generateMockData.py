# Generate a 100-row CSV with columns: id, name, brand, category, price, stock, features
import pandas as pd
import random

random.seed(42)

brands = [
    "Apple","Dell","HP","Lenovo","Asus","Acer","Samsung","LG","Sony","Logitech",
    "Razer","Corsair","HyperX","Kingston","Seagate","Western Digital","NVIDIA","AMD",
    "Intel","TP-Link","Netgear","Canon","Epson","Xiaomi","Huawei","MSI","Gigabyte"
]

categories = [
    "Laptop","Desktop","Monitor","Keyboard","Mouse","Headphones","Smartphone","Tablet","Smartwatch",
    "Printer","Router","SSD","HDD","GPU","CPU","Motherboard","Power Supply","Case",
    "Webcam","Microphone","Speakers","Docking Station","Charger","Cable","Chair","Gaming Console","VR Headset"
]

# Simple model name parts by category for more realistic names
model_tokens = {
    "Laptop": ["Pro","Air","Notebook","ZenBook","ThinkPad","IdeaPad","Pavilion","Swift","Predator","ROG","Victus"],
    "Desktop": ["Tower","Mini","Cube","Workstation","Gaming","All-in-One"],
    "Monitor": ["UltraWide","4K","QHD","Curved","IPS","OLED","Gaming"],
    "Keyboard": ["Mechanical","Wireless","60%","TKL","RGB","Low-Profile"],
    "Mouse": ["Wireless","Ergonomic","Gaming","Laser","Optical"],
    "Headphones": ["Wireless","ANC","Gaming","Studio","In-Ear","Over-Ear"],
    "Smartphone": ["Pro","Max","Plus","Lite","5G","Ultra"],
    "Tablet": ["Pro","Mini","Air","Plus"],
    "Smartwatch": ["Sport","Classic","Pro","Fit"],
    "Printer": ["Laser","InkTank","InkJet","Mono","Color"],
    "Router": ["AX6000","AX5400","AXE","Tri-Band","Mesh","Gigabit"],
    "SSD": ["NVMe","SATA","Gen4","Gen5"],
    "HDD": ["7200rpm","NAS","Surveillance"],
    "GPU": ["RTX 4070","RTX 4080","RTX 4090","RX 7800 XT","RX 7900 XTX"],
    "CPU": ["i5-13400","i7-13700","i9-14900K","Ryzen 5 7600","Ryzen 7 7800X3D","Ryzen 9 7950X"],
    "Motherboard": ["B650","X670E","Z790","B760","X570"],
    "Power Supply": ["650W","750W","850W","1000W","Modular","Gold"],
    "Case": ["ATX","mATX","Mini-ITX","Mesh","RGB"],
    "Webcam": ["1080p","2K","4K","HDR","Streaming"],
    "Microphone": ["USB","XLR","Podcast","Condenser"],
    "Speakers": ["2.0","2.1","Bluetooth","Soundbar","Studio"],
    "Docking Station": ["USB-C","Thunderbolt","Triple-Display"],
    "Charger": ["65W","100W","GaN","USB-C"],
    "Cable": ["HDMI 2.1","DisplayPort 1.4","USB-C 3.2","Thunderbolt 4","Ethernet Cat6"],
    "Chair": ["Ergonomic","Mesh","Gaming","Lumbar"],
    "Gaming Console": ["GenX","Pro","Slim","Digital"],
    "VR Headset": ["Standalone","PCVR","4K","OLED","Base Station"]
}

def make_name(brand, category):
    token = random.choice(model_tokens.get(category, ["Model"]))
    base_num = random.randint(1, 9999)
    return f"{brand} {category} {token} {base_num}"

def price_for_category(category):
    ranges = {
        "Laptop": (500, 2800),
        "Desktop": (600, 3500),
        "Monitor": (120, 1500),
        "Keyboard": (25, 250),
        "Mouse": (15, 180),
        "Headphones": (20, 500),
        "Smartphone": (150, 2200),
        "Tablet": (120, 1500),
        "Smartwatch": (70, 900),
        "Printer": (90, 1200),
        "Router": (40, 600),
        "SSD": (30, 500),
        "HDD": (35, 350),
        "GPU": (250, 2500),
        "CPU": (120, 1200),
        "Motherboard": (100, 700),
        "Power Supply": (60, 350),
        "Case": (40, 300),
        "Webcam": (20, 300),
        "Microphone": (30, 400),
        "Speakers": (30, 600),
        "Docking Station": (60, 400),
        "Charger": (15, 120),
        "Cable": (5, 60),
        "Chair": (80, 600),
        "Gaming Console": (250, 1000),
        "VR Headset": (250, 1500)
    }
    lo, hi = ranges.get(category, (20, 500))
    return round(random.uniform(lo, hi), 2)

def features_for(category, brand):
    base = []
    if category in ["Laptop","Desktop","Smartphone","Tablet"]:
        ram = random.choice([8,16,32,64])
        storage = random.choice([128,256,512,1024,2048])
        base += [f"RAM:{ram}GB", f"Storage:{storage}GB"]
    if category in ["Laptop","Desktop"]:
        base += [f"CPU:{random.choice(model_tokens['CPU'])}"]
        if category=="Laptop":
            base += [f"GPU:{random.choice(model_tokens['GPU'])}"]
            base += [f"Screen:{random.choice(['13.3\"','14\"','15.6\"','16\"','17\"'])}"]
    if category=="Monitor":
        base += [f"Resolution:{random.choice(['1920x1080','2560x1440','3840x2160'])}", f"Refresh:{random.choice([60,75,120,144,165])}Hz"]
    if category=="Router":
        base += [f"Standard:{random.choice(['Wi-Fi 6','Wi-Fi 6E','Wi-Fi 7'])}", f"Ports:{random.choice([3,4,5,8])}"]
    if category in ["SSD","HDD"]:
        base += [f"Capacity:{random.choice([256,512,1024,2048,4096])}GB", f"Interface:{random.choice(['NVMe','SATA'])}"]
    if category in ["GPU","CPU","Motherboard"]:
        base += [f"Year:{random.choice([2023,2024,2025])}"]
    if category in ["Keyboard","Mouse","Headphones","Speakers","Webcam","Microphone"]:
        base += [f"Wireless:{random.choice(['Yes','No'])}"]
    # Always add brand and warranty
    base += [f"Brand:{brand}", f"Warranty:{random.choice([12,24,36])}m"]
    return "; ".join(base)

rows = []
for i in range(1, 101):
    category = random.choice(categories)
    brand = random.choice(brands)
    name = make_name(brand, category)
    price = price_for_category(category)
    stock = random.randint(0, 50)
    features = features_for(category, brand)
    rows.append({
        "id": i,
        "name": name,
        "brand": brand,
        "category": category,
        "price": price,
        "stock": stock,
        "features": features
    })

df = pd.DataFrame(rows, columns=["id","name","brand","category","price","stock","features"])

# Save CSV
path = "./inventory_example.csv"
df.to_csv(path, sep="\t", index=False)

import caas_jupyter_tools
caas_jupyter_tools.display_dataframe_to_user("MakersTech Inventory Example (100 rows)", df)

path
