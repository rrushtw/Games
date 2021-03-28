$(document).ready(function() {

});

$('.homeIcon').on('click', function() {
    window.location.href = './Dashboard.html';
});

$('.sideIcon').on('click', function() {
    var isVisible = $('.sideMenu').is(':visible');

    if (isVisible) {
        //use removeAttr instead of hide.
        $('.sideMenu').removeAttr('style');
    } else {
        $('.sideMenu').show();
    }
});

function ShowSubLlist(dom) {
    var isVisible = $(dom).next().is(':visible');

    if (isVisible) {
        $(dom).next().hide();
    } else {
        $(dom).next().fadeIn();
    }
}