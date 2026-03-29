import matplotlib.pyplot as plt
import numpy as np

try:
    print("\n========== Beam Deflection Calculator ==========")

    print("1. Point Load (center)")
    print("2. Uniform Load (UDL)")

    choice = int(input("Choose load type: "))

    L = float(input("Length (m): "))
    E = float(input("Young's Modulus (Pa): "))
    I = float(input("Moment of Inertia (m^4): "))

    if choice == 1:
        P = float(input("Load (N): "))
        deflection = (P * L**3) / (48 * E * I)

    elif choice == 2:
        w = float(input("Load per meter (N/m): "))
        deflection = (5 * w * L**4) / (384 * E * I)

    else:
        print("Invalid choice")
        exit()

    # Convert to mm
    deflection_mm = deflection * 1000

    print(f"\n📊 Maximum Deflection = {deflection:.6f} m")
    print(f"📊 Maximum Deflection = {deflection_mm:.3f} mm")

    # Graph
    x = np.linspace(0, L, 100)
    y = deflection * np.sin(np.pi * x / L)

    plt.plot(x, y)
    plt.title("Beam Deflection Curve")
    plt.xlabel("Length (m)")
    plt.ylabel("Deflection (m)")
    plt.grid()

    plt.show()

except:
    print("Invalid input! Please enter numbers only.")
    
