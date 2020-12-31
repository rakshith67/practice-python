def center_text(*args):
    text = "-".join([str(arg) for arg in args])
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


center_text("Spam and Eggs")
center_text("Spam and Eggs", "Eggs")
center_text("Spam and Eggs", "Spam", "Spam")
center_text("Spam and Eggs", "Spam")
center_text("Spam and Eggs", 2, 4, "Eggs")
