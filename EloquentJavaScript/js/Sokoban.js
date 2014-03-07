/**
 * Square is an object with properties and methods.
 * Looking at the example in Ch 13 it looks like the method "construct" is called every time a new Square object is created
 * I did not expect that and I did not understand why it happens
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

			if (this.content != null) {
				var image = dom("IMG", {src: "img/sokoban/" +
					this.content + ".gif"});
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

var SokobanField = {
		construct: function(level) {
			var tbody = dom("TBODY");
			this.squares = [];
			this.bouldersToGo = level.boulders;

			for (var y = 0; y < level.field.length; y++) {
				var line = level.field[y];
				var tableRow = dom("TR");
				var squareRow = [];
				for (var x = 0; x < line.length; x++) {
					var tableCell = dom("TD");
					tableRow.appendChild(tableCell);
					var square = Square.create(line.charAt(x), tableCell);
					squareRow.push(square);
					if (square.hasPlayer())
						this.playerPos = new Point(x, y);
				}
				tbody.appendChild(tableRow);
				this.squares.push(squareRow);
			}

			this.table = dom("TABLE", {"class": "sokoban"}, tbody);
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