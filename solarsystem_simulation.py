from vpython import *
import numpy as np
# Constants

G = 6.67e-11  # Gravitational constant
M_sun = 1.98e30  # Mass of the Sun
AU = 1.496e11  # 1 Astronomical Unit (Earth-Sun distance)
dt = 24 * 3600  # ✅ 1 day in seconds

# Create scene
scene = canvas(title="3D Solar System Simulation", width=800, height=600)

# Sun
sun = sphere(pos=vector(0, 0, 0), radius=6.955e9, color=color.yellow, emissive=True)

# Earth
earth = sphere(pos=vector(1.5e11, 0, 0), radius=6.378e9, color=color.blue, make_trail=True)
earth_velocity = vector(0, 29780, 0)  # Earth's orbital speed
M_earth = 5.972e24  # Mass of Earth

# Mars
mars = sphere(pos=vector(2.279e11, 0, 0), radius=3.389e6, color=color.red, make_trail=True)
mars_velocity = vector(0, 24070, 0)  # Mars' orbital speed
M_mars = 6.42e23  # Mass of Mars

# Gravity function
def gravity_force(body_pos, sun_pos, body_mass):
    r_vector = sun_pos - body_pos
    r_mag = mag(r_vector)

    if r_mag < 1e5:  # Prevent division by zero
        return vector(0, 0, 0)

    force_mag = (G * M_sun * body_mass) / (r_mag**2)
    force_dir = norm(r_vector)
    return force_dir * force_mag

# Simulation loop
while True:
    rate(100)

    # Earth updates
    F_gravity_earth = gravity_force(earth.pos, sun.pos, M_earth)
    earth_velocity += (F_gravity_earth / M_earth) * dt
    earth.pos += earth_velocity * dt

    # Mars updates
    F_gravity_mars = gravity_force(mars.pos, sun.pos, M_mars)
    mars_velocity += (F_gravity_mars / M_mars) * dt
    mars.pos += mars_velocity * dt
