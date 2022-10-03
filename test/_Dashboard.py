
# OLD CODE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import tkinter as tk
from tkinter import messagebox, BooleanVar
from tkinter import ttk
from utils.readDashboardSettings import ReadDashboardSettings
from string import digits

# TODO:
# -[x] Check if the 'Dashboard.ini' exist in config folder
# -[x] Read in data dynamically from the config file
    # and inset into entry widget
# -[] Allow the user to edit and save the data 
# -[] limit the upload and download speed entry to 3 char and to allow only int


class DashboardApp:
    dashboard_settings = ReadDashboardSettings()
    def __init__(self, master=None):
        self.DashboardToplevel = tk.Tk() if master is None else tk.Toplevel(master)
        
        
        # Getting image path for the app banner and icon
        self.img_Speed_Tracker_logo = tk.PhotoImage(file="./res/image/Speed_Tracker_logo.png")
        self.img_Speed_Tracker_Banner = tk.PhotoImage(file="./res/image/Speed_Tracker_Banner.png")
        
        
        # Build toplevel window
        self.DashboardToplevel.geometry("585x530+355+100")
        self.DashboardToplevel.iconphoto(True, self.img_Speed_Tracker_logo)
        self.DashboardToplevel.resizable(False, False)
        self.DashboardToplevel.title("Speed Tracker Dashboard")
        
        
        # Creating the main frame to place all widgets
        self.MainFrame = tk.Frame(self.DashboardToplevel)
        
        
        # Creating the banner frame to place the app banner
        self.BannerFrame = tk.Frame(self.MainFrame)
        #  Adding the banner image to the banner frame
        self.BannerLabel = tk.Label(self.BannerFrame)
        
        # Customizing banner label
        self.BannerLabel.configure(image=self.img_Speed_Tracker_Banner)

        
        # Creating the form frame 
        self.FormFrame = tk.Frame(self.MainFrame)
        
        # Adding the Settings label frames
        self.SettingsLabelframe = tk.LabelFrame(self.FormFrame)
        
        # Adding the  widgets to the Settings label frame
        
        # Label
        self.uploadSpeedLabel = tk.Label(self.SettingsLabelframe)
        # Entry
        self.UploadSpeedEntry = ttk.Entry(self.SettingsLabelframe)
        
        # label
        self.DownloadSpeedLabel = tk.Label(self.SettingsLabelframe)
        # Entry
        self.DownloadSpeedEntry = ttk.Entry(self.SettingsLabelframe)
        
        # Label
        self.RecipientEmailLabel = tk.Label(self.SettingsLabelframe)
        # Entry
        self.RecipientEmailEntry = ttk.Entry(self.SettingsLabelframe)
        
        # Label
        self.ModemLocationLabel = tk.Label(self.SettingsLabelframe)
        # Entry
        self.ModemLocationEntry = ttk.Entry(self.SettingsLabelframe)
        
        # Edit Speed Settings Checkbutton
        self.speed_settings_value = BooleanVar()
        self.EditSpeedSettingsCheckbutton = tk.Checkbutton(self.SettingsLabelframe, variable=self.speed_settings_value)
        
        
        
        
        # Adding the Sender's Email label frame
        self.SendersEmailLabelframe = tk.LabelFrame(self.FormFrame)
        
        # Adding the widget ti the Senders Email label frame
        
        # Label
        self.SenderEmailLabel = tk.Label(self.SendersEmailLabelframe)
        # Entry
        self.SenderEmailEntry = tk.Entry(self.SendersEmailLabelframe)
        
        # Label
        self.SenderPasswordLabel = tk.Label(self.SendersEmailLabelframe)
        # Entry
        self.SenderPasswordEntry = tk.Entry(self.SendersEmailLabelframe)
        
        # Edit Sender Email Checkbutton
        self.edit_sender_email_value = BooleanVar()
        self.EditSenderEmailCheckbutton = tk.Checkbutton(self.SendersEmailLabelframe, variable=self.edit_sender_email_value)
        
        
        
        # Creating the control frame
        self.ControlFrame = tk.Frame(self.MainFrame)
        
        # Adding the Save and Exit buttons along with the version label
        self.VersionLabel = tk.Label(self.ControlFrame)
        self.SaveBtn = tk.Button(self.ControlFrame)
        self.ExitBtn = tk.Button(self.ControlFrame)
        
        
        
        
        
        
        
        
        # Customizing buttons and label
        
        # Speed Setting Frame
        self.SettingsLabelframe.configure(
            font="{@Microsoft YaHei UI} 12 {}",
            height=260,
            text="Speed Settings",
            width=580,
        )
        # Upload speed
        # Label
        self.uploadSpeedLabel.configure(
            font="{Microsoft} 11 {}", text="Upload Speed in MB:"
        )
        # Entry
        self.UploadSpeedEntry.configure(
            font="{@Microsoft YaHei UI} 10 {}", state="disabled"
        )
 
        # Reading data from config
        _upload_ = DashboardApp.dashboard_settings.get_upload()
        self.UploadSpeedEntry["state"] = "normal"
        self.UploadSpeedEntry.delete("0", "end")
        self.UploadSpeedEntry.insert("0", _upload_)
        self.UploadSpeedEntry["state"] = "disabled"
        

        # Download speed
        # Label
        self.DownloadSpeedLabel.configure(
            font="{Microsoft} 11 {}", text="Download Speed in MB:"
        )
        # Entry
        self.DownloadSpeedEntry.configure(
            font="{@Microsoft YaHei UI} 10 {}", state="disabled"
        )
        # Reading data from config
        _download_ = DashboardApp.dashboard_settings.get_download()
        self.DownloadSpeedEntry["state"] = "normal"
        self.DownloadSpeedEntry.delete("0", "end")
        self.DownloadSpeedEntry.insert("0", _download_)
        self.DownloadSpeedEntry["state"] = "disabled"
        
        # Edit Speed Settings Checkbutton
        self.EditSpeedSettingsCheckbutton.configure(
            cursor="hand2", font="{Microsoft} 10 {}",
            overrelief="flat", takefocus=True, text="Edit settings?",
        )
        
        
        # Recipient Email
        # Label
        self.RecipientEmailLabel.configure(
            font="{Microsoft} 11 {}", text="Recipient Email:"
        )
        # Entry
        self.RecipientEmailEntry.configure(
            font="{@Microsoft YaHei UI} 10 {}", state="disabled"
        )
        # Reading data from config
        _recipient_ = DashboardApp.dashboard_settings.get_recipient_email()
        self.RecipientEmailEntry["state"] = "normal"
        self.RecipientEmailEntry.delete("0", "end")
        self.RecipientEmailEntry.insert("0", _recipient_)
        self.RecipientEmailEntry["state"] = "disabled"
        
        # Modem Location
        # Label
        self.ModemLocationLabel.configure(
            font="{Microsoft} 11 {}", text="Modem Location:"
        )
        # Entry
        self.ModemLocationEntry.configure(
            font="{@Microsoft YaHei UI} 10 {}", state="disabled"
        )
        
        # Reading data from config
        _location_ = DashboardApp.dashboard_settings.get_modem_loc()
        self.ModemLocationEntry["state"] = "normal"
        self.ModemLocationEntry.delete("0", "end")
        self.ModemLocationEntry.insert("0", _location_)
        self.ModemLocationEntry["state"] = "disabled"
        
        # Edit Speed Settings Checkbutton
        self.EditSpeedSettingsCheckbutton.configure(command=self.edit_speed_settings)
        
        
        
        

        
        
        
        # Email Sender Frame
        self.SendersEmailLabelframe.configure(
            font="{@Microsoft YaHei UI} 12 {}",
            height=120,
            text="Sender's Email",
            width=580,
        )
        # Label
        self.SenderEmailLabel.configure(font="{Microsoft} 11 {}", text="Email:")
        # Entry
        self.SenderEmailEntry.configure(
            font="{@Microsoft YaHei UI} 10 {}", state="disabled"
        )
        # Reading data from config
        _sender_ = DashboardApp.dashboard_settings.get_sender_email()
        self.SenderEmailEntry["state"] = "normal"
        self.SenderEmailEntry.delete("0", "end")
        self.SenderEmailEntry.insert("0", _sender_)
        self.SenderEmailEntry["state"] = "disabled"
        
        # Label
        self.SenderPasswordLabel.configure(font="{Microsoft} 11 {}", text="Password:")
        self.SenderPasswordEntry.configure(
            font="{@Microsoft YaHei UI} 10 {}", show="*", state="disabled"
        )
        # Reading data from config
        _password_ = DashboardApp.dashboard_settings.get_password()
        self.SenderPasswordEntry["state"] = "normal"
        self.SenderPasswordEntry.delete("0", "end")
        self.SenderPasswordEntry.insert("0", _password_)
        self.SenderPasswordEntry["state"] = "disabled"
        
        # Edit Sender Email Checkbutton
        self.EditSenderEmailCheckbutton.configure(command=self.edit_sender_email)
        
        # Entry
        self.EditSenderEmailCheckbutton.configure(
            cursor="hand2",
            font="{Microsoft} 10 {}",
            overrelief="flat",
            text="Edit sender info?"
        )
        
        
        
        
        
        
        
        
        
        
        # Control Frame
        self.ControlFrame.configure(height=50, width=585)
        # App version label
        self.VersionLabel.configure(font="{@Microsoft YaHei} 8 {}", pady=10, text="V0.1.2")
        # Save button
        self.SaveBtn.configure(
            activebackground="#299693",
            activeforeground="#ffffff",
            background="#ffffff",
            cursor="arrow",
            default="disabled",
            disabledforeground="#1c0037",
            font="{Microsoft} 11 {}",
            foreground="#299693",
            state="disabled", text="Save",
            command=self.save_config
        )
        # Exit button
        self.ExitBtn.configure(
            activebackground="#cd0532",
            activeforeground="#ffffff",
            background="#ffffff",
            cursor="hand2",
            default="normal",
            disabledforeground="#1c0037",
            font="{Microsoft} 11 {}",
            foreground="#cd0532",
            state="normal", text="Close",
            command=self.exit_dashboard
        )



        
        
        #######################
        # PACKING AND PLACING #
        #     ALL WIDGETS     #
        #######################

        # Body
        self.MainFrame.pack(side="top")
        
        # Section 1
        self.BannerFrame.pack(side="top")
        self.BannerLabel.pack(side="top")
        
        # Section 2
        self.FormFrame.pack(side="top")
        self.SettingsLabelframe.pack(side="top")
        self.uploadSpeedLabel.place(anchor="nw", relx=0.05, rely=0.06, x=0, y=0)
        self.UploadSpeedEntry.place(relx=0.05, rely=0.25, x=0, y=0)
        self.DownloadSpeedLabel.place(anchor="nw", relx=0.61, rely=0.06, x=0, y=0)
        self.DownloadSpeedEntry.place(relx=0.61, rely=0.25, x=0, y=0)
        self.RecipientEmailLabel.place(anchor="nw", relx=0.05, rely=0.57, x=0, y=0)
        self.RecipientEmailEntry.place(relx=0.05, rely=0.73, x=0, y=0)
        self.ModemLocationLabel.place(anchor="nw", relx=0.61, rely=0.57, x=0, y=0)
        self.ModemLocationEntry.place(relx=0.61, rely=0.73, x=0, y=0)
        self.EditSpeedSettingsCheckbutton.place(relx=0.38, rely=0.87, x=0, y=0)
        
        # Section 3
        self.SendersEmailLabelframe.pack(side="top")
        self.SenderEmailLabel.place(anchor="nw", relx=0.05, rely=0.06, x=0, y=0)
        self.SenderEmailEntry.place(relx=0.05, rely=0.42, x=0, y=0)
        self.SenderPasswordLabel.place(anchor="nw", relx=0.61, rely=0.06, x=0, y=0)
        self.SenderPasswordEntry.place(relx=0.61, rely=0.42, x=0, y=0)
        self.EditSenderEmailCheckbutton.place(relx=0.38, rely=0.65, x=0, y=0)
       
        # Section 4
        self.ControlFrame.pack(side="top")
        self.VersionLabel.place(anchor="nw", relx=0.05, rely=0.09, x=0, y=0)
        self.SaveBtn.place(anchor="nw", relx=0.72, rely=0.17, x=0, y=0)
        self.ExitBtn.place(anchor="nw", relx=0.83, rely=0.17, x=0, y=0)



        # Launching the toplevel window
        self.mainwindow = self.DashboardToplevel



    def run(self):
        self.mainwindow.mainloop()


        # validate data
    def is_valid_input(self, text:str) -> bool:
        """
        Get the speed entry and validate if its 
        length is greater than 3 char or if it only
        contains digits.

        Args:
            text (str): the minimum upload or download speed

        Returns:
            bool: _description_
        """
        max_length = 3 
        if len(text) > max_length:
            return False
        for char in text:
            if char not in digits:
                return False
                
                
                
            


    def edit_speed_settings(self):
        """
        Enable all entry widgets in the Speed Settings
        label frame if the check button is selected and 
        also the save button in the control frame.
        
        Otherwise disable the previous enabled widgets. 
        """
        if self.speed_settings_value.get():
            
            # Enabling the save button 
            self.SaveBtn.configure(state='normal', cursor='hand2', background="#299693", foreground="#ffffff")
        
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
                self.SaveBtn.configure(state='disable', cursor='arrow',  background="#ffffff", foreground="#299693")
                    



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
                self.SaveBtn.configure(state='normal', cursor='hand2', background="#299693", foreground="#ffffff")
 
        else:
            # Enabling the Email  and Password entry
            self.SenderEmailEntry.configure(state='disable')
            self.SenderPasswordEntry.configure(state='disable')
            # Hide the password
            self.SenderPasswordEntry.configure(show='*')
            
            # Check if the button is enabled
            if not self.speed_settings_value.get():
                # Disabling the save button 
                self.SaveBtn.configure(state='disable', cursor='arrow', background="#ffffff", foreground="#299693")




    def save_config(self):
        # validate entries
            # confirm is the user can to save to new data
        pass




    def exit_dashboard(self):
        # check if the user is sure that they want to exit
        if messagebox.askyesno('Close Dashboard', 'Are you sure you want to close the dashboard?'):
            self.DashboardToplevel.destroy()

if __name__ == "__main__":
    app = DashboardApp()
    app.run()













