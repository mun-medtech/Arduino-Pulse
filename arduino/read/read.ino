const int analogPin = A0;
int rawValue = 0;
float voltage = 0.0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  rawValue = analogRead(analogPin);
  voltage = rawValue * (5.0 / 1023.0);

  Serial.print("Raw: ");
  Serial.print(rawValue);
  Serial.print("  |  Voltage: ");
  Serial.print(voltage, 2);
  Serial.println(" V");

  delay(500);
}