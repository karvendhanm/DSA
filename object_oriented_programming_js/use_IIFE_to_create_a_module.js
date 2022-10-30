let bird = {
    name: 'Donald',
    numLegs: 2
};

let motionModule = (function() {
    return {
        glideMixin: function (obj) {
            obj.glide = function () {
                console.log('Gliding on the water');
            };
        },
        flyMixin: function(obj) {
            obj.fly = function() {
                console.log('Flying, wooosh!');
            };
        }
    }
})();

motionModule.glideMixin(bird);
bird.glide();