## function call
    This example demonstrates how to integrate openAPi with extrnal API.
Visionapi example demostates how to leverage vision API to identify object and photo and try to calculate the price. It also shows how to provied custom data in faciliate the calculation.  In this example we go further to
reterive the price from thried party api.

## server
Node Rest services which return the price
/price/{item}
example: http://localhost:3000/price/apple
{"item":"apple","price":{"price":0.99},"unixTimestamp":1723999534732}

### Client

In real-world applications, user-provided information can be obtained through <a href="https://platform.openai.com/docs/guides/function-calling"> function calling</a> API  or by training custom models. We'll demonstrate both approaches in later examples.
