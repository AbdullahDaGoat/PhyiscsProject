// Written by Abdullah Khan

#define STEPPER_PIN_1 9
#define STEPPER_PIN_2 10
#define STEPPER_PIN_3 11
#define STEPPER_PIN_4 12

int step_number = 0;
const int step_sequence[4][4] = {
  {HIGH, HIGH, LOW, LOW},
  {LOW, HIGH, HIGH, LOW},
  {LOW, LOW, HIGH, HIGH},
  {HIGH, LOW, LOW, HIGH}
};

void setup() {
  // Set all the stepper motor pins as outputs
  pinMode(STEPPER_PIN_1, OUTPUT);
  pinMode(STEPPER_PIN_2, OUTPUT);
  pinMode(STEPPER_PIN_3, OUTPUT);
  pinMode(STEPPER_PIN_4, OUTPUT);
}

void loop() {
  // Move the stepper motor 1000 steps in a counter-clockwise direction
  for (int a = 0; a < 1000; a++) {
    OneStep(false);  // Always move in counter-clockwise direction
    delay(2);        // Increase delay between steps if motor needs more time to start
  }

  // Uncomment the following line to stop the motor
  // stopMotor();
}

void OneStep(bool dir) {
  // Always move in counter-clockwise direction
  digitalWrite(STEPPER_PIN_1, step_sequence[step_number][0]);
  digitalWrite(STEPPER_PIN_2, step_sequence[step_number][1]);
  digitalWrite(STEPPER_PIN_3, step_sequence[step_number][2]);
  digitalWrite(STEPPER_PIN_4, step_sequence[step_number][3]);

  // Increment or decrement the step number
  if (dir) {
    step_number++;
    if (step_number > 3) {
      step_number = 0;
    }
  } else {
    step_number--;
    if (step_number < 0) {
      step_number = 3;
    }
  }
}

// Function to stop the motor
void stopMotor() {
  digitalWrite(STEPPER_PIN_1, LOW);
  digitalWrite(STEPPER_PIN_2, LOW);
  digitalWrite(STEPPER_PIN_3, LOW);
  digitalWrite(STEPPER_PIN_4, LOW);
}
