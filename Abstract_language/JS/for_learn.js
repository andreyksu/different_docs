function F(){
	let local_var = "Lolal_var";
	this.hello = "hello";
	this.fff = function (){
		console.log(this.hello);
	}
	let ffff = function(){
		console.log(local_var);
	}
	ffff();
	return ffff;
}

console.log("F = ", F)
console.log("F.prototype = ", F.prototype);
console.log("F.prototype.constructor = ", F.prototype.constructor)
console.log("F.__proto__", F.__proto__)

let param = F();
param();

/*

var ff = new F();

console.log("ff = ", ff)
console.log("ff.__proto__ = ", ff.__proto__);
console.log("ff.__proto__.constructor = ", ff.__proto__.constructor);

function A(){
        this.a = "aaa";
        
        this.inerA = function (){
            console.log("From Function innerA");
        }
    }
    
    function B() {
        this.b = "bbb";        
        
        this.inerB = function (){
            console.log("From Function innerB");
        }        
    }
    
    function C(name) {
        this.c = "ccc";
        
        this.inerC = function(){
            console.log("From Function innerC");
        }
        this.inerC();
    }
    
    A.prototype.outerA = function(){
        console.log("From Function outerA");
    }
    
    //a = new A();    
    //B.prototype = a; // B.prototype используется одни раз только при new B(); и все.
    console.log("B.prototype.constructor = ", B.prototype.constructor);
    B.prototype = new A(); //Важно, что таким образом мы терям конструктор B - и остается единственный конструктор А. В таком случае нужно прямо в constructor засунуть B.prototype.constructor = B
    console.log("B.prototype.constructor = ", B.prototype.constructor); //Важно. что 
    B.prototype.outerB = function (){
        console.log("From Function outerB");
    }//здесь мы записал в объект "a" фнукцию outerB.  Ибо прототип указывает на объект "а". А вот в объекте "а" есть прототип куда записан outerA()
    //b = new B();    
    //C.prototype = b;
    C.prototype = new B();
    C.prototype.outerC2 = function (){
        console.log("From Function outerC2");
    }
c = new C();

*/