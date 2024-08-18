// Simple dataservices will lookup the proce from itemprice map

const itemprice = {
    'apple': { price: 0.99 },
    'banana': { price: 0.5 },
    'orange': { price: 1.25 },
  };


function getPrice(item) {
    return itemprice[item] || 0.0;
}  

module.exports = {
    getPrice
};