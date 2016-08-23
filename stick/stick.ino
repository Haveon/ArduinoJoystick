int zeroX = 515;
int zeroY = 501;

void setup() {
  Serial.begin(9600);
}

void loop() {
  // Check to see if there is a byte to read in buffer
  if (Serial.available()>0){
    // Remove byte from buffer
    Serial.read();
    
    // Read joystick
    int x = analogRead(A0) - zeroX;
    int y = analogRead(A1) - zeroY;
    int sel = !digitalRead(7);
    
    // Send data back on wire
    Serial.print(x);
    Serial.print(",");
    Serial.print(y);
    Serial.print(",");
    Serial.println(sel);
  }
}
