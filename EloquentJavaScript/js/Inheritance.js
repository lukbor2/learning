/**
 * 
 */

function clone(object) {
	function OneShotConstructor(){}
	OneShotConstructor.prototype = object;
	return new OneShotConstructor();
};

Object.prototype.inherit = function(baseConstructor) {
	this.prototype = clone(baseConstructor.prototype);
	this.prototype.constructor = this;
};
Object.prototype.method = function(name, func) {
	this.prototype[name] = func;
};

function StrangeArray(){}
StrangeArray.inherit(Array);
StrangeArray.method("push", function(value) {
	Array.prototype.push.call(this, value);
	Array.prototype.push.call(this, value);
});

Object.prototype.create = function() {
	var object = clone(this);
	if (typeof object.construct == "function")
		object.construct.apply(object, arguments);
	return object;
};

Object.prototype.extend = function(properties) {
	var result = clone(this);
	forEachIn(properties, function(name, value) {
		result[name] = value;
	});
	return result;
};