/* Deks Nexa - mesure d'audience GA4.
   La balise gtag.js est chargée dans le <head> de chaque page.
   Ce fichier envoie les événements de conversion, sans jamais bloquer
   la redirection vers WhatsApp. */
(function () {
    "use strict";

    var send = function (name, params) {
        if (typeof window.gtag === "function") {
            window.gtag("event", name, params);
        }
    };

    window.dnTrack = send;

    // Tous les liens qui contiennent « wa.me » : boutons, liens du menu, assistant, pied de page.
    document.addEventListener("click", function (event) {
        var link = event.target && event.target.closest ? event.target.closest('a[href*="wa.me"]') : null;
        if (!link) {
            return;
        }
        var text = (link.textContent || link.getAttribute("aria-label") || "").replace(/\s+/g, " ").trim();
        send("whatsapp_click", {
            page_path: window.location.pathname,
            link_text: text.slice(0, 100)
        });
    }, true);
})();
