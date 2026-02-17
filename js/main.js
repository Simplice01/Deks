(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.navbar').addClass('sticky-top shadow-sm');
        } else {
            $('.navbar').removeClass('sticky-top shadow-sm');
        }
    });
    
    
    // Dropdown on mouse hover
    const $dropdown = $(".dropdown");
    const $dropdownToggle = $(".dropdown-toggle");
    const $dropdownMenu = $(".dropdown-menu");
    const showClass = "show";
    
    $(window).on("load resize", function() {
        if (this.matchMedia("(min-width: 992px)").matches) {
            $dropdown.hover(
            function() {
                const $this = $(this);
                $this.addClass(showClass);
                $this.find($dropdownToggle).attr("aria-expanded", "true");
                $this.find($dropdownMenu).addClass(showClass);
            },
            function() {
                const $this = $(this);
                $this.removeClass(showClass);
                $this.find($dropdownToggle).attr("aria-expanded", "false");
                $this.find($dropdownMenu).removeClass(showClass);
            }
            );
        } else {
            $dropdown.off("mouseenter mouseleave");
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 25,
        dots: false,
        loop: true,
        center: true,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            }
        }
    });


    // Portfolio isotope and filter
    var portfolioIsotope = $('.portfolio-container').isotope({
        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
    });
    $('#portfolio-flters li').on('click', function () {
        $("#portfolio-flters li").removeClass('active');
        $(this).addClass('active');

        portfolioIsotope.isotope({filter: $(this).data('filter')});
    });
    
})(jQuery);


function toggleDetails(button) {
  const content = button.closest('.service').querySelector('.service-content');
  const isVisible = content.style.display === 'block';
  content.style.display = isVisible ? 'none' : 'block';
  button.textContent = isVisible ? '▼' : '▲';
}

function openModal(service) {
  const details = {
    web: `
      <h3>Développement Web</h3>
      <p>Création de sites vitrines, blogs, e-commerces, SEO, et intégration de solutions de paiement sécurisées.</p>
      <ul>
        <li>Site vitrine</li>
        <li>Site e-commerce</li>
        <li>Blog professionnel</li>
        <li>Référencement (SEO)</li>
        <li>Paiement en ligne</li>
      </ul>
    `,
    mobile: `
      <h3>Applications Mobiles</h3>
      <p>Nous développons des applications intuitives et performantes pour Android et iOS.</p>
      <ul>
        <li>App native (iOS/Android)</li>
        <li>App de gestion de tâches</li>
        <li>App réseau social</li>
        <li>App de jeux mobiles</li>
        <li>Intégration paiements</li>
      </ul>
    `,
    software: `
      <h3>Développement de Logiciels</h3>
      <p>Logiciels sur mesure adaptés aux besoins spécifiques de votre entreprise.</p>
      <ul>
        <li>ERP / CRM personnalisés</li>
        <li>Gestion de stock</li>
        <li>Outils cloud computing</li>
        <li>Automatisation métiers</li>
        <li>Mise à jour & maintenance</li>
      </ul>
    `,
        shopify: `
    <h3>Création de Boutique Shopify</h3>
    <p>Lancez votre boutique en ligne avec un site Shopify professionnel, rapide et optimisé pour les ventes.</p>
    <ul>
        <li>Conception et personnalisation complète du thème</li>
        <li>Ajout de produits, collections et fiches détaillées</li>
        <li>Intégration des paiements et livraisons</li>
        <li>Optimisation mobile et SEO</li>
        <li>Formation à la gestion de la boutique</li>
    </ul>
    `,
        systemeio: `
    <h3>Création de Tunnel de Vente Systeme.io</h3>
    <p>Automatisez vos ventes avec des tunnels optimisés pour convertir vos visiteurs en clients.</p>
    <ul>
        <li>Création de pages de capture, de vente et de remerciement</li>
        <li>Intégration des paiements et email marketing</li>
        <li>Configuration des automatisations (emails, upsells, downsells)</li>
        <li>Connexion à votre domaine personnalisé</li>
        <li>Conseils stratégiques pour maximiser vos conversions</li>
    </ul>
    `,
    graphisme: `
  <h3>Design Graphique & Identité Visuelle</h3>
  <p>Offrez à votre marque une image professionnelle et percutante avec un design unique.</p>
  <ul>
    <li>Création de logo sur mesure</li>
    <li>Charte graphique complète (couleurs, typographies, icônes)</li>
    <li>Affiches, bannières web et flyers promotionnels</li>
    <li>Visuels pour réseaux sociaux</li>
    <li>Refonte graphique de votre image existante</li>
  </ul>
`
  };

  document.getElementById('modalDetails').innerHTML = details[service];
  document.getElementById('serviceModal').style.display = 'flex';
}

function closeModal() {
  document.getElementById('serviceModal').style.display = 'none';
}

