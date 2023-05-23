var sort_input = $('#sort-input');
var sort_type = $('select[name="sort_by"]');

if (sort_type.val() === 'recent') {
    sort_by_recent();
}

function sort_by_recent() {
    var reviews = $('.review');
    reviews.sort(function(a, b) {
        var dateA = new Date($(a).find('p:eq(0)').text().split(': ')[1]);
        var dateB = new Date($(b).find('p:eq(0)').text().split(': ')[1]);
        return dateB - dateA;
    });
    $('#reviews-container').html(reviews);
}

function sort_by_oldest() {
    var reviews = $('.review');
    reviews.sort(function(a, b) {
        var dateA = new Date($(a).find('p:eq(0)').text().split(': ')[1]);
        var dateB = new Date($(b).find('p:eq(0)').text().split(': ')[1]);
        return dateA - dateB;
    });
    $('#reviews-container').html(reviews);
}

function sort_by_overall() {
    var reviews = $('.review');
    reviews.sort(function(a, b) {
        var ratingA = parseInt($(a).find('p:eq(2)').text().split(': ')[1]);
        var ratingB = parseInt($(b).find('p:eq(2)').text().split(': ')[1]);
        return ratingB - ratingA;
    });
    $('#reviews-container').html(reviews);
}

function sort_by_overall_low() {
    var reviews = $('.review');
    reviews.sort(function(a, b) {
        var ratingA = parseInt($(a).find('p:eq(2)').text().split(': ')[1]);
        var ratingB = parseInt($(b).find('p:eq(2)').text().split(': ')[1]);
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
});
