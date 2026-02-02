
void setup() {
  Serial.begin(115200);
  Serial1.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT); // Built-in LED
}

void loop() {
  int val = analogRead(A0);

  // Send to Laptop
  Serial.println(val);
  
  // Send to Linux
  Serial1.println(val);

  // Blink the LED so we know the code is alive!
  digitalWrite(LED_BUILTIN, HIGH);
  delay(50);
  digitalWrite(LED_BUILTIN, LOW);
  delay(50);
}
