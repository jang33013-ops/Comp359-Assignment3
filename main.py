
from prufer_decoder import decode_prufer, print_step_by_step

def main():
    print("Prüfer Code Decoder")
    print("Enter a Prüfer code as space-separated integers (e.g. 4 4 4 5):")
    
    user_input = input("Prüfer code: ").strip()
    if not user_input:
        print("No input provided. Exiting.")
        return
    
    try:
        code = list(map(int, user_input.split()))
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        return
    
    edges = decode_prufer(code)
    
    print("\nDecoded tree edges:")
    for u, v in edges:
        print(f"{u} -- {v}")
    
    print("\nStep-by-step decoding process:")
    print_step_by_step(code)

if __name__ == "__main__":
    main()
