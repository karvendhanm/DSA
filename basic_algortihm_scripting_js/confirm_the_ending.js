function confirmEnding(str, target) {
    let _pattern = new RegExp(`.*?${target}$`);
    str = _pattern.test(str);
    return str;
}

console.log(confirmEnding("Bastian", "n"));