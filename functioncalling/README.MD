# Function calling
<a href="https://github.com/a35ksyd/openaiexamples/tree/main/visionapi">Visionapi</a> demostates how to leverage vision API to identify object and photo and try to calculate the price. It also shows how to provied custom data in faciliate the calculation.  In this example we go further to reterive the price from thrid party api.

## Server
Rest services which return the price
/price/{item}
example: http://localhost:3000/price/apple
{"item":"apple","price":{"price":0.99},"unixTimestamp":1723999534732}

## Client
The client getting the price infromation from external service by <a href="https://platform.openai.com/docs/guides/function-calling"> function calling</a>.
