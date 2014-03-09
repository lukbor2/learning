/**
 * 
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









