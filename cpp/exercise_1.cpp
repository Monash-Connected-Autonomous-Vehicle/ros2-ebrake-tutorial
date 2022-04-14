
/* MCAV C++ Tutorial
Exercise 1 - Parrot

Make a program (the parrot) that will indefinitely repeat back every word that the user
types into the terminal.

However, when the user types “dead-parrot”, then the parrot will say “No, I am just
resting”. If the user types “exit-parrot”, then the program terminates.

 */

#include <iostream>

std::string user_response;
std::string exit_response = "exit-parrot";
std::string dead_response = "dead-parrot";

int main()
{
    std::cout << "This is the Norweigan Blue Parrot Bot!" << std::endl;
    
    // Loop infinitely
    while(1) {
        
        // Get User input (N.B. cin breaks on whitespace)
        std::cout << "\nUser: "; 
        std::cin >> user_response;

        // Compare user response to set phrases
        if (user_response.compare(exit_response) == 0) 
        {
            
            return 0;
            
        } else if (user_response.compare(dead_response) == 0)
        {
            std::cout << "Parrot: No, I am just resting" << std::endl;
        
        } else {

            std::cout << "Parrot: " << user_response << std::endl;
        
        }
    
    }
}