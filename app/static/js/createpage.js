document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');

    var homeTypeRadios = document.querySelectorAll('input[name="home_type"]');
    var homeTypeField = document.querySelector('input[name="home_type"]:checked');
    
    var hallField = document.getElementById('hallField');
    var addressFields = document.getElementById('addressFields');
    var additionalFields = document.getElementById('additionalFields');

    var location_step_button = document.getElementById('location_step_button');
    var review_step_button = document.getElementById('review_step_button');
    var review_step_back_button = document.getElementById('review_step_back_button');
    var submit = document.getElementById('submit');
    var details_step_back_button = document.getElementById('details_step_back_button');

    var location_step = document.getElementById('location_step');
    var review_step = document.getElementById('review_step');
    var details_step = document.getElementById('details_step');


    
    function div_validity_check(formId, buttonId) {
      var form = document.getElementById(formId);
      var button = document.getElementById(buttonId);
      var fields = form.querySelectorAll('input, select, textarea');
    
      for (var i = 0; i < fields.length; i++) {
        if (!fields[i].checkValidity()) {
          button.disabled = true;
          return;
        }
      }
      button.disabled = false;
    }

    function toggleFields() {
      var rent = document.getElementById('rent');
      var address_line_1 = document.getElementById('address_line_1');
      var city = document.getElementById('city');
      var postcode = document.getElementById('postcode');

      if (homeTypeField.value === 'house') {
        addressFields.style.display = 'block';
        hallField.style.display = 'none';
        additionalFields.style.display = 'block';
        rent.required = true;
        address_line_1.required = true;
        city.required = true;
        postcode.required = true;
      } else {
        addressFields.style.display = 'none';
        hallField.style.display = 'block';
        additionalFields.style.display = 'none';
        rent.required = false;
        address_line_1.required = false;
        city.required = false;
        postcode.required = false;
      }
    }

    function location(){
      location_step.style.display = 'block';
      review_step.style.display = 'none';
      details_step.style.display = 'none';
    }

    function review(){
      location_step.style.display = 'none';
      review_step.style.display = 'block';
      details_step.style.display = 'none';
    }

    function details(){
      location_step.style.display = 'none';
      review_step.style.display = 'none';
      details_step.style.display = 'block';
    }



    location_step.addEventListener('input', function() {
      div_validity_check('location_step', 'location_step_button');
    });

    location_step_button.addEventListener('click', function() {
      review();
      div_validity_check('review_step', 'review_step_button');
    });

    review_step.addEventListener('input', function() {
      div_validity_check('review_step', 'review_step_button');
    });

    review_step_button.addEventListener('click', function() {
      details();
      div_validity_check('details_step', 'submit');
    });

    review_step_back_button.addEventListener('click', function() {
      location();
      div_validity_check('location_step', 'location_step_button');
    });

    details_step.addEventListener('input', function() {
      div_validity_check('details_step', 'submit');
    });

    details_step_back_button.addEventListener('click', function() {
      review();
      div_validity_check('review_step', 'review_step_button');
    });



    for (var i = 0; i < homeTypeRadios.length; i++) {
      homeTypeRadios[i].addEventListener('change', function() {
        homeTypeField = document.querySelector('input[name="home_type"]:checked');
        toggleFields();
        div_validity_check('location_step', 'location_step_button');
      });
    }

    toggleFields();
    location();
    div_validity_check('location_step', 'location_step_button');
  });
