import tkinter
import math
# find the color on the colorhunt.co

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer_count = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_count)
    timer.config(text="Timer", fg=GREEN)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text=f"00:00")
    check_mark.config(text=" ")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer.config(text="Break", fg=GREEN, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer.config(text="Short Break", fg=PINK, bg=YELLOW)
    else:
        count_down(WORK_MIN * 60)
        timer.config(text="Work", fg=RED, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer_count

    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer_count = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # marks = ""
        # work_sessions = math.floor(reps/2)
        # for _ in range(work_sessions):
        #     marks += "✔"
        #     check_mark.config(text=marks)
            # do not work
        if reps == 2:
            print("reps = 2")
            check_mark.config(text="✔")
        elif reps == 4:
            check_mark.config(text=" ✔✔", fg=GREEN, bg=YELLOW)
        elif reps == 6:
            check_mark.config(text="✔✔✔", fg=GREEN, bg=YELLOW)



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
#count_down(6)

#Label
timer = tkinter.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 33, "bold"))
timer.grid(column=1, row=0)
timer.config(padx=0, pady=0, bg=YELLOW)

check_mark = tkinter.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 33, "bold"))
check_mark.grid(column=1, row=3)
check_mark.config(padx=0, pady=0, bg=YELLOW)


#Button
def button_clicked():
    print("click")

left_button = tkinter.Button(text="start", highlightthickness=0, command=start_timer)
left_button.grid(column=0, row=2)

right_button = tkinter.Button(text="reset", highlightthickness=0, command=reset_timer)
right_button.grid(column=2, row=2)




window.mainloop()