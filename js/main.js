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
        SaaS: `
<h3>Plateformes SaaS</h3>
<p>Développement de plateformes SaaS modernes permettant de proposer des services en ligne accessibles par abonnement. Les solutions sont conçues pour être sécurisées, évolutives et faciles à utiliser par vos utilisateurs.</p>

<ul>
    <li>Conception d’applications web SaaS personnalisées</li>
    <li>Système de comptes utilisateurs et gestion des rôles</li>
    <li>Tableau de bord et gestion des données</li>
    <li>API sécurisée et architecture évolutive</li>
    <li>Intégration de paiements et gestion des abonnements</li>
</ul>
    `,
        Automatisation: `
<h3>Automatisation</h3>
<p>Mise en place de systèmes automatisés permettant de simplifier vos tâches répétitives, d’optimiser votre organisation et de gagner du temps dans la gestion de votre activité.</p>

<ul>
    <li>Automatisation de tâches et workflows</li>
    <li>Synchronisation entre différentes applications</li>
    <li>Automatisation de notifications et d’actions</li>
    <li>Intégration d’API et connexion entre services</li>
    <li>Mise en place de systèmes automatisés pour améliorer la productivité</li>
</ul>
    `,
    Intégrations: `
<h3>Intégrations API</h3>
<p>Connexion de vos applications à des services externes afin d’automatiser les échanges de données, d’ajouter de nouvelles fonctionnalités et d’améliorer l’efficacité de vos systèmes.</p>
<ul>
  <li>Connexion à des API de paiement, messagerie ou notification</li>
  <li>Synchronisation de données entre plusieurs applications</li>
  <li>Intégration de services tiers dans vos plateformes web</li>
  <li>Mise en place d’échanges sécurisés entre systèmes</li>
  <li>Développement de solutions sur mesure adaptées à vos besoins</li>
</ul>
`
  };

  document.getElementById('modalDetails').innerHTML = details[service];
  document.getElementById('serviceModal').style.display = 'flex';
}

function closeModal() {
  document.getElementById('serviceModal').style.display = 'none';
}


document.addEventListener("DOMContentLoaded", function () {
    const faqBoxes = document.querySelectorAll(".faq-box");

    faqBoxes.forEach((box) => {
        const button = box.querySelector(".faq-question");
        const icon = box.querySelector(".faq-icon");

        button.addEventListener("click", function () {
            const isActive = box.classList.contains("active");

            faqBoxes.forEach((item) => {
                item.classList.remove("active");
                const itemIcon = item.querySelector(".faq-icon");
                if (itemIcon) {
                    itemIcon.textContent = "+";
                }
            });

            if (!isActive) {
                box.classList.add("active");
                if (icon) {
                    icon.textContent = "−";
                }
            }
        });
    });
});


document.addEventListener("DOMContentLoaded", function () {
    const portfolioBoxes = document.querySelectorAll(".portfolio-box");

    portfolioBoxes.forEach((box) => {
        const button = box.querySelector(".portfolio-question");
        const icon = box.querySelector(".portfolio-icon");

        button.addEventListener("click", function () {
            const isActive = box.classList.contains("active");

            portfolioBoxes.forEach((item) => {
                item.classList.remove("active");
                const itemIcon = item.querySelector(".portfolio-icon");
                if (itemIcon) {
                    itemIcon.textContent = "+";
                }
            });

            if (!isActive) {
                box.classList.add("active");
                if (icon) {
                    icon.textContent = "−";
                }
            }
        });
    });
});
