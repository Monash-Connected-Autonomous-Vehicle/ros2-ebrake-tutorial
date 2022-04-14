/* 
MCAV C++ Tutorial
Exercise 3 -  Black Jack

This time, you need to create a text-based Black Jack game. For simplicity, the rules are
modified.

Rules:
1. Both the player and the dealer start with 2 cards. (all 4 cards are readable by the
    player)
2. The player is then asked whether they want another card (cin >> userinput). If the
    player types “y”, the game board is again displayed (clear the screen and display the
    board again), now with the updated hand. If the player types “n”, the round ends.
3. If at any point the player’s cards total exceeds 21, the round ends.
4. Both the dealer’s points total and the player’s points total should always be
    displayed.
5. Deck: The deck will be 1 standard deck of playing cards. Cards with number value 2-
    10 are worth their number value in points. All face cards (Jack, Queen, King) are all
    worth 10 also. Aces are worth either 1 or 11.
6. When the round ends, the dealer will now draw cards until the dealer’s total is 17 or
    more. If the players total is more than 21, the player loses. Else, if the dealer’s total
    is more than 21, the player wins. Else, if the dealer’s total is greater or equal to the
    player’s total, the player loses.
7. After the round ends, the final score and hands are displayed, along with which
    player won. The cards from the dealers and players hands are put into the discard
    pile.
8. During the game, you should keep track of which cards are still remaining in the
    deck, which cards are in the player’s and dealer’s hands, and which cards are in the
    discard pile. Once the deck has 15 cards or less remaining, the discard pile is added
    back into the deck and shuffled.

Code:
1. You will need to create a class called “Card”, which contains:
    a. Private variables containing the card value and suit.
    b. Public functions including:
        i. A constructor
        ii. Functions to return the card value and suit.
        iii. Other functions if you need them.

2. The deck of cards, dealer’s and player’s hands, and the discard pile, all have to be
vectors of pointers to objects of the Card class. Eg: vector<Card *> deck;
3. You will need to have 3 different files.
    a. black_jack.cpp: This is file contains the main() file.
    b. Card.h: This file contains the header file for the “Card” class.
    c. Card.cpp: This file contains the function definitions for the functions in the
    “Card” class.
 */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <random>
#include <cstdlib>
#include <ctime>
#include <chrono>

#include "Card.h"

using namespace std;


// Container definitions
vector<Card *> deck;
vector<Card *> player_hand;
vector<Card *> dealer_hand;
vector<Card *> discard_pile;

// Game Variables
int player_wins = 0;
int dealer_wins = 0;

// Helper Variables
bool clear_screen = false;

// Function Declarations

// Deck Management
void createDeck();
void shuffleDeck(vector<Card *> &deck); 
void showDeck();
void moveCards(vector<Card *> &from_hand, vector<Card *> &to_hand);

// Dealing Cards
Card * drawCard();
void dealCards(int n_cards, vector<Card * > &hand, bool drama);

// Hand Management
int getHandValue(vector<Card *> &hand);
void showHand(vector<Card *> &hand);
bool checkHandValue(vector<Card *> &hand);
int countAces(int card_value);
void modifyAces(Card &card, bool reset_round);

// Game Management
int playRound(); 
void beginRound();
void endRound(bool player_lost);
void showRoundStatus(bool clear_screen);
void resetRound();
int continuePlaying(int &playGame);

// Function Definitions
void createDeck() {
    // Create the Deck

    // Standard 52 card pack
    // 0 - 12: Hearts
    // 13 - 26: Diamonds
    // 27 - 40: Spades
    // 41 - 52: Clubs

    vector<string> suits = {"Hearts", "Diamonds", "Spades", "Clubs"};
    vector<string> card_names = {"Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"};
    vector<int> card_values = {11, 2, 3, 4, 5,  6, 7, 8, 9, 10, 10, 10, 10};

    vector<int> deck_ids;
    vector<int> deck_values;
    vector<string> deck_names;

    // Assign Card IDs
    for( int i = 0; i < 52; i++ ) {
        deck_ids.push_back( i );
    }

    // Assign Card Values
    for (int i = 0; i<=3; i++) {
        for (const auto& value : card_values) {

            deck_values.push_back(value);
        }

    }

    // Assign Card Names (Suit + Card)
    for (const auto& suit : suits) {

        for (const auto& name : card_names) {
            
            string card_name = name + " of " + suit;
            
            deck_names.push_back(card_name);
        
        }

    }

    // Create a Card Class for each card, assign to deck vector
    for (int i=0; i < deck_ids.size(); i++) {

        // For each card id, name and value
        // create a new card class
        // append to deck

        int card_id = deck_ids[i];
        string card_name = deck_names[i];
        int card_value = deck_values[i]; 

        Card * card_pointer = new Card(card_id, card_name, card_value);

        deck.push_back(card_pointer);
    }

    // Shuffle the deck
    shuffleDeck(deck);


}

void shuffleDeck(vector<Card *> &deck) {

    // Shuffle the deck
    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count(); 
    std::shuffle(std::begin(deck), std::end(deck), std::default_random_engine(seed));

}

void showDeck() {
    /* Print the Deck */

    cout << "DECK" << endl;
    
    for (auto& card: deck) {

        (*card).printString();

    }
}

Card * drawCard() {

    // Assumes the deck is already shuffled
    Card * drawn_card = deck.back();
    deck.pop_back();

    return drawn_card;

}

void dealCards(int n_cards, vector<Card * > &hand, bool drama) {
    /* Deal the specifed amount of cards to the specified hand */

    for (int i = 0; i < n_cards; i++) {
        
        Card * drawn_card = drawCard();

        hand.push_back(drawn_card);
        
        if (drama) {
            cout << "Draw: "; 
            (*drawn_card).printString();
        }
    }

}


int countAces(int card_value) {
    
   // Return 1 if card is an ace.

    if (card_value == 11 || card_value == 1) {
        return 1;
    }
    return 0;

}

void modifyAces(Card &card, bool reset_round) {
    /* Modify the value of the Ace based on game state */

    if (card.getValue() == 11 && reset_round == false) {
        
        // Change aces value to 1  
        card.setValue(1);
    }

    if (card.getValue() == 1 && reset_round == true) {
        
        // Reset aces value back to 11 at end of round
        card.setValue(11);
    }

}


int getHandValue(vector<Card *> &hand) {
    /*  
        Return the value of hand
    
        Modifies the value of aces if hand is bust
    */

    int hand_value = 0;
    int n_aces = 0;

    for (auto& card: hand) {
        
        hand_value += (*card).getValue();

        n_aces += countAces((*card).getValue());
    }

    // Check for aces if hand is bust
    if (hand_value > 21 && n_aces > 0) {

        hand_value = 0;

        for (auto& card: hand) {
            
            // Modifiy the value of the aces cards if bust
            modifyAces((*card), false);

            hand_value += (*card).getValue();
    }


    }

    return hand_value;
}

bool checkHandValue(vector<Card *> &hand) {
    /*  Returns true if hand value greater than 21 */

    int hand_value = getHandValue(hand);

    if (hand_value> 21) { 
        return true;
    } 
    return false;
}

int playRound() {

    /* 
    Deal cards to player while they:
      * still ask for them
      * are not bust
    Otherwise, end the round 
     */

    cout << "\nWhat would you like to do?" << endl;
    cout << "Hit (y) OR Stick (n)" << endl; 
    string player_option;
    cin >> player_option;

    if (player_option == "y") {
        
        system("clear");
        cout << "\nDealing to Player:" << endl;
        dealCards(1, player_hand, true);

        if (checkHandValue(player_hand)) {
            
            // Player is bust, round ends automatically
            endRound(true);
            return 0;
        }

        // Player is not bust, continue
        showRoundStatus(false);
        return 1;


    } else {
        // Player chooses to end the round
        endRound(false);
        return 0;
        
    }
        

}

void showHand(vector<Card *> &hand){
    /* Show the cards in the hand */
    
    for (auto& card: hand) {

        (*card).printString();

    }

}

void showRoundStatus(bool clear_screen) {
    /* Show the current status of the game */
    
    int deck_count = deck.size();
    int discard_count = discard_pile.size();
    int player_score = getHandValue(player_hand);
    int dealer_score = getHandValue(dealer_hand); 

    // Clear the screen if required
    if (clear_screen) {
        system("clear");
    }

    cout << "\n--------Round Status--------" << endl;
    
    // Show the player's hand and score
    cout << "\nPlayer Hand: " << player_score << endl;
    showHand(player_hand);
    //cout << "Player Score: " << player_score << endl;
    
    // Show the dealer's hand and score
    cout << "\nDealer Hand: " << dealer_score << endl;
    showHand(dealer_hand);
    //cout << "Dealer Score: " << dealer_score << endl;

    // Show the status of the deck
    cout << "\nCards Remaining: " << endl;
    cout << "Deck: " << deck_count << " Discard: " << discard_count << endl;

}

void beginRound() {

    // Initial Deal
    system("clear");
    cout << "\n---------New Round-----------" << endl;
    cout << "\nInitial Deal..." << endl;

    dealCards(2, player_hand, false);
    dealCards(2, dealer_hand, false);

    // Show Initial Game Status
    showRoundStatus(false);

}

void endRound(bool player_lost) {

    /* 
    End of Round Behaviour
        * If Player is bust - > dealer wins
        * If Player ends the round -> dealer draws until greater than 17
        * If Dealer is bust -> player wins
        * If Dealer > Player -> dealer wins
        * If Player > Dealer -> player wins
     * Both Player and Dealer hands are moved to discard pile
     */

    showRoundStatus(true);

    if (player_lost) {

        // Player is bust, player loses
        cout << "\n---------Round End---------" << endl;
        cout << "Player Bust: Dealer Wins! "  << endl;
        dealer_wins++;

    } else {

        // player chooses to end the round:
        // dealer draws until greater than 17:

        cout << "\n---------Round End---------" << endl;
        cout << "\nDealing to Dealer..." << endl;

        while(getHandValue(dealer_hand) <= 17) {
            dealCards(1, dealer_hand, true);
            cout << "Dealer Hand: " << getHandValue(dealer_hand) << endl;
        }
    
        // if dealer > 21: dealer loses
        // else if dealer greater than player, dealer wins

        if (checkHandValue(dealer_hand)) {
            cout << "Dealer Bust: Player Wins! "  << endl;
            player_wins++;
        } else if (getHandValue(dealer_hand) >= getHandValue(player_hand)) {
            cout << "Dealer High: Dealer Wins!" << endl;
            dealer_wins++;
        } else {
            cout << "Player High: Player Wins!" << endl;
            player_wins++;
        }
    }

    // Clean up Hands and Reset Round
    resetRound();    

}

void moveCards(vector<Card *> &from_hand, vector<Card *> &to_hand) {

    /* Move all the cards from one container to another */

     for (auto& card: from_hand) {

        // Reset the ace values back to 11
        modifyAces((*card), true);

        to_hand.push_back(card);

    }
    from_hand.clear();
}

void resetRound() {
    
    // Move Player and Dealer cards to discard pile
    moveCards(player_hand, discard_pile);
    moveCards(dealer_hand, discard_pile);

    // If deck is low, refill it, and shuffle
    if (deck.size() < 15) {
        moveCards(discard_pile, deck);
        
        // Reshuffle the Deck
        shuffleDeck(deck);
    }

}

int continuePlaying(int &playGame) {

        // Show Game Statistics and continue playing
    cout << "\n--------Game Statistics--------\n" << endl;
    cout << "Player Wins: " << player_wins << endl;
    cout << "Dealer Wins: " << dealer_wins << endl;

    cout << "\nContinue Playing? (1=yes, 0=no) \n"; 
    cin >> playGame;

    return playGame;
}

int main() {

    // Create Game and Deck
    createDeck();

    // Game Flags
    int keep_playing = 1;
    int playGame = 1;

    while (playGame) {

        // Begin the Round (Initial Deal)
        beginRound();

        while(keep_playing) {
            
            // Keep dealing to the player while they haven't lost
            keep_playing = playRound();
        
        }
        
        keep_playing = continuePlaying(playGame);

    }
    return 0;
}

// g++ -std=c++14 -g black_jack.cpp -o black_jack




