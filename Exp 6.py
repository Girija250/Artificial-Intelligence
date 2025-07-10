def vacuum_cleaner():
    # Initial input
    location = input("Enter starting location (A or B): ").strip().upper()
    state = {
        'A': input("Enter status of Room A (Clean or Dirty): ").strip().capitalize(),
        'B': input("Enter status of Room B (Clean or Dirty): ").strip().capitalize()
    }

    print("\nInitial State:")
    print(f"Location: {location}")
    print(f"Room A: {state['A']}, Room B: {state['B']}")

    # Actions and transitions
    if state[location] == 'Dirty':
        print(f"Action: Suck at Room {location}")
        state[location] = 'Clean'

    if location == 'A':
        print("Action: Move Right to Room B")
        if state['B'] == 'Dirty':
            print("Action: Suck at Room B")
            state['B'] = 'Clean'
    else:
        print("Action: Move Left to Room A")
        if state['A'] == 'Dirty':
            print("Action: Suck at Room A")
            state['A'] = 'Clean'

    # Final state
    print("\nFinal State:")
    print(f"Room A: {state['A']}, Room B: {state['B']}")
    print("All rooms are clean!")

# Run the simulation
vacuum_cleaner()
