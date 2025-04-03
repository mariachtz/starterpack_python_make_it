def show_book_page(book, page_size, title, page_count):
    W  = '\033[0m'  # White (reset to normal)
    O  = '\033[33m' # Orange
    B  = '\033[34m' # Blue
    print("\n" * 40)
    print(f"{O}==== {title} -- Page {page_count} ===={W}")
    for i in range (0, page_size, 1):
        line_content = book.readline()
        # Capitalize chapter titles and color them in blue
        if line_content.startswith("CHAPTER"):
            line_content = f"{B}{line_content.title()}{W}"

        # Print line with numbering
        print(f"{O}{i+1:02d} |{W} {line_content}")
    return input(f"{O}If you want to read the next page, press ENTER: {W}")


def read_book(book_path, page_size, title):
    page_count = 1
    book = open(book_path, "r" , encoding="utf8")
    action = show_book_page(book, page_size, title, page_count)
    page_count += 1
    while action == "":
        show_book_page(book, page_size, title, page_count)
        page_count += 1
    book.close()  

page_size =15
book_title = "LES MISERABLES"
book_path = "book.txt"
read_book(book_path,page_size, book_title)