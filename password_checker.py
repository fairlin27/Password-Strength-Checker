import re

# Color Codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# =========================
# SCREEN 1 - INPUT SCREEN
# =========================
print(CYAN + "✧" + "=" * 70 + "✧" + RESET)
print(GREEN + "|  🔒                PASSWORD STRENGTH CHECKER                🛡️  |" + RESET)
print(CYAN + "✧" + "=" * 70 + "✧" + RESET)

password = input(MAGENTA + "\n🔑 Enter your password: " + RESET)

print(MAGENTA + "\n" + "-" * 50 + RESET)
print(GREEN + "\n✅ Password received successfully!" + RESET)

print(YELLOW + "\n💡 Tip: Strong passwords keep your account safe." + RESET)
print(YELLOW + "   Use uppercase, lowercase, numbers and special characters." + RESET)

# =========================
# SCREEN 2 - VALIDATION
# =========================
score = 0
suggestions = []

print(CYAN + "\nChecking Password Strength...\n" + RESET)

# Length Check
if len(password) >= 8:
    score += 1
    print(GREEN + "✓ Minimum 8 characters : PASS" + RESET)
else:
    print(RED + "✗ Minimum 8 characters : FAIL" + RESET)
    suggestions.append("Use at least 8 characters")

# Uppercase Check
if re.search(r"[A-Z]", password):
    score += 1
    print(GREEN + "✓ Uppercase letter     : PASS" + RESET)
else:
    print(RED + "✗ Uppercase letter     : FAIL" + RESET)
    suggestions.append("Add uppercase letter")

# Lowercase Check
if re.search(r"[a-z]", password):
    score += 1
    print(GREEN + "✓ Lowercase letter     : PASS" + RESET)
else:
    print(RED + "✗ Lowercase letter     : FAIL" + RESET)
    suggestions.append("Add lowercase letter")

# Number Check
if re.search(r"[0-9]", password):
    score += 1
    print(GREEN + "✓ Number               : PASS" + RESET)
else:
    print(RED + "✗ Number               : FAIL" + RESET)
    suggestions.append("Add numbers")

# Special Character Check
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
    print(GREEN + "✓ Special character    : PASS" + RESET)
else:
    print(RED + "✗ Special character    : FAIL" + RESET)
    suggestions.append("Add special character")

print("\n" + "=" * 50)

# Strength Result
if score <= 2:
    print(RED + "Password Strength: WEAK" + RESET)
elif score <= 4:
    print(YELLOW + "Password Strength: MEDIUM" + RESET)
else:
    print(GREEN + "Password Strength: STRONG" + RESET)

# Suggestions
if suggestions:
    print(YELLOW + "\nSuggestions to Improve:" + RESET)
    for suggestion in suggestions:
        print("•", suggestion)

# =========================
# SCREEN 3 - FINAL RESULT
# =========================
print(CYAN + "\n" + "=" * 70 + RESET)
print(GREEN + "                FINAL SECURITY REPORT                " + RESET)
print(CYAN + "=" * 70 + RESET)

print("\nPassword Entered :", password)
print("Security Score   :", score, "/ 5")

if score <= 2:
    print(RED + "\nOverall Status   : WEAK PASSWORD" + RESET)
    print(RED + "Risk Level       : HIGH" + RESET)
elif score <= 4:
    print(YELLOW + "\nOverall Status   : MEDIUM PASSWORD" + RESET)
    print(YELLOW + "Risk Level       : MODERATE" + RESET)
else:
    print(GREEN + "\nOverall Status   : STRONG PASSWORD" + RESET)
    print(GREEN + "Risk Level       : LOW" + RESET)

print("\nRecommendation:")
if score == 5:
    print(GREEN + "Excellent! Your password is highly secure." + RESET)
else:
    print(YELLOW + "Improve password using above suggestions." + RESET)

print(MAGENTA + "\n" + "=" * 70 + RESET)
print(MAGENTA + "★   Password Analysis Completed Successfully!   ★" + RESET)
print(MAGENTA + "=" * 70 + RESET)