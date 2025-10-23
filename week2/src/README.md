# 🃏 Poker BlackJack (Still thinking of a clever name)

Classic Texas Holdem poker, but with additional black jack rules. For 2-8 players.

---
## Project Details

Week 2 of the project a week challenge! I am doing something with OOP since I need to touch up on it for interviews and tests. This card game randomly came into my head while I was yapping on a call with Nityant Rathi.

---

## 🔄 Gameplay Overview

### 1. Deal & Initial Betting
- Follow standard Texas Hold'em rules: each player receives **two cards**.  
- The **Flop**, **Turn**, and **River** occur with **betting rounds** and a **Blackjack Hit Phase** in between.

---

### 2. Hit Phases
- After each betting round, the blackjack round occurs and all players still in the hand may choose to **Hit**.  
- **Limits:**  
  - Each player may Hit **up to 3 times per hand**, but **no more than once per betting turn**.  
- When hitting:  
  - The dealer gives the player **one face-down card**.  
  - The player calculates their Blackjack total using these values:  
    ```
    2–10 → face value
    J, Q, K → 10
    A → 1 or 11 (whichever benefits the player)
    ```
  - If the total exceeds 21 → **Bust** → marked for elimination after the hand ends.  
    - A busted player **cannot win the pot**, but if all remaining players busted, winner goes to the lowest busting hand or big blind/closest to big blind.

---

### 3. Using Hit Cards
- If a player's total is ≤ 21, hit cards **can be used** as part of their **best five-card Poker hand** at showdown.  
- Hit cards are **personal**, not community cards.  
- Blackjack totals — unless exactly 21 or a bust — **have no further effect** on gameplay.

---

### 4. Fake Hit Chip
- Each player starts with **one Fake Hit Chip**.  
- Using it:  
  - The dealer gives **one card that cannot contribute** to the hand (no Blackjack or Poker value).  
  - The player sees the card, giving them potential information, while others see that a "hit" occurred.  
- **Usage Limits:**  
  - Once per betting round.  
  - Discarded after the hand ends if used.  

**Buying More:**  
- Every ⌊total_players ÷ 2⌋ rounds, players recieve **one additional Fake Hit Chip**

### 5. Final Round
- After the **final betting round and Hit Phase**, remaining players reveal their hands.  
- **Best Poker hand** wins the main pot.  
- If one or more losing players have **exactly 21**, they split a **20% bonus pot** (from the main pot).

---

## ⚙️ Tech Stack

**Languages:**  
- Python (backend)

**Frameworks / Libraries:**  


---

## Next Steps

---

## What I learned

---

## How to Run


---

## Images


