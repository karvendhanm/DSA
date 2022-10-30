function booWho(bool) {
    let _bool = false;
    if(typeof bool === 'boolean') { _bool = true}
    return _bool;
}

console.log(booWho(null));