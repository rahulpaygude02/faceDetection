import tkinter as tk
from tkinter import *
import argparse
import tkinter.font as font

from collect_data_images.collect_images import Datacollector

class RegistrationModule:

    def __init__(self,logFileName):

        self.logFileName = logFileName
        self.window = tk.Tk()
        self.window.title('Face Recognition')

        # this removes the maximize button
        self.window.resizable(0, 0)

        window_height = 600
        window_width = 880

        
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        #This method is used to set the dimensions of the Tkinter window and is used to set the position of the main window on the user’s desktop.

        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        self.window.configure(background='white')

        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        header = tk.Label(self.window, text="Employee Monitoring Registration", width=80, height=2, fg="white", bg="#363e75",
                          font=('times', 18, 'bold', 'underline'))
        
        header.place(x=0,y=0)

        clientID = tk.Label(self.window, text="Client ID", width=10, height=2, fg="white", bg="#363e75", font=('times', 15))
        clientID.place(x=80, y=80)

        displayVariable = StringVar()
        self.clientIDTxt = tk.Entry(self.window, width=20, text=displayVariable, bg="white", fg="black",
                               font=('times', 15, 'bold'))
        self.clientIDTxt.place(x=205, y=80)

        empID = tk.Label(self.window, text="EmpID", width=10, fg="white", bg="#363e75", height=2, font=('times', 15))
        empID.place(x=450, y=80)

        self.empIDTxt = tk.Entry(self.window, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
        self.empIDTxt.place(x=575, y=80)

        empName = tk.Label(self.window, text="Emp Name", width=10, fg="white", bg="#363e75", height=2, font=('times', 15))
        empName.place(x=80, y=140)

        self.empNameTxt = tk.Entry(self.window, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
        self.empNameTxt.place(x=205, y=140)

        emailId = tk.Label(self.window, text="Email ID :", width=10, fg="white", bg="#363e75", height=2, font=('times', 15))
        emailId.place(x=450, y=140)

        self.emailIDTxt = tk.Entry(self.window, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
        self.emailIDTxt.place(x=575, y=140)

        mobileNo = tk.Label(self.window, text="Mobile No :", width=10, fg="white", bg="#363e75", height=2,
                            font=('times', 15))
        mobileNo.place(x=450, y=140)

        self.mobileNoTxt = tk.Entry(self.window, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
        self.mobileNoTxt.place(x=575, y=140)

        notify = tk.Label(self.window, text="Notification : ", width=15, fg="white", bg="#363e75", height=2,
                        font=('times', 15))
        notify.place(x=80, y=260)

        self.message = tk.Label(self.window, text="", bg="white", fg="black", width=30, height=1,
                                activebackground="#e47911", font=('times', 15))
        self.message.place(x=220, y=220)
        
        takeImg = tk.Button(self.window, text="Take Images", command=self.collectUserImageForRegistration, fg="white", bg="#363e75", width=15,
                            height=2,
                            activebackground="#118ce1", font=('times', 15, ' bold '))
        takeImg.place(x=80, y=350)

        self.window.mainloop()


    def collectUserImageForRegistration(self):
        clientIDVal = (self.clientIDTxt.get())
        empIDVal = self.empIDTxt.get()
        name = (self.empNameTxt.get())
        ap = argparse.ArgumentParser()

        ap.add_argument("--faces", default=50,
                            help="Number of faces that camera will get")
        ap.add_argument("--output", default="../datasets/train/" + name,
                            help="Path to faces output")
        args = vars(ap.parse_args())

        trnngDataCollctrObj = Datacollector(args)
        trnngDataCollctrObj.collectImagesFromCamera()

        notifctn = "We have collected " + str(args["faces"]) + " images for training."
        self.message.configure(text=notifctn)
        
            


logFileName = "ProceduralLog.txt"
regStrtnModule = RegistrationModule(logFileName)