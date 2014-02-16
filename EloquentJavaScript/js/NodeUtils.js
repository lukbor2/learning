/**
Some utilities to create nodes. From Chapter 12 
 **/

/**
 * The dom function creates a DOM node.
 * Its first argument gives the tag name of the node, its second argument is an object containing the attributes of the node, 
 * or null when no attributes are needed.
 * After that, any amount of arguments may follow, and these are added to the node as child nodes. 
 * When strings appear here, they are first put into a text node.
 */

function dom(name, attributes) {
	var node = document.createElement(name);
	if (attributes) {
		forEachIn(attributes, function(name, value) {
			setNodeAttribute(node, name, value);
/**
 * the forEachIn function uses attributes as object and calls the action
 * using object and object[property], so object[property] is where the value of the
 * attribute to set comes from.
 */
			
		});
	}
	for (var i = 2; i < arguments.length; i++) {
		var child = arguments[i];
		if (typeof child == "string")
			child = document.createTextNode(child);
		node.appendChild(child);
	}
	return node;
}

/**
 * The function setNoteAttribute manages the exception driven by old
 * versions of Internet Explorer (see Chapter 12).
 * But basically it just sets the value of a given attribute in a given node.
 **/
function setNodeAttribute(node, attribute, value) {
	if (attribute == "class")
		node.className = value;
	else if (attribute == "checked")
		node.defaultChecked = value;
	else if (attribute == "for")
		node.htmlFor = value;
	else if (attribute == "style")
		node.style.cssText = value;
	else
		node.setAttribute(attribute, value);
}

function removeElement(node){
	if (node.parentNode){
		node.parentNode.removeChild(node);
	}
	
	
}