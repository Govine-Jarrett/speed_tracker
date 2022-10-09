#!/usr/bin/python3
from string import digits
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from utils.emailChecker import is_email_valid
from utils.updateDashboardSettings import UpdateDashboardSettings
from utils.readDashboardSettings import ReadDashboardSettings
from utils.emailServers import EmailServers
# from utils.encryptionManager import create_key, read_key, encrypt_password, decrypt_password
# from utils.encryptionManager import MASTER_KEY_FILE
from utils.createDashboardSettings import config_file_path, system




class DashboardApp:
    def __init__(self, master=None):
        # build ui
        self.DashboardToplevel = tk.Tk() if master is None else tk.Toplevel(master)
        
        self.load_dashboard_settings = ReadDashboardSettings()
        self.update_dashboard_settings = UpdateDashboardSettings()
        secure_servers = EmailServers()
        
        # Setting the max length for speed entries
        self.max_char_for_speed = 3
        
        
   




        #######################
        #     INITIALIZING    #
        #     ALL WIDGETS     #
        #######################



        # MainFrame
        self.MainFrame = ttk.Frame(self.DashboardToplevel)
        
        # Section 1
        self.BannerFrame = ttk.Frame(self.MainFrame)
        self.BannerLabel = ttk.Label(self.BannerFrame)
        
        # Section 2
        self.FormFrame = tk.Frame(self.MainFrame)

        # Section 2: 1
        self.SpeedLabelframe = ttk.Labelframe(self.FormFrame)
        self.UploadSpeedLabel = ttk.Label(self.SpeedLabelframe)
        self.DownloadSpeedLabel = ttk.Label(self.SpeedLabelframe)
        self.ModemLocationLabel = ttk.Label(self.SpeedLabelframe)
        self.RecipientEmailLabel = ttk.Label(self.SpeedLabelframe)
        self.UploadSpeedEntry = ttk.Entry(self.SpeedLabelframe)
        self.DownloadSpeedEntry = ttk.Entry(self.SpeedLabelframe)
        self.ModemLocationEntry = ttk.Entry(self.SpeedLabelframe)
        self.RecipientEmailEntry = ttk.Entry(self.SpeedLabelframe)
        self.EditSpeedSettingsCheckbutton = ttk.Checkbutton(self.SpeedLabelframe)
        
        # Section 2: 2
        self.EmailSenderLabelframe = ttk.Labelframe(self.FormFrame)
        self.EmailSenderLabel = ttk.Label(self.EmailSenderLabelframe)
        self.EmailSenderEntry = ttk.Entry(self.EmailSenderLabelframe)
        self.PasswordLabel = ttk.Label(self.EmailSenderLabelframe)
        self.PasswordEntry = ttk.Entry(self.EmailSenderLabelframe)
        self.ServerPortLabel = ttk.Label(self.EmailSenderLabelframe)
        self.SelectServerLabel = ttk.Label(self.EmailSenderLabelframe)
        self.ServerPortCombobox = ttk.Combobox(self.EmailSenderLabelframe)
        self.ServerCombobox = ttk.Combobox(self.EmailSenderLabelframe)
        self.EditSenderEmailCheckbutton = ttk.Checkbutton(self.EmailSenderLabelframe)

        
        # Section 3
        self.ControlFrame = ttk.Frame(self.MainFrame)
        self.SaveBtn = ttk.Button(self.ControlFrame)
        self.CloseBtn = ttk.Button(self.ControlFrame)
        self.VersionLabel = ttk.Label(self.ControlFrame)











        #######################
        #     LOAD IN ALL     #
        #     IMAGES FOR      #
        #       WIDGETS       #
        #######################

        # App logo
        self.img_Speed_Tracker_logo = tk.PhotoImage(file="./res/image/Speed_Tracker_logo.png")
        
        # App banner
        self.img_Speed_Tracker_Banner = tk.PhotoImage(file="./res/image/Speed_Tracker_Banner.png")









        #######################
        #    STYLING WIDGETS  #
        #######################
        
        
 


        #######################
        #     READING DATA    #
        #     FROM CONFIG     #
        #######################

        
        # SPEED SETTINGS
        
        # Upload Speed Entry
        _upload_ = self.load_dashboard_settings.get_upload()
        self.UploadSpeedEntry["state"] = "normal"
        self.UploadSpeedEntry.delete("0", "end")
        self.UploadSpeedEntry.insert("0", _upload_)
        self.UploadSpeedEntry["state"] = "disabled"
        
        # Download Speed Entry
        _download_ = self.load_dashboard_settings.get_download()
        self.DownloadSpeedEntry["state"] = "normal"
        self.DownloadSpeedEntry.delete("0", "end")
        self.DownloadSpeedEntry.insert("0", _download_)
        self.DownloadSpeedEntry["state"] = "disabled"
        
        # Recipient Email Entry
        _recipient_ = self.load_dashboard_settings.get_recipient_email()
        self.RecipientEmailEntry["state"] = "normal"
        self.RecipientEmailEntry.delete("0", "end")
        self.RecipientEmailEntry.insert("0", _recipient_)
        self.RecipientEmailEntry["state"] = "disabled"

        # Modem Location Entry
        _location_ = self.load_dashboard_settings.get_modem_loc()
        self.ModemLocationEntry["state"] = "normal"
        self.ModemLocationEntry.delete("0", "end")
        self.ModemLocationEntry.insert("0", _location_)
        self.ModemLocationEntry["state"] = "disabled"






        # EMAIL SENDER
        _sender_ = self.load_dashboard_settings.get_sender_email()
        self.EmailSenderEntry["state"] = "normal"
        self.EmailSenderEntry.delete("0", "end")
        self.EmailSenderEntry.insert("0", _sender_)
        self.EmailSenderEntry["state"] = "disabled"      



            
        _password_ = self.load_dashboard_settings.get_password()
        self.PasswordEntry["state"] = "normal"
        self.PasswordEntry.delete("0", "end")
        self.PasswordEntry.insert("0", _password_)
        self.PasswordEntry["state"] = "disabled"


        _port_ = self.load_dashboard_settings.get_port()
        self.ServerPortCombobox.set(_port_)
        
        _server_ = self.load_dashboard_settings.get_server()
        self.ServerCombobox.set(_server_)







        #######################
        #     CONFIGURING     #
        #     ALL WIDGETS     #
        #######################

        # Toplevel
        self.DashboardToplevel.title("Dashboard")
        self.DashboardToplevel.geometry("585x530+355+100")
        # App logo
        self.DashboardToplevel.iconphoto(True, self.img_Speed_Tracker_logo)
        self.DashboardToplevel.configure(height=600, width=585)
        self.DashboardToplevel.resizable(False, False)
        
        # Main Frame
        
        # Banner Frame
        # App banner
        self.BannerLabel.configure(image=self.img_Speed_Tracker_Banner)

        # Form Frame
        
        
        # Speed Settings Label Frame
        self.SpeedLabelframe.configure(height=260, text="Speed Settings", width=580)
        
        
        
        
        self.UploadSpeedLabel.configure(text="Upload Speed in MB:")
        self.DownloadSpeedLabel.configure(text="Download Speed in MB:")
        self.ModemLocationLabel.configure(text="Modem Location:")
        self.RecipientEmailLabel.configure(text="Email Address:")
        

        self.UploadSpeedEntry.configure(state="disabled")
        self.DownloadSpeedEntry.configure(state="disabled")
        self.RecipientEmailEntry.configure(state="disabled")
        self.ModemLocationEntry.configure(state="disabled")
        
        self.speed_settings_value = tk.BooleanVar()
        self.EditSpeedSettingsCheckbutton.configure(
            cursor="hand2", text="Edit speed?", variable=self.speed_settings_value,
            command=self.edit_speed_settings
        )
        
        
        
        # Email Sender Label Frame
        self.EmailSenderLabelframe.configure(height=120, text="Email Sender", width=580)
        
        
        self.EmailSenderLabel.configure(text="Email Address:")
        self.EmailSenderEntry.configure(state="disabled")
        
        self.PasswordLabel.configure(text="Password:")
        self.PasswordEntry.configure(show="*", state="disabled")
        
        
        _server_port_value = secure_servers.get_ports()
        self.ServerPortLabel.configure(text="Port:")
        self.ServerPortCombobox.configure(
            state="disabled", values=_server_port_value, width=9
        )
        
        _server_value = secure_servers.get_servers()
        self.SelectServerLabel.configure(text="Server:")
        self.ServerCombobox.configure(
            state="disabled", values=_server_value, width=15
        )
        
        # Check button for editing sender email
        self.email_sender_value = tk.BooleanVar()
        self.EditSenderEmailCheckbutton.configure(
            cursor="hand2", text="Edit email?", variable=self.email_sender_value,command=self.edit_email_sender
        )

        
        
        # Control Frame
        self.ControlFrame.configure(height=60, width=585)
        self.VersionLabel.configure(text="V0.1.2")
        self.SaveBtn.configure(state="disabled", text="S A V E", command=self.save_settings)
        self.CloseBtn.configure(cursor="hand2", text="C L O S E",command=self.close_dashboard)
















        #######################
        # PACKING AND PLACING #
        #     ALL WIDGETS     #
        #######################


        # Main body
        self.MainFrame.pack(side="top")

        # Section 1
        self.BannerFrame.pack(side="top")
        self.BannerLabel.pack(side="top")
        
        
        # Section 2
        self.FormFrame.pack(side="top")

        # Section 2: 1
        self.SpeedLabelframe.pack(side="top")
        self.DownloadSpeedLabel.place(anchor="nw", relx=0.62, rely=0.13, x=0, y=0)
        self.UploadSpeedLabel.place(anchor="nw", relx=0.14, rely=0.13, x=0, y=0)
        self.ModemLocationLabel.place(anchor="nw", relx=0.62, rely=0.50, x=0, y=0)
        self.RecipientEmailLabel.place(anchor="nw", relx=0.14, rely=0.50, x=0, y=0)
        self.UploadSpeedEntry.place(anchor="nw", relx=0.14, rely=0.25, x=0, y=0)
        self.DownloadSpeedEntry.place(anchor="nw", relx=0.62, rely=0.25, x=0, y=0)
        self.ModemLocationEntry.place(anchor="nw", relx=0.62, rely=0.62, x=0, y=0)
        self.RecipientEmailEntry.place(anchor="nw", relx=0.14, rely=0.62, x=0, y=0)
        self.EditSpeedSettingsCheckbutton.place(
            anchor="nw", relx=0.14, rely=0.88, x=0, y=0
        )
        
        # Section 2: 2
        self.EmailSenderLabelframe.pack(side="top")
        self.EmailSenderLabel.place(anchor="nw", relx=0.01, rely=0.1, x=0, y=0)
        self.EmailSenderEntry.place(anchor="nw", relx=0.01, rely=0.31, x=0, y=0)
        self.PasswordLabel.place(anchor="nw", relx=0.30, rely=0.08, x=0, y=0)
        self.PasswordEntry.place(anchor="nw", relx=0.30, rely=0.31, x=0, y=0)
        self.ServerPortLabel.place(anchor="nw", relx=0.60, rely=0.08, x=0, y=0)
        self.SelectServerLabel.place(anchor="nw", relx=0.79, rely=0.08, x=0, y=0)
        self.ServerCombobox.place(anchor="nw", relx=0.79, rely=0.29, x=0, y=0)
        self.ServerPortCombobox.place(anchor="nw", relx=0.6, rely=0.29, x=0, y=0)
        self.EditSenderEmailCheckbutton.place(
            anchor="nw", relx=0.01, rely=0.7, x=0, y=0
        )
        
        # Section 3
        self.ControlFrame.pack(side="top")
        self.VersionLabel.place(anchor="nw", relx=0.02, rely=0.36, x=0, y=0)
        self.SaveBtn.place(relx=0.62, rely=0.23, width=100, x=0, y=0)
        self.CloseBtn.place(anchor="nw", relx=0.81, rely=0.23, width=100, x=0, y=0)



        # Launching the toplevel window
        self.mainwindow = self.DashboardToplevel
  
  
  
  
  
#######################
#   BUSINESS LOGICS   #
#######################



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
            if not self.email_sender_value.get():
                # Disabling the save button 
                self.SaveBtn.configure(state='disable', cursor='arrow')
                



    def edit_email_sender(self):
        """
        Enable the sender's email and password entry widgets
        if the check button is selected.
        
        Otherwise disable them.
        """
        if self.email_sender_value.get():
            # Enabling the Email  and Password entry
            self.EmailSenderEntry.configure(state='normal')
            self.PasswordEntry.configure(state='normal')
            # Show the password
            self.PasswordEntry.configure(show='')
            

            # Enabling the save button and Combobox
            self.SaveBtn.configure(state='normal', cursor='hand2')
    
            self.ServerPortCombobox.configure(state='normal', cursor='hand2')
            self.ServerCombobox.configure(state='normal', cursor='hand2')
                
 
        else:
            # Enabling the Email  and Password entry
            self.EmailSenderEntry.configure(state='disable')
            self.PasswordEntry.configure(state='disable')
            # Hide the password
            self.PasswordEntry.configure(show='*')
            

            # Disabling the save button 
            self.SaveBtn.configure(state='disable', cursor='arrow')
            self.ServerPortCombobox.configure(state='disable', cursor='arrow')
            self.ServerCombobox.configure(state='disable', cursor='arrow')





    def is_speed_valid(self) -> bool:
            """
            Check if the entries are valid for the speed settings,
            and also check if all entries for both settings contains data. 

            Returns:
                bool: returns true if all conditions are met, else false.
            """
            
            upload_speed = self.UploadSpeedEntry.get()
            download_speed = self.DownloadSpeedEntry.get()
            recipient = self.RecipientEmailEntry.get()
            modem_loc = self.ModemLocationEntry.get()
            sender = self.EmailSenderEntry.get()
            sender_pwd = self.PasswordEntry.get()
            port = self.ServerPortCombobox.get()
            server_port = self.ServerCombobox.get()
            
            
            all_entries = [upload_speed, 
                           download_speed,
                           recipient, 
                           modem_loc, 
                           sender,sender_pwd,
                           port, server_port] 
            
            # Checking if all entries contains data
            have_data = True
            for entry in all_entries:
                if len(entry) == 0:
                    have_data = False
            if not have_data:
                messagebox.showwarning('Empty entry', 'Please fill in all the entries.')            
                return False
        
            # Check if both speed entries contains letters
            letter_is_in = False
            for char in upload_speed + download_speed:
                if char not in digits:
                    letter_is_in = True
            
            if letter_is_in:
                messagebox.showwarning('Digits only','Both speeds should only contain digits.')
                return False
            
            if len(upload_speed) > self.max_char_for_speed or len(download_speed) > self.max_char_for_speed:
                messagebox.showwarning('Max length','The speed should contain no more than 3 digits.')
                return False
            # else
            return True 


    
    
    def is_both_email_valid(self) -> bool:
        """
        Check if both recipient and sender email is valid.

        Returns:
            bool: if both are valid return true else false
        """
        
        both_valid = True 
        
        sender = self.EmailSenderEntry.get()
        recipient = self.RecipientEmailEntry.get()
        
        # Checking the recipient email
        if not is_email_valid(recipient):
            messagebox.showwarning('Recipient Email','Please use a valid email address.')
            return False
        
        # Checking the senders email
        if not is_email_valid(sender):
            messagebox.showwarning('Email Sender','Please use a valid email address along\nwith the appropriate port and server.')
            return False
            
            
        if both_valid:
            return True
    



    def save_settings(self):
        """
        Save the data from each entry
        """
        # Getting both email to check if they are valid
       
        if self.is_speed_valid() and self.is_both_email_valid():
                # Unhide config file and folder
                system(f'attrib -h {config_file_path}')
                # system(f'attrib -h {MASTER_KEY_FILE}')
                # Uncheck combobox
                if self.email_sender_value:
                    self.email_sender_value.set(False)
                    # Disable entries for the Email sender settings
                    self.EmailSenderEntry.configure(state="disabled")
                    self.PasswordEntry.configure(show="*", state="disabled")
                    self.ServerPortCombobox.configure(state="disabled")
                    self.ServerCombobox.configure(state="disabled")
                    # Then saving the data
                    self.update_dashboard_settings.set_sender_email(self.EmailSenderEntry.get())
                    self.update_dashboard_settings.set_port(self.ServerPortCombobox.get())
                    self.update_dashboard_settings.set_server(self.ServerCombobox.get())
                    
                    
                    # Checking if dashboard is been used for the first time
                    # first_time = self.load_dashboard_settings.get_status()
                    # if first_time:
                    #     # create a new encryption key
                    #     create_key()
                    #     print('First time using app')
                    #     # update the status
                    #     self.update_dashboard_settings.set_status()
                    # # Encrypting the password before storing
                    # secure_pwd = str(encrypt_password(read_key(), self.PasswordEntry.get()))
                    # self.update_dashboard_settings.set_password(secure_pwd)
                    
                    new_pwd =  self.PasswordEntry.get()
                    self.update_dashboard_settings.set_password(new_pwd)
                    
                    
                    # Disabling the save button
                    if not self.speed_settings_value:
                        self.SaveBtn.configure(state='disable', cursor='arrow')
                        
                    
                    
                if self.speed_settings_value:
                    # Uncheck combobox
                    self.speed_settings_value.set(False)
                    # Disable entries for the Email sender settings
                    self.UploadSpeedEntry.configure(state="disabled")
                    self.DownloadSpeedEntry.configure(state="disabled")
                    self.RecipientEmailEntry.configure(state="disabled")            
                    self.ModemLocationEntry.configure(state="disabled")
                    # Then saving the data
                    self.update_dashboard_settings.set_upload(self.UploadSpeedEntry.get())
                    self.update_dashboard_settings.set_download(self.DownloadSpeedEntry.get())
                    self.update_dashboard_settings.set_recipient_email(self.RecipientEmailEntry.get())
                    self.update_dashboard_settings.set_modem_loc(self.ModemLocationEntry.get())
                    # Disabling the save button
                    if not self.email_sender_value:
                        self.SaveBtn.configure(state='disable', cursor='arrow')
                    
                messagebox.showinfo('Settings Saved', 'The new settings was saved successfully.')
                
                # Load in the newly stored data
            
                # get_new_pwd = self.load_dashboard_settings
                # _password_ = get_new_pwd.get_password()
                # # pwd = decrypt_password(read_key(), _password_)
                # self.PasswordEntry["state"] = "normal"
                # self.PasswordEntry.delete("0", "end")
                # self.PasswordEntry.insert("0", _password_)
                # self.PasswordEntry["state"] = "disabled"

                # Hiding config folder and file
                system(f'attrib +h {config_file_path}')
                # system(f'attrib +h {MASTER_KEY_FILE}')
                    





    def close_dashboard(self):
        """
        Confirm if the user want to close the dashboard.
        """
        if messagebox.askyesno('Close Dashboard', 'Are you sure you want to close the dashboard?'):
            self.DashboardToplevel.destroy()




if __name__ == "__main__":
    app = DashboardApp()
    app.run()


# TODO:
# -[x] Validate the data before saving.
# -[x] disable all entries after the data was update.
# -[x] Show a pop dialog that the entries was save.
# -[x] Hide the config file and folder.
# -[x] Encrypt the password before saving to config.
# -[x] Check if the app is been used for the first time then load in the un encrypted password.
# -[V] Remove feature to Encrypt the password before saving to config.
# -[] Insert the newly stored data into the entry.


# BUG:
# -[x] if the speed settings check button is marked tick and i try to also tick the sender email check button
# -[x] fix File not found - ./res/config/master.key