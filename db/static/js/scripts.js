$( window ).on('load', function() {
    var checkboxes = $("form input:checkbox");
    var parents = checkboxes.parent();

    checkboxes.addClass("custom-control-input");
    parents.attr('class', 'custom-control custom-checkbox mr-sm-2');
    parents.wrap("<div class='col-auto my-1'></div>");
    $("label", parents).addClass("custom-control-label");

    function swap(a, b) {
        a = $(a); b = $(b);
        var tmp = $('<span>').hide();
        a.before(tmp);
        b.before(a);
        tmp.replaceWith(b);
    }

    swap("textarea", $("label", $("textarea").parent()));

    $(".custom-checkbox label").each(function(){
        $(this).text($(this).text().slice(0,-1));
    })

    $("button.close").attr("data-dismiss", "alert");
    $("button.close").attr("aria-label", "Close");

    $("body").css("display", "block");
});