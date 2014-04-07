$(function () {
        $('#wikipedia').highcharts({
            title: {
                text: 'Number of Wikipedia pageviews per month',
                x: -20 //center
            },
            xAxis: {
                title: {
                    text: 'YYYYMM'
                },
                categories: ['201301', '201302', '201303', '201304', '201305', '201306', '201307', '201308', '201309', '201310', '201311', '201312', '201401', '201402']
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
                data: [329938, 321178, 349374, 324800, 297749, 211787, 177399, 202992, 182510, 272679, 258345, 210897, 200095, 188497]
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
                categories: ['01-05', '01-12', '01-19', '01-26', '02-02', '02-09', '02-16', '02-23', '03-02', '03-09', '03-16', '03-23', '03-30', '04-06', '04-13', '04-20', '04-27', '05-04', '05-11', '05-18', '05-25', '06-01', '06-08', '06-15', '06-22', '06-29', '07-06', '07-13', '07-20', '07-27', '08-03', '08-10', '08-17', '08-24', '08-31', '09-07', '09-14', '09-21', '09-28', '10-05', '10-12', '10-19', '10-26', '11-02', '11-09', '11-16', '11-23', '11-30', '12-07', '12-14', '12-21', '12-28', '01-04', '01-11', '01-18', '01-25', '02-01', '02-08', '02-15', '02-22', '03-01', '03-08']
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
                data: [31, 40, 36, 37, 38, 38, 37, 36, 37, 36, 35, 42, 41, 38, 39, 40, 41, 40, 38, 39, 36, 36, 36, 33, 31, 29, 28, 29, 26, 25, 26, 44, 28, 29, 31, 29, 32, 32, 32, 33, 38, 35, 35, 58, 43, 50, 41, 36, 41, 41, 51, 36, 33, 37, 39, 39, 39, 39, 35, 35, 34, 33]
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
    
