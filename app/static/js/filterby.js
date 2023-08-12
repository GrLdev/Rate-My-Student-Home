function filterReviews() {
    var minRating = $('#filter-input').val();
    var minRent = $('#rent-min-input').val();
    var maxRent = $('#rent-max-input').val();
    var minBedrooms = $('#bedrooms-min-input').val();
    var maxBedrooms = $('#bedrooms-max-input').val();
    var minBathrooms = $('#bathrooms-min-input').val();
    var maxBathrooms = $('#bathrooms-max-input').val();

    $('.review').each(function() {
        var reviewDate = new Date($(this).data('review-date'));
        var overallRating = parseInt($(this).data('review-overall-rating'));
        var rent = parseInt($(this).data('rent'));
        var bedrooms = parseInt($(this).data('bedrooms'));
        var bathrooms = parseInt($(this).data('bathrooms'));

        var shouldShow = true;

        if (minRating !== "all" && overallRating < parseInt(minRating)) {
            shouldShow = false;
        }

        if (minRent !== "all" && rent < parseInt(minRent)) {
            shouldShow = false;
        }

        if (maxRent !== "all" && rent > parseInt(maxRent)) {
            shouldShow = false;
        }

        if (minBedrooms !== "all" && bedrooms < parseInt(minBedrooms)) {
            shouldShow = false;
        }

        if (maxBedrooms !== "all" && bedrooms > parseInt(maxBedrooms)) {
            shouldShow = false;
        }

        if (minBathrooms !== "all" && bathrooms < parseInt(minBathrooms)) {
            shouldShow = false;
        }

        if (maxBathrooms !== "all" && bathrooms > parseInt(maxBathrooms)) {
            shouldShow = false;
        }

        if (shouldShow) {
            $(this).show();
        } else {
            $(this).hide();
        }
    });
}

// Call the filterReviews() function when the filter criteria change
$('#filter-input, #rent-min-input, #rent-max-input, #bedrooms-min-input, #bedrooms-max-input, #bathrooms-min-input, #bathrooms-max-input').on('change', function() {
    filterReviews();
});