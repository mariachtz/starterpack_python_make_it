# 📖 Python Book Reader  

A simple **Python-based book reader** that displays a text file page by page in the terminal, with formatted chapter titles and line numbering.  

## 🚀 Features  
- **Paginated Reading:** Read large text files in a structured manner.  
- **Chapter Formatting:** Detects and highlights chapter titles in **blue**.  
- **Line Numbering:** Displays line numbers for better readability.  
- **Interactive Navigation:** Press **ENTER** to move to the next page.  

## 🛠 Requirements  
- Python 3.x  
- A text file (`book.txt`) containing the book content  

## 🔧 Installation & Usage  

1. **Clone or Download** this repository.  
2. **Prepare a text file** (`book.txt`) in the same directory.  
3. **Run the script:**  

   ```bash
   python book_reader.py
   ```

4. Navigate through the book by pressing ENTER to move to the next page.

## 📜 Code Overview
The script consists of two main functions:

- show_book_page(book, page_size, title, page_count)

    - Displays a formatted page from the book with chapter detection and line numbering.

- read_book(book_path, page_size, title)

    - Reads the book page by page and waits for user input to proceed.

## ✨ Customization
You can modify the script to change:

- Page size (number of lines per page) → Adjust the page_size variable.
- Book title → Set the book_title variable.
- File path → Change the book_path variable to the desired book file.

## 📌 Example Output
```
==== LES MISERABLES -- Page 1 ====
01 | CHAPTER ONE: AN OVERVIEW
02 | It was a cold and stormy night...
03 | The wind howled through the trees...
...
15 | The story continues...
If you want to read the next page, press ENTER: 
```
## 🤝 Contributions
Feel free to fork this project and enhance its functionality!