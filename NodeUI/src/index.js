//const io = require("socket.io-client");
const Chart = require('chart.js');

const DATA_COUNT = 12;
const labels = [];

const PesoData = [];
const TempData = [];
const LuzData = [];
const HumData = [];

//const socket = io();

for (let i = 0; i < DATA_COUNT; ++i) {
  labels.push(i.toString());
  TempData.push(0);
  PesoData.push(0);
  LuzData.push(0);
  HumData.push(0);
}

const data = {
  labels: labels,
  datasets: [
    {
      label: 'Temperatura[C]',
      data: TempData,
      fill: false,
      borderColor: '#E35D52',
    },
    {
      label: 'Humedad Relativa[%]',
      data: HumData,
      fill: false,
      borderColor: '#52C7E3'
    },
    {
      label: 'Peso-Masa[Kg]',
      data: PesoData,
      fill: false,
      borderColor: '#D38D38',
    },
    {
      label: 'Luminocidad[%]',
      data: LuzData,
      fill: false,
      borderColor: '#8338D3'
    }
  ]
};

const config = {
  type: 'line',
  data: data,
  options: {
    responsive: false,
    plugins: {
      title: {
        display: true,
        text: 'Chart.js Line Chart - Cubic interpolation mode'
      },
    },
    interaction: {
      intersect: false,
    },
    scales: {
      x: {
        display: true,
        title: {
          display: true
        }
      },
      y: {
        display: true,
        title: {
          display: true,
          text: 'Value'
        },
        suggestedMin: 0,
        suggestedMax: 100
      }
    }
  },
};


const ctx = document.getElementById('myChart').getContext("2d");
ctx.canvas.width = 1024;
ctx.canvas.height = 600;

const myChart = new Chart(ctx, config);

function addData(chart, alias, data) {
    chart.data.datasets.forEach((dataset) => {
        if( dataset.label == alias )
        {
          dataset.data.shift();
          dataset.data.push(data);
        }
    });
    chart.update();
}

//socket.on ('perceptionData', (data) => {
//    addData( myChart, 'Temperatura[C]', data.Temp );
//    addData( myChart, 'Humedad Relativa[%]' , data.Hum );    
//    addData( myChart, 'Peso-Masa[Kg]' , data.Peso );    
//    addData( myChart, 'Luminocidad[%]' , data.Luz );    
//});