# Calculates the conservation of momentum and kinetic energy

def conservation_of_momentum(m1, m2, v1, v2):
    """
    Calculates the conservation of momentum
    """
    return m1*v1 + m2*v2

def kinetic_energy(m, v):
    """
    Calculates the kinetic energy
    """
    return 0.5*m*v**2

def main():
    m1 = float(input("Enter the mass of the first object: "))
    m2 = float(input("Enter the mass of the second object: "))
    v1 = float(input("Enter the velocity of the first object: "))
    v2 = float(input("Enter the velocity of the second object: "))
    print("The conservation of momentum is", conservation_of_momentum(m1, m2, v1, v2))
    print("The kinetic energy is", kinetic_energy(m1, v1) + kinetic_energy(m2, v2))

if __name__ == "__main__":
    main()