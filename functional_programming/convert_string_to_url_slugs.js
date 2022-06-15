// Only change code below this line
function urlSlug(title) {

    const pattern = /\s{2,}/g;
    let url = title.trim();
    url = url.replace(pattern, " ");
    url = url.toLowerCase();
    url = url.split(" ");
    url =  url.join("-");
    return url

}
// Only change code above this line
console.log(urlSlug("Winter Is Coming"));
console.log(urlSlug(" Winter Is  Coming"));
console.log(urlSlug("A Mind Needs Books Like A Sword Needs A Whetstone"));
console.log(urlSlug("Hold The Door"));
