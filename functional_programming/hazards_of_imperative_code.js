const Window = function (tabs) {
    this.tabs = tabs;
}

Window.prototype.join = function(otherWindow) {
    this.tabs = this.tabs.concat(otherWindow.tabs);
    return this;
};

window.prototype.tabOpen = function(tab) {
    this.tabs.push(tab);
    return this;
}



