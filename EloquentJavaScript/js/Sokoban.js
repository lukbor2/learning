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
		}
};