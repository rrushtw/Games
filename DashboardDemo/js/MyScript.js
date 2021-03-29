$(document).ready(function() {

});

$(window).on('resize', function() {
    DrawDonut();
    DrawLineChart();
    DrawPieChart();
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

//#region google chart
google.charts.load('current', { 'packages': ['corechart', ] });
google.charts.setOnLoadCallback(DrawLineChart);

function DrawLineChart() {
    var data = google.visualization.arrayToDataTable([
        ['Year', 'Sales', 'Expenses'],
        ['2004', 1000, 400],
        ['2005', 1170, 460],
        ['2006', 660, 1120],
        ['2007', 1030, 540],
        ['2008', 1000, 400],
        ['2009', 1170, 460],
        ['2010', 660, 1120],
        ['2011', 1030, 540],
    ]);

    var options = {
        title: 'Company Performance',
        curveType: 'function',
        legend: { position: 'bottom' }
    };

    var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

    chart.draw(data, options);
}

google.charts.load('current', { 'packages': ['gauge'] });
google.charts.setOnLoadCallback(DrawDonut);

function DrawDonut() {
    var data = google.visualization.arrayToDataTable([
        ['Label', 'Value'],
        ['Sales', 1010],
    ]);

    var options = {
        greenFrom: 1000,
        greenTo: 1500,
        yellowFrom: 500,
        yellowTo: 700,
        redFrom: 0,
        redTo: 500,
        minorTicks: 10,
        max: 1500,
        min: 0,
    };

    var chart = new google.visualization.Gauge(document.getElementById('Salse'));
    chart.draw(data, options);


    data = google.visualization.arrayToDataTable([
        ['Label', 'Value'],
        ['Expenses', 990],
    ]);

    options = {
        yellowFrom: 1000,
        yellowTo: 1200,
        redFrom: 1200,
        redTo: 1500,
        minorTicks: 10,
        max: 1500,
        min: 0,
    };

    chart = new google.visualization.Gauge(document.getElementById('Expense'));
    chart.draw(data, options);
}

google.charts.load('current', { 'packages': ['corechart'] });
google.charts.setOnLoadCallback(DrawPieChart);

function DrawPieChart() {
    var data = google.visualization.arrayToDataTable([
        ['Task', 'Hours per Day'],
        ['Work', 11],
        ['Eat', 2],
        ['Commute', 2],
        ['Watch TV', 2],
        ['Sleep', 7]
    ]);

    var options = {
        title: 'My Daily Activities',
        fontSize: 17
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart'));

    chart.draw(data, options);
}
//#endregion