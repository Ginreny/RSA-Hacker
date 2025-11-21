# RSA Hacker

Command-line RSA cryptanalysis tool for demonstrating known vulnerabilities in RSA encryption systems.

## Quick Start

### One-Line Execution

```bash
# Build and run
docker build -t rsa-hacker . && docker run --rm rsa-hacker -n 90581 -e 17993

# Create alias (recommended)
alias rsa-hacker='docker run --rm rsa-hacker'
rsa-hacker --list-attacks
rsa-hacker -n 90581 -e 17993
```

## Usage

### Basic Commands

```bash
# Show help
docker run --rm rsa-hacker --help

# List all attack methods
docker run --rm rsa-hacker --list-attacks

# List key defect types
docker run --rm rsa-hacker --list-defects

# Auto attack (recommended)
docker run --rm rsa-hacker -n <MODULUS_N> -e <EXPONENT_E>

# Specify attack method
docker run --rm rsa-hacker -n <MODULUS_N> -e <EXPONENT_E> --attack wiener

# Attack by defect type
docker run --rm rsa-hacker -n <MODULUS_N> -e <EXPONENT_E> --defect low_private_key
```

## Examples

### Example 1: Auto Attack (Recommended)

```bash
docker run --rm rsa-hacker -n 90581 -e 17993
```

Output:
```
[SUCCESS] Private key recovered!
Private Key (d): 5
```

### Example 2: Wiener Attack (Small Private Exponent)

```bash
docker run --rm rsa-hacker \
  -n 460657813884289609896372056585544172485318117026246263899744329237492701820627219556007788200590119136173895989001982261875246093034700530620311149777699 \
  -e 354611102441307572056572181827925899198345350228753730931089393275463916544456626894245415096107834465778409532373187125903733234602888378112808763326353 \
  --attack wiener
```

### Example 3: FactorDB Query

```bash
docker run --rm rsa-hacker -n 13290059 -e 65537 --attack factordb
```

### Example 4: Using Alias

```bash
# Add to ~/.bashrc or ~/.zshrc
alias rsa-hacker='docker run --rm rsa-hacker'

# Usage
rsa-hacker --list-attacks
rsa-hacker -n 90581 -e 17993
rsa-hacker -n 1591 -e 65 --attack pollard_rho
```

## Attack Methods

### Factorization Attacks

| Method | Description | Usage |
|--------|-------------|-------|
| **DIXON** | Dixon's factorization algorithm for medium-sized moduli | `--attack dixon` |
| **ECM** | Elliptic Curve Method, effective for medium-sized factors | `--attack ecm` |
| **FERMAT1/FERMAT2** | Fermat's factorization, works when p and q are close | `--attack fermat1` |
| **POLLARD_P_1** | Pollard's p-1, works when p-1 is smooth | `--attack pollard_p_1` |
| **POLLARD_RHO** | Pollard's Rho, probabilistic factorization | `--attack pollard_rho` |
| **SIQS** | Self-Initializing Quadratic Sieve, advanced factorization | `--attack siqs` |
| **WILLIAMS_PP1** | Williams' p+1, works when p+1 is smooth | `--attack williams_pp1` |

### Mathematical Weakness Attacks

| Method | Description | Usage |
|--------|-------------|-------|
| **WIENER** | Wiener's attack, works when d < n^0.25 | `--attack wiener` |

### Other Methods

| Method | Description | Usage |
|--------|-------------|-------|
| **FACTORDB** | Query online factorization database | `--attack factordb` |
| **SOLUTION** | Automatically select best attack method | Default or `--attack solution` |

## Key Defect Types

| Defect | Description | Usage |
|--------|-------------|-------|
| **LOW_PRIVATE_KEY** | Private exponent too small | `--defect low_private_key` |
| **P_1_SMOOTH** | p-1 is a smooth number | `--defect p_1_smooth` |
| **PP_1_SMOOTH** | p+1 is a smooth number | `--defect pp_1_smooth` |
| **SMALL_N** | Modulus too small | `--defect small_n` |

## Command-Line Arguments

### Required Arguments

- `-n, --modulus` - RSA modulus N
- `-e, --exponent` - Public exponent e

### Optional Arguments

- `--attack` - Specify attack method
- `--defect` - Specify defect type
- `--list-attacks` - List all attack methods
- `--list-defects` - List all defect types
- `--version` - Show version
- `-h, --help` - Show help

## Installation

### Method 1: Docker (Recommended)

```bash
# Build image
docker build -t rsa-hacker .

# Run
docker run --rm rsa-hacker [ARGS]
```

### Method 2: Local Python

```bash
# Install Python 3.10+
brew install python@3.11  # macOS
apt install python3.11    # Linux

# Install dependencies
pip3 install -r requirements.txt

# Run
PYTHONPATH=.:$PYTHONPATH python3 rsa_hacker_cli.py [ARGS]
```

## Test Cases

```bash
# Test 1: Small modulus
docker run --rm rsa-hacker -n 90581 -e 17993
# Expected: d = 5

# Test 2: Wiener vulnerability
docker run --rm rsa-hacker \
  -n 460657813884289609896372056585544172485318117026246263899744329237492701820627219556007788200590119136173895989001982261875246093034700530620311149777699 \
  -e 354611102441307572056572181827925899198345350228753730931089393275463916544456626894245415096107834465778409532373187125903733234602888378112808763326353 \
  --attack wiener
# Expected: Successfully recover private key

# Test 3: FactorDB
docker run --rm rsa-hacker -n 13290059 -e 65537 --attack factordb
# Expected: Retrieve factorization from database
```

## Output Examples

### Success Output

```
╔══════════════════════════════════════════════════════════════╗
║                      RSA-HACKER CLI                          ║
╚══════════════════════════════════════════════════════════════╝

[Auto Attack Mode]
Modulus N: 90581
Public Key e: 17993

Analyzing key characteristics and selecting optimal attack...

================================================================================
[SUCCESS] Private key recovered!
================================================================================

Private Key (d): 5

You can now decrypt messages using:
  plaintext = pow(ciphertext, d, n)
```

### Failure Output

```
================================================================================
[FAILED] Unable to recover private key
================================================================================

Possible reasons:
  - Key size is too large for the selected attack
  - The key doesn't have the expected vulnerability
  - Try a different attack method (use --list-attacks)
```

### Docker Compose

```bash
docker-compose run rsa-hacker -n 90581 -e 17993
```

## Project Structure

```
RSA-Hacker/
├── rsa_hacker_cli.py    # CLI main program
├── attacks/             # Attack implementations (11+ methods)
│   ├── single_key/      # Single key attacks
│   └── multi_key/       # Multi-key attacks
├── generators/          # Key generation tools
├── lib/                 # Number theory core library
├── test/                # Test scripts
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Compose configuration
└── requirements.txt     # Python dependencies
```

## Requirements

- **Python:** 3.10+ (requires match-case syntax)
- **Docker:** 20.10+ (recommended)
- **Dependencies:**
  - gmpy2 - High-precision arithmetic
  - primefac - Prime factorization
  - cryptography - RSA key handling
  - bitarray - Bit array operations
  - requests - HTTP requests (FactorDB)

## Important Notes

### Use Cases

- Educational purposes
- Security research
- Authorized penetration testing
- CTF competitions

### Limitations

- Only effective against weak RSA implementations
- Cannot break properly implemented RSA (2048+ bit keys)
- Some methods (SIQS, ECM) require significant time for large numbers
- FactorDB attack requires network connection


## References

- [RSA Cryptosystem](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [Wiener's Attack](https://en.wikipedia.org/wiki/Wiener%27s_attack)
- [Pollard's Rho Algorithm](https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm)
- [FactorDB](http://factordb.com/)

---

**Version:** 2.0
**Last Updated:** 2025-11-21

