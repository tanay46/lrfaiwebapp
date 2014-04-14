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
                valueSuffix: ' Rank in Month'
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
                categories: ['Apr-13', 'May-13', 'Jun-13', 'Jul-13', 'Aug-13', 'Sep-13', 'Oct-13', 'Nov-13', 'Dec-13', 'Jan-14', 'Feb-14', 'Mar-14']
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
                data: [3067, 3500, 2593, 3924, 4908, 2566, 4901, 3872, 3326, 5623, 4470]
            },{
                name: ' People Talking About This (This Month)',
                data: [11776, 7838, 9852, 14585, 11477, 6637, 12560, 13344, 7205, 22188, 12007]
            }]

});

        $('#auction').highcharts({
            title: {
                text: 'Most Recent Auctions',
                x: -20 //center
            },
            xAxis: {
                title: {
                    text: 'Work'
                },
                categories: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
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
                data: [5000, 5000, 1500000, 12000, 12000, 3000, 1500, 3000, 100000, 60000, 750000, 1000000, 750000, 15000, 15000, 35000, 30000, 2000, 600000]
            },{
                name: ' Estimated Maximum',
                data: [7000, 7000, 2500000, 15000, 15000, 5000, 2000, 5000, 150000, 80000, 950000, 1500000, 950000, 20000, 20000, 45000, 50000, 3000, 800000]
            },{
                name: ' Sale Price',
                data: [6875, 8125, 1805000, 35625, 16250, 3750, 3125, 10000, 242500, 134500, 1184500, 2322500, 842500, 18750, 23750, 56250, 37500, 3400, 1082500]
            }]

});

 
    });
    
