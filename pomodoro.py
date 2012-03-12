import Tkinter
import datetime
import commands


class PomodoroTimer():
    """
        Simple pomodoro timer app
    """
    def __init__(self):
        self.root = Tkinter.Tk()
        self.root.title("Pomodoro timer")
        self.label = Tkinter.Label(font=("Helvetica Neue", 44), width=10)
        self.label.pack(ipadx=10, ipady=10, )
        self.start_pomodoro()
        self.update_timer()
        self.beeped = False
        self.break_passed = False
        self.root.mainloop()

    def reset_time(self, event=None, minutes=1):
        self.beeped = False
        self.end = datetime.datetime.now() + datetime.timedelta(
                                                        minutes=minutes)

    def start_break(self, event=None):
        self.reset_time(minutes=5)
        self.break_passed = True
        self.beeped = False
        self.label.configure(fg="dark green")
        self.label.unbind("<Button-1>")

    def start_pomodoro(self, event=None):
        self.reset_time(minutes=25)
        self.label.configure(fg="black")
        self.break_passed = False
        self.label.unbind("<Button-1>")

    def update_timer(self):
        rem = self.end - datetime.datetime.now()
        rem = int(rem.total_seconds())
        if(rem > 0):
            hours, remainder = divmod(rem, 3600)
            minutes, seconds = divmod(remainder, 60)
            text = '%02d:%02d' % (minutes, seconds)
        else:
            if not self.beeped:
                commands.getstatusoutput('osascript -e "beep 3"')
                self.beeped = True

            if not self.break_passed:
                text = "Break"
                self.label.bind("<Double-Button-1>", self.start_break)
            else:
                text = "Pomodoro"
                self.label.bind("<Double-Button-1>", self.start_pomodoro)

        self.label.configure(text=text)
        self.root.after(1000, self.update_timer)

app = PomodoroTimer()
