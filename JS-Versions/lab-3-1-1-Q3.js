// First name validator

let firstName = prompt("Please enter your first name: ").trim();

function correctName(firstName) {
    // Convert the firstName to title case, there is no inbuilt function for this so we will have to write our own
    let titleCase = firstName[0].toUpperCase() + firstName.slice(1).toLowerCase();
    //also needs to convert the first letter after a space or hyphen to uppercase
    for (let i = 0; i < titleCase.length; i++) {
        if (titleCase[i] === " " || titleCase[i] === "-") {
            titleCase = titleCase.slice(0, i + 1) + titleCase[i + 1].toUpperCase() + titleCase.slice(i + 2);
        }
    }

    return titleCase;
}

// Check if the first name is valid
// A valid name only contains letters, spaces and hyphens.

function isValidName(firstName) {
    let regex = /^[a-zA-Z\s-]+$/;
    return regex.test(firstName);
    console.log(regex.test(firstName));
}

alert("Your first name is " + correctName(firstName) + " and it is " + isValidName(firstName) + " that it is valid.");