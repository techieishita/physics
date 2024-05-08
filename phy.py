import tkinter as tk


# Define the functions for the physics formulas
def calculate_force():
    try:
        mass = float(entry_mass_force.get())
        acceleration = float(entry_acceleration_force.get())
        force = mass * acceleration
        label_force_result.config(text="Force = " + str(force))
    except ValueError:
        label_force_result.config(text="Please enter valid numbers.")

def calculate_velocity():
    try:
        initial_velocity = float(entry_initial_velocity_velocity.get())
        acceleration = float(entry_acceleration_velocity.get())
        time = float(entry_time_velocity.get())
        velocity = initial_velocity + acceleration * time
        label_velocity_result.config(text="Velocity = " + str(velocity))
    except ValueError:
        label_velocity_result.config(text="Please enter valid numbers.")

def calculate_displacement():
    try:
        initial_velocity = float(entry_initial_velocity.get())
        acceleration = float(entry_acceleration_2.get())
        time = float(entry_time_2.get())
        displacement = initial_velocity * time + 0.5 * acceleration * time**2
        label_displacement_result.config(text="Displacement = " + str(displacement))
    except ValueError:
        label_displacement_result.config(text="Please enter valid numbers.")

def calculate_energy():
    try:
        mass = float(entry_mass_2.get())
        velocity = float(entry_velocity.get())
        energy = 0.5 * mass * velocity**2
        label_energy_result.config(text="Energy = " + str(energy))
    except ValueError:
        label_energy_result.config(text="Please enter valid numbers.")

def calculate_power():
    try:
        work = float(entry_work_power.get())
        time = float(entry_time_power.get())
        power = work / time
        label_power_result.config(text="Power = " + str(power))
    except ValueError:
        label_power_result.config(text="Please enter valid numbers.")

       
# Create the main window
root = tk.Tk()
root.title("Physics Formulas")
# Disable window resizing
root.resizable(False, False)

# Add a physics theme to the GUI
root.config(bg="#1E1E1E")
title_label = tk.Label(root, text="")
title_label.grid(row=0, column=0, padx=10, pady=30)


# Create a heading label
heading_label = tk.Label(root, text="Physics Project", bg="#1E1E1E", fg="#FFFFFF", font=("Helvetica", 20))
heading_label.grid(row=0, column=0, padx=10, pady=10)

# Create a frame for each physics formula and its associated button and label
frame_force = tk.Frame(root, bg="#282828")
frame_force.grid(row=1, column=0, padx=10, pady=10)

label_force = tk.Label(frame_force, text=" Force Formula: F = m * a ", fg="#FFFFFF", bg="#585858", font=("Helvetica", 13))
label_force.pack(side=tk.LEFT)

label_mass_force = tk.Label(frame_force, text="  Mass: ", fg="#FFFFFF", bg="#282828", font=("Helvetica", 15))
label_mass_force.pack(side=tk.LEFT)
entry_mass_force = tk.Entry(frame_force,font=("Helvetica", 11))
entry_mass_force.pack(side=tk.LEFT)

label_acceleration_force = tk.Label(frame_force, text="  Acceleration:  ", fg="#FFFFFF", bg="#282828", font=("Helvetica", 15))
label_acceleration_force.pack(side=tk.LEFT)
entry_acceleration_force = tk.Entry(frame_force,font=("Helvetica", 11))
entry_acceleration_force.pack(side=tk.LEFT)



#------------------------------------------------------------------

frame_forcer = tk.Frame(root, bg="#282828")
frame_forcer.grid(row=2, column=0, padx=10, pady=10)




button_force = tk.Button(frame_forcer, text="Calculate Force", command=calculate_force)
button_force.configure(bg="#404040", fg="#FFFFFF", font=("Helvetica", 15))
button_force.pack(side=tk.LEFT)




label_force_result = tk.Label(frame_forcer, text="", fg="#FFFFFF", bg="#282828", font=("Helvetica", 15))
label_force_result.pack(side=tk.LEFT)
#______________________________________________________________________


frame_velocity = tk.Frame(root, bg="#282828")
frame_velocity.grid(row=3, column=0, padx=10, pady=10)

label_velocity = tk.Label(frame_velocity, text="Velocity Formula: V = Vi + a * t", fg="#FFFFFF", bg="#585858", font=("Helvetica", 13))
label_velocity.pack(side=tk.LEFT)

label_initial_velocity_velocity = tk.Label(frame_velocity, text=" Initial Velocity: ", fg="#FFFFFF", bg="#282828", font=("Helvetica", 15))
label_initial_velocity_velocity.pack(side=tk.LEFT)

entry_initial_velocity_velocity = tk.Entry(frame_velocity,font=("Helvetica", 11))
entry_initial_velocity_velocity.pack(side=tk.LEFT)

label_acceleration_velocity = tk.Label(frame_velocity, text=" Acceleration: ", fg="#FFFFFF", bg="#282828", font=("Helvetica", 15))
label_acceleration_velocity.pack(side=tk.LEFT)
entry_acceleration_velocity = tk.Entry(frame_velocity,font=("Helvetica", 11))
entry_acceleration_velocity.pack(side=tk.LEFT)

label_time_velocity = tk.Label(frame_velocity, text=" Time: ", fg="#FFFFFF", bg="#282828", font=("Helvetica", 15))
label_time_velocity.pack(side=tk.LEFT)
entry_time_velocity = tk.Entry(frame_velocity,font=("Helvetica", 11))
entry_time_velocity.pack(side=tk.LEFT)


frame_velocityr = tk.Frame(root, bg="#282828")
frame_velocityr.grid(row=4, column=0, padx=10, pady=10)

button_velocity = tk.Button(frame_velocityr, text="Calculate Velocity", command=calculate_velocity)
button_velocity.configure(bg="#404040", fg="#FFFFFF", font=("Helvetica", 15))
button_velocity.pack(side=tk.LEFT)

label_velocity_result = tk.Label(frame_velocityr, text="", fg="#FFFFFF", bg="#282828", font=("Helvetica", 15))
label_velocity_result.pack(side=tk.LEFT)

frame_displacement = tk.Frame(root, bg="#282828")
frame_displacement.grid(row=5, column=0, padx=10, pady=10)

label_displacement = tk.Label(frame_displacement, text=" Displacement Formula: D = Vi * t + 0.5 * a * t^2 ", fg="#FFFFFF", bg="#585858", font=("Helvetica", 13))
label_displacement.pack(side=tk.LEFT)
label_initial_velocity = tk.Label(frame_displacement, text=" Initial Velocity: ", fg="#FFFFFF", bg="#282828", font=("Helvetica", 15))
label_initial_velocity.pack(side=tk.LEFT)

entry_initial_velocity = tk.Entry(frame_displacement,font=("Helvetica", 11))
entry_initial_velocity.pack(side=tk.LEFT)
label_acceleration_2 = tk.Label(frame_displacement, text=" Acceleration: ", fg="#FFFFFF", bg="#282828", font=("Helvetica", 15))
label_acceleration_2.pack(side=tk.LEFT)
entry_acceleration_2 = tk.Entry(frame_displacement,font=("Helvetica", 11))
entry_acceleration_2.pack(side=tk.LEFT)
label_time_2 = tk.Label(frame_displacement, text=" Time: ", fg="#FFFFFF", bg="#282828", font=("Helvetica", 15))
label_time_2.pack(side=tk.LEFT)
entry_time_2 = tk.Entry(frame_displacement,font=("Helvetica", 11))
entry_time_2.pack(side=tk.LEFT)


frame_displacementr = tk.Frame(root, bg="#282828")
frame_displacementr.grid(row=6, column=0, padx=10, pady=10)

button_displacement = tk.Button(frame_displacementr, text="Calculate Displacement", command=calculate_displacement)
button_displacement.configure(bg="#404040", fg="#FFFFFF", font=("Helvetica", 15))
button_displacement.pack(side=tk.LEFT)

label_displacement_result = tk.Label(frame_displacementr, text="", fg="#FFFFFF", bg="#282828", font=("Helvetica", 15))
label_displacement_result.pack(side=tk.LEFT)

frame_energy = tk.Frame(root, bg="#282828")
frame_energy.grid(row=7, column=0, padx=10, pady=10)

label_energy = tk.Label(frame_energy, text=" Energy Formula: E = 0.5 * m * V^2 ", fg="#FFFFFF", bg="#585858", font=("Helvetica", 13))
label_energy.pack(side=tk.LEFT)
label_mass_2 = tk.Label(frame_energy, text=" Mass: ", fg="#FFFFFF", bg="#282828", font=("Helvetica", 15))
label_mass_2.pack(side=tk.LEFT)
entry_mass_2 = tk.Entry(frame_energy,font=("Helvetica", 11))
entry_mass_2.pack(side=tk.LEFT)

label_velocity = tk.Label(frame_energy, text=" Velocity: ", fg="#FFFFFF", bg="#282828", font=("Helvetica", 15))
label_velocity.pack(side=tk.LEFT)
entry_velocity = tk.Entry(frame_energy,font=("Helvetica", 11))
entry_velocity.pack(side=tk.LEFT)


frame_energyr = tk.Frame(root, bg="#282828")
frame_energyr.grid(row=8, column=0, padx=10, pady=10)

button_energy = tk.Button(frame_energyr, text="Calculate Energy", command=calculate_energy)
button_energy.configure(bg="#404040", fg="#FFFFFF", font=("Helvetica", 15))
button_energy.pack(side=tk.LEFT)

label_energy_result = tk.Label(frame_energyr, text="", fg="#FFFFFF", bg="#282828", font=("Helvetica", 15))
label_energy_result.pack(side=tk.LEFT)


frame_power = tk.Frame(root, bg="#282828")
frame_power.grid(row=9, column=0, padx=10, pady=10)

label_power = tk.Label(frame_power, text=" Power Formula: P = W / t ", fg="#FFFFFF", bg="#585858", font=("Helvetica", 13))
label_power.pack(side=tk.LEFT)

label_work_power = tk.Label(frame_power, text=" Work: ", fg="#FFFFFF", bg="#282828", font=("Helvetica", 15))
label_work_power.pack(side=tk.LEFT)
entry_work_power = tk.Entry(frame_power,font=("Helvetica", 11))
entry_work_power.pack(side=tk.LEFT)

label_time_power = tk.Label(frame_power, text=" Time: ", fg="#FFFFFF", bg="#282828", font=("Helvetica", 15))
label_time_power.pack(side=tk.LEFT)
entry_time_power = tk.Entry(frame_power,font=("Helvetica", 11))
entry_time_power.pack(side=tk.LEFT)


frame_powerr = tk.Frame(root, bg="#282828")
frame_powerr.grid(row=10, column=0, padx=10, pady=10)

button_power = tk.Button(frame_powerr, text="Calculate Power", command=calculate_power)
button_power.configure(bg="#404040", fg="#FFFFFF", font=("Helvetica", 15))
button_power.pack(side=tk.LEFT)

label_power_result = tk.Label(frame_powerr, text="", fg="#FFFFFF", bg="#282828", font=("Helvetica", 15))
label_power_result.pack(side=tk.LEFT)

# Create a Footer label
heading_label = tk.Label(root, text="By Vinisha Shukla, Class 8-F", bg="#1E1E1E", fg="#FFFFFF", font=("Helvetica", 13))
heading_label.grid(row=11, column=0, padx=10, pady=20)



# Set the size of the window
root.geometry("1500x700")

# Create a canvas to add the background image to
canvas = tk.Canvas(root, width=500, height=700,bg="#1E1E1E")
canvas.grid(row=0, column=1, rowspan=13, padx=0, pady=0)


# Add the background image
bg_img = tk.PhotoImage(file="bck4.png")
canvas.create_image(-50, 0, anchor=tk.NW, image=bg_img)



root.mainloop()
