.include "m8def.inc"

; Start macro.inc ===============================================================================================================================================
								
;= End macro.inc  ===============================================================================================================================================
 
 
; RAM ===========================================================================================================================================================
		.DSEG
; FLASH =========================================================================================================================================================
		.CSEG

.ORG 0x000
	RJMP 	Inital_Restart	
.ORG INT0addr
	RETI
.ORG INT1addr
	RETI
.ORG OC2addr
	RETI
.ORG OVF2addr
	RETI
.ORG ICP1addr
	RETI
.ORG OC1Aaddr
	RETI
.ORG OC1Baddr
	RETI
.ORG OVF1addr
	RETI
.ORG OVF0addr
	RETI
.ORG SPIaddr
	RETI
.ORG URXCaddr
	RETI
.ORG UDREaddr
	RETI
.ORG UTXCaddr
	RETI
.ORG ADCCaddr
	RETI
.ORG ERDYaddr
	RETI
.ORG ACIaddr
	RETI
.ORG TWIaddr
	RETI
.ORG SPMRaddr
	RETI


Inital_Restart:
		LDI		R16,Low(RAMEND)
		OUT		SPL,R16

		LDI		R16,High(RAMEND)
		OUT		SPH,R16

		SEI							; разрешаем глобальные прерывания
		LDI		R17, (1<<RXCIE)		; разрешаем прерывание по приему байта.
		OUT		UCSRB, R17

		RJMP	MainLoop

MainLoop:
		LDI		R16, 3
		SBRS 	R16, 3				; если 3ий бит 1 в R16 то перепрыгиваем через команду. SBRC - аналогично но для 0_ля. Аналогичные команды SBIC/SBIS но для регистров перефирии. Но для первых 1f регистров.									
		RCALL	None				; но так как у нас 3ий 0 то мы попадаем на команду
									; а можно и так ANDI	R16,1<<2 - т.е. накладываем побитовую маску 00000100 т.е. & и если получим 0 получаем, что в этом регистре в R16 был 0, то идем смотреть фла z и прыгаем командой BREQ.
		LDI		R17, 5
CPP:	CP		R16, R17			; производится вычитание из R16 значения R17. Вычитание производится внутри без влияения на регистры. Если выскочил Z то идем на метку.
		BREQ	Plus
		RJMP MainLoop

None:
		NOP
		RET
		

Plus:
		INC		R16
		RJMP 	CPP				
									;INC 	Rd 	Increment 				Rd = Rd + 1 		Z,N,V 	
									;DEC 	Rd 	Decrement 				Rd = Rd - 1  		Z,N,V 	
									;TST 	Rd 	Test for Zero or Minus 	Rd = Rd AND Rd  	Z,N,V 	
									;CLR 	Rd 	Clear Register 			Rd = Rd XOR Rd		Z,N,V 	
									;SER 	Rd 	Set Register 			Rd = $FF 			None

; EEPROM ==================================================
			.ESEG			; Сегмент EEPROM
