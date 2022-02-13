from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FFAB76"
RED = "#FF6363"
ROUGE_VIGNE = "#8C0000"
VERT = "#95CD41"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 1
reps = 0
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break Time", fg=ROUGE_VIGNE)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break Time", fg=ROUGE_VIGNE)

    else:
        count_down(work_sec)
        timer_label.config(text="Working Time", fg=ROUGE_VIGNE)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
            check_marks_label.config(text=marks, bg=VERT, fg=ROUGE_VIGNE)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=VERT)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=VERT, fg=ROUGE_VIGNE)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=VERT, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 50, "bold"))
canvas.grid(column=1, row=1)

reset_button = Button(text="Reset", highlightthickness=0, bg=VERT, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks_label = Label(text="", bg=VERT, fg=ROUGE_VIGNE)
check_marks_label.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

window.mainloop()
