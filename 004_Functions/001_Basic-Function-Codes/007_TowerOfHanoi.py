def tower_of_hanoi(n, source, target, helper):

    """
    Solves the Tower of Hanoi problem.
    
    Parameters:
    n (int): Number of disks
    source (str): The name of the source rod
    target (str): The name of the target rod
    helper (str): The name of the helper rod
    """

    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
    # Move n-1 disks from source to helper
    tower_of_hanoi(n - 1, source, helper, target)

    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")

    # Move n-1 disks from helper to target
    tower_of_hanoi(n - 1, helper, target, source)


num_disks = 3
print("\n")
tower_of_hanoi(num_disks, 'A', 'C', 'B')
