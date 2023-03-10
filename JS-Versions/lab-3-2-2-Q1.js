// Triangle analysis

// This program reads in the lengths of the sides of a triangle and
// determines the type of triangle from the following classifications:
//   Equilateral: All sides are equal
//   Isosceles: Exactly two sides are equal
//   Scalene: All sides are different
//   Not a triangle: The sum of any two sides is less than or equal to the

const triEqual = "Equilateral";
const triIsos = "Isosceles";
const triScal = "Scalene";

let side1 = prompt("Enter the length of side 1: ");
let side2 = prompt("Enter the length of side 2: ");
let side3 = prompt("Enter the length of side 3: ");

// Check that all sides are valid numbers
if (isNaN(side1) || isNaN(side2) || isNaN(side3)) {
    console.log("Invalid input");
} else {
    // Convert string to float
    side1 = parseFloat(side1);
    side2 = parseFloat(side2);
    side3 = parseFloat(side3);

    // Check that all sides are positive
    if (side1 <= 0 || side2 <= 0 || side3 <= 0) {
        alert("Invalid input");
    } else {
        if (side1 == side2 == side3) {
            alert(`Triangle type is ${triEqual}`);
        } else if (side1 == side2 || side1 == side3 || side2 == side3) {
            alert(`Triangle type is ${triIsos}`);
        } else {
            alert(`Triangle type is ${triScal}`);
        }
    }
}