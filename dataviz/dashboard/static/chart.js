
let width, height, gradient;
function getGradient(ctx, chartArea) {
    const chartWidth = chartArea.right - chartArea.left;
    const chartHeight = chartArea.bottom - chartArea.top;
    if (!gradient || width !== chartWidth || height !== chartHeight) {

        width = chartWidth;
        height = chartHeight;
        gradient = ctx.createLinearGradient(0, chartArea.bottom, 0, chartArea.top);
        gradient.addColorStop(0, 'rgba(0, 49, 92, 0.9)');
        gradient.addColorStop(0.5, 'rgba(116, 240, 59, 0.9)');
        gradient.addColorStop(1, 'rgba(0, 34, 116, 0.9)');
    }

    return gradient;
}


const ctx = document.getElementById('dashcanvas').getContext('2d');
const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'December'],
        datasets: [{
            label: 'Looping tension',
            data: [45, 39, 50, 41, 36, 45, 40, 39, 50, 41, 36, 45],
            fill: false,
            tension: 2,
            borderColor: function(context) {
                const chart = context.chart;
                const {ctx, chartArea} = chart;
        
                if (!chartArea) {
                  // This case happens on initial chart load
                  return;
                }
                return getGradient(ctx, chartArea);
              },
        }]
        },
    
    maintainAspectRatio: false,
    aspectRatio: 1|4,
    options: {
        responsive: true,
        animations: {
            
            tension: {
                duration: 1000,
                easing: 'linear',
                from: 1,
                to: 0,
                loop: true
            }
        },
        scales: {
            x: {
                grid: {
                    drawBorder: false,
                    display: false
                },
                ticks: {
                    display: false
                }
            },
            y: { // defining min and max so hiding the dataset does not change scale range
                min: 30,
                max: 50,
                grid: {
                    
                    display: false
                },
                ticks: {
                    display: false
                }
            },
            height: 50
        
        },
        
        plugins: {
            legend: {
                display: false
            }
        }
         
    }
    
});



fetch('/intensity-data/')
.then(response => response.json())
.then(data => {
    const ctx = document.getElementById('myintensity').getContext('2d');
    const chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labelsx,
            datasets: [
                {
                    label: 'data points with above intensity',
                    data: data.labelsy,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    hoverBackgroundColor: "rgba(90, 100, 255, 0.3)",
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                },
                
            ]
        },
        options: {
            scales: {
            y: {
                beginAtZero: true
            }
            }
        }
    });
});


fetch('/pub-data/')
.then(response => response.json())
.then(data => {
    const ctx = document.getElementById('pubdata').getContext('2d');
    const chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labelsx,
            datasets: [
                {
                    label: 'data points with same date',
                    data: data.labelsy,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    hoverBackgroundColor: "rgba(90, 100, 255, 0.7)",
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                },
                
                {
                    type: 'line',
                    label: 'data points with same date',
                    data: data.labelsy,
                    fill: false,
                    borderColor: 'rgba(255, 199, 132, 1)',
                    borderWidth: 3,
                    tension: 0.5, 
                    
                },
                
                
                
            ]
            
        },
        options: {
            scales: {
                x: {
                    grid: {
                        display: false
                    }
                },
                y: {
                    beginAtZero: true,
                    grid: {
                        display: false
                    }
                },
                
            }
        }
    });
});


fetch('/year_topics/')
.then(response => response.json())
.then(data => {
    const ctx = document.getElementById('year_datas').getContext('2d');
    const chart = new Chart(ctx, {
        type: 'scatter',
        data: {
            labels: data.dx,
            datasets: [
                {
                    type: 'bar',
                    label: 'data points with same date',
                    data: data.dy,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    hoverBackgroundColor: "rgba(90, 100, 255, 0.7)",
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                },
                
                
            ]
        },
        options: {
            scales: {
            y: {
                beginAtZero: true
            }
            }
        }
    });
});


fetch('/published_yr_data/')
.then(response => response.json())
.then(data => {
    const ctx = document.getElementById('published_datas_line').getContext('2d');
    const chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.dx,
            datasets: [
                {
                    label: 'Number of data point published in particular years',
                    data: data.dy,
                    fill: false,
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1,
                    tension: 0.1, 
                    fill: true
                },
                
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
});


fetch('/published_yr_data/')
.then(response => response.json())
.then(data => {
    const ctx = document.getElementById('published_datas_pie').getContext('2d');
    const chart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: data.dx,
            datasets: [
                {
                    label: 'number of data points published in same year',
                    data: data.dy,
                    backgroundColor: data.COLORS,
        
                },
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Chart.js Pie Chart'
                }
            }
        },
    });
});


fetch('/published_month_data/')
.then(response => response.json())
.then(data => {
    const ctx = document.getElementById('published_datas_doughnut').getContext('2d');
    const chart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels:  ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            datasets: [
                {
                    label: 'number of data points published in same year',
                    data: data.dy,
                    backgroundColor: data.COLORS,
        
                },
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Chart.js Pie Chart'
                }
            }
        },
    });
});


fetch('/country_month_data/')
.then(response => response.json())
.then(data => {
    const ctx = document.getElementById('scatterdata').getContext('2d');
    dataset_data = []
    
    for ( let i = 0; i < data.data.length; i++){
        const newDataset = {}
        newDataset.label = data.data[i].label
        newDataset.data = data.data[i].data
        newDataset.backgroundColor = data.data[i].bgcolor

        dataset_data.push(newDataset)

    }

    const chart2 = new Chart(ctx, {
        type: 'bubble',
        data: {
            labels:  data.lebels,
            datasets: dataset_data,
        },
        options: {
            
                scales: {
                    x: {
                        grid: {
                            display: false
                        }
                    },
                    y: {
                        grid: {
                            display: false
                        }
                    }
                },
                title: {
                    display: true,
                    text: 'Custom Chart Title',
                    padding: {
                        top: 10,
                        bottom: 30
                    }
                },
                subtitle: {
                    display: true,
                    text: 'Custom Chart Subtitle'
                }
        
        },
        
    });
});

