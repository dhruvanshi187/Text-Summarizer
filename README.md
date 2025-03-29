 📄 NLTK-based Text Summarization API

 📌 Introduction
This is a **Flask-based API** that performs text summarization using the `NLTK` library. It processes input text and generates a concise summary.

---

🔧 Installation

1️⃣ Prerequisites
- Python 3.x installed on your system
- Required Python libraries: `Flask` and `NLTK`

 2️⃣ Install Dependencies
Run the following command to install the required packages:
```bash
pip install flask nltk
```

Additionally, download the necessary NLTK data:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

🚀 Usage

 1️⃣ Run the API
Start the Flask server using the following command:
```bash
python text_summ.py
```
By default, the API will be available at `http://127.0.0.1:5000/summarize`

 2️⃣ Make a POST Request
Send a **POST request** with text data to get the summarized output.

 **Example Request:**
```json
{
  "text": "Your input text goes here. The API will generate a summary based on the text length."
}
```

#### **Example Response:**
```json
{
  "summary": "Generated summary based on input text."
}
```

---

 📌 Features
 
✅ Extracts key sentences using `NLTK`

✅ Uses `Punkt` tokenizer and `stopwords` for processing

✅ Returns summary in **JSON format**

✅ Simple and easy-to-use API

---

 🛠 Technologies Used
 
- **Flask** - Web framework for API
- **NLTK** - Library for natural language processing
- **Python** - Backend programming language

---

📌 Limitations

🚨 May not work well for extremely short texts
🚨 Works best with well-structured paragraphs

---

 👨‍💻 Author
 
Developed by **Dhruvanshi Senjaliya**

---

 📜 License
 
This project is **open-source** and available under the MIT License.


