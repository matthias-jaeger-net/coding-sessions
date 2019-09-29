/**
 * Method that draws a single Smiley
 * @param x Coordinate x-position
 * @param y Coordinate y-positon
 * @param w Width of the object
 * @param h Height of the object
 */
void Smiley(float x, float y, float w, float h) 
{
  // Random parameters of a Smiley
  float eyeOffsetX   = w * 0.20 * random(0, 1);
  float eyeOffsetY   = h * 0.17 * random(0, 1);
  float eyeWidth     = w * 0.20 * random(0, 1);
  float eyeHeight    = h * 0.20 * random(0, 1);
  float pupil        = eyeWidth * random(0, 1);
  float smileWidth   = w * 0.50 * random(0, 1);
  float smileHeight  = w * 0.35 * random(0, 1);
  float smileOffsetY = w * 0.09 * random(0, 1);

  // Colors of the smiley
  color smileyBase   = color(int(#F7D416));
  color smileyEye    = color(int(#EDECE4));
  color smileyPupil  = color(int(#535353));
  color smileyMouth  = smileyPupil;

  // Drawing the parameters
  noStroke();

  fill(smileyBase);
  ellipse(x, y, w, h);

  fill(smileyEye);
  ellipse(x - eyeOffsetX, y - eyeOffsetY, eyeWidth, eyeHeight);
  ellipse(x + eyeOffsetX, y - eyeOffsetY, eyeWidth, eyeHeight);

  fill(smileyPupil);
  ellipse(x - eyeOffsetX, y - eyeOffsetY, pupil, pupil);
  ellipse(x + eyeOffsetX, y - eyeOffsetY, pupil, pupil);

  fill(smileyMouth);
  arc(x, y + smileOffsetY, smileWidth, smileHeight, 0, PI);
}

/**
 * A processing program using the Smiley Method
 */
void setup() 
{
  // Define the size of the canvas
  size(1200, 800);
  
  // Clear the canvas with white
  background(255);
  
  // Make a grid of Smileys
  int smileWidth  = 100;
  int smileHeight = 100;
  for (int row = 0; row < smileWidth; row++) {
    for (int col = 0; col < smileHeight; col++) {
      int x = row * smileWidth;
      int y = col * smileHeight;
      Smiley(x, y, smileWidth * 0.9, smileHeight * 0.9);
    }
  }
  
  // Export the image
  save("smiles.jpg");
  
  // Done 
  exit();
}
