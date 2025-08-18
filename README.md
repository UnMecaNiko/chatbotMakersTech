# Makers Tech Inventory Assistant  

**Version 2** – Built with **Dify** and **Gemini 2.5 Flash**  

---

## 🚀 Overview  
The **Makers Tech Inventory Assistant** is a conversational AI that helps customers explore and analyze the company’s technology inventory in real time.  
It not only answers questions about stock, prices, brands, and categories, but also provides **personalized recommendations** and **proactive suggestions** that make product discovery intuitive and engaging.  

For Makers Tech, the assistant represents a powerful tool to **improve customer experience, increase product visibility, and drive sales efficiency**.  

---

## ⚙️ Architecture  
- **Model**: Gemini 2.5 Flash (Chat)  
- **Strategy**: FunctionCalling  
- **Active Tools**:  
  - `SQL Execute`: Runs direct queries on the inventory database  
  - `Get Table Schema`: Validates schema and data types  
  - `WolframAlpha`: Handles all mathematical operations (averages, sums, ratios, variance, etc.)  

---

## 📦 Database Schema  
The `inventory` table includes:  

- `id` (INT) – Unique identifier  
- `name` (TEXT) – Product name  
- `brand` (TEXT) – Supported values include Apple, Dell, HP, Lenovo, Asus, Acer, Samsung, LG, Sony, Logitech, Razer, Corsair, HyperX, Kingston, Seagate, Western Digital, NVIDIA, AMD, Intel, TP-Link, Netgear, Canon, Epson, Xiaomi, Huawei, MSI, Gigabyte  
- `category` (TEXT) – Examples: Laptop, Desktop, Monitor, Mouse, GPU, CPU, Smartphone, VR Headset, Printer, Router, Tablet, etc.  
- `price` (FLOAT, USD) – Product price  
- `stock` (INT) – Quantity available  
- `features` (TEXT) – Additional specifications  

---

## ✨ Key Features (Version 2)  
- **Personalized Recommendations**  
  - Matches user’s preferred **brand**, **category**, and **budget**.  
  - Provides up to 5 items per list (top within budget, by brand, by category).  
  - Deduplicated and ranked for quality results.  

- **Proactive Guidance**  
  - Suggests follow-up queries such as:  
    - *“Would you like to see the cheapest option?”*  
    - *“Do you want to explore products from another brand?”*  
    - *“Shall I show you which items are running low in stock?”*  

- **Smart Fallbacks**  
  - If no product matches perfectly, the assistant proposes alternatives (e.g., slightly above budget or similar category).  

- **Mathematical Analysis**  
  - Uses WolframAlpha for operations like averages, totals, and price comparisons.  
  - Example: *“The average cost of all mouse products is $145.01.”*  

---

## 💡 Example Queries  
- *Based on my preferences, what is the most expensive product that i can buy?.*  
- *Show me all Dell items currently in stock.*  
- *What is the average cost of mouse products?*  
- *How many laptops are available from HP?*  
- *Which products are running low in stock?*  

