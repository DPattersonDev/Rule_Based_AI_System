# Rule-Based IT Troubleshooting Assistant
# This program uses predefined rules instead of machine learning.

def troubleshoot(problem):
    problem = problem.lower().strip()

    # Rule 1: Network problems
    if "internet" in problem or "wifi" in problem or "network" in problem:
        return (
            "Network Issue Detected:\n"
            "1. Check that Wi-Fi or the Ethernet cable is connected.\n"
            "2. Restart the computer and router/modem.\n"
            "3. Check whether other devices can connect.\n"
            "4. If the issue continues, check the network adapter or contact IT support."
        )

    # Rule 2: Slow computer problems
    elif "slow" in problem or "lag" in problem or "freezing" in problem:
        return (
            "Performance Issue Detected:\n"
            "1. Close programs that are not being used.\n"
            "2. Restart the computer.\n"
            "3. Check available storage space.\n"
            "4. Check Task Manager for programs using unusually high CPU or memory."
        )

    # Rule 3: Login problems
    elif "login" in problem or "log in" in problem or "password" in problem or "locked" in problem:
        return (
            "Login Issue Detected:\n"
            "1. Verify the username and password.\n"
            "2. Make sure Caps Lock is off.\n"
            "3. Try the password reset option if available.\n"
            "4. If the account is locked, contact an administrator or help desk."
        )

    # Rule 4: Printer problems
    elif "printer" in problem or "print" in problem:
        return (
            "Printer Issue Detected:\n"
            "1. Check that the printer is powered on and connected.\n"
            "2. Make sure paper and ink/toner are available.\n"
            "3. Check the print queue for stuck jobs.\n"
            "4. Restart the printer and try again."
        )

    # Rule 5: Unknown issue
    else:
        return (
            "I do not have a predefined rule for that issue. "
            "Please collect more details and contact technical support."
        )


print("Welcome to the Rule-Based IT Troubleshooting Assistant!")
print("Describe your problem, or type 'exit' to quit.")

while True:
    user_problem = input("\nWhat problem are you having? ")

    if user_problem.lower().strip() == "exit":
        print("Goodbye!")
        break

    print()
    print(troubleshoot(user_problem))
