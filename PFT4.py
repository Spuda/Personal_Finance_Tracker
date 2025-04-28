import customtkinter
import tkinter as tk

categories = []
values = []

FONT_BIG = ("Arial", 18)
FONT_MEDIUM = ("Arial", 16)

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def add_category():
    cat = category_entry.get()
    amount = amount_entry.get()

    if cat and amount:
        try:
            categories.append(cat)
            values.append(float(amount))
            feedback.configure(text=f"Dodano: {cat} - ${amount}", font=FONT_MEDIUM)
        except ValueError:
            feedback.configure(text="Unesite ispravan broj za trošak.", font=FONT_MEDIUM)

        category_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)

def finish_entry():
    user_income = float(dohodak.get())
    total_expense = sum(values)
    remaining = user_income - total_expense

    clear_frame(scrollable_frame)

    # Centered container frame inside scrollable_frame
    center_frame = customtkinter.CTkFrame(scrollable_frame, fg_color="transparent")
    center_frame.pack(pady=10)

    customtkinter.CTkLabel(center_frame, text="Kategorije i troškovi:", font=FONT_BIG).pack(pady=10)

    for i in range(len(categories)):
        line = f"{categories[i]}: ${values[i]}"
        customtkinter.CTkLabel(center_frame, text=line, font=FONT_MEDIUM).pack(pady=2)

    result = f"\nDohodak: ${user_income}\nUkupno troškova: ${total_expense}\nPreostalo: ${remaining}"
    customtkinter.CTkLabel(center_frame, text=result, font=FONT_BIG).pack(pady=20)

def show_input():
    clear_frame(scrollable_frame)

    user_text = dohodak.get()
    user_odabir = odabir.get()

    if user_odabir == "1":
        customtkinter.CTkLabel(scrollable_frame, text="Upiši kategoriju:", font=FONT_MEDIUM).pack()
        global category_entry
        category_entry = customtkinter.CTkEntry(scrollable_frame, width=200, font=FONT_MEDIUM)
        category_entry.pack()

        customtkinter.CTkLabel(scrollable_frame, text="Upiši trošak:", font=FONT_MEDIUM).pack()
        global amount_entry
        amount_entry = customtkinter.CTkEntry(scrollable_frame, width=200, font=FONT_MEDIUM)
        amount_entry.pack()

        global feedback
        feedback = customtkinter.CTkLabel(scrollable_frame, text="", font=FONT_MEDIUM)
        feedback.pack()

        customtkinter.CTkButton(scrollable_frame, text="Dodaj", command=add_category, font=FONT_MEDIUM).pack(pady=5)
        customtkinter.CTkButton(scrollable_frame, text="Završi unos", command=finish_entry, font=FONT_MEDIUM).pack(pady=5)

    elif user_odabir == "2":
        try:
            user_income = float(user_text)
            p = user_income * 0.5
            z = user_income * 0.3
            i = user_income * 0.2

            customtkinter.CTkLabel(scrollable_frame, text="50-30-20 pravilo", font=FONT_BIG).pack(pady=10)
            customtkinter.CTkLabel(scrollable_frame, text=f"50% potrebe: ${p}", font=FONT_MEDIUM).pack()
            customtkinter.CTkLabel(scrollable_frame, text=f"30% želje: ${z}", font=FONT_MEDIUM).pack()
            customtkinter.CTkLabel(scrollable_frame, text=f"20% štednja: ${i}", font=FONT_MEDIUM).pack()
        except ValueError:
            customtkinter.CTkLabel(scrollable_frame, text="Unesite ispravan broj dohotka.", font=FONT_MEDIUM).pack()

    else:
        customtkinter.CTkLabel(scrollable_frame, text="Neispravan odabir!", font=FONT_MEDIUM).pack()

# === Main window ===
root = customtkinter.CTk()
root.title("Personal Finance Tracker")
root.geometry("800x600")

customtkinter.CTkLabel(root, text="Upiši dohodak:", font=FONT_BIG).pack(padx=10, pady=10)
dohodak = customtkinter.CTkEntry(root, width=200, font=FONT_MEDIUM)
dohodak.pack(padx=10, pady=10)

customtkinter.CTkLabel(
    root,
    text="1 - Ručni unos troškova\n2 - Automatska podjela (50-30-20)",
    font=FONT_BIG
).pack(padx=10, pady=10)
odabir = customtkinter.CTkEntry(root, width=30, font=FONT_MEDIUM)
odabir.pack(padx=10, pady=10)

customtkinter.CTkButton(root, text="Nastavi", command=show_input, font=FONT_BIG).pack(pady=20)

# Scrollable frame for dynamic content
scrollable_frame = customtkinter.CTkScrollableFrame(root, width=750, height=250)
scrollable_frame.pack(padx=20, pady=10, fill="both", expand=True)

root.mainloop()
