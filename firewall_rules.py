"""
Week 05 INDIVIDUAL ASSIGNMENT -- Firewall Port Rules
ITIA 1510 Cybersecurity Automation

Topic: functions, from Week 04. No lists and no dictionaries.

A firewall change request lists the port numbers someone wants opened. Every
one of them gets a decision: ALLOW, REVIEW or BLOCK. The decision depends on
which range the port falls in, and on whether the service that normally runs
there sends traffic unencrypted.

The input loop, the counters and the summary are already written. What is
missing is the FUNCTIONS. Work through the TODOs in order.

Run the file before changing anything. It works, but every port comes back
invalid and blocked, because the functions return placeholders.
"""

# Port ranges, as assigned by IANA.
#   1 - 1023        well-known   system services: SSH, DNS, HTTPS ...
#   1024 - 49151    registered   applications: databases, dev servers ...
#   49152 - 65535   dynamic      short-lived client connections
#   anything else   invalid      not a port at all


def is_valid_port(port):
    """True when port is a real port number, 1 through 65535."""
    # TODO 1
    #   Return whether port is at least 1 and no more than 65535.
    return False


def port_range(port):
    """Return 'well-known', 'registered', 'dynamic' or 'invalid'."""
    # TODO 2
    #   Call is_valid_port first. When it says the port is not valid, return
    #   'invalid' -- do not repeat the 1 to 65535 test here.
    #   Otherwise use if / elif / else on the ranges in the table above.
    return "invalid"


def is_cleartext(port):
    """True for the services that send traffic unencrypted:
    21 FTP, 23 Telnet, 80 HTTP and 110 POP3."""
    # TODO 3
    #   Compare port to each of the four numbers with == and join the
    #   comparisons with or. No lists this week.
    return False


def rule_for(port):
    """Return 'BLOCK', 'REVIEW' or 'ALLOW' for one port."""
    # TODO 4
    #   BLOCK   an invalid port, or a clear-text service
    #   REVIEW  a dynamic port -- nothing should be listening there on purpose
    #   ALLOW   everything else
    #   Build this out of the three functions above. It should not contain a
    #   single port number of its own.
    return "BLOCK"


allowed = 0
review = 0
blocked = 0

print("=" * 54)
print("FIREWALL PORT RULES")
print("=" * 54)
print("Enter a port number to check, or 'done' to finish.")
print()

while True:
    entry = input("Port: ")

    if entry == "done":
        break

    # A typo should not end the program. Count nothing and go back round.
    if entry.isdigit() == False:
        print("  That is not a whole number.")
        print()
        continue

    port = int(entry)
    decision = rule_for(port)

    print("  " + entry.ljust(7) + port_range(port).ljust(12) + decision)

    # TODO 5
    #   Add 1 to allowed, review or blocked, whichever matches decision.

    print()

print("-" * 54)
print("CHANGE REQUEST SUMMARY")
print("-" * 54)
print("Allowed:          " + str(allowed))
print("Needs review:     " + str(review))
print("Blocked:          " + str(blocked))
print("=" * 54)
