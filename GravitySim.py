import turtle
import math
import time  # Added this so the 'sleep' function works

# 1. Collecting data
print("--- Gravity Simulator ---")
g1 = float(input("Input gravitational acceleration 1: "))
g2 = float(input("Input gravitational acceleration 2: "))
height = float(input("Input starting height (Try up to 250): "))

# 2. Setup the Environment
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#1C1C26")
screen.tracer(0) # This turns off animation for manual updating
screen.title("Gravity Simulator: Comparison Mode")

# 3. Setting up the ground
ground = turtle.Turtle()
ground.penup()
ground.goto(-400, -250)
ground.pendown()
ground.color("white")
ground.forward(800)
ground.hideturtle()

# 4. Creating the Probes 
probe_a = turtle.Turtle()
probe_a.shape("square")
probe_a.color("#00CCFF") 
probe_a.penup()
probe_a.goto(-150, height)

probe_b = turtle.Turtle()
probe_b.shape("square")
probe_b.color("#FF3366") 
probe_b.penup()
probe_b.goto(150, height)

# 5. Physics Variables
v1 = 0 
v2 = 0 
time_step = 0.01 

# 6. Dual-Fall Loop
print("Dropping both probes...")
while probe_a.ycor() > -250 or probe_b.ycor() > -250:
    
    # Update Probe A
    if probe_a.ycor() > -250:
        v1 += g1 * time_step
        new_y_a = probe_a.ycor() - v1
        if new_y_a < -250: new_y_a = -250
        probe_a.sety(new_y_a)
        
    # Update Probe B
    if probe_b.ycor() > -250:
        v2 += g2 * time_step
        new_y_b = probe_b.ycor() - v2
        if new_y_b < -250: new_y_b = -250
        probe_b.sety(new_y_b)
    
    screen.update() # This is CRUCIAL when you will use tracer for your codes! Yes you🫵 guy on GitHub
    time.sleep(0.01)

print("Mission Complete: All probes landed.")
screen.mainloop()