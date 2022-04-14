/* MCAV C++ Assignment - Project 2 Shopping List

This time, you need to create a program that acts as a basic shopping list.
The user has the options to either add items, remove items, or display the entire list.

How it works:
1. The program will wait for user input (eg: cin >> userinput):
    a. If the user enters “add”, the program will request another input. Once the user has entered a word, 
        the program will add this to the list.
    b. If the user enters “remove”, the program will request another input. Once the user has entered a word, 
        the program will check if it exists in the list. If the item exists in the list, it will be removed. 
        If the item does not exist already, the program will say so.
    c. If the user enters “display”, the program will display the entire list.

2. The “shopping list” has to be a vector of pointers of a string.
    a. Eg: vector<string *> list; 
*/

#include <iostream>
#include <vector>
#include <string>
#include <memory>

using namespace std;

string user_action;

std::vector<std::string *> shopping_list;


// Function to add items to the list
void addItem() {
    /* Add item to shopping list via user input*/
    // NB. Breaks on whitespace

    string item_to_add;
    std::cout << "Add this item: "; 
    std::cin >> item_to_add;

    // Create new string pointer
    std::string * string_pointer_to_add = new std::string(item_to_add);

    // Add pointer to shopping list
    shopping_list.push_back(string_pointer_to_add);

};

void removeItem() {
    /* Remove item from the shopping list via user input*/

    string item_to_remove; 
    std::cout << "Remove this item: "; 
    std::cin >> item_to_remove;

    // Loop through to check if the item is in the list
    int i = 0;
    bool itemContained = false;
    for (const auto& item : shopping_list) {   
     
        // Remove the item and pointer if it is in the list
        if (item_to_remove.compare((*item)) == 0) {
            
            // delete pointer, remove pointer from list
            delete item;
            shopping_list.erase(shopping_list.begin() + i);
            itemContained = true;
                        
            std::cout << "Removed " << item_to_remove << " from your list... " << std::endl;

        }

        i++;  

    }
    
    // Display error if item not in the list
    if (itemContained == false) {
        std::cout << "The list does not contain this item..." << std::endl;
    }



};


void displayList() {
    /* Display all the items in the shopping list */    

    // Print all items in the shopping list
    std::cout << "Displaying Shopping List 5000: " << std::endl;

    // Check if list is empty first
    if (shopping_list.empty()) {

        std::cout << "Shopping List is empty. Please add some items first." << std::endl;

    } else {

        for (const auto& item : shopping_list)
        {
            std::cout << "> " << *item << std::endl;
        }
    }
    
};



int main()
{

    cout << "Welcome to the Shopping List 5000" << endl;

    // Loop infinitely
    while (1) {

        // Wait for User input action
        cout << "User action (add/remove/display): ";
        cin >> user_action;

        if (user_action.compare("add") == 0) {
            
            // Add an item to the list
            addItem();

        } else if (user_action.compare("remove") == 0) {
            
            // remove an item to the list
            removeItem();

        } else if (user_action.compare("display") == 0) {
            
            // display the entire list
            displayList();

        } else {

            // action type error checking
            cout << "Unsupported action" << endl;
        }

    }
}