#!/usr/bin/env python3
import re
import sys

def whisper_regex():
    """
    The Regex Whisperer - Because regex should whisper sweet nothings, not scream errors.
    """
    print("\n🔮 Regex Whisperer - I speak fluent regex (unlike you)\n")
    
    # Get user input with gentle encouragement
    text = input("Paste the text you're trying to match (or type 'quit' to escape this madness): ")
    if text.lower() == 'quit':
        print("\n🏃 Wise choice. Sometimes running away IS the solution.")
        return
    
    pattern = input("\nWhat pattern are you trying? (Be honest, I won't judge... much): ")
    
    try:
        # The magic happens here (or fails spectacularly)
        matches = re.findall(pattern, text)
        
        if matches:
            print(f"\n🎉 Found {len(matches)} match(es):")
            for i, match in enumerate(matches, 1):
                print(f"  {i}. {match}")
            
            # Show what actually matched in context
            print(f"\n📝 Full matches in context:")
            for match in re.finditer(pattern, text):
                start = max(0, match.start() - 20)
                end = min(len(text), match.end() + 20)
                context = text[start:end]
                print(f"   ...{context}...")
        else:
            print("\n😶 No matches found. Maybe your regex is ghosting you?")
            
            # Offer a terrible suggestion (because why not)
            if '.*' not in pattern:
                print(f"   Try adding '.*' somewhere. Can't hurt, right? (It probably will)")
            
    except re.error as e:
        print(f"\n💥 Regex error: {e}")
        print("   Your regex is broken. Like my will to live after debugging this.")
    except Exception as e:
        print(f"\n🤯 Unexpected error: {e}")
        print("   The universe is collapsing. Or maybe just your regex.")
    
    print("\n" + "="*50)
    print("Remember: Regex is just someone's bad day, frozen in code forever.")
    print("="*50)

if __name__ == "__main__":
    # Because one loop is never enough for regex debugging
    while True:
        whisper_regex()
        again = input("\nTry another? (yes/no): ").lower()
        if again not in ['yes', 'y']:
            print("\n👋 Farewell. May your regexes be ever in your favor.")
            break
