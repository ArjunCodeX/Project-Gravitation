import turtle
import math

# 1. User Interface: Setting constants for the simulation
print("--- PROJECT GRAVITATION: MISSION PREP ---")
# Pro-tip: 1000 GS and 2.0 Velocity creates a near-perfect circle at distance 250
g_strength = float(input("Enter Gravity Strength (Try 1000): "))
p_distance = float(input("Enter starting height of probe (Use upto 599): "))
v_launch = float(input("Enter Launch Velocity (Try 2.0 for orbit if GS is 1000 and d is 250): "))

# 2. Setup the "Cosmos" (Environment)
screen = turtle.Screen()
screen.setup(width=800, height=600) # Fixed size to show the full orbit
screen.bgcolor("#1C1C26")
screen.tracer(0) 
screen.title("Project Gravitation: Orbital Simulator")

# 3. Create Planet 
earth = turtle.Turtle()
earth.shape("circle")
earth.color("#00CCFF")
earth.shapesize(3) 

# 4. Create the Probe (Astra/Shard)
probe = turtle.Turtle()
probe.shape("triangle") # Represents the sharp edge of the shard
probe.color("grey")
probe.penup()
probe.goto(0, p_distance) 
probe.pendown()

# 5. Velocity Vectors
vx = v_launch
vy = 0 

# 6. The Physics Engine
while True:
    # A. Determine distance using Pythagoras
    rx = probe.xcor()
    ry = probe.ycor()
    distance = math.sqrt(rx**2 + ry**2)

    # B. Collision Detection
    if distance < 35:
        print("MISSION FAILURE: Impact with the Absolute.")
        break

    # C. Gravity Calculation (F = G / r^2)
    force = g_strength / (distance**2)

    # D. Vector Decomposition (Ensures pull is always toward center)
    accel_x = -force * (rx / distance)
    accel_y = -force * (ry / distance)

    # E. Integration (Updating motion)
    vx += accel_x
    vy += accel_y
    probe.goto(rx + vx, ry + vy)

    screen.update()

    # F. Escape Velocity check
    if distance > 1000:
        print("MISSION ENDED: Probe escaped into deep space.")
        break

screen.mainloop()