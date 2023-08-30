function startBurger() {
    return new Promise((resolve, reject) => {
        console.log("walking to the butcher...");
        setTimeout(() => {
            console.log("getting the beef from the butcher");
            resolve("beef");
        }, 2000)
    })
}


startBurger()
    .then(meatType => {
        console.log("getting the buns from the bakery");
        return [meatType, "whole grains"];
    })
    .then(([bunsType, meatType]) => {
        console.log("preparing the burger...");
        console.log(`The ${meatType} burger with ${bunsType} buns is created`);
    })


let goodGrades = true;

let endSemester = new Promise(function (resolve, reject) {
    if (goodGrades) {
        resolve("I will get a gift");
    } else {
        reject("I won't get the gift");
    }
});

endSemester.then(function (fromResolve) {
    console.log(fromResolve);
}
).catch(function (fromReject) {
    console.log(fromReject);
}
)
console.log("end of semester");
