import tkinter
# find the color on the colorhunt.co

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    print(count)
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=20, pady=20, bg=YELLOW)


# def say_something(thing):
#     print(thing)
#
# window.after(1000, say_something, "Fuck!!!")

canvas = tkinter.Canvas(width=280, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(140, 112, image=tomato_img)
timer_text = canvas.create_text(140, 132, text="00:00", fill="white", font=(FONT_NAME, 33, "bold"))
canvas.grid(column=1, row=1)
count_down(6)
#Label
timer = tkinter.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 33, "bold"))
timer.grid(column=1, row=0)
timer.config(padx=0, pady=0, bg=YELLOW)
check_mark = tkinter.Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 33, "bold"))
check_mark.grid(column=1, row=3)

#Button
def button_clicked():
    print("click")

left_button = tkinter.Button(text="start", highlightthickness=0, command=button_clicked)
left_button.grid(column=0, row=2)

right_button = tkinter.Button(text="reset", highlightthickness=0, command=button_clicked)
right_button.grid(column=2, row=2)




window.mainloop()