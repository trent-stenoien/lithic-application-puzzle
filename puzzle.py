#!/usr/bin/env python3
"""
You found the hidden challenge. Nice.

This is part of the application process. The goal is not to prove that you can
do cryptography by hand. The goal is to show curiosity, follow-through, basic
technical fluency, and clear written communication.

What to do next:

1. Save this decoded file as:

      puzzle.py

2. Create a small public GitHub repository.

3. Add this file to the repository as:

      puzzle.py

4. Run the script from your terminal using your real name:

      DONT_PANIC=1 python3 puzzle.py --candidate "Your Name"

   Example:

      DONT_PANIC=1 python3 puzzle.py --candidate "Jane Applicant"

5. Add a README.md to your repository that includes:

   - A short explanation of how you found the hidden challenge
   - How you decoded the original string
   - What this script does
   - The command you ran
   - The exact output you received
   - The final decrypted answer
   - Any tools you used, including AI tools

6. Include the public GitHub repository link in your job application.

A strong submission is clear, honest, and easy to run. We do not care whether
you used AI, CyberChef, Python, Google, Stack Overflow, or another tool. We care
that you noticed the challenge, investigated it, and explained your process well.

Do not submit only the answer. Submit the GitHub repository.
"""

import argparse
import hashlib
import os


# The answer is encrypted with a tiny XOR.
# This is intentionally simple. The point is not advanced cryptography.
password = b"\xed\xc1"
_key = b"\xd9\xf3\xed\xfb\xa7\n\xb8\xfb<\xfbO^\xfb"


def decrypt_password() -> str:
    return bytes(a ^ b for a, b in zip(password, _key)).decode()


def generate_proof(candidate_name: str, answer: str) -> str:
    normalized_name = candidate_name.strip().lower()

    if not normalized_name:
        raise ValueError("Candidate name cannot be empty.")

    proof_input = f"{normalized_name}:{answer}:so-long-and-thanks"
    return hashlib.sha256(proof_input.encode("utf-8")).hexdigest()[:12]


def main() -> None:
    if os.getenv("DONT_PANIC") != "1":
        raise RuntimeError(
            "Set DONT_PANIC=1 and try again.\n\n"
            "Example:\n"
            '    DONT_PANIC=1 python3 puzzle.py --candidate "Your Name"'
        )

    parser = argparse.ArgumentParser(
        description=(
            "Decrypt the hidden answer and generate a "
            "candidate-specific proof code."
        )
    )
    parser.add_argument(
        "--candidate",
        required=True,
        help="Your full name, used to generate your proof code.",
    )

    args = parser.parse_args()

    result = decrypt_password()
    proof = generate_proof(args.candidate, result)

    print(f"Decrypted password: {result}")
    print(f"Candidate: {args.candidate}")
    print(f"Proof code: {proof}")

    assert result == "42", "Don't panic - but decryption failed!"


if __name__ == "__main__":
    main()
