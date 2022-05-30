function titleCase(str) {
    let _arr = str.split(" ");
    for(let i = 0; i < _arr.length; i++) {
        _arr[i] = _arr[i].charAt(0).toUpperCase() + (_arr[i].slice(1)).toLowerCase();
    }
    str = _arr.join(" ");
    return str;
}

titleCase("I'm a little tea pot");