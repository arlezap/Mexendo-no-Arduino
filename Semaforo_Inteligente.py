// Definindo os pinos
const int pinLuzVerde = 8;    // Pino para o LED verde
const int pinLuzAmarela = 9;  // Pino para o LED amarelo
const int pinLuzVermelha = 10; // Pino para o LED vermelho
const int pinBuzzer = 7;      // Pino para o buzzer

#define emissorTrig 6
#define recepEcho 5

long duracao;
int distancia;

// Definindo os tempos
const int tempoAmarelo = 2000; // Tempo da luz amarela em milissegundos
const int tempoBuzzer = 100;    // Tempo do buzzer em milissegundos
const int tempoVermelho = 5000; // Tempo do LED vermelho em milissegundos

void setup() {
  // Configurando os pinos como saída
  pinMode(pinLuzVerde, OUTPUT);
  pinMode(pinLuzAmarela, OUTPUT);
  pinMode(pinLuzVermelha, OUTPUT);
  pinMode(pinBuzzer, OUTPUT);
  pinMode(emissorTrig, OUTPUT);
  pinMode(recepEcho, INPUT);
  
  // Inicialmente, todos os LEDs e o buzzer estão desligados
  digitalWrite(pinLuzVerde, HIGH); // O LED verde começa aceso
  digitalWrite(pinLuzAmarela, LOW);
  digitalWrite(pinLuzVermelha, LOW);
  digitalWrite(pinBuzzer, LOW);

  Serial.begin(9600);
}

void loop() {
  // Faz a leitura da distância
  dist();

  // Se houver algo detectado, acende o LED amarelo e depois o vermelho
  if (distancia < 30) {
    // Desliga o LED verde
    digitalWrite(pinLuzVerde, LOW);

    // Acende o LED amarelo por 1 segundo
    digitalWrite(pinLuzAmarela, HIGH);
    delay(tempoAmarelo);
    digitalWrite(pinLuzAmarela, LOW);
    
    // Acende o LED vermelho
    digitalWrite(pinLuzVermelha, HIGH);
    
    // Aciona o buzzer enquanto o LED vermelho estiver aceso
    digitalWrite(pinBuzzer, HIGH);
    
    // Aguarda 5 segundos com o LED vermelho e buzzer acesos
    delay(tempoVermelho);
    
    // Desliga o LED vermelho e o buzzer
    digitalWrite(pinLuzVermelha, LOW);
    digitalWrite(pinBuzzer, LOW);

    // Acende novamente o LED verde
    digitalWrite(pinLuzVerde, HIGH);
  }
}

void dist() {
  digitalWrite(emissorTrig, LOW);
  delayMicroseconds(2);
  digitalWrite(emissorTrig, HIGH);
  delayMicroseconds(10);
  digitalWrite(emissorTrig, LOW);
  duracao = pulseIn(recepEcho, HIGH);
  distancia = duracao * 0.034 / 2;
  Serial.println(distancia);
}
