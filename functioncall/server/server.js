const express = require('express');
const dataservice = require('./dataservices')
const app = express();
const port = 3000; 



app.get('/price/:item', (req, res) => {
    const item = req.params.item;
    const itemePrice = dataservice.getPrice(item);
    const unixTimestamp = Date.now();

    res.json({
        item: item,
        price: itemePrice,
        unixTimestamp: unixTimestamp,
    });
});

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});