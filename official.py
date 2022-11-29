# UNEMPLOYMENT ANALYSIS IN INDIA (YEAR : 2020)

from tkinter import *
import seaborn as sns
from matplotlib import pyplot as plt
from pymongo import MongoClient
from PIL import ImageTk, Image

client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
UnemploymentCollection = db["Unemployment sample 1"]

allStates = []  # 2D list containing all the necessary details of every state - each state's values is a list
stateNames = UnemploymentCollection.distinct("Region")   # List of all state names

avg = []    # List containing the average unemployment rate for each state 
sum = 0
for i in range(len(stateNames)):
    results = UnemploymentCollection.find({"Region":stateNames[i]}) # To append into the all states list
    results1 = UnemploymentCollection.find({"Region":stateNames[i]})    # To find the average unemployment rate
    allStates.append(list(results))
    for result in results1:
        sum = sum + float(result[' Estimated Unemployment Rate (%)'])
    avg.append(sum/28)
    sum = 0

# Plotting the unemployment rate for India

def plot_country_avg(state, avg1):
    for i in range(len(state)):
        ax = sns.barplot(x=avg1, y=state)
        ax.set_xlabel('Estimated Unemployment Rate (%)')
        ax.set_ylabel('States')
    plt.show()

# Plotting the unemployment rate for each state
dates = []
unemployment = []
def plot_items_statewise(state):
    for i in range(len(state)):
        dates.append(state[i][' Date']) # x-axis for the graph of state-wise analysis
        unemployment.append(float(state[i][' Estimated Unemployment Rate (%)']))    # y-axis for the graph of state-wise analysis
    ax = sns.violinplot(x=dates, y=unemployment)
    ax.set_xlabel('Date of observation')
    ax.set_ylabel('Estimated Unemployment Rate (%)')
    plt.show() 

# To create another window displaying all the states
def displayStates():
    top = Toplevel()
    top.geometry("1600x900")
    global bg
    # Define image
    bg = ImageTk.PhotoImage(file="C:/Users/91978/Desktop/SEM - 2/UNEMPLOYMENT ANALYSIS IN INDIA/logos_images/unemployment_in_india.png")

    # Creating the label
    bg_label = Label(top, image=bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame1 = LabelFrame(top, text="Select from the following menu", padx=1, pady=1)
    frame1.place(relx=0.5, rely=0.5, anchor=CENTER)

    for i in range(14):
        button = Button(frame1, text=stateNames[i], width = 20, padx=20, pady=8, command=lambda:plot_items_statewise(allStates[i]), fg='white', bg='black').grid(row=i, column=4)
    for i in range(14, 28):
        button1 = Button(frame1, text=stateNames[i], width = 20, padx=20, pady=8, command=lambda:plot_items_statewise(allStates[i]), fg='white', bg='black').grid(row=i-14, column=14)

    back = Button(top, text="<<", padx=10, pady=8, command=top.destroy).grid(row=0, column=0)
    top.attributes('-fullscreen', True)
    top.bind("<Escape>", lambda event:top.destroy())

# Plotting the employment rate for each state
dates1 = []
employment = []
def plot_items_statewiseEmp(state):
    for i in range(len(state)):
        dates1.append(state[i][' Date']) # x-axis for the graph of state-wise analysis
        employment.append(float(state[i][' Estimated Employed']))    # y-axis for the graph of state-wise analysis
    ax = sns.boxenplot(x=dates1, y=employment)
    ax.set_xlabel('Date of observation')
    ax.set_ylabel('Estimated Employed')
    plt.show() 

# To create another window displaying all the states
def displayStates1():
    top1 = Toplevel()
    top1.geometry("1600x900")
    global bg
    # Define image
    bg = ImageTk.PhotoImage(file="C:/Users/91978/Desktop/SEM - 2/UNEMPLOYMENT ANALYSIS IN INDIA/logos_images/unemployment_in_india.png")

    # Creating the label
    bg_label = Label(top1, image=bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame2 = LabelFrame(top1, text="Select from the following menu", padx=1, pady=1)
    frame2.place(relx=0.5, rely=0.5, anchor=CENTER)

    for i in range(14):
        button = Button(frame2, text=stateNames[i], width = 20, padx=20, pady=8, command=lambda:plot_items_statewiseEmp(allStates[i]), fg='white', bg='black').grid(row=i, column=4)
    for i in range(14, 28):
        button1 = Button(frame2, text=stateNames[i], width = 20, padx=20, pady=8, command=lambda:plot_items_statewiseEmp(allStates[i]), fg='white', bg='black').grid(row=i-14, column=14)

    back = Button(top1, text="<<", padx=10, pady=8, command=top1.destroy).grid(row=0, column=0, sticky=SE)
    top1.attributes('-fullscreen', True)
    top1.bind("<Escape>", lambda event:top1.destroy())

# Plotting the estimated labour participation for each state

def plot_items_statewiseEstLabour(state):
    dates2 = [] # Labels - state-wise analysis
    estlabour = []
    for i in range(len(state)):
        dates2.append(state[i][' Date']) 
        estlabour.append(float(state[i][' Estimated Labour Participation Rate (%)']))    # y-axis for the graph of state-wise analysis
    ax = sns.barplot(x=dates2, y=estlabour)
    ax.set_xlabel('Date of observation')
    ax.set_ylabel('Estimated Labour Participation Rate (%)')
    plt.show() 

# To create another window displaying all the states
def displayStates2():
    top2 = Toplevel()
    top2.geometry("1600x900")
    global bg
    # Define image
    bg = ImageTk.PhotoImage(file="C:/Users/91978/Desktop/SEM - 2/UNEMPLOYMENT ANALYSIS IN INDIA/logos_images/unemployment_in_india.png")

    # Creating the label
    bg_label = Label(top2, image=bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame3 = LabelFrame(top2, text="Select from the following menu", padx=1, pady=1)
    frame3.place(relx=0.5, rely=0.5, anchor=CENTER)

    for i in range(14):
        button = Button(frame3, text=stateNames[i], width = 20, padx=20, pady=8, command=lambda:plot_items_statewiseEstLabour(allStates[i]), fg='white', bg='black').grid(row=i, column=4)
    for i in range(14, 28):
        button1 = Button(frame3, text=stateNames[i], width = 20, padx=20, pady=8, command=lambda:plot_items_statewiseEstLabour(allStates[i]), fg='white', bg='black').grid(row=i-14, column=14)

    back = Button(top2, text="<<", padx=10, pady=8, command=top2.destroy).grid(row=0, column=0)
    top2.attributes('-fullscreen', True)
    top2.bind("<Escape>", lambda event:top2.destroy())
 
root = Tk()
root.title("UNEMPLOYMENT ANALYSIS IN INDIA")
root.iconbitmap("C:\\Users\\91978\\Desktop\\SEM - 2\\UNEMPLOYMENT ANALYSIS IN INDIA\\logos_images\\psg logo.ico")
root.geometry("1200x800")

# Define image
background = ImageTk.PhotoImage(file="C:/Users/91978/Desktop/SEM - 2/UNEMPLOYMENT ANALYSIS IN INDIA/logos_images/unemployment.png")

# Create label
background_label = Label(root, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Creating a frame
frame = LabelFrame(root, text="Select from the following menu", padx=1, pady=1)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Creating buttons
myButton1 = Button(frame, text = "Unemployment Analysis in India for a year", padx=50, pady=10, command=lambda : plot_country_avg(stateNames, avg), fg = 'white', bg = 'black', width=50)
myButton2 = Button(frame, text = "Unemployment in a State for a year", padx=50, pady=10, command=displayStates, fg = 'white', bg = 'black', width=50)
myButton3 = Button(frame, text = "Estimated Employment", padx=50, pady=10, command=displayStates1, fg = 'white', bg = 'black', width=50)
myButton4 = Button(frame, text = "Estimated Labour Participation Rate for a state", padx=50, pady=10, command=displayStates2, fg = 'white', bg = 'black', width=50)

button_quit = Button(frame, text="Exit", command=root.destroy, bg="red")

myButton1.pack()
myButton2.pack()
myButton3.pack()
myButton4.pack()
button_quit.pack()

root.attributes('-fullscreen', True)

root.mainloop()