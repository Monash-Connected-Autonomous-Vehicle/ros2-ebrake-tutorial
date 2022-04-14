
// Card Class cpp File

#include <iostream>
#include <string> 

using namespace std;

class Card {
    /* 
        Card Class for BlackJack game
        id: id of the card (see black_jack.cpp)
        name: suit and number of the card
        value: value of the card in blackjack

     */
    private:
        int id;
        string name;
        int value;


    public:
        Card (int, string, int);

        int getValue(){
            // Return the value of a Card
            return value;
        }

        void setValue(int new_value) {
            // Set the value of a card
            value = new_value;
        }
        void printString() {
            // Print the card name, and value
            std::cout << name << " (" << value << ")" << std::endl;
        
        }

};


Card::Card(int card_id, string card_name, int card_value) {
    // Card Constructor (id, name, value)
    id = card_id;
    name = card_name;
    value = card_value;

}