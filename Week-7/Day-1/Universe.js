// define the array of planets
const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];


planets.forEach((planet, index) => {
  const planetDiv = document.createElement("div");
  planetDiv.classList.add("planet");
  planetDiv.classList.add(`planet-${index + 1}`); // add class for background color
  planetDiv.textContent = planet;
  
  // append planet div to the section
  const universeSection = document.getElementById("universe");
  universeSection.appendChild(planetDiv);
});


