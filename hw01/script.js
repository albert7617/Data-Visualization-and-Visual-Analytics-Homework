var data;
const dataName = ['sepal length', 'sepal width', 'petal length', 'petal width'];

const render = (data, xAsis, yAsis) => {    
  let width = parseInt(d3.select("#chart").style("width"), 10) - 20;
  let height = 500;
  d3.select("#chart svg").remove();
  const svg = d3
    .select("#chart")
    .append("svg")
    .attr("height", height)
    .attr("width", width);

  const circleRadius = 10;

  const xValue = d => d[xAsis];
  const xAxisLabel = xAsis;
  
  const yValue = d => d[yAsis];
  const yAxisLabel = yAsis;
  
  const margin = { top: 60, right: 40, bottom: 88, left: 150 };
  const innerWidth = width - margin.left - margin.right;
  const innerHeight = height - margin.top - margin.bottom;
  
  const xScale = d3.scaleLinear()
    .domain(d3.extent(data, xValue))
    .range([0, innerWidth])
    .nice();
  
  const yScale = d3.scaleLinear()
    .domain(d3.extent(data, yValue))
    .range([innerHeight, 0])
    .nice();
  
  const g = svg.append('g')
    .attr('transform', `translate(${margin.left},${margin.top})`);
  
  const xAxis = d3.axisBottom(xScale)
    .tickSize(-innerHeight)
    .tickPadding(15);
  
  const yAxis = d3.axisLeft(yScale)
    .tickSize(-innerWidth)
    .tickPadding(10);
  
  const yAxisG = g.append('g').call(yAxis);
  yAxisG.selectAll('.domain').remove();
  
  yAxisG.append('text')
      .attr('class', 'axis-label')
      .attr('y', -93)
      .attr('x', -innerHeight / 2)
      .attr('fill', 'black')
      .attr('transform', `rotate(-90)`)
      .attr('text-anchor', 'middle')
      .text(yAxisLabel);
  
  const xAxisG = g.append('g').call(xAxis)
    .attr('transform', `translate(0,${innerHeight})`);
  
  xAxisG.select('.domain').remove();
  
  xAxisG.append('text')
      .attr('class', 'axis-label')
      .attr('y', 75)
      .attr('x', innerWidth / 2)
      .attr('fill', 'black')
      .text(xAxisLabel);
  
  g.selectAll('circle').data(data)
    .enter().append('circle')
      .attr('class', d => d.class)
      .attr('cy', d => yScale(yValue(d)))
      .attr('cx', d => xScale(xValue(d)))
      .attr('r', circleRadius);
  
};

d3.csv('iris.csv')
  .then(csv => {
    render(csv, dataName[$('input[name="x-axis"]:checked').val()], dataName[$('input[name="y-axis"]:checked').val()]);
    data = csv
    console.log(data);
  });

window.addEventListener('resize', () => { render(data, dataName[$('input[name="x-axis"]:checked').val()], dataName[$('input[name="y-axis"]:checked').val()]) });

$('input[name="x-axis"]').on('change', function(event) {
  render(data, dataName[$('input[name="x-axis"]:checked').val()], dataName[$('input[name="y-axis"]:checked').val()]);
}); 

$('input[name="y-axis"]').on('change', function(event) {
  render(data, dataName[$('input[name="x-axis"]:checked').val()], dataName[$('input[name="y-axis"]:checked').val()]);
}); 



