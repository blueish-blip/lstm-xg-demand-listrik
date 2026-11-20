const ctx = document.getElementById('demandChart').getContext('2d');

// Placeholder Data - Akan diganti dengan data dari CSV/JSON
const demandData = {
    labels: ['01:00', '02:00', '03:00', '04:00', '05:00'],
    datasets: [
        {
            label: 'Actual Demand',
            data: [970, 912, 900, 889, 893],
            borderColor: '#FFD3B6',
            backgroundColor: '#FFD3B6',
            tension: 0
        },
        {
            label: 'XGBoost Prediction',
            data: [965, 915, 895, 885, 898],
            borderColor: '#A8E6CF',
            backgroundColor: '#A8E6CF',
            tension: 0
        }
    ]
};

new Chart(ctx, {
    type: 'line',
    data: demandData,
    options: {
        responsive: true,
        plugins: {
            legend: { position: 'bottom' }
        },
        scales: {
            y: { grid: { display: false } },
            x: { grid: { display: false } }
        }
    }
});