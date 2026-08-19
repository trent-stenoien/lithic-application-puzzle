# Application Puzzle

This was a puzzle hidden inside of the Technical Support Lead application. The Python script is in this repo. Before I dive into my process, I have to say this is a 

## Finding the puzzle

In my first attempts, I inspected the HTML, searching for keywords like "code" and "hidden", but I couldn't find any matches. Unsuccessful there, I tried highlighting the page itself to look for white-on-white text. The only hidden text I found this way was a prompt injection aimed at weeding out applicants who use AI to auto-fill applications without review. After more searching, I pasted the page's HTML into Claude and asked what I might be missing, which pointed me to the "problem-solving" link. Decoding that link's URL slug with a standard base64 decoder revealed the Python script in this repo.

## What does this script do?

1. The first line instructs the operating system to execute a Python script using the python3 interpreter the current $PATH environment variable. This is followed by a long comment with instructions for applicants like myself.
2. Next, we import dependencies:
   - argparse: Parses command-line arguments
   - hashlib: Provides hashing functions
   - os: Grants access to environment variables like `DONT_PANIC`
3. A password and key are defined as raw byte strings.
4. Two helper functions are defined:
   - `decrypt_password()`: Decodes the password and key combination.
   - `generate_proof()`: Takes in `candidate_name`, normalizes it, does an existence check, then converts/returns the name, answer, and "so-long-and-thanks" into a SHA-256 Cryptographic Hash, returning the first 12 hex characters as a "proof code".
5. In main():
   1. Ensure environment variable "DONT_PANIC" was set to 1, else throw an error.
   1. Instantiate the `argparse` parser and description.
   1. Add the `--candidate` as a parser argument.
   1. Parse arguments, decrypts password, and uses both to generate the proof code.
   1. Last, print out the variables we just defined.
   1. The final line of main() throws a debugging error if `result` does not equal 42.
6. In the last section, `if __name__ == "__main__"` ensures that this code won't run if imported as a module.

## My command and output

Command: 
```
DONT_PANIC=1 python3 puzzle.py --candidate "Trent Stenoien"
```

Output:
```
Decrypted password: 42
Candidate: Trent Stenoien
Proof code: 6d43b4a1d561
```

## Tools used

- **Claude:** Used minimally to help quickly search the HTML for the hidden code and as an extra layer of security to ensure the program was safe to run.
- **[Base64 decoder](https://www.base64decode.org/):** This translated the base64 string into Python code.
- **Google:** Since I haven't used much Python, I had to search for the dependencies and some functions to understand them better.
