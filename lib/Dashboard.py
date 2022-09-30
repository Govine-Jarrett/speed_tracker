#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox, BooleanVar

class DashboardApp:
    def __init__(self, master=None):
        # build ui
        self.DashboardToplevel = tk.Tk() if master is None else tk.Toplevel(master)
        self.MainFrame = tk.Frame(self.DashboardToplevel)
        self.BannerFrame = tk.Frame(self.MainFrame)
        self.BannerLabel = tk.Label(self.BannerFrame)
        self.img_Speed_Tracker_Banner = tk.PhotoImage(file="./res/image/Speed_Tracker_Banner.png")
        self.BannerLabel.configure(image=self.img_Speed_Tracker_Banner)
        self.BannerLabel.pack(side="top")
        self.BannerFrame.configure(height=100, width=585)
        self.BannerFrame.pack(side="top")
        self.FormFrame = tk.Frame(self.MainFrame)
        self.SettingsLabelframe = tk.LabelFrame(self.FormFrame)
        self.uploadSpeedLabel = tk.Label(self.SettingsLabelframe)
        self.uploadSpeedLabel.configure(
            font="{Microsoft} 11 {}", text="Upload Speed in MB:"
        )
        self.uploadSpeedLabel.place(anchor="nw", relx=0.05, rely=0.06, x=0, y=0)
        self.UploadSpeedEntry = tk.Entry(self.SettingsLabelframe)
        self.UploadSpeedEntry.configure(
            font="{@Microsoft YaHei UI} 10 {}", state="disabled"
        )
        _text_ = "100"
        self.UploadSpeedEntry["state"] = "normal"
        self.UploadSpeedEntry.delete("0", "end")
        self.UploadSpeedEntry.insert("0", _text_)
        self.UploadSpeedEntry["state"] = "disabled"
        self.UploadSpeedEntry.place(relx=0.05, rely=0.25, x=0, y=0)
        self.DownloadSpeedLabel = tk.Label(self.SettingsLabelframe)
        self.DownloadSpeedLabel.configure(
            font="{Microsoft} 11 {}", text="Download Speed in MB:"
        )
        self.DownloadSpeedLabel.place(anchor="nw", relx=0.61, rely=0.06, x=0, y=0)
        self.DownloadSpeedEntry = tk.Entry(self.SettingsLabelframe)
        self.DownloadSpeedEntry.configure(
            font="{@Microsoft YaHei UI} 10 {}", state="disabled"
        )
        _text_ = "100"
        self.DownloadSpeedEntry["state"] = "normal"
        self.DownloadSpeedEntry.delete("0", "end")
        self.DownloadSpeedEntry.insert("0", _text_)
        self.DownloadSpeedEntry["state"] = "disabled"
        self.DownloadSpeedEntry.place(relx=0.61, rely=0.25, x=0, y=0)
        self.RecipientEmailLabel = tk.Label(self.SettingsLabelframe)
        self.RecipientEmailLabel.configure(
            font="{Microsoft} 11 {}", text="Recipient Email:"
        )
        self.RecipientEmailLabel.place(anchor="nw", relx=0.05, rely=0.57, x=0, y=0)
        self.RecipientEmailEntry = tk.Entry(self.SettingsLabelframe)
        self.RecipientEmailEntry.configure(
            font="{@Microsoft YaHei UI} 10 {}", state="disabled"
        )
        _text_ = "youremail@example.com"
        self.RecipientEmailEntry["state"] = "normal"
        self.RecipientEmailEntry.delete("0", "end")
        self.RecipientEmailEntry.insert("0", _text_)
        self.RecipientEmailEntry["state"] = "disabled"
        self.RecipientEmailEntry.place(relx=0.05, rely=0.73, x=0, y=0)
        self.ModemLocationLabel = tk.Label(self.SettingsLabelframe)
        self.ModemLocationLabel.configure(
            font="{Microsoft} 11 {}", text="Modem Location:"
        )
        self.ModemLocationLabel.place(anchor="nw", relx=0.61, rely=0.57, x=0, y=0)
        self.ModemLocationEntry = tk.Entry(self.SettingsLabelframe)
        self.ModemLocationEntry.configure(
            font="{@Microsoft YaHei UI} 10 {}", state="disabled"
        )
        _text_ = "Office"
        self.ModemLocationEntry["state"] = "normal"
        self.ModemLocationEntry.delete("0", "end")
        self.ModemLocationEntry.insert("0", _text_)
        self.ModemLocationEntry["state"] = "disabled"
        self.ModemLocationEntry.place(relx=0.61, rely=0.73, x=0, y=0)
        self.EditSpeedSettingsCheckbutton = tk.Checkbutton(self.SettingsLabelframe)
        self.EditSpeedSettingsCheckbutton.configure(
            cursor="hand2", font="{Microsoft} 10 {}", overrelief="flat", takefocus=True
        )
        
        
        
        
        self.speed_settings_value = BooleanVar()
        self.EditSpeedSettingsCheckbutton.configure(text="Edit settings?", variable=self.speed_settings_value)
        
        
        
        
        
        self.EditSpeedSettingsCheckbutton.place(relx=0.38, rely=0.87, x=0, y=0)
        self.EditSpeedSettingsCheckbutton.configure(command=self.edit_speed_settings)
        self.SettingsLabelframe.configure(
            font="{@Microsoft YaHei UI} 12 {}",
            height=260,
            text="Speed Settings",
            width=580,
        )
        self.SettingsLabelframe.pack(side="top")
        self.SendersEmailLabelframe = tk.LabelFrame(self.FormFrame)
        self.SenderEmailLabel = tk.Label(self.SendersEmailLabelframe)
        self.SenderEmailLabel.configure(font="{Microsoft} 11 {}", text="Gmail:")
        self.SenderEmailLabel.place(anchor="nw", relx=0.05, rely=0.06, x=0, y=0)
        self.SenderEmailEntry = tk.Entry(self.SendersEmailLabelframe)
        self.SenderEmailEntry.configure(
            font="{@Microsoft YaHei UI} 10 {}", state="disabled"
        )
        _text_ = "speedtracker@gmail.com"
        self.SenderEmailEntry["state"] = "normal"
        self.SenderEmailEntry.delete("0", "end")
        self.SenderEmailEntry.insert("0", _text_)
        self.SenderEmailEntry["state"] = "disabled"
        self.SenderEmailEntry.place(relx=0.05, rely=0.42, x=0, y=0)
        self.SenderPasswordLabel = tk.Label(self.SendersEmailLabelframe)
        self.SenderPasswordLabel.configure(font="{Microsoft} 11 {}", text="Password:")
        self.SenderPasswordLabel.place(anchor="nw", relx=0.61, rely=0.06, x=0, y=0)
        self.SenderPasswordEntry = tk.Entry(self.SendersEmailLabelframe)
        self.SenderPasswordEntry.configure(
            font="{@Microsoft YaHei UI} 10 {}", show="*", state="disabled"
        )
        _text_ = "Password123"
        self.SenderPasswordEntry["state"] = "normal"
        self.SenderPasswordEntry.delete("0", "end")
        self.SenderPasswordEntry.insert("0", _text_)
        self.SenderPasswordEntry["state"] = "disabled"
        self.SenderPasswordEntry.place(relx=0.61, rely=0.42, x=0, y=0)
        
        
        self.edit_sender_email_value = BooleanVar()
        
        self.EditSenderEmailCheckbutton = tk.Checkbutton(self.SendersEmailLabelframe)
        self.EditSenderEmailCheckbutton.configure(
            cursor="hand2",
            font="{Microsoft} 10 {}",
            overrelief="flat",
            text="Edit sender info?",
            variable=self.edit_sender_email_value
        )
        

        self.EditSenderEmailCheckbutton.place(relx=0.38, rely=0.65, x=0, y=0)
        self.EditSenderEmailCheckbutton.configure(command=self.edit_sender_email)
        self.SendersEmailLabelframe.configure(
            font="{@Microsoft YaHei UI} 12 {}",
            height=120,
            text="Sender's Email",
            width=580,
        )
        self.SendersEmailLabelframe.pack(side="top")
        self.FormFrame.configure(height=500, width=585)
        self.FormFrame.pack(side="top")
        self.ControlFrame = tk.Frame(self.MainFrame)
        self.SaveBtn = tk.Button(self.ControlFrame)
        self.SaveBtn.configure(
            activebackground="#299693",
            activeforeground="#ffffff",
            background="#ffffff",
            cursor="arrow",
        )
        self.SaveBtn.configure(
            default="disabled",
            disabledforeground="#1c0037",
            font="{Microsoft} 11 {}",
            foreground="#299693",
        )
        self.SaveBtn.configure(state="disabled", text="Save")
        self.SaveBtn.place(anchor="nw", relx=0.72, rely=0.17, x=0, y=0)
        self.SaveBtn.configure(command=self.save_config)
        self.VersionLabel = tk.Label(self.ControlFrame)
        self.VersionLabel.configure(
            font="{@Microsoft YaHei} 8 {}", pady=10, text="V0.1.2"
        )
        self.VersionLabel.place(anchor="nw", relx=0.05, rely=0.09, x=0, y=0)
        self.ExitBtn = tk.Button(self.ControlFrame)
        self.ExitBtn.configure(
            activebackground="#cd0532",
            activeforeground="#ffffff",
            background="#ffffff",
            cursor="hand2",
        )
        self.ExitBtn.configure(
            default="normal",
            disabledforeground="#1c0037",
            font="{Microsoft} 11 {}",
            foreground="#cd0532",
        )
        self.ExitBtn.configure(state="normal", text="Exit")
        self.ExitBtn.place(anchor="nw", relx=0.83, rely=0.17, x=0, y=0)
        self.ExitBtn.configure(command=self.exit_dashboard)
        self.ControlFrame.configure(height=50, width=585)
        self.ControlFrame.pack(side="top")
        self.MainFrame.configure(height=600, width=585)
        self.MainFrame.pack(side="top")
        self.img_Speed_Tracker_logo = tk.PhotoImage(file="./res/image/Speed_Tracker_logo.png")
        self.DashboardToplevel.configure(height=600, width=585)
        self.DashboardToplevel.iconphoto(True, self.img_Speed_Tracker_logo)
        self.DashboardToplevel.resizable(False, False)
        self.DashboardToplevel.title("Speed Tracker Dashboard")

        # Main widget
        self.mainwindow = self.DashboardToplevel

    def run(self):
        self.mainwindow.mainloop()




    def edit_speed_settings(self):
        """
        Enable all entry widgets in the Speed Settings
        label frame if the check button is selected and 
        also the save button in the control frame.
        
        Otherwise disable the previous enabled widgets. 
        """
        if self.speed_settings_value.get():

            # Enabling the save button 
            self.SaveBtn.configure(state='normal', cursor='hand2')
        
            # Enabling the Upload and download entry  
            self.UploadSpeedEntry.configure(state='normal')
            self.DownloadSpeedEntry.configure(state='normal')
            
            # Enabling the Recipient Email and Modem Location entry
            self.RecipientEmailEntry.configure(state='normal')
            self.ModemLocationEntry.configure(state='normal')
            
        else:
            # Disabling the Upload and Download entry  
            self.UploadSpeedEntry.configure(state='disable')
            self.DownloadSpeedEntry.configure(state='disable')
            
            # Disabling the Recipient Email and Modem Location entry
            self.RecipientEmailEntry.configure(state='disable')
            self.ModemLocationEntry.configure(state='disable')
            
            # Check if the button is enabled
            if not self.edit_sender_email_value.get():
                # Disabling the save button 
                self.SaveBtn.configure(state='disable', cursor='arrow')
                    



    def edit_sender_email(self):
        """
        Enable the sender's email and password entry widgets
        if the check button is selected.
        
        Otherwise disable them.
        """
        if self.edit_sender_email_value.get():
            # Enabling the Email  and Password entry
            self.SenderEmailEntry.configure(state='normal')
            self.SenderPasswordEntry.configure(state='normal')
            # Show the password
            self.SenderPasswordEntry.configure(show='')
            
            # Check if the button is enabled
            if not self.speed_settings_value.get():
                # Enabling the save button 
                self.SaveBtn.configure(state='normal', cursor='hand2')
 
        else:
            # Enabling the Email  and Password entry
            self.SenderEmailEntry.configure(state='disable')
            self.SenderPasswordEntry.configure(state='disable')
            # Hide the password
            self.SenderPasswordEntry.configure(show='*')
            
            # Check if the button is enabled
            if not self.speed_settings_value.get():
                # Disabling the save button 
                self.SaveBtn.configure(state='disable', cursor='arrow')




    def save_config(self):
        pass




    def exit_dashboard(self):
        # check if the user is sure that they want to exit
        if messagebox.askyesno('Close Dashboard', 'Are you sure you want to exit the dashboard?'):
            self.DashboardToplevel.destroy()

if __name__ == "__main__":
    app = DashboardApp()
    app.run()
