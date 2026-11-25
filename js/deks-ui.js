/* Deks Nexa — apparition douce des blocs au défilement (toutes les pages).
   Les blocs sont visibles par défaut : l'animation ne s'applique que si
   <html> porte la classe « js » (ajoutée dans le <head>). Ce script
   ajoute « dn-ready » ; sans lui, une sécurité CSS affiche tout. */
(function () {
    "use strict";

    var root = document.documentElement;
    var items = Array.prototype.slice.call(document.querySelectorAll(".dn-reveal"));
    var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    var showAll = function () {
        items.forEach(function (el) {
            el.classList.add("is-visible");
        });
    };

    root.classList.add("dn-ready");

    /* Carrousel des avis : boutons précédent / suivant sur le défilement natif. */
    Array.prototype.forEach.call(document.querySelectorAll("[data-carousel]"), function (carousel) {
        var track = carousel.querySelector(".dn-reviews-list");
        var prev = carousel.querySelector('[data-dir="-1"]');
        var next = carousel.querySelector('[data-dir="1"]');
        if (!track || !prev || !next) {
            return;
        }
        var step = function () {
            var card = track.querySelector("li");
            var gap = parseFloat(window.getComputedStyle(track).columnGap) || 16;
            return card ? card.getBoundingClientRect().width + gap : track.clientWidth;
        };
        var update = function () {
            prev.disabled = track.scrollLeft <= 2;
            next.disabled = track.scrollLeft + track.clientWidth >= track.scrollWidth - 2;
        };
        var move = function (direction) {
            track.scrollBy({ left: direction * step(), behavior: reduceMotion ? "auto" : "smooth" });
        };
        prev.addEventListener("click", function () { move(-1); });
        next.addEventListener("click", function () { move(1); });
        track.addEventListener("scroll", update, { passive: true });
        window.addEventListener("resize", update);
        update();
    });


    if (!items.length) {
        return;
    }

    if (reduceMotion || !("IntersectionObserver" in window)) {
        showAll();
        return;
    }

    // Petit décalage en cascade entre les éléments d'une même liste.
    items.forEach(function (el) {
        var parent = el.parentElement;
        var siblings = parent ? Array.prototype.filter.call(parent.children, function (child) {
            return child.classList.contains("dn-reveal");
        }) : [el];
        el.style.setProperty("--rd", Math.min(siblings.indexOf(el), 5) * 80 + "ms");
    });

    var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-visible");
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: "0px 0px -10% 0px" });

    items.forEach(function (el) {
        observer.observe(el);
    });

    // Impression : tout doit être visible.
    window.addEventListener("beforeprint", showAll);
})();
