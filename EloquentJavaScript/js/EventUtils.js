/**
 * Some functions used for event handling
 */

function registerEventHandler(node, event, handler){
	/** the function assumes the event parameter matches what is expected by adding the
	 * event listener.
	 * And with IE the event name is the same with "on" before it.
	 * Furthermore the parameter node represents the id of the node
	 */

	if(node.addEventListener)
		node.addEventListener(event, handler, false);
	else if (node.attachEvent)
		node.attachEvent("on" + event, handler);

}

function unregisterEventHandler(node, event, handler){
	if(node.removeEventListener)
		node.removeEventListener(event, handler, false);
	else if (node.detachEvent)
		node.detachEvent("on" + event, handler);
}

function showEvent(event) {
	show(event || window.event);
}

function reportClick(event) {
	event = event || window.event;
	var target = event.target || event.srcElement;
	var pageX = event.pageX, pageY = event.pageY;
	if (pageX == undefined) {
		pageX = event.clientX + document.body.scrollLeft;
		pageY = event.clientY + document.body.scrollTop;
	}

	console.log("Mouse clicked at " + pageX + ", " + pageY + ". Inside element: " + target);

}

function printKeyCode(event) {
	event = event || window.event;
	console.log("Key " + event.keyCode + " was pressed.");
}

function normaliseEvent(event) {
	if (!event.stopPropagation) {
		event.stopPropagation = function() {this.cancelBubble = true;};
		event.preventDefault = function() {this.returnValue = false;};
	}
	if (!event.stop) {
		event.stop = function() {
			this.stopPropagation();
			this.preventDefault();
		};
	}

	if (event.srcElement && !event.target)
		event.target = event.srcElement;
	if ((event.toElement || event.fromElement) && !event.relatedTarget)
		event.relatedTarget = event.toElement || event.fromElement;
	if (event.clientX != undefined && event.pageX == undefined) {
		event.pageX = event.clientX + document.body.scrollLeft;
		event.pageY = event.clientY + document.body.scrollTop;
	}
	if (event.type == "keypress") {
		if (event.charCode === 0 || event.charCode == undefined)
			event.character = String.fromCharCode(event.keyCode);
		else
			event.character = String.fromCharCode(event.charCode);
	}

	return event;
}

function addHandler(node, type, handler) {
	function wrapHandler(event) {
		handler(normaliseEvent(event || window.event));
	}
	registerEventHandler(node, type, wrapHandler);
	return {node: node, type: type, handler: wrapHandler};
}

function removeHandler(object) {
	unregisterEventHandler(object.node, object.type, object.handler);
}