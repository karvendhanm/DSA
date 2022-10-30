function urlSlug(title) {

    const pattern = /\s{2,}/g;
    let url = title.trim();
    url = url.toLowerCase();
    url = url.replace(pattern, " ");
    url = url.split(" ");
    url =  url.join("-");
    return url

}


function _urlSlug(title) {

    let url = title.trim();
    url = url.toLowerCase();
    url = url.split(" ");
    url = url.reduce(function(_lst, item) {
        item != "" ? _lst.push(item) : 0
        return _lst;
    }, []);
    url =  url.join("-");
    return url

}


console.log(_urlSlug(" Winter Is  Coming"));
console.log(_urlSlug("Winter Is Coming"));
console.log(_urlSlug("A Mind Needs Books Like A Sword Needs A Whetstone"));
console.log(_urlSlug("Hold The Door"));
