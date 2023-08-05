var sort_input = $('#sort-input');
var sort_type = $('select[name="sort_by"]');

if (sort_type.val() === 'recent') {
    sort_by_recent();
}

function sort_by_recent() {
    var reviews = $('.review');
    reviews.sort(function(a, b) {
        var dateA = new Date($(a).data('review-date'));
        var dateB = new Date($(b).data('review-date'));
        return dateB - dateA;
    });
    $('#reviews-container').html(reviews);
}

function sort_by_oldest() {
    var reviews = $('.review');
    reviews.sort(function(a, b) {
        var dateA = new Date($(a).data('review-date'));
        var dateB = new Date($(b).data('review-date'));
        return dateA - dateB;
    });
    $('#reviews-container').html(reviews);
}

function sort_by_overall() {
    var reviews = $('.review');
    reviews.sort(function(a, b) {
        var ratingA = parseInt($(a).data('review-overall-rating'));
        var ratingB = parseInt($(b).data('review-overall-rating'));
        return ratingB - ratingA;
    });
    $('#reviews-container').html(reviews);
}

function sort_by_overall_low() {
    var reviews = $('.review');
    reviews.sort(function(a, b) {
        var ratingA = parseInt($(a).data('review-overall-rating'));
        var ratingB = parseInt($(b).data('review-overall-rating'));
        return ratingA - ratingB;
    });
    $('#reviews-container').html(reviews);
}

function sort_by_rent_high() {
    var reviews = $('.review');
    reviews.sort(function(a, b) {
        var ratingA = parseInt($(a).data('rent'));
        var ratingB = parseInt($(b).data('rent'));
        return ratingB - ratingA;
    });
    $('#reviews-container').html(reviews);
}

function sort_by_rent_low() {
    var reviews = $('.review');
    reviews.sort(function(a, b) {
        var ratingA = parseInt($(a).data('rent'));
        var ratingB = parseInt($(b).data('rent'));
        return ratingA - ratingB;
    });
    $('#reviews-container').html(reviews);
}

sort_input.on('change', function() {
    var sort_by = sort_type.val();
    console.log(sort_by);
    if ($(this).val() === 'recent') {
        sort_by_recent();
    } 
    else if ($(this).val() === 'oldest') {
        sort_by_oldest();
    }
    else if ($(this).val() === 'overall_high') {
        sort_by_overall();
    }
    else if ($(this).val() === 'overall_low') {
        sort_by_overall_low();
    }
    else if ($(this).val() === 'rent_high') {
        sort_by_rent_high();
    } 
    else if ($(this).val() === 'rent_low') {
        sort_by_rent_low();
    }
});
