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
                name: 'Pageviews for Artist 1',
                data: wikiy
            },{
                name: 'Pageviews for Artist 2',
                data: wikiy2
            }]
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
                    text: 'Ranking this month:'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                valueSuffix: ''
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle',
                borderWidth: 0
            },
            series: [{
                name: 'Ranking this month for Artist 1',
                data: artnet
            },{
                name: 'Ranking this month for artist 2',
                data: artnet2
            }]
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
                name: 'Relative Popularity Artist 1',
                data: gtrendsy
            },{
                name: 'Relative Popularity Artist 2',
                data: gtrendsy2
            }]
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
                name: ' Number of Likes for Artist 1 (This Month)',
                data: fby
            },{
                name: ' People Talking About Artist 1 (This Month)',
                data: fby2
            },{
                name: ' Number of Likes for Artist 2 (This Month)',
                data: fby_2
            },{
                name: ' People Talking About Artist 2 (This Month)',
                data: fby2_2
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
                name: ' Estimated Minimum for Artist 1 works',
                data: auclow
            },{
                name: ' Estimated Maximum for Artist 1 works',
                data: auchigh
            },{
                name: ' Sale Price for Artist 1 works',
                data: aucfinal
            }, {
                name: ' Estimated Minimum for Artist 2 works',
                data: auclow2
            },{
                name: ' Estimated Maximum for Artist 2 works',
                data: auchigh2
            },{
                name: ' Sale Price for Artist 2 works',
                data: aucfinal2
            }]

});

        if(typeof auclow != 'undefined' && auclow.length > 0 && auclow2.length > 0){
            $('#no-auction-data').hide();

            var p = calculateAuctionStats();
            var rounded_p = (p).toFixed(2);
            var p2 = calculateAuctionStats2();
            var rounded_p2 = (p2).toFixed(2);
            $('#trend-percent').html(rounded_p + ", " + rounded_p2);
            var ex_sale_price;
            if (p < 0){
                $('#auction-trend').html("On average, recent auctions have sold " + rounded_p + "% and " + rounded_p2 + "% of the price range <font color='red'>below</font> the high estimate respectively.");
                ex_sale_price = 1100 - parseFloat(rounded_p);
                $('#trend-percent').css("color", "red");
            } else {
                $('#auction-trend').html("On average, recent auctions have sold " + rounded_p + "% and " + rounded_p2 + "% of the price range <font color='green'>above</font> the high estimate respectively.");
                ex_sale_price = 1100 + parseFloat(rounded_p);    
                $('#trend-percent').css("color", "green");
                }
            $('#trend-tooltip').attr("title", "E.g. a piece with a predicted sale price range of $1000 to $1100 would have sold for $" + ex_sale_price);
            $("#trend-tooltip").tooltip();
        }
        else {
            $('#auction-container').hide();
            $('#no-auction-data').show();
        }
        
        if(typeof fby2 == 'undefined' || fby2.length == 0){
            $('#fb-container').hide();
            $('#no-fb-data').show();
            
        }
        else {
            $('#no-fb-data').hide();
        }            

        $("#export").click(function () {
            var chartlist = []
            var wikipedia = $('#wikipedia').highcharts();
            chartlist.push(wikipedia);
            if (fbx) {
                var fb = $('#fb').highcharts();
                chartlist.push(fb);
            }
            var google = $('#google').highcharts();
            chartlist.push(google);
            if (artnet) {
                var artnet = $('#artnet').highcharts();
                chartlist.push(artnet);
            }
            if (aucx) {
                var auction = $('#auction').highcharts();
                chartlist.push(auction);
            }
            printCharts(chartlist);
        });
    });

function printCharts(charts) {
    var origDisplay = [],
        origParent = [],
        body = document.body,
        childNodes = body.childNodes;

    // hide all body content
    var x = document.getElementsByTagName("h1")[0]
    Highcharts.each(childNodes, function (node, i) {
        if (node.nodeType === 1) {
            origDisplay[i] = node.style.display;
            node.style.display = "none";
        }
    });

    body.appendChild(x);
    console.log("HI");

    // put the charts back in
    $.each(charts, function (i, chart) {
        origParent[i] = chart.container.parentNode;
        body.appendChild(chart.container);
    });

    // print
    window.print();

    // allow the browser to prepare before reverting
    setTimeout(function () {
        // put the chart back in
        $.each(charts, function (i, chart) {
            origParent[i].appendChild(chart.container);
        });

        // restore all body content
        Highcharts.each(childNodes, function (node, i) {
            if (node.nodeType === 1) {
                node.style.display = origDisplay[i];
            }
        });
    }, 500);
}

    
function calculateAuctionStats(){
    if (!aucx || aucx && aucx.length < 1){
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

function calculateAuctionStats2(){
    if (!aucx2 || aucx2 && aucx2.length < 1){
        return 0;
    }
    var totalpercent = 0;
    for (var i = 0; i < aucx2.length; i++) {
        var range = auchigh2[i]-auclow2[i];
        var sale_diff_from_high = aucfinal2[i]-auchigh2[i];
        var percent = sale_diff_from_high/range;
        totalpercent += percent;
    } 
    var avgpercent = totalpercent/aucx2.length;
    return avgpercent*100;
}