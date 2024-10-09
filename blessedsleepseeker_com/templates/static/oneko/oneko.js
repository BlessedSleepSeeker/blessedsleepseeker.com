// Pokéneko v0.3 by https://james.nekoweb.org/
// https://jamesschoch.github.io/Pokeneko/

// Pokéneko is built using sprites from PDMCollab's Sprite Repository.
// https://sprites.pmdcollab.org

// This snippet uses sprites from https://sprites.pmdcollab.org/#/0399

var pokemon = {"pokedex":"0399","shiny":false,"animData":{"Walk":{"$":{},"Name":"Walk","Index":"0","FrameWidth":"32","FrameHeight":"32","Durations":{"$":{},"Duration":["8","10","8","10"]},"animURL":"https://jamesschoch.github.io/Pokeneko/sprite/0399/Walk-Anim.png"},"Idle":{"$":{},"Name":"Idle","Index":"7","FrameWidth":"32","FrameHeight":"32","Durations":{"$":{},"Duration":["20","14","20","14"]},"animURL":"https://jamesschoch.github.io/Pokeneko/sprite/0399/Idle-Anim.png"}}};
var trackerjson;
    pokemon.state = "none";
    var walkAnimInterval, idleAnimInterval;
    var dirlisting;
    var distancePx = 0;
    var CurrentMouseXPostion;
    var CurrentMouseYPostion;
    var scale = 2;
    var rotation = 0;
    var rotations = 8;
    var state;
    var laststate;
    var frameCounter;
    var animPlaying = false;
    var mouseIdleTime = 0;
    var anglevar;

    var sprite = document.createElement("div");
    sprite.id = "sprite";
    sprite.style.position = "fixed";
    sprite.style.zIndex = "1000000";
    sprite.style.width = "64px";
    sprite.style.height = "64px";
    sprite.style.pointerEvents = "none";
    sprite.style.top = "50%";
    sprite.style.left = "50%";

    document.body.appendChild(sprite);

    function getOffset(element) {
        if (!element.getClientRects().length) {
            return { top: 0, left: 0 };
        }

        var rect = element.getBoundingClientRect();
        var win = element.ownerDocument.defaultView;
        return (
            {
                top: rect.top + win.pageYOffset,
                left: rect.left + win.pageXOffset
            });
    }

    function timerIncrement() {
        mouseIdleTime = mouseIdleTime + 1;
    }

    function updateDistanceRotation() {
        var spriteX = getOffset(document.getElementById("sprite")).left + 32;
        var spriteY = getOffset(document.getElementById("sprite")).top + 32;
        distancePx = distance(spriteX, spriteY, CurrentMouseXPostion, CurrentMouseYPostion);
        anglevar = angle360(spriteX, spriteY, CurrentMouseXPostion, CurrentMouseYPostion);
        if (anglevar > 67.5 && anglevar < 112.5) {
            rotation = 0;
        } else if (anglevar > 22.5 && anglevar < 67.5) {
            rotation = 1;
        } else if (anglevar > 337.5 || anglevar < 22.5) {
            rotation = 2;
        } else if (anglevar > 292.5 && anglevar < 337.5) {
            rotation = 3;
        } else if (anglevar > 247.5 && anglevar < 292.5) {
            rotation = 4;
        } else if (anglevar > 202.5 && anglevar < 247.5) {
            rotation = 5;
        } else if (anglevar > 157.5 && anglevar < 202.5) {
            rotation = 6;
        } else if (anglevar > 112.5 && anglevar < 157.5) {
            rotation = 7;
        }
    }

    function addEvent(elm, evType, fn, useCapture) {
        if (elm.addEventListener) {
            elm.addEventListener(evType, fn, useCapture);
            return true;
        }
        else if (elm.attachEvent) {
            var r = elm.attachEvent('on' + evType, fn);
            return r;
        }
        else {
            elm['on' + evType] = fn;
        }
    }

    document.onmousemove = function (event) {
        CurrentMouseXPostion = event.pageX;
        CurrentMouseYPostion = event.pageY;
        updateDistanceRotation();
        mouseIdleTime = 0;
    }

    function angle(cx, cy, ex, ey) {
        var dy = ey - cy;
        var dx = ex - cx;
        var theta = Math.atan2(dy, dx);
        theta *= 180 / Math.PI;

        return theta;
    }

    function distance(cx, cy, ex, ey) {
        var dx = cx - ex;
        var dy = cy - ey;
        return Math.sqrt(dx * dx + dy * dy);
    }

    function angle360(cx, cy, ex, ey) {
        var theta = angle(cx, cy, ex, ey);
        if (theta < 0) theta = 360 + theta;
        return theta;
    }

    function setSprite(animName, frame) {
        var animData = pokemon.animData[animName];
        var sprite = document.getElementById("sprite");
        if (animName !== "Sleep") {
            var rotations = 8;
        } else {
            var rotations = 1;
        }
        sprite.style.backgroundImage = "url(" + animData.animURL + ")";
        sprite.style.backgroundSize = (animData.FrameWidth * scale * animData.Durations.Duration.length) + "px " + (animData.FrameHeight * scale * rotations) + "px";
        sprite.style.width = animData.FrameWidth * scale + "px";
        sprite.style.height = animData.FrameHeight * scale + "px";
        sprite.style.backgroundPosition = (0 - ((animData.FrameWidth * (frame % animData.Durations.Duration.length)) * scale)) + "px " + (0 - ((rotation * animData.FrameHeight) * scale)) + "px";
        sprite.style.imageRendering = "pixelated";

    }

    var runningAnim;
    var runningAnimName = "";

    function runAnim(animName) {
        if (pokemon.pokedex) {
            if (runningAnimName === animName) {
                return;
            } else {
                clearInterval(runningAnim);
                var frames = [];
                for (var i = 0; i < pokemon.animData[animName].Durations.Duration.length; i++) {
                    for (var j = 0; j < pokemon.animData[animName].Durations.Duration[i]; j++) {
                        frames.push(i);
                    }
                }

                runningAnimName = animName;
                var i = 0;
                runningAnim = setInterval(function () {
                    setSprite(animName, frames[i]);
                    i++;
                    if (i == frames.length) {
                        setSprite(animName, frames[i]);
                        i = 0;
                    }
                }, 33);
            }
        }
    }

    var moveSprite = setInterval(function () {

        if (pokemon.pokedex) {
            if (distancePx >= 55) {
                state = "Walk";
                runAnim("Walk");

            } else {
                state = "Idle";
                runAnim("Idle");
            }
            if (state == "Walk") {

                var sprite = document.getElementById("sprite");
                var spriteX = getOffset(document.getElementById("sprite")).left;
                var spriteY = getOffset(document.getElementById("sprite")).top;

                var angle = angle360(spriteX, spriteY, CurrentMouseXPostion, CurrentMouseYPostion);
                var dx = Math.cos(angle * Math.PI / 180) * 4;
                var dy = Math.sin(angle * Math.PI / 180) * 4;
                sprite.style.left = spriteX + dx + "px";
                sprite.style.top = spriteY + dy + "px";

            }
            updateDistanceRotation();

            laststate = state;
        }
    }, 33);