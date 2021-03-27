$(document).ready(function() {

});

function ShowSubLlist(dom) {
    var isVisible = $(dom).next().is(':visible');

    if (isVisible) {
        $(dom).next().hide();
    } else {
        $(dom).next().fadeIn();
    }
}