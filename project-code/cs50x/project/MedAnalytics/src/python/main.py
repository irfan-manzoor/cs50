import subprocess  # For running the C program
import pandas as pd  # For handling and processing CSV data
from tkinter import *  # For creating the GUI interface
from tkinter import filedialog, messagebox  # For file dialog and message box functionalities
import matplotlib.pyplot as plt  # For plotting visualizations
from sklearn.linear_model import LinearRegression  # For performing linear regression forecasting
import os  # For file and directory handling

# GUI setup: Function to open a file dialog and get the file path
def open_file():
    filepath = filedialog.askopenfilename()  # Open a file dialog to choose the CSV file
    if filepath:  # If a file is selected
        process_data(filepath)  # Pass the file path to process the data

# Function to process the CSV data (read, analyze, visualize, save results)
def process_data(filepath):
    # Read data from the selected CSV file using pandas
    data = pd.read_csv(filepath)

    # Calculate averages of the health parameters
    avg_heart_rate = data['heart_rate'].mean()  # Average heart rate
    avg_glucose = data['blood_glucose'].mean()  # Average blood glucose
    avg_temp = data['temperature'].mean()  # Average temperature (now in Fahrenheit)

    # Prepare the result string for showing and saving
    results = f"Averages:\nHeart Rate: {avg_heart_rate:.2f} bpm\nGlucose: {avg_glucose:.2f} mg/dL\nTemperature: {avg_temp:.2f}°F"
    
    # Show the averages in a message box to the user
    messagebox.showinfo("Results", results)

    # Ensure the 'reports' directory exists before saving the report
    if not os.path.exists('reports'):
        os.makedirs('reports')

    # Save the health report to a text file in the 'reports' directory
    with open("reports/health_report.txt", "w") as f:
        f.write(results)

    # Plot visualizations of the health data
    plot_visualizations(data)

    # Call the C program for further analysis, passing the file path
    run_c_program(filepath)

# Function to visualize the health data using matplotlib
def plot_visualizations(data):
    # Create a figure with 3 subplots for heart rate, blood glucose, and temperature
    fig, axs = plt.subplots(3, 1, figsize=(8, 10))
    
    # Plot heart rate data
    axs[0].plot(data['heart_rate'], color='red')
    axs[0].set_title('Heart Rate Over Time')  # Set the title for the subplot
    axs[0].set_ylabel('BPM')  # Label the y-axis for heart rate

    # Plot blood glucose data
    axs[1].plot(data['blood_glucose'], color='blue')
    axs[1].set_title('Blood Glucose Over Time')  # Set the title for the subplot
    axs[1].set_ylabel('mg/dL')  # Label the y-axis for blood glucose

    # Plot temperature data (now in Fahrenheit)
    axs[2].plot(data['temperature'], color='green')
    axs[2].set_title('Temperature Over Time')  # Set the title for the subplot
    axs[2].set_ylabel('°F')  # Label the y-axis for temperature
    axs[2].set_xlabel('Time')  # Label the x-axis for all plots

    # Adjust layout for better spacing between subplots
    plt.tight_layout()

    # Display the plots
    plt.show()

# Function to run the external C program for additional analysis
def run_c_program(filepath):
    # Locate the C program relative to the current file location
    c_program = os.path.join(os.path.dirname(__file__), '..', 'c_program', 'analysis_program')
    
    # Run the C program, passing the file path as an argument, and capture the output
    result = subprocess.run([c_program, filepath], capture_output=True, text=True)
    return result.stdout  # Return the output from the C program

# Function to forecast health trends using linear regression
def forecast_health():
    # Load sample data from CSV for forecasting
    data = pd.read_csv("data/data.csv")
    
    # Prepare the data for linear regression (X = time steps, Y = heart rate)
    X = data.index.values.reshape(-1, 1)  # Index values (time)
    Y = data['heart_rate'].values  # Heart rate values
    
    # Train the linear regression model using the time and heart rate data
    model = LinearRegression().fit(X, Y)
    
    # Predict future heart rate values based on the model
    predictions = model.predict(X)

    # Plot the actual heart rate values vs. the predicted (forecasted) values
    plt.plot(X, Y, label="Actual Heart Rate")
    plt.plot(X, predictions, label="Forecast")
    plt.legend()  # Add a legend to distinguish between actual and predicted values
    plt.title("Heart Rate Forecast")  # Set the title of the plot
    plt.savefig("visualization/health_trends.png")  # Save the forecast plot as an image
    plt.show()  # Display the plot

# Main GUI window setup
root = Tk()  # Create a new Tkinter window
root.title("MedAnalytics")  # Set the window title

# Button to open and process the CSV file, triggering open_file() when clicked
Button(root, text="Open CSV File", command=open_file).pack(pady=10)

# Button to forecast health trends, triggering forecast_health() when clicked
Button(root, text="Forecast Health", command=forecast_health).pack(pady=10)

# Start the Tkinter main loop to run the GUI
root.mainloop()
