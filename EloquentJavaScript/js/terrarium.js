/**
 * I did not completely finish the terrarium example because i don't have the function like inPlacePrinter()
 * and because it becomes overly complicated.
 */
function Dictionary(startValues) {
	this.values = startValues || {};
};

Dictionary.prototype.store = function(name, value) {
	this.values[name] = value;
};

Dictionary.prototype.lookup = function(name) {
	return this.values[name];
};

Dictionary.prototype.contains = function(name) {
	return Object.prototype.hasOwnProperty.call(this.values, name)
	&& Object.prototype.propertyIsEnumerable.call(this.values,
			name);
};

Dictionary.prototype.each = function(action) {
	forEachIn(this.values, action);
};

Dictionary.prototype.names = function() {
	var names = [];
	this.each(function(name, value) {names.push(name);});
	return names;
};


var thePlan =
	["############################",
	 "#      #    #      o      ##",
	 "#                          #",
	 "#          #####           #",
	 "##         #   #    ##     #",
	 "###           ##     #     #",
	 "#           ###      #     #",
	 "#   ####                   #",
	 "#   ##       o             #",
	 "# o  #         o       ### #",
	 "#    #                     #",
	 "############################"];

function Point(x,y){
	this.x = x;
	this.y = y;
};

Point.prototype.add = function(other){
	return new Point(this.x + other.x, this.y + other.y);
};

Point.prototype.isEqualTo = function(other){
	return (this.x == other.x && this.y == other.y);
};

function Grid(width, height) {
	this.width = width;
	this.height = height;
	this.cells = new Array(width * height);
};

Grid.prototype.valueAt = function(point) {
	return this.cells[point.y * this.width + point.x];
};
Grid.prototype.setValueAt = function(point, value) {
	this.cells[point.y * this.width + point.x] = value;
};
Grid.prototype.isInside = function(point) {
	return point.x >= 0 && point.y >= 0 &&
	point.x < this.width && point.y < this.height;
};
Grid.prototype.moveValue = function(from, to) {
	this.setValueAt(to, this.valueAt(from));
	this.setValueAt(from, undefined);
};
Grid.prototype.each = function(action){
	for(var y = 0; y < this.height; y++){
		for(var x = 0; x < this.width; x++){
			var point = new Point(x, y);
			action(point, this.valueAt(point));
		};
	};
};

var directions = new Dictionary(
		{"n":  new Point( 0, -1),
			"ne": new Point( 1, -1),
			"e":  new Point( 1,  0),
			"se": new Point( 1,  1),
			"s":  new Point( 0,  1),
			"sw": new Point(-1,  1),
			"w":  new Point(-1,  0),
			"nw": new Point(-1, -1)});

function StupidBug() {};
StupidBug.prototype.act = function(surroundings) {
	return {type: "move", direction: "s"};
};

var wall = {};

function Terrarium(plan) {
	var grid = new Grid(plan[0].length, plan.length);
	for (var y = 0; y < plan.length; y++) {
		var line = plan[y];
		for (var x = 0; x < line.length; x++) {
			grid.setValueAt(new Point(x, y),
					elementFromCharacter(line.charAt(x)));
		}
	}
	this.grid = grid;
}

function elementFromCharacter(character) {
	if (character == " ")
		return undefined;
	else if (character == "#")
		return wall;
	else if (character == "o")
		return new StupidBug();
}

wall.character = "#";
StupidBug.prototype.character = "o";

function characterFromElement(element) {
	if (element == undefined)
		return " ";
	else
		return element.character;
};

Terrarium.prototype.toString = function (){
	/**
	 * This is a simple version of the toString function, just for testing
	 * 
	 * this.grid.each(function(point, value){console.log(point.x + ": " + point.y + ": " + characterFromElement(value));});
	 * 
	 */
	var res = "";
	w = this.grid.width-1;
	this.grid.each(function(p,v){ 
		if (p.x == w)
			res = res + characterFromElement(v) + "\n";
		else
			res = res + characterFromElement(v);});
	return res;

};

Terrarium.prototype.listActingCreatures = function() {
	var found = [];
	this.grid.each(function(point, value) {
		if (value != undefined && value.act)
			found.push({object: value, point: point});
	});
	return found;
};


/**
 * This is my version of listSurroundings. It seems to work, but check the one in the book too.
 */

Terrarium.prototype.listSurroundings = function(center){
	var g = this.grid;
	var result ={};
	directions.each(function(name, dir){
		var p = center.add(dir);
		if (g.isInside(p))
			result[name]= characterFromElement(g.valueAt(p));
		else
			result[name] ="#";
	}
	);
	return result;
};


/**
 * Check this function - processCreature - I don't understand how it works.
 * creature.point, creature.object --> listActingCreatures returns an array of objects, each object has two properties: object and point
 * 
 * The function processCreature is called on the array returned by listActingCreatures
 */

Terrarium.prototype.processCreature = function(creature) {
	var surroundings = this.listSurroundings(creature.point);
	var action = creature.object.act(surroundings);
	if (action.type == "move" && directions.contains(action.direction)) {
		var to = creature.point.add(directions.lookup(action.direction));
		if (this.grid.isInside(to) && this.grid.valueAt(to) == undefined)
			this.grid.moveValue(creature.point, to);
	}
	else {
		throw new Error("Unsupported action: " + action.type);
	}
};

function bind(func, object) {
	return function(){
		return func.apply(object, arguments);
	};
}

Terrarium.prototype.step = function() {
	forEach(this.listActingCreatures(),
			bind(this.processCreature, this));
};

Terrarium.prototype.start = function() {
	if (!this.running)
		this.running = setInterval(bind(this.step, this), 500);
};

Terrarium.prototype.stop = function() {
	if (this.running) {
		clearInterval(this.running);
		this.running = null;
	}
};


var creatureTypes = new Dictionary();
creatureTypes.register = function(constructor) {
	this.store(constructor.prototype.character, constructor);
};

function elementFromCharacter(character) {
	if (character == " ")
		return undefined;
	else if (character == "#")
		return wall;
	else if (creatureTypes.contains(character))
		return new (creatureTypes.lookup(character))();
	else
		throw new Error("Unknown character: " + character);
};

function BouncingBug() {
	this.direction = "ne";
}
BouncingBug.prototype.act = function(surroundings) {
	if (surroundings[this.direction] != " ")
		this.direction = (this.direction == "ne" ? "sw" : "ne");
	return {type: "move", direction: this.direction};
};
BouncingBug.prototype.character = "%";

creatureTypes.register(BouncingBug);


function randomElement(array) {
	if (array.length == 0)
		throw new Error("The array is empty.");
	return array[Math.floor(Math.random() * array.length)];
}

function DrunkBug() {};
DrunkBug.prototype.act = function(surroundings) {
	return {type: "move",
		direction: randomElement(directions.names())};
};
DrunkBug.prototype.character = "~";

/**
 * Using the clone function to simulate inheritance
 */

function clone(object) {
	function OneShotConstructor(){}
	OneShotConstructor.prototype = object;
	return new OneShotConstructor();
};

function LifeLikeTerrarium(plan) {
	Terrarium.call(this, plan);
}
LifeLikeTerrarium.prototype = clone(Terrarium.prototype);
LifeLikeTerrarium.prototype.constructor = LifeLikeTerrarium;

