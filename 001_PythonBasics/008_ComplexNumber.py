import cmath

# Creating a complex number
z = 3 + 4j  # z = a + bj, where 'a' is the real part and 'b' is the imaginary part

# Displaying the complex number
print(f"Complex Number: {z}")

# Accessing the real and imaginary parts
real_part = z.real  # Real part of the complex number
imaginary_part = z.imag  # Imaginary part of the complex number
print(f"Real Part: {real_part}")
print(f"Imaginary Part: {imaginary_part}")

# Calculating the magnitude (modulus) of the complex number
magnitude = abs(z)  # Equivalent to sqrt(a^2 + b^2)
print(f"Magnitude: {magnitude}")

# Calculating the phase angle (in radians)
phase_angle = cmath.phase(z)  # Angle made with the positive real axis
print(f"Phase Angle (in radians): {phase_angle}")

# Converting to polar coordinates
polar_coordinates = cmath.polar(z)  # Returns (magnitude, phase_angle)
print(f"Polar Coordinates: {polar_coordinates}")

# Converting from polar to rectangular form
magnitude, phase = polar_coordinates
rectangular_form = cmath.rect(magnitude, phase)  # Converts back to a + bj form
print(f"Rectangular Form from Polar: {rectangular_form}")

# Adding, subtracting, multiplying, and dividing complex numbers
z1 = 1 + 2j
z2 = 2 - 3j

addition = z1 + z2
subtraction = z1 - z2
multiplication = z1 * z2
division = z1 / z2

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")

# Finding the conjugate of a complex number
conjugate = z.conjugate()  # Changes the sign of the imaginary part
print(f"Conjugate: {conjugate}")

# Using cmath functions for advanced operations
z_sqrt = cmath.sqrt(z)  # Square root of the complex number
z_exp = cmath.exp(z)  # Exponential of the complex number
z_log = cmath.log(z)  # Natural logarithm of the complex number

print(f"Square Root: {z_sqrt}")
print(f"Exponential: {z_exp}")
print(f"Natural Logarithm: {z_log}")

'''
Summary of Common Functions:
- abs(z): Magnitude of the complex number
- z.real, z.imag: Real and imaginary parts
- z.conjugate(): Conjugate of the complex number
- cmath.phase(z): Phase angle in radians
- cmath.polar(z): Converts to polar coordinates
- cmath.rect(r, phi): Converts polar to rectangular
- cmath.sqrt(z), cmath.exp(z), cmath.log(z): Advanced mathematical operations
'''