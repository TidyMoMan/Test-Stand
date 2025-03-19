#include <Arduino.h>
#include "HX711.h"

const int CELL_DOUT = 2;
const int CELL_SCK = 3;

HX711 cell;

void setup() {
  Serial.begin(115200);
  cell.begin(CELL_DOUT, CELL_SCK);
}

void loop() {

  if (cell.is_ready()) {
    long reading = cell.read();
    Serial.println(reading);
  }  
}

//baseline (no attachment hardware) -> ~ -6000
//180g -> ~ -2000
//402g -> ~ 2700
//2285g -> 42500