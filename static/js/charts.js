$(document).ready(function() {

        // console.log(wikix);
        console.log(wikiy);
        $('#wikipedia').highcharts({
            title: {
                text: 'Number of Wikipedia pageviews per month',
                x: -20 //center
            },
            xAxis: {
                title: {
                    text: 'YYYYMM'
                },
                categories: wikix
            },
            yAxis: {
                title: {
                    text: 'Pageviews'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                valueSuffix: ' Pageviews'
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle',
                borderWidth: 0
            },
            series: [{
                name: 'Pageviews',
                data: wikiy
            },]
        });
        $('#artnet').highcharts({
            title: {
                text: 'Artnet Ranking',
                x: -20 //center
            },
            xAxis: {
                title: {
                    text: 'Month'
                },
                categories: ["October", "November", "December", "January", "February", "March"]
            },
            yAxis: {
                title: {
                    text: 'Ranking'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                valueSuffix: ' Rank in Months'
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle',
                borderWidth: 0
            },
            series: [{
                name: 'Ranking',
                data: artnet
            },]
        });
        $('#google').highcharts({
            title: {
                text: 'Google Popularity',
                x: -20 //center
            },
            xAxis: {
                title: {
                    text: 'Week ending YYYY-MM-DD'
                },
                categories: gtrendsx
            },
            yAxis: {
                title: {
                    text: ' Relative Popularity'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle',
                borderWidth: 0
            },
            series: [{
                name: 'Relative Popularity',
                data: gtrendsy
            },]
});

        $('#fb').highcharts({
            title: {
                text: 'Facebook Trends',
                x: -20 //center
            },
            xAxis: {
                title: {
                    text: 'Month'
                },
                categories: fbx
            },
            yAxis: {
                title: {
                    text: ' Users'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle',
                borderWidth: 0
            },
            series: [{
                name: ' Number of Likes (This Month)',
                data: fby
            },{
                name: ' People Talking About This (This Month)',
                data: fby2
            }]

});

        $('#auction').highcharts({
            title: {
                text: 'Most Recent Auctions',
                x: -20 //center
            },
            xAxis: {
                title: {
                    text: 'Date of Auction'
                },
                categories: aucx
            },
            yAxis: {
                title: {
                    text: ' Price'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle',
                borderWidth: 0
            },
            series: [{
                name: ' Estimated Minimum',
                data: auclow
            },{
                name: ' Estimated Maximum',
                data: auchigh
            },{
                name: ' Sale Price',
                data: aucfinal
            }]

});

var p = calculateAuctionStats();
var rounded_p = (p).toFixed(2);

$('#trend-percent').html(rounded_p);


var ex_sale_price;
if (p < 0){
    $('#auction-trend').html("On average, recent auctions have sold " + rounded_p + "% of the price range <font color='red'>below</font> the high estimate.");
    ex_sale_price = 1100 - parseFloat(rounded_p);
    $('#trend-percent').css("color", "red");
} else {
    $('#auction-trend').html("On average, recent auctions have sold " + rounded_p + "% of the price range <font color='green'>above</font> the high estimate.");
    ex_sale_price = 1100 + parseFloat(rounded_p);    
    $('#trend-percent').css("color", "green");
    }
$('#trend-tooltip').attr("title", "E.g. a piece with a predicted sale price range of $1000 to $1100 would have sold for $" + ex_sale_price);
$("#trend-tooltip").tooltip();
    
    });
    
function calculateAuctionStats(){
    if (aucx.length < 1){
        return 0;
    }
    var totalpercent = 0;
    for (var i = 0; i < aucx.length; i++) {
        var range = auchigh[i]-auclow[i];
        var sale_diff_from_high = aucfinal[i]-auchigh[i];
        var percent = sale_diff_from_high/range;
        totalpercent += percent;
    } 
    var avgpercent = totalpercent/aucx.length;
    return avgpercent*100;
}

