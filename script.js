const ctx = document.getElementById('demandChart').getContext('2d');

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
            legend: { labels: { color: '#f8fafc' } }
        },
        scales: {
            y: { grid: { color: '#334155' }, ticks: { color: '#94a3b8' } },
            x: { grid: { color: '#334155' }, ticks: { color: '#94a3b8' } }
        }
    }
});

document.getElementById('predict-btn').addEventListener('click', () => {
    const temp = parseFloat(document.getElementById('temp').value);
    const hour = parseFloat(document.getElementById('hour').value);
    
    // Simulasi hasil prediksi
    const prediction = 800 + (temp * 4.5) + (hour * 8.2);
    
    document.getElementById('prediction-result').innerText = prediction.toFixed(2) + " MW";
});