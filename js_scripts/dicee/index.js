
// Getting all the required html items using queryselector
const image1 = document.querySelector(".img1")
const image2 = document.querySelector(".img2")
const heading = document.querySelector("h1")
const roll = document.querySelector(".roll-btn")


// showRandomDice Method
const showRandomDice = () => {
    const randomNumber1 = Math.floor(Math.random() * 6) + 1  // Creates a random number for dice 1
    const randomNumber2 = Math.floor(Math.random() * 6) + 1  // Creates a random number for dice 2
    const dice1 = "images/dice" + randomNumber1 + ".png";    // Creates the image path for dice 1 according to its number
    const dice2 = "images/dice" + randomNumber2 + ".png";    // Creates the image path for dice 2 according to its number
    image1.setAttribute("src", dice1)                        // Sets the image for dice 1 to the image created in the previous step
    image2.setAttribute("src", dice2)                        // Sets the image for dice 2 to the image created in the previous step
    if (randomNumber1 > randomNumber2) {                     // Check which dice has greater value 
        heading.innerText = "🚩Player 1 Won"                 // If dice1 then sets the heading to '🚩 Player 1 Won'
    } else if (randomNumber1 < randomNumber2) {              // Else If dice2 then sets the heading to 'Player 2 Won 🚩'
        heading.innerText = "Player 2 Won 🚩"
    } else {                                                // Else sets the heading to 'Draw!'
        heading.innerText = "Draw!"
    }
}


// Add click event listener to roll  variable (means to the 'roll-btn' class)
roll.addEventListener("click", () => {
    // Call the showandomDice method to generate  random dice number for each dice and display the dice images accordingly
    showRandomDice();
})