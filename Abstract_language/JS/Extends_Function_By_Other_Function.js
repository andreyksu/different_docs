function Hero(name, level) {
	this.name = name;
	this.level = level;
}

Hero.prototype.greet = function() {
	return `${this.name} says hello.`;
};

function Mage(name, level, spell) {
	Hero.call(this, name, level);
	this.spell = spell;
}

//Mage.prototype = Object.create(Hero.prototype)

mage = new Mage('Le', 2, 'Maj')
console.log(mage.name)
console.log(mage.greet())

hero = new Hero('Me', 3)
console.log(hero.greet())