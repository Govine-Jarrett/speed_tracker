#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class DashboardApp:
    def __init__(self, master=None):
        # build ui
        self.DashboardToplevel = tk.Tk() if master is None else tk.Toplevel(master)
        self.MainFrame = ttk.Frame(self.DashboardToplevel)
        self.BannerFrame = ttk.Frame(self.MainFrame)
        self.BannerLabel = ttk.Label(self.BannerFrame)
        self.img_Speed_Tracker_Banner = tk.PhotoImage(file="C:/Users/devgo/OneDrive/Desktop/Local_Projects/speed_tracker/res/image/Speed_Tracker_Banner.png")
        self.BannerLabel.configure(image=self.img_Speed_Tracker_Banner)
        self.BannerLabel.pack(side="top")
        self.BannerFrame.pack(side="top")
        self.BodyFrame = ttk.Frame(self.MainFrame)
        self.SpeedLabelframe = ttk.Labelframe(self.BodyFrame)
        self.UploadSpeedLabel = ttk.Label(self.SpeedLabelframe)
        self.UploadSpeedLabel.configure(text="Upload Speed in MB:")
        self.UploadSpeedLabel.place(anchor="nw", relx=0.14, rely=0.13, x=0, y=0)
        self.DownloadSpeedLabel = ttk.Label(self.SpeedLabelframe)
        self.DownloadSpeedLabel.configure(text="Download Speed in MB:")
        self.DownloadSpeedLabel.place(anchor="nw", relx=0.62, rely=0.13, x=0, y=0)
        self.ModemLocationLabel = ttk.Label(self.SpeedLabelframe)
        self.ModemLocationLabel.configure(text="Modem Location:")
        self.ModemLocationLabel.place(anchor="nw", relx=0.62, rely=0.50, x=0, y=0)
        self.RecipientEmailLabel = ttk.Label(self.SpeedLabelframe)
        self.RecipientEmailLabel.configure(text="Email Address:")
        self.RecipientEmailLabel.place(anchor="nw", relx=0.14, rely=0.50, x=0, y=0)
        self.uploadSpeedEntry = ttk.Entry(self.SpeedLabelframe)
        self.uploadSpeedEntry.configure(state="disabled", validate="key")
        _text_ = "150"
        self.uploadSpeedEntry["state"] = "normal"
        self.uploadSpeedEntry.delete("0", "end")
        self.uploadSpeedEntry.insert("0", _text_)
        self.uploadSpeedEntry["state"] = "disabled"
        self.uploadSpeedEntry.place(anchor="nw", relx=0.14, rely=0.25, x=0, y=0)
        self.uploadSpeedEntry.configure(validatecommand=self.is_speed_valid)
        self.DownloadSpeedEntry = ttk.Entry(self.SpeedLabelframe)
        self.DownloadSpeedEntry.configure(state="disabled")
        _text_ = "150"
        self.DownloadSpeedEntry["state"] = "normal"
        self.DownloadSpeedEntry.delete("0", "end")
        self.DownloadSpeedEntry.insert("0", _text_)
        self.DownloadSpeedEntry["state"] = "disabled"
        self.DownloadSpeedEntry.place(anchor="nw", relx=0.62, rely=0.25, x=0, y=0)
        self.ModemLocationEntry = ttk.Entry(self.SpeedLabelframe)
        self.ModemLocationEntry.configure(state="disabled")
        _text_ = "Home Office"
        self.ModemLocationEntry["state"] = "normal"
        self.ModemLocationEntry.delete("0", "end")
        self.ModemLocationEntry.insert("0", _text_)
        self.ModemLocationEntry["state"] = "disabled"
        self.ModemLocationEntry.place(anchor="nw", relx=0.62, rely=0.62, x=0, y=0)
        self.RecipientEmailEntry = ttk.Entry(self.SpeedLabelframe)
        self.RecipientEmailEntry.configure(state="disabled")
        _text_ = "example@domin.com"
        self.RecipientEmailEntry["state"] = "normal"
        self.RecipientEmailEntry.delete("0", "end")
        self.RecipientEmailEntry.insert("0", _text_)
        self.RecipientEmailEntry["state"] = "disabled"
        self.RecipientEmailEntry.place(anchor="nw", relx=0.14, rely=0.62, x=0, y=0)
        self.EditSpeedSettingsCheckbutton = ttk.Checkbutton(self.SpeedLabelframe)
        self.speed_settings_value = tk.BooleanVar()
        self.EditSpeedSettingsCheckbutton.configure(
            cursor="hand2", text="Edit speed?", variable=self.speed_settings_value
        )
        self.EditSpeedSettingsCheckbutton.place(
            anchor="nw", relx=0.14, rely=0.88, x=0, y=0
        )
        self.EditSpeedSettingsCheckbutton.configure(command=self.edit_speed_settings)
        self.SpeedLabelframe.configure(height=260, text="Speed Settings", width=580)
        self.SpeedLabelframe.pack(side="top")
        self.EmailSenderLabelframe = ttk.Labelframe(self.BodyFrame)
        self.EmailSenderLabel = ttk.Label(self.EmailSenderLabelframe)
        self.EmailSenderLabel.configure(text="Email Address:")
        self.EmailSenderLabel.place(anchor="nw", relx=0.01, rely=0.1, x=0, y=0)
        self.EmailSenderEntry = ttk.Entry(self.EmailSenderLabelframe)
        self.EmailSenderEntry.configure(state="disabled", validate="key")
        _text_ = "speed.tracker@gmail.com"
        self.EmailSenderEntry["state"] = "normal"
        self.EmailSenderEntry.delete("0", "end")
        self.EmailSenderEntry.insert("0", _text_)
        self.EmailSenderEntry["state"] = "disabled"
        self.EmailSenderEntry.place(anchor="nw", relx=0.01, rely=0.31, x=0, y=0)
        self.EmailSenderEntry.configure(validatecommand=self.is_email_valid)
        self.PasswordLabel = ttk.Label(self.EmailSenderLabelframe)
        self.PasswordLabel.configure(text="Password:")
        self.PasswordLabel.place(anchor="nw", relx=0.30, rely=0.08, x=0, y=0)
        self.PasswordEntry = ttk.Entry(self.EmailSenderLabelframe)
        self.PasswordEntry.configure(show="*", state="disabled")
        _text_ = "Password123"
        self.PasswordEntry["state"] = "normal"
        self.PasswordEntry.delete("0", "end")
        self.PasswordEntry.insert("0", _text_)
        self.PasswordEntry["state"] = "disabled"
        self.PasswordEntry.place(anchor="nw", relx=0.30, rely=0.31, x=0, y=0)
        self.ServerPortLabel = ttk.Label(self.EmailSenderLabelframe)
        self.ServerPortLabel.configure(text="Port:")
        self.ServerPortLabel.place(anchor="nw", relx=0.60, rely=0.08, x=0, y=0)
        self.SelectServerLabel = ttk.Label(self.EmailSenderLabelframe)
        self.SelectServerLabel.configure(text="Server:")
        self.SelectServerLabel.place(anchor="nw", relx=0.79, rely=0.08, x=0, y=0)
        self.ServerCombobox = ttk.Combobox(self.EmailSenderLabelframe)
        self.ServerCombobox.configure(
            state="disabled", values="smtp.gmail.com smtp.mail.yahoo.com", width=15
        )
        self.ServerCombobox.place(anchor="nw", relx=0.79, rely=0.29, x=0, y=0)
        self.ServerPortCombobox = ttk.Combobox(self.EmailSenderLabelframe)
        self.ServerPortCombobox.configure(
            state="disabled", values="995 587 465 110 25", width=9
        )
        self.ServerPortCombobox.place(anchor="nw", relx=0.6, rely=0.29, x=0, y=0)
        self.EditSenderEmailCheckbutton = ttk.Checkbutton(self.EmailSenderLabelframe)
        self._email_sender_value = tk.BooleanVar()
        self.EditSenderEmailCheckbutton.configure(
            cursor="hand2", text="Edit email?", variable=self._email_sender_value
        )
        self.EditSenderEmailCheckbutton.place(
            anchor="nw", relx=0.01, rely=0.7, x=0, y=0
        )
        self.EditSenderEmailCheckbutton.configure(command=self.edit_email_sender)
        self.EmailSenderLabelframe.configure(height=120, text="Email Sender", width=580)
        self.EmailSenderLabelframe.pack(side="top")
        self.BodyFrame.pack(side="top")
        self.ControlFrame = ttk.Frame(self.MainFrame)
        self._SaveBtn = ttk.Button(self.ControlFrame)
        self._SaveBtn.configure(state="disabled", text="S A V E")
        self._SaveBtn.place(relx=0.62, rely=0.23, width=100, x=0, y=0)
        self._SaveBtn.configure(command=self.save_settings)
        self.CloseBtn = ttk.Button(self.ControlFrame)
        self.CloseBtn.configure(cursor="hand2", text="C L O S E")
        self.CloseBtn.place(anchor="nw", relx=0.81, rely=0.23, width=100, x=0, y=0)
        self.CloseBtn.configure(command=self.close_dashboard)
        self.VersionLabel = ttk.Label(self.ControlFrame)
        self.VersionLabel.configure(text="V0.1.2")
        self.VersionLabel.place(anchor="nw", relx=0.02, rely=0.36, x=0, y=0)
        self.ControlFrame.configure(height=60, width=585)
        self.ControlFrame.pack(side="top")
        self.MainFrame.pack(side="top")
        self.img_Speed_Tracker_logo = tk.PhotoImage(file="C:/Users/devgo/OneDrive/Desktop/Local_Projects/speed_tracker/res/image/Speed_Tracker_logo.png")
        self.DashboardToplevel.configure(height=600, width=585)
        self.DashboardToplevel.iconphoto(True, self.img_Speed_Tracker_logo)
        self.DashboardToplevel.resizable(False, False)
        self.DashboardToplevel.title("Dashboard")

        # Main widget
        self.mainwindow = self.DashboardToplevel

    def run(self):
        self.mainwindow.mainloop()

    def is_speed_valid(self):
        pass

    def edit_speed_settings(self):
        pass

    def is_email_valid(self):
        pass

    def edit_email_sender(self):
        pass

    def save_settings(self):
        pass

    def close_dashboard(self):
        pass


if __name__ == "__main__":
    app = DashboardApp()
    app.run()
