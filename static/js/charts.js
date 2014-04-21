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

        $("#export").click(function () {
            var wikipedia = $('#wikipedia').highcharts();
            var fb = $('#fb').highcharts();
            var google = $('#google').highcharts();
            var artnet = $('#artnet').highcharts();
            var auction = $('#auction').highcharts();
            printCharts([wikipedia, artnet, fb, google, auction]);
        });

        function printCharts(charts) {

            var origDisplay = [],
                origParent = [],
                body = document.body,
                childNodes = body.childNodes;

            // hide all body content
            Highcharts.each(childNodes, function (node, i) {
                if (node.nodeType === 1) {
                    origDisplay[i] = node.style.display;
                    node.style.display = "none";
                }
            });

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

 
    });
    
