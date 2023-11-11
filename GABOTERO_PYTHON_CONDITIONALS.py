#Author: Justin Gabotero -- Integrative #3

def continue_input():
  u_inp = input("Would you like to continue?").lower()
  if u_inp == "yes":
    print("Continuing...\nComplete!")
  elif u_inp == "no":
    print("Exiting...")
    return
  else:
    print("Please try again, and answer with 'yes' or 'no'.")
  continue_input()

continue_input()
