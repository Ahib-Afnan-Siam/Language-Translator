from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from textblob import TextBlob
from googletrans import Translator, LANGUAGES

root = Tk()
root.title("My Translator")
root.geometry("1080x400")
root.config(bg="white")

def label_change():
    c1 = combo1.get()
    c2 = combo2.get()
    lebel1.configure(text=c1)
    lebel2.configure(text=c2)
    root.after(500, label_change)

def translate_now():
    try:
        text_ = text1.get(1.0, END).strip()
        c3 = combo1.get()
        c4 = combo2.get()
        if text_:
            translator = Translator()
            src_lang_code = [code for code, lang in LANGUAGES.items() if lang == c3.lower()]
            dest_lang_code = [code for code, lang in LANGUAGES.items() if lang == c4.lower()]
            if not src_lang_code or not dest_lang_code:
                messagebox.showerror("My Translator", "Invalid source or destination language.")
                return
            translation = translator.translate(text_, src=src_lang_code[0], dest=dest_lang_code[0])
            text2.delete(1.0, END)
            text2.insert(END, translation.text)
    except Exception as e:
        print(f"Exception: {e}")  # Print the exception for debugging
        messagebox.showerror("My Translator", f"Error occurred: {e}")

# Icon
try:
    img_icon = PhotoImage(file="translate.png")
    root.iconphoto(False, img_icon)
except Exception as e:
    print("Error loading image:", e)

# Arrow Image
arrow_img = Image.open("two-arrows.png")
if arrow_img.mode == 'RGBA':
    white_bg = Image.new("RGB", arrow_img.size, "white")
    arrow_img = Image.alpha_composite(white_bg.convert("RGBA"), arrow_img)

arrow_img = arrow_img.resize((150, 150), Image.LANCZOS)
arrow_img_tk = ImageTk.PhotoImage(arrow_img)

image_label = Label(root, image=arrow_img_tk, width=150)
image_label.place(x=460, y=140)

# Translate Button
trans_button = Button(root, text="Translate", font="Roboto 15 bold italic",
                      activebackground="white", cursor="arrow", bd=5, bg="red", fg="black",
                      command=translate_now)
trans_button.place(x=480, y=300)

# First Frame
combo1 = ttk.Combobox(root, values=list(LANGUAGES.values()), font="Roboto 14", state="r")
combo1.place(x=120, y=20)
combo1.set("English")

lebel1 = Label(root, text="English", font="Segoe 30 bold", bg="black", width=18, bd=5, relief=GROOVE)
lebel1.place(x=20, y=50)

f1 = Frame(root, bg="black", bd=5)
f1.place(x=10, y=118, width=440, height=210)

text1 = Text(f1, font="Roboto 20", bg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side="right", fill="y")

scrollbar1.config(command=text1.yview)
text1.config(yscrollcommand=scrollbar1.set)

# Second Frame
combo2 = ttk.Combobox(root, values=list(LANGUAGES.values()), font="Roboto 14", state="r")
combo2.place(x=740, y=20)
combo2.set("Select Language")

lebel2 = Label(root, text="English", font="Segoe 30 bold", bg="black", width=18, bd=5, relief=GROOVE)
lebel2.place(x=630, y=50)

f2 = Frame(root, bg="black", bd=5)
f2.place(x=620, y=118, width=440, height=210)

text2 = Text(f2, font="Roboto 20", bg="black", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side="right", fill="y")

scrollbar2.config(command=text2.yview)
text2.config(yscrollcommand=scrollbar2.set)

label_change()
root.mainloop()
