importScripts('https://albert7617.github.io/Data-Visualization-and-Visual-Analytics-Homework/hw04/lib/science.v1.min.js', 
  'https://albert7617.github.io/Data-Visualization-and-Visual-Analytics-Homework/hw04/lib/tiny-queue.js',
  'https://albert7617.github.io/Data-Visualization-and-Visual-Analytics-Homework/hw04/lib/reorder.v1.min.js');

onmessage = function(e) {
  postMessage(reorder.optimal_leaf_order().distance(science.stats.distance.braycurtis)(e.data));
}