/**
 * Square is an object with properties and methods.
 */

var Square = {
		construct: function(character, tableCell) {
			this.background = "empty";
			if (character == "#")
				this.background = "wall";
			else if (character == "*")
				this.background = "exit";

			this.tableCell = tableCell;
			this.tableCell.className = this.background;

			this.content = null;
			if (character == "0")
				this.content = "boulder";
			else if (character == "@")
				this.content = "player";
			/* Note the images for wall, empty and exit are managed via the css style sheet, not here */
			if (this.content != null) {
				var image = dom("IMG", {src: "img/sokoban/" + this.content + ".gif"});
				console.log("img/sokoban/" + this.content + ".gif");
				this.tableCell.appendChild(image);
			}
		},

		hasPlayer: function() {
			return this.content == "player";
		},
		hasBoulder: function() {
			return this.content == "boulder";
		},
		isEmpty: function() {
			return this.content == null && this.background == "empty";
		},
		isExit: function() {
			return this.background == "exit";
		},
		moveContent: function(destSquare){
			destSquare.content = this.content;
			this.content = null;
			if (destSquare.content != null) {
				var image = dom("IMG", {src: "img/sokoban/" +
					destSquare.content + ".gif"});
				destSquare.tableCell.appendChild(image);
			}
		},
		clearContent:  function() {
			this.content = null;
			removeElement(this.tableCell.lastChild);
		}
};

/**
 * SokobenField has a constructor to which is given an object from the sokobanLevels array, 
 * and is responsible for building both a table of DOM nodes and a grid of Square objects.
 * SokobanField will also take care of the details of moving the player and boulders around.
 */

var SokobanField = {
		construct: function(level) {
			var tbody = dom("TBODY"); /* TBODY is an HTML tag; Table Body. So tbody is a DOM node (the function dom returns a node) */
			this.squares = [];
			this.bouldersToGo = level.boulders; /* the property boulders holds the number of boulders in the level */

			for (var y = 0; y < level.field.length; y++) {
				var line = level.field[y];
				var tableRow = dom("TR");
				var squareRow = [];
				for (var x = 0; x < line.length; x++) {
					var tableCell = dom("TD");
					tableRow.appendChild(tableCell);
					/**
					 * The code in the book var square = Square.create(line.charAt(x), tableCell);
					 * does not work. So I changed it using Object.create and then square.construct
					 */
					
					var square = Object.create(Square);
						square.construct(line.charAt(x), tableCell);
					squareRow.push(square);
					if (square.hasPlayer())
						this.playerPos = new Point(x, y); /* Point is defined in terrarium.js */
				}
				tbody.appendChild(tableRow); /* row added to table body */
				this.squares.push(squareRow);
			}

			this.table = dom("TABLE", {"class": "sokoban"}, tbody); /* A TABLE node is created with class sokoban and tbody is added as child */
			this.score = dom("DIV", null, "...");
			this.updateScore();
		},

		getSquare: function(position) {
			return this.squares[position.y][position.x];
		},
		updateScore: function() {
			this.score.firstChild.nodeValue = this.bouldersToGo + 
			" boulders to go.";
		},
		won: function() {
			return this.bouldersToGo <= 0;
		}
};

SokobanField.place = function(where) {
	where.appendChild(this.score);
	where.appendChild(this.table);
};
SokobanField.remove = function() {
	removeElement(this.score);
	removeElement(this.table);
	}; 

SokobanField.move = function(direction){
		goingto = this.playerPos.add(direction); /* point where I'm trying to go */
		goingtosquare = this.getSquare(goingto);
		playersquare = this.getSquare(this.playerPos);
		if (goingtosquare.isEmpty()){
				console.log("Moving player into empty square...");
				playersquare.moveContent(goingtosquare);
				playersquare.clearContent();
				this.playerPos = goingto;
		}
		else {
			if (goingtosquare.hasBoulder()){
				console.log("There is a boulder ...");
				beyondBoulder = goingto.add(direction);
				beyondBouldersquare = this.getSquare(beyondBoulder);
				if (beyondBouldersquare.isExit()){
					console.log("There is an exit ...");
					this.bouldersToGo--;
					this.updateScore();
					goingtosquare.clearContent();
					playersquare.moveContent(goingtosquare);
					playersquare.clearContent();
					this.playerPos = goingto;
				}
				if (beyondBouldersquare.isEmpty()){
					console.log("Just push the boulder ...");
					goingtosquare.moveContent(beyondBouldersquare);
					goingtosquare.clearContent();
					playersquare.moveContent(goingtosquare);
					playersquare.clearContent();
					this.playerPos = goingto;
				}
			}
			
		}

	};
	
	var SokobanGame = {
			construct: function(place) {
				this.level = null;
				this.field = null;

				var newGame = dom("BUTTON", null, "New game");
				// Considering how the tag BUTTON works, adding New Game as a text node (which is what the dom function does)
				// is what we need to show New Game as the label of the button
				addHandler(newGame, "click", method(this, "newGame")); // I don't understand this syntax with method. I understand it calls newGame, but I never saw this syntax
				var reset = dom("BUTTON", null, "Reset level"); // same as the newGame button
				addHandler(reset, "click", method(this, "reset")); // I don't understand what method is
				
				this.container = dom("DIV", null, dom("H1", null, "Sokoban"), dom("DIV", null, newGame, " ", reset)); // The nodes newGame, reset and
				// HI are added to the DIV node created here. Thenk with the code below the DIV node is appended to place. 
				
				place.appendChild(this.container);

				addHandler(document, "keydown", method(this, "keyDown"));
				this.newGame();
			},

			newGame: function() {
				this.level = 0;
				this.reset();
			},
			reset: function() {
				if (this.field)
					this.field.remove();
				// var sokobanField = Object.create(SokobanField);
				this.field = Object.create(SokobanField);
				this.field.construct(sokobanLevels[this.level]);
				this.field.place(this.container);
			},

			keyDown: function(event) {
				// To be filled in
				
				var arrowKeyCodes = new Dictionary({
					  37: new Point(-1, 0), // left
					  38: new Point(0, -1), // up
					  39: new Point(1, 0),  // right
					  40: new Point(0, 1)   // down
					});
				event = event || window.event;
				norm_event = normaliseEvent(event);
				
				var charCode = norm_event.keyCode;
				if (arrowKeyCodes.contains(charCode)){
					this.field.move(arrowKeyCodes.lookup(charCode));
					norm_event.stop;
				}
				
				
				if(this.field.won() && this.level == sokobanLevels.length-1){
					alert("You won the game!! Now starting a new game....");
					this.newGame();
				}
				else if(this.field.won() && this.level < sokobanLevels.length-1){
					alert("You won the level!! Going to next level....");
					this.level++;
					this.reset();
				}
				
			}
	};
	
/** sokobanLevels represents the levels of the game in text format
 * for some reason when I copied it from the book most of the spaces are cut.
 * So I amended just the first value adding the spaces. Not all the others.
 * It means just the first level will render properly on the screen
 */	
	var sokobanLevels = [
{field: ["###### ##### ",
         "#   #   #  # ",
         "# 0 #### 0 # ",
         "# 0  @  0  # ",
         "#  ######0 # ",
         "####  ### ###",
         "        #   #",
         "       #0   #",
         "       # 0  #",
         "      ## 0  #",
         "      #*0 0 #",
         "     ########"],
boulders: 10},
{field: ["########### ",
"# # # ",
"# 00#00 @# ",
"# 0 # ",
"# # # ",
"## ######### ",
"# 0 # # ",
"# 00 #0 0 0# ",
"# 0 0 # ",
"# 000#0 0 ###",
"# # 0 0 *#",
"##############"],
boulders: 20},
{field: ["########## ",
"#@ *# ",
"# ## ",
"####### ######",
" # #",
" # 0 0 0 0 0 #",
"######## #####",
"# 0 0 0 0 #",
"# 0 #",
"##### ########",
" # 0 0 0 # ",
" # 0 # ",
" # 0 0 0 ## ",
"####### #### ",
"# 0 # ",
"# # ",
"# ###### ",
"##### "],
boulders: 16},
{field: [" #### ",
"## @######## ",
"# # ",
"# 0#####0# # ",
"# # # 0 # ",
"# 0 0 0## ",
"# 0 0 # # ",
"# ####0 ## # ",
"# 0 0 # ## ",
"# ###0# 0 ##",
"# # 0# 0 *#",
"# 0 ####",
"##### # # ",
" ####### "],
boulders: 12},
{field: ["###### #####",
"# #*## ## #",
"# #### 0 #",
"# 00 # # 0 #",
"## 00# 00 ##",
" #0 0 #0 # ",
" # 00 # # 0# ",
" # 0 0#### 0 # ",
" # # ## ",
" #### 0 # ## ",
" ### ## # ",
" # 0 # ",
" #@ # # ",
" ####### "],
boulders: 18}]; 