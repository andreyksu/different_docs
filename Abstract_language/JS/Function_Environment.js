'use strict'

let a = 'peer';

function outer(append){
	let b = 'beer';	
	function inner(info){
		b += append;
		console.log('%s ----- b ===== %s', info, b);
		console.log('%s ----- a ===== %s', info, a);
		try{
			console.log('%s ----- c ===== %s', info, c);	
		}catch(exception){
			console.log('ReferenceError');
			}		
    	}
	return inner;
}

a = 'Peer';

let first = outer('a');

a = 'PEer';
first('1');

let c = "Xer";
a = 'PEEr';
first('2');


a = 'PEER';


let second = outer('l');

a = 'PEERR';
second('3');


//1 ----- b ===== beera
//1 ----- a ===== PEer
//ReferenceError

//2 ----- b ===== beeraa
//2 ----- a ===== PEEr
//2 ----- c ===== Xer

//3 ----- b ===== beerl
//3 ----- a ===== PEERR
//3 ----- c ===== Xer


//Т.е. что внутренняя, что внешняя функция из глобальных переменных берет крайнее значение.