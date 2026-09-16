# ITIA 1510 Week 05: Firewall Port Rules

Individual assignment. Topic: **functions**, from Week 04.

A firewall change request lists the port numbers someone wants opened. Your
program decides, for every port, whether to **ALLOW** it, flag it for
**REVIEW**, or **BLOCK** it. Open `firewall_rules.py` and work through the five
numbered TODOs in order. No lists and no dictionaries.

## Get your own copy

1. On this repository's GitHub page, click **Use this template**, then
   **Create a new repository**.
2. Set **Owner** to your own account and name the repository
   `ITIA1510-Firewall-Port-Rules`. Choose **Public**, then click
   **Create repository**.
3. Clone your new repository, not this one:

   ```
   git clone <your repository url>
   cd ITIA1510-Firewall-Port-Rules
   ```

## Do the work on a branch

Do all of the git work with git commands from the command line. Do not edit,
upload or merge files in the GitHub web interface.

4. Create the branch before you change anything:

   ```
   git checkout -b week05-firewall-port-rules
   ```

5. Write the code. Commit as you go, so a crashed laptop does not cost you the
   evening:

   ```
   git add firewall_rules.py
   git commit -m "Describe what you just finished"
   ```

6. Push the branch:

   ```
   git push -u origin week05-firewall-port-rules
   ```

## Demonstrate, then merge

7. **Demonstrate the program to your instructor** from the branch you just
   pushed, using the debugger in VS Code. The demonstration is required: it is
   worth half the grade, and an assignment that is never demonstrated earns no
   points.
8. After the demonstration, merge into main and push:

   ```
   git checkout main
   git merge week05-firewall-port-rules
   git push origin main
   ```

9. Submit the link to your repository in Canvas.

If it is not finished at 8:55 PM, keep working, or demonstrate what you have,
then commit, push, merge and submit it for partial credit.

## Check your work

These are the answers a finished program gives. The edges are where it goes
wrong, so check both sides of each one.

| Port  | Range      | Decision |
|-------|------------|----------|
| 0     | invalid    | BLOCK    |
| 1     | well-known | ALLOW    |
| 23    | well-known | BLOCK    |
| 443   | well-known | ALLOW    |
| 1023  | well-known | ALLOW    |
| 1024  | registered | ALLOW    |
| 49151 | registered | ALLOW    |
| 49152 | dynamic    | REVIEW   |
| 65535 | dynamic    | REVIEW   |
| 65536 | invalid    | BLOCK    |

Entering 22, 23, 443, 50000 and 70000 in one run ends with 2 allowed, 1 needing
review and 2 blocked.
