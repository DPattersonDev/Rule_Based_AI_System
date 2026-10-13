# Rule-Based IT Troubleshooting Assistant

## Part 1: Initial Project Ideas

### 1. IT Troubleshooting Assistant
- **Description:** A system that helps users troubleshoot common computer and network problems such as internet issues, slow computers, login problems, and printer problems.
- **Rule-Based Approach:** The system checks the user's input for predefined keywords and uses `if-elif-else` statements to provide troubleshooting steps.

### 2. Cybersecurity Password Advisor
- **Description:** A system that evaluates basic information about a password and provides security recommendations.
- **Rule-Based Approach:** The program checks conditions such as password length and whether uppercase letters, lowercase letters, numbers, and special characters are included.

### 3. Help Desk Ticket Priority System
- **Description:** A system that assigns IT support requests a priority such as Low, Medium, High, or Critical.
- **Rule-Based Approach:** The program uses predefined rules based on the type of issue and how many users are affected.

### Chosen Idea: IT Troubleshooting Assistant

I chose the IT Troubleshooting Assistant because it relates closely to my previous experience working with computers, networks, and technical support. It also gives me a practical way to see how an AI system can provide useful recommendations using predefined rules instead of machine learning.

---

## Part 2: Rules/Logic for the Chosen System

1. **IF** the input contains "internet," "wifi," or "network" → provide network troubleshooting steps.
2. **IF** the input contains "slow," "lag," or "freezing" → provide performance troubleshooting steps.
3. **IF** the input contains "login," "log in," "password," or "locked" → provide login troubleshooting steps.
4. **IF** the input contains "printer" or "print" → provide printer troubleshooting steps.
5. **ELSE** → explain that no predefined rule matches and recommend contacting technical support.

---

## Part 3: Sample Inputs and Outputs

### Test 1
**Input:** `My internet is not working`

**Output:** Network troubleshooting steps are displayed.

### Test 2
**Input:** `My computer is very slow`

**Output:** Performance troubleshooting steps are displayed.

### Test 3
**Input:** `I cannot login to my account`

**Output:** Login troubleshooting steps are displayed.

---

## Part 4: Reflection

My rule-based system is an IT Troubleshooting Assistant that provides basic troubleshooting steps for common computer problems. The program asks the user to describe the problem they are experiencing. It then converts the input to lowercase and checks the text for specific keywords. Keywords related to internet or network problems trigger one set of troubleshooting instructions, while keywords related to slow performance, login problems, or printers trigger other sets of instructions. If the user enters a problem that does not match any of the predefined rules, the program recommends gathering more information and contacting technical support. The program does not learn from the user or use machine learning. Its behavior depends entirely on the rules that were written in advance.

One challenge I encountered while using AI to help design the project was deciding how complicated the system should be. AI can quickly suggest many features, but the purpose of this assignment is to demonstrate a simple rule-based system. I had to keep the program focused on conditionals instead of adding features that would make the project unnecessarily complex. Another challenge was choosing keywords that would recognize different ways a user might describe the same problem. For example, a login problem could include words such as "login," "password," or "locked."

Working with AI helped me organize the rules, turn them into Python conditionals, and think about additional test cases. The project helped demonstrate how useful systems could make decisions before modern machine learning by following carefully designed rules and heuristics.
