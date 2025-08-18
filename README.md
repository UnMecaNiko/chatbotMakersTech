# Makers Tech Inventory Assistant  

**Version 1** – Built with Dify and Gemini 2.5 Flash  

## 🚀 Overview  
The **Makers Tech Inventory Assistant** is a conversational AI designed to help users explore and analyze the company’s technology inventory.  
It provides clear, natural answers to queries about stock, prices, brands, and categories, while also suggesting next steps for further exploration.  

## ⚙️ Architecture  
- **Model**: Gemini 2.5 Flash (Chat)  
- **Strategy**: FunctionCalling  
- **Active Tools**:  
  - `SQL Execute`: Direct queries to the inventory database  
  - `Get Table Schema`: Schema and data type validation  
  - `WolframAlpha`: All mathematical operations (averages, sums, ratios, variance, etc.)  

## 📦 Database Schema  
The `inventory` table contains the following fields:  
- `id` (INT)  
- `name` (TEXT)  
- `brand` (TEXT) – valid values: Apple, Dell, HP, Lenovo, Asus, Acer, Samsung, LG, Sony, Logitech, Razer, Corsair, HyperX, Kingston, Seagate, Western Digital, NVIDIA, AMD, Intel, TP-Link, Netgear, Canon, Epson, Xiaomi, Huawei, MSI, Gigabyte  
- `category` (TEXT) – valid values: Laptop, Desktop, Monitor, Keyboard, Mouse, Headphones, Smartphone, Tablet, Smartwatch, Printer, Router, SSD, HDD, GPU, CPU, Motherboard, Power Supply, Case, Webcam, Microphone, Speakers, Docking Station, Charger, Cable, Chair, Gaming Console, VR Headset  
- `price` (FLOAT, USD)  
- `stock` (INT)  
- `features` (TEXT)  

## 💡 Example Queries  
- *How many laptops are in stock?*  
- *What is the most expensive desktop?*  
- *What is the average cost of mouse items?*  
- *What is the total stock of Huawei products?*  
- *If I sell all cables, how much revenue will I get?*  

## ✨ Key Features  
- Natural language answers that are clear and concise  
- Mandatory use of WolframAlpha for all math operations  
- Follow-up suggestions after every answer (e.g., *“Would you like me to also show you the cheapest option?”*)  

## 🔮 Roadmap  
- **Version 2 (future release):**  
  - User personalization  
  - Advanced filtering (e.g., laptops over $1,000 with stock > 10)  
  - Recommendation system based on user preferences  
