#!/usr/bin/env python3
"""
RSA-Hacker Command Line Interface

A command-line tool for testing RSA cryptographic vulnerabilities.
"""

import sys
import argparse
import gmpy2
from attacks.attack_enum import AttackEnum
from attacks.defect_enum import DefectEnum
from attacks.single_key.solution import Solution


def print_banner():
    """Print the RSA-Hacker banner"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                      RSA-HACKER CLI                          ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(banner)


def list_attacks():
    """List all available attack methods"""
    print("\n[Available Attack Methods]")
    print("-" * 80)
    for attack in AttackEnum:
        print(f"  {attack.name:25s} - {attack.value}")
    print()


def list_defects():
    """List all known key defect types"""
    print("\n[Known Key Defect Types]")
    print("-" * 80)
    for defect in DefectEnum:
        print(f"  {defect.name:25s} - {defect.value}")
    print()


def auto_attack(n, e):
    """
    Automatically select and execute the best attack method

    Args:
        n: RSA modulus
        e: Public exponent

    Returns:
        Private key d if successful, None otherwise
    """
    print("\n[Auto Attack Mode]")
    print(f"Modulus N: {n}")
    print(f"Public Key e: {e}")
    print("\nAnalyzing key characteristics and selecting optimal attack...")

    solution = Solution()
    result = solution.attack(e, n)

    return result


def manual_attack(n, e, attack_name):
    """
    Execute a specific attack method

    Args:
        n: RSA modulus
        e: Public exponent
        attack_name: Name of the attack to use

    Returns:
        Private key d if successful, None otherwise
    """
    print("\n[Manual Attack Mode]")
    print(f"Modulus N: {n}")
    print(f"Public Key e: {e}")
    print(f"Attack Method: {attack_name}")
    print("\nExecuting attack...\n")

    try:
        attack_enum = AttackEnum[attack_name.upper()]
        attack = attack_enum.get_instance()
        result = attack.attack(e, n)
        return result
    except KeyError:
        print(f"Error: Unknown attack method '{attack_name}'")
        print("Use --list-attacks to see available methods")
        return None
    except Exception as ex:
        print(f"Attack failed: {str(ex)}")
        return None


def defect_attack(n, e, defect_name):
    """
    Execute attack based on key defect type

    Args:
        n: RSA modulus
        e: Public exponent
        defect_name: Name of the defect type

    Returns:
        Private key d if successful, None otherwise
    """
    print("\n[Defect-Based Attack Mode]")
    print(f"Modulus N: {n}")
    print(f"Public Key e: {e}")
    print(f"Defect Type: {defect_name}")
    print("\nExecuting attack...\n")

    try:
        defect_enum = DefectEnum[defect_name.upper()]
        attack = defect_enum.get_instance()
        result = attack.attack(e, n)
        return result
    except KeyError:
        print(f"Error: Unknown defect type '{defect_name}'")
        print("Use --list-defects to see available types")
        return None
    except Exception as ex:
        print(f"Attack failed: {str(ex)}")
        return None


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description='RSA-Hacker: Educational tool for testing RSA vulnerabilities',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Auto attack (recommended)
  %(prog)s -n 12345678901234567890 -e 65537

  # Use specific attack method
  %(prog)s -n 12345678901234567890 -e 65537 --attack wiener

  # Use defect-based attack
  %(prog)s -n 12345678901234567890 -e 65537 --defect small_e

  # List available methods
  %(prog)s --list-attacks
  %(prog)s --list-defects
        """
    )

    # Main arguments
    parser.add_argument('-n', '--modulus', type=str,
                        help='RSA modulus N')
    parser.add_argument('-e', '--exponent', type=str,
                        help='Public exponent e')

    # Attack methods
    parser.add_argument('--attack', type=str,
                        help='Specific attack method to use')
    parser.add_argument('--defect', type=str,
                        help='Key defect type to exploit')

    # Information
    parser.add_argument('--list-attacks', action='store_true',
                        help='List all available attack methods')
    parser.add_argument('--list-defects', action='store_true',
                        help='List all known key defect types')
    parser.add_argument('--version', action='version', version='RSA-Hacker CLI v1.0')

    args = parser.parse_args()

    # Show banner
    print_banner()

    # Handle list options
    if args.list_attacks:
        list_attacks()
        return 0

    if args.list_defects:
        list_defects()
        return 0

    # Validate required arguments
    if not args.modulus or not args.exponent:
        print("Error: Both --modulus (-n) and --exponent (-e) are required for attacks\n")
        parser.print_help()
        return 1

    # Convert to gmpy2 integers
    try:
        n = gmpy2.mpz(args.modulus)
        e = gmpy2.mpz(args.exponent)
    except Exception as ex:
        print(f"Error: Invalid number format - {str(ex)}")
        return 1

    # Execute attack
    result = None

    if args.attack:
        result = manual_attack(n, e, args.attack)
    elif args.defect:
        result = defect_attack(n, e, args.defect)
    else:
        result = auto_attack(n, e)

    # Display results
    print("\n" + "=" * 80)
    if result is not None and result != -1:
        print("[SUCCESS] Private key recovered!")
        print("=" * 80)
        print(f"\nPrivate Key (d): {result}")
        print(f"\nYou can now decrypt messages using:")
        print(f"  plaintext = pow(ciphertext, d, n)")
        print()
        return 0
    else:
        print("[FAILED] Unable to recover private key")
        print("=" * 80)
        print("\nPossible reasons:")
        print("  - Key size is too large for the selected attack")
        print("  - The key doesn't have the expected vulnerability")
        print("  - Try a different attack method (use --list-attacks)")
        print()
        return 1


if __name__ == '__main__':
    sys.exit(main())
