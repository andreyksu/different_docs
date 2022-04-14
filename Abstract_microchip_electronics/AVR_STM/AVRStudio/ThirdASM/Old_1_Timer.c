#define F_CPU 4000000UL
#define DIVISOR 1024
#define DELTA_TIME 20

#define COUNT (20/(DIVISOR/F_CPU)) //78 = 0100 1110 =4E

#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/wdt.h>

volatile unsigned char toggel = 0;
volatile unsigned char tick = 0;

ISR(TIMER0_COMP_vect){

	/*
	if(toggel == 0){
		PORTB = 0x78;
		toggel++;
	}else{
		PORTB = 0x00;
		toggel = 0;
	}
	*/
	PORTB = 0x00;
	
}


void init(){
	//T0
	cli();
	wdt_reset();
	WDTCR = 0xFF;
	WDTCR = 0x10;
	

	TCCR0=(0<<WGM00) | (0<<COM01) | (0<<COM00) | (1<<WGM01) | (1<<CS02) | (0<<CS01) | (1<<CS00); //TCCR0 = 0b00001101;
	TCNT0=0x00;
	OCR0=0x78;	//OCR0=0x78;	//OCR0 = 0b01001110;	
	TIMSK = 0b00000010;
	sei();

	//I/O
	DDRB = 0b11111111;
}

int main(void){	
	init();
	PORTB = 0b00000000;

	while(1){
		if(tick == TCNT0){
			tick++;
			PORTB = TCNT0;
		}
		asm volatile("nop");
	}
	return 0;
}
