function repeatStringNumTimes(str, num) {
    if (num <= 0) { return "" }
    let tmp_str = str;
    for(let i=0; i<(num-1); i++) {
        str += tmp_str;
    }
    return str;
}

repeatStringNumTimes("abc", 3);