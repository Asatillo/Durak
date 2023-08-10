# DURAK - an implimentation of the well known game with playing cards.

Durak (Russian: дурак, "fool") is a traditional Russian card game that is popular in many post-Soviet states. The objective of the game is to shed all one's cards when there are no more cards left in the deck. At the end of the game, the last player with cards in their hand is the durak or 'fool'.

## Rules

### Setup
The game is typically played with two to five people, with six players if desired, using a deck of 36 cards, for example a standard 52-card deck from which the numerical cards 2 through 5 have been removed. In theory, the limit for a game with one deck of 36 cards is six players, but this extends a considerable advantage to the player who attacks first, and a considerable disadvantage to the player who defends first. Variants exist that use more than one deck.

The deck is shuffled, and each player is dealt six cards. The bottom card of the stock is turned and placed face up on the table, its suit determining the trump suit for the current deal. For example, if it is the 7 of diamonds, then diamonds rank higher than all plain-suit cards. The rest of the pack is then placed on half over the turnup and at right angles to it, so that it remains visible. These cards form the prikup or talon. The turnup remains part of the talon and is drawn as the last card. Cards discarded due to successful defences are placed in a discard pile next to the talon.

### Playing
The player who has the lowest trump card will be the first attacker (note that there is no obligation to play that lowest trump card as the first card). The player to the attacker's left is always the defender. After each round of attack play proceeds clockwise. If the attack succeeds (see below), the defender loses their turn and the attack passes to the player on the defender's left. If the attack fails, the defender becomes the next attacker.

### First attack
Cards are ranked 6 7 8 9 10 J Q K A (ascending order). A trump card of any rank beats all cards in the other three suits. For example, a 6 of trumps beats an ace of any other suit.

The attacker opens their turn by playing a card face up on the table as an attacking card. The player to the attacker's left is the defender. They respond to the attack with a defending card.

### Defending
The defender attempts to beat the attack card by playing a higher-ranking defending card from their hand. For example, if the attacker plays a 7♠ the defender must play a higher spade such as the 10♠ or a card from the trump suit to defend successfully. The defender must play a higher card of the same suit as the attack card or play a card of the trump suit (there is no obligation to play the card of the same suit, you can use trump cards to beat off the attack anytime). The defending cards are placed on top of the attack card overlapping it, so both cards are visible and it is clear which cards are attacking and defending cards.

After the first attack, if the defender is successful, the attacker may launch a new attack. If they cannot or if they pass, then the player to the left of the defender may start a new attack or pass the chance to attack to the next non-defender going clockwise around the table. For each new attack which is defended successfully by the defender, the player who led that attack (played the last attack card) may start a new attack. After the original attack, attacks can only be made if the new attack card matches the rank of any card which has already been played during that round. If the player who led the last attack chooses not to attack again (and all future attacks during the round of attacks) then the original attacker may make a new attack, if they pass on making an attack then players to the defenders left may attack or pass and so on going clockwise around the table. There cannot be more than six attacks in each round. Each new attack card is placed to the left of the last attack card and the defender plays their defending card on top of the new attack card creating a row of attack and defence cards. The defender must respond to the new attack in the same fashion as the first attack by playing a card of the same suit of the new attack card with a higher rank or a trump card. All other players may make a new attack if the defender has successfully defended the last attack. The original attacker has priority for making an attack, then the player to defender's left has priority and so forth going clockwise. Some variants only allow cards to be added to the attack once the first defending card has been played.

At any point during a round of attacks, if a defender is unwilling or unable to beat the most recent attack card, they may give up their defence and must pick up all the cards played during that round of attack (both defending and attacking). In addition the other players may choose to shed cards matching ranks of any card which have already been played in this round which the defender must also pick up. In this case the round of attacks ends and the player to the defender's left starts a new round of attacks.

If, however, the defender has beaten all attacking cards and no other players are willing to make another attack or if the defender beats the sixth attack card, the defender has won the round of attacks. In this case all cards from that round of attack are placed in the discard pile and the defender starts a new round of attacks as the attacker and the player to his or her left becomes the new defender.

No players may examine the discard pile at any point.

### End of turn
At the end of each round of attacks against a defender, whether or not the defence was successful, each player draws new cards from the deck until they have six cards in their hand unless the deck has been exhausted. The main attacker draws as many cards as necessary first, followed by any other attackers in clockwise order, and finally the defender. The defender's final card must beat the last attack card, otherwise they must pick up all the cards played during that round of attacks. If the talon is exhausted, and a player has played all their cards, they are eliminated from the game.

### Winning and losing
The last person left with cards in their hand is the loser (the fool or durak). In some variants, this player becomes the dealer for the next round. The player to the fool's right may become the first attacker for the next round.

Some variants declare the winner of the round to be the first player to empty their hand and leave the game. In others, there are no winners, only the loser.

### Team play
Four players can play as two pairs. Six can play as three teams of two, or two teams of three. The members of each team sit opposite one another (with two players on each team), or alternating (with three). In some variants, the team with the lowest trump starts the first round, but in subsequent rounds the winning team from the previous round begins.

When playing in teams, players may not add to attacks on their teammates.

### Fool with epaulettes
If the last card played by an attacker is a six, and the defender loses, the defender is cheerfully pronounced durak s galstukom (lit. 'a fool with a necktie'), and the six card may be symbolically placed on his chest. This is worse than declaring the loser simply as a durak, because of the handicap of having a low-value Six through the final part of the game. If the attacker plays two sixes, the loser is even called a durak with "epaulettes on both shoulders" in Russian "durak s pogonami".

Some variants use the ties as scoring points. If someone has a six as a tie, the opponents must next score against them using a seven, and so on until someone receives an ace as a tie. To score, the winning individual or team must not only end with the correct tie value, but must include at least one non-trump card in the final attack. As it goes with two sixes either.

## Roadmap:

- Create the class for Card
- Create the class for the Deck
- Create the class for the Game
- Create the web version of the game