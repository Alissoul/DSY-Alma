
document.addEventListener('DOMContentLoaded', () => {

   // Barra de navegación
   var elems = document.querySelectorAll('.sidenav');
   var instances = M.Sidenav.init(elems);

   // Deslizador
   var elems = document.querySelectorAll('.slider');
   var instances = M.Slider.init(elems, {
       indicators: false,
       height: 500,
       duration: 500,
       interval:3000
    });
    //Carousel
   var elems = document.querySelectorAll('.carousel');
   var instances = M.Carousel.init(elems);

    //Material Box
   var elems = document.querySelectorAll('.materialboxed');
   var instances = M.Materialbox.init(elems);

   //Plegable
   var elems = document.querySelectorAll('.collapsible');
   var instances = M.Collapsible.init(elems);

});