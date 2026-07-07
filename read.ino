const int analogPin = A0;
int rawValue = 0;
float voltage = 0.0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  rawValue = analogRead(analogPin);
  Serial.println(rawValue);
  delay(100);
}