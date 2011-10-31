import Tkinter
import datetime
import commands


class App():
    def __init__(self):
        self.root = Tkinter.Tk()
        self.label = Tkinter.Label(font=("Helvetica Neue", 44), width=10)
        self.label.pack(ipadx=10, ipady=10, )
        self.reset_time()
        self.update_timer()
        self.beeped = False
        self.root.mainloop()

    def reset_time(self, event=None):
        self.beeped = False
        self.end = datetime.datetime.now() + datetime.timedelta(minutes=25)

    def update_timer(self):
        rem = self.end - datetime.datetime.now()
        rem = int(rem.total_seconds())
        if(rem > 0):
            hours, remainder = divmod(rem, 3600)
            minutes, seconds = divmod(remainder, 60)
            text = '%s:%s:%s' % (hours, minutes, seconds)
        else:
            text = "pomodoro"
            if not self.beeped:
                commands.getstatusoutput('osascript -e "beep 3"')
                self.beeped = True
            self.label.bind("<Button-1>", self.reset_time)
        self.label.configure(text=text)
        self.root.after(1000, self.update_timer)

app = App()
