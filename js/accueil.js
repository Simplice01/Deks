/* Deks Nexa — héros de la page d'accueil.
   - une lumière bleue très douce qui dérive lentement et suit la souris ;
   - en option, une grille de points (canvas) : data-dots="on" sur le canvas ;
   - le compteur de la maquette, joué une seule fois.
   Rien ne bouge si le visiteur a demandé moins d'animations. */
(function () {
    "use strict";

    var hero = document.querySelector(".dn-hero");
    if (!hero) {
        return;
    }

    var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var glowEl = hero.querySelector(".dn-hero-glow");
    var canvas = hero.querySelector(".dn-hero-canvas");
    var showDots = canvas && canvas.getAttribute("data-dots") === "on";
    var ctx = showDots && canvas.getContext ? canvas.getContext("2d") : null;

    var width = 0;
    var height = 0;
    var points = [];
    var glow = { x: 0, y: 0 };
    var target = { x: 0, y: 0 };
    var pointerInside = false;
    var inView = true;
    var running = false;
    var rafId = 0;

    var autoTarget = function (time) {
        target.x = width * (0.68 + 0.18 * Math.sin(time / 7000));
        target.y = height * (0.42 + 0.16 * Math.cos(time / 8600));
    };

    var buildPoints = function () {
        if (!ctx) {
            return;
        }
        var gap = width < 768 ? 32 : 28;
        var offsetX = (width % gap) / 2 + gap / 2;
        var offsetY = (height % gap) / 2 + gap / 2;
        points = [];
        for (var y = offsetY; y < height; y += gap) {
            for (var x = offsetX; x < width; x += gap) {
                points.push({ x: x, y: y, phase: Math.random() * Math.PI * 2 });
            }
        }
    };

    var drawDots = function (time) {
        if (!ctx) {
            return;
        }
        ctx.clearRect(0, 0, width, height);
        var reach = 220;
        for (var i = 0; i < points.length; i++) {
            var p = points[i];
            var alpha = 0.07 + 0.04 * Math.sin(time / 1600 + p.phase);
            var dx = p.x - glow.x;
            var dy = p.y - glow.y;
            var d = Math.sqrt(dx * dx + dy * dy);
            if (d < reach) {
                var k = 1 - d / reach;
                alpha += 0.35 * k * k;
            }
            ctx.fillStyle = "rgba(255,255,255," + alpha.toFixed(3) + ")";
            ctx.fillRect(p.x - 0.75, p.y - 0.75, 1.5, 1.5);
        }
    };

    var render = function (time) {
        if (!pointerInside) {
            autoTarget(time);
        }
        glow.x += (target.x - glow.x) * 0.045;
        glow.y += (target.y - glow.y) * 0.045;
        if (glowEl) {
            glowEl.style.transform = "translate3d(" + glow.x.toFixed(1) + "px," + glow.y.toFixed(1) + "px,0)";
        }
        drawDots(time);
    };

    var resize = function () {
        var rect = hero.getBoundingClientRect();
        width = Math.max(1, Math.round(rect.width));
        height = Math.max(1, Math.round(rect.height));
        if (ctx) {
            var dpr = Math.min(window.devicePixelRatio || 1, 2);
            canvas.width = Math.round(width * dpr);
            canvas.height = Math.round(height * dpr);
            ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
            buildPoints();
        }
        if (!glow.x) {
            autoTarget(0);
            glow.x = target.x;
            glow.y = target.y;
        }
        if (!running) {
            render(0);
        }
    };

    var frame = function (time) {
        render(time);
        rafId = window.requestAnimationFrame(frame);
    };

    var start = function () {
        if (running || reduceMotion) {
            return;
        }
        running = true;
        rafId = window.requestAnimationFrame(frame);
    };

    var stop = function () {
        running = false;
        window.cancelAnimationFrame(rafId);
    };

    var refresh = function () {
        if (inView && !document.hidden) {
            start();
        } else {
            stop();
        }
    };

    if (glowEl || ctx) {
        var queued = false;
        var queueResize = function () {
            if (queued) {
                return;
            }
            queued = true;
            window.requestAnimationFrame(function () {
                queued = false;
                resize();
            });
        };

        if ("ResizeObserver" in window) {
            new ResizeObserver(queueResize).observe(hero);
        } else {
            window.addEventListener("resize", queueResize);
        }
        resize();

        if (!reduceMotion) {
            hero.addEventListener("pointermove", function (event) {
                if (event.pointerType !== "mouse") {
                    return;
                }
                var rect = hero.getBoundingClientRect();
                target.x = event.clientX - rect.left;
                target.y = event.clientY - rect.top;
                pointerInside = true;
            });
            hero.addEventListener("pointerleave", function () {
                pointerInside = false;
            });
        }

        if ("IntersectionObserver" in window) {
            new IntersectionObserver(function (entries) {
                inView = entries[0].isIntersecting;
                refresh();
            }).observe(hero);
        }

        document.addEventListener("visibilitychange", refresh);
        refresh();
    }

    /* Compteur de la maquette : monte une seule fois à l'arrivée. */
    var counter = hero.querySelector(".dn-app-count");
    if (counter && !reduceMotion) {
        var goal = parseInt(counter.getAttribute("data-count"), 10) || 0;
        var duration = 1400;
        var startTime = null;
        counter.textContent = "0";

        var step = function (now) {
            if (startTime === null) {
                startTime = now;
            }
            var progress = Math.min((now - startTime) / duration, 1);
            counter.textContent = String(Math.round(goal * (1 - Math.pow(1 - progress, 3))));
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };

        window.setTimeout(function () {
            window.requestAnimationFrame(step);
        }, 600);
    }
})();
