

let arrow

function setup() {
  canvas = createCanvas(window.innerWidth, window.innerHeight);
}

function preload() {
  arrow = loadImage('arrow.png')
  console.log(arrow)
}

function draw() {
  w = window.innerWidth / 2
  h =  window.innerHeight / 2

  // Orbit
  fill('white')
  strokeWeight(4)
  stroke(51)
  circle(w, h - 200, 400)

  // Star
  fill('red')
  noStroke()
  circle(w, h - 200, 50);

  image(arrow, w -20, h -50, 200, 100)

  // planet
  fill('purple')
  circle(w, h, 30)

  // text
  text('hello', w -20, h -50)
}
