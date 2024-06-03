#include <Wire.h>

void setup() {
  Serial.begin(9600);
  Wire.begin(7);  // Comienza como maestro
  Wire.onReceive(receiveEvent);
}

void receiveEvent(int howMany) {
  while (Wire.available()) { // Mientras haya datos disponibles
    char c = Wire.read(); // Lee los datos enviados por el maestro
    Serial.print(c); // Opcional: imprimir los datos para depuración
  }
  Serial.println(); // Salto de línea después de la lectura completa
}

void loop() {
  if (Serial.available()) {
    String str = Serial.readString();

    Wire.beginTransmission(8);  // Dirección del Arduino esclavo
    Wire.write(str.c_str());
    Wire.endTransmission();
    delay(100);  // Da tiempo para procesar
  }
}