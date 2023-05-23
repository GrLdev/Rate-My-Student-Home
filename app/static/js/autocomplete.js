$(document).ready(function() {
    var searchInput = $("#search-input");
    var searchType = $("input[name='search_type']");
    

    // Check if the selected search type is "Address" on page load
    if (searchType.filter(":checked").val() === "address") {
        enableAutocompleteAddress();
    }
    else if (searchType.filter(":checked").val() === "halls") {
        enableAutocompleteHalls();
        searchInput.autocomplete("search"); 
    }
    else if (searchType.filter(":checked").val() === "agent") {
        enableAutocompleteAgent();
        searchInput.autocomplete("search");
    }

    // Event listener to check the selected search type and enable/disable autocomplete accordingly
    searchType.on("change", function() {
        searchInput.val("");
        if ($(this).val() === "address") {
            enableAutocompleteAddress();
        } 
        else if ($(this).val() === "halls") {
            enableAutocompleteHalls();
            searchInput.autocomplete("search"); 
        }
        else if ($(this).val() === "agent") {
            enableAutocompleteAgent();
            searchInput.autocomplete("search");
        }
        else {
            disableAutocompleteAddress();
        }
    });

    function enableAutocompleteAddress() {
        searchInput.autocomplete({
            source: function(request, response) {
                $.ajax({
                    url: "/autocomplete-address",
                    data: {
                        term: request.term
                    },
                    dataType: "json",
                    success: function(data) {
                        response(data.addresses);
                    }
                });
            },
            minLength: 1,
            appendTo: "#autocomplete-container",
            select: function(event, ui) {
                searchInput.val(ui.item.value);
                $("#search-form").submit();
            }
        }).autocomplete("widget").css({"max-height": "400px", "overflow-y": "auto"});;
    }

    function enableAutocompleteHalls() {
        searchInput.autocomplete({
            source: function(request, response) {
                $.ajax({
                    url: "/autocomplete-halls",
                    data: {
                        term: request.term
                    },
                    dataType: "json",
                    success: function(data) {
                        response(data.addresses);
                    }
                });
            },
            minLength: 0,
            appendTo: "#autocomplete-container",
            select: function(event, ui) {
                searchInput.val(ui.item.value);
                $("#search-form").submit();
            }
        }).autocomplete("widget").css({"max-height": "400px", "overflow-y": "auto"});;
    }

    function enableAutocompleteAgent() {
        searchInput.autocomplete({
            source: function(request, response) {
                $.ajax({
                    url: "/autocomplete-agent",
                    data: {
                        term: request.term
                    },
                    dataType: "json",
                    success: function(data) {
                        response(data.agents);
                    }
                });
            },
            minLength: 0,
            appendTo: "#autocomplete-container",
            select: function(event, ui) {
                searchInput.val(ui.item.value);
                $("#search-form").submit();
            }
        }).autocomplete("widget").css({"max-height": "400px", "overflow-y": "auto"});
    }

    function disableAutocompleteAddress() {
        searchInput.autocomplete("destroy");
    }
});
