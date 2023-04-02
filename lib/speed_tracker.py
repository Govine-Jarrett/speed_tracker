#!/usr/bin/python3
# 10/9/2022
# 7/2/2022
# Check your network speed and notify you via email if the network upload and download speeds are below the pre-defined speeds from the dashboard.

from tkinter import messagebox
import speedtest
from utils.readDashboardSettings import ReadDashboardSettings
from utils.convertBytes import convert_bytes


# Load dashboard settings
dashboard_settings = ReadDashboardSettings() 




upload_speed = dashboard_settings.get_upload()
download_speed = dashboard_settings.get_download()
recipient = dashboard_settings.get_recipient_email()
modem_loc = dashboard_settings.get_modem_loc()
sender = dashboard_settings.get_sender_email()
sender_pwd = dashboard_settings.get_password()
port = dashboard_settings.get_port()
server_port = dashboard_settings.get_server()



# Check if app is been used for the first time.
is_first = dashboard_settings.get_status()
if not is_first:
    # Start the process of tracking the network speed
    try:
        # THE BEST RESULTS
        s = speedtest.Speedtest()
        
        # USE TO DECIDE IF THE EMAIL SHOULD BE SENT
        is_best_results = True
            
            
    except Exception as error:
        # THIS WILL NOT GIVE THE BEST RESULTS BECAUSE WE ARE USING HTTPS
        s = speedtest.Speedtest(secure=True)
        
        is_best_results = False
        # FOR TESTING
        messagebox.showerror('SPEED TRACKER', error)
    
    finally:
        
        threads = 1
        s.get_servers()
        s.get_best_server()
        s.download(threads=threads)
        s.upload(threads=threads)
        s.results.share()
        results_dict = s.results.dict()
        
        
        
        
        
        
        
        # VIEWING THE DATA FROM RESULT
            
        us = convert_bytes(results_dict.get('upload'))
        ds = convert_bytes(results_dict.get('download'))
        ping = results_dict.get('ping')
        link = results_dict.get('share')
        
        test_results = [us, ds, ping, link]
        for result in test_results:
            print(result, end='\n')
        
        # Record the previous speed results in to a excel file
        # TODO: [] Write a function to create the excel file and a folder 
        # TODO: [] Write a function to store the new results in the create file 
       
        # Check if the speed is below the pre-define limits
            #TODO: [] Send the report to recipient's email   
            # Sending email
            if is_best_results:
                pass 

        # Keep track of the speed and when it was logged.






else:
    messagebox.showwarning('Speed Tracker','Please launch the dashboard app to configure the speed tracker.')















# # If you want to test against a specific server
# # servers = [1234]

# threads = None
# # If you want to use a single threaded test
# # threads = 1


# while True:
#     config_file_path = 'setting/speedTracker.ini'
#     app_settings = ConfigParser()
#     app_settings.read(config_file_path)

#     if environ_var_exists() and settings_exists():
#         email_provider = app_settings['DEFAULT']['emailProvider']
#         min_ds = app_settings['DEFAULT']['minDownloadSpeed']
#         min_us = app_settings['DEFAULT']['minUploadSpeed']
#         receiver_email = app_settings['DEFAULT']['receiverEmail']
#         modem_loc = app_settings['DEFAULT']['modemLocation']
#         print('PASS: evn and settings test')
        

#         s = speedtest.Speedtest()
#         s.get_servers(servers)
#         s.get_best_server()
#         s.download(threads=threads)
#         s.upload(threads=threads)
#         s.results.share()
#         results_dict = s.results.dict()
        
#         ds = convert_bytes(results_dict.get('download'))
#         us = convert_bytes(results_dict.get('upload'))
#         ping = results_dict.get('ping')
#         link = results_dict.get('share')
        
#         # print('PASS: speed test')
        
#         if email_is_valid(receiver_email, email_provider):
#             send_email(us, ds, ping, link, receiver_email, modem_loc)
#             # print('PASS: validate  and send email test')
#             break
#         else:
#             # print('PASS: email is not valid test')
#             # print('Go to setting and change the receiver email.')
#             break
#     else:
#         create_settings()      
#         # print('PASS: create settings test')


# TODO:
# -[] Link to the dashboard
# -[] Run the speedtest several time and find the average speed.
# -[] Log each time the test is run





















sample_data = {'download': 149760887.81690148, 'upload': 131314054.91164869, 'ping': 2.901, 'server': {'url': 'http://speedtest1.flowjamaica.com:8080/speedtest/upload.php', 'lat': '17.9683', 'lon': '-76.7827', 'name': 'Kingston', 'country': 'Jamaica', 'cc': 'JM', 'sponsor': 'FLOW Jamaica', 'id': '14260', 'host': 'speedtest1.flowjamaica.com:8080', 'd': 3.707838307522677, 'latency': 2.901}, 'timestamp': '2022-07-02T23:11:45.745337Z', 'bytes_sent': 151519232, 'bytes_received': 190362476, 'share': 'http://www.speedtest.net/result/13359052207.png', 'client': {'ip': '216.10.217.245', 'lat': '17.9962', 'lon': '-76.8019', 'isp': 'Flow', 'isprating': '3.7', 'rating': '0', 'ispdlavg': '0', 'ispulavg': '0', 'loggedin': '0', 'country': 'JM'}}


"""
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime, timedelta

# function to handle scheduling the task
def schedule_task():
    # get the task name and program path from the text fields
    task_name = task_entry.get()
    program_path = program_entry.get()
    start_time = start_time_entry.get()

    # check if the task already exists
    result = subprocess.run(["schtasks", "/query", "/tn", task_name], capture_output=True)
    if "Ready" in result.stdout.decode():
        # if the task is already active, ask the user if they want to change the time or cancel the task
        message_box_result = messagebox.askquestion("Task Already Exists", f"The task '{task_name}' is already scheduled. Do you want to change the start time?", icon='warning')
        if message_box_result == 'yes':
            # if the user wants to change the time, delete the existing task and schedule a new one
            subprocess.run(["schtasks", "/delete", "/tn", task_name, "/f"])
        else:
            # if the user does not want to change the time, do not schedule the task
            return

    # calculate the start time of the task
    try:
        start_time_dt = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        messagebox.showerror("Invalid Start Time", "Please enter a valid start time in the format 'YYYY-MM-DD HH:MM:SS'.")
        return

    now = datetime.now()
    if start_time_dt <= now:
        messagebox.showerror("Invalid Start Time", "Please enter a start time that is in the future.")
        return

    time_diff = start_time_dt - now
    start_delay = f"{time_diff.seconds // 60}M"

    # run the schtasks command to schedule the task
    try:
        subprocess.run(["schtasks", "/create", "/tn", task_name, "/tr", program_path, "/sc", "once", "/st", start_time, "/sd", start_time, "/ru", "System", "/it", "/f"])
        messagebox.showinfo("Task Scheduled", f"The task '{task_name}' has been scheduled to start at {start_time}.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error Scheduling Task", f"An error occurred while scheduling the task: {e.stderr.decode()}")

# function to open a file dialog to select a program
def select_program():
    # show the file dialog and get the path of the selected file
    program_path = filedialog.askopenfilename()

    # set the text of the program entry field to the selected program path
    program_entry.delete(0, tk.END)
    program_entry.insert(0, program_path)

# create the GUI
root = tk.Tk()

# create the task label and entry field
task_label = tk.Label(root, text="Task Name:")
task_entry = tk.Entry(root)
task_label.pack()
task_entry.pack()

# create the program label, entry field, and button to select a program
program_label = tk.Label(root, text="Program Path:")
program_entry = tk.Entry(root)
program_button = tk.Button(root, text="Select Program", command=select_program)
program_label.pack()
program_entry.pack()
program_button.pack()

"""

