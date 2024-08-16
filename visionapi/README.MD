## Vision API
    This example demonstrates  how to leverage OpenAI's vision to detect objects within uploaded images. The example also covers how to supply domain knowledge to the API for improved problem-solving and how to incorporate user-specific data into API calls.

### First example
<br>
The first example showcases a scenario where a user uploads three pictures. The goal is to have the OpenAI API identify the objects in the images and, furthermore, provide an estimate of their prices.<br>
The reply is as follow <br>
<b>Apple** - Known item. Orange - Known item. **Dog** -Know item, but not able to calculate the price</b>
<br>
Choice(finish_reason='length', index=0, logprobs=None, message=ChatCompletionMessage(content="In the images, the items are:\n\n1. An apple (known item)\n2. An orange (known item)\n3. A dog (unknown in terms of selling price as it typically wouldn't be sold in a grocery context)\n\nAssuming standard prices in a grocery store:\n\n- Apple: $0.50 each\n- Orange: $0.75 each\n\n**Calculating the total:**\n\n- Total for apple: $0.50\n- Total for orange: $0.75\n\n", refusal=None, role='assistant', function_call=None, tool_calls=None))<br>


### Second example 
The second example demonstrates how the price information detailed below is supplied as an input to the API.
{"type": "text","text": "Apple: $1, Orange: $2."},<br>
<br>
Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="Let's identify the items and calculate the total price.\n\n**Known Items:**\n1. Apple: $1\n2. Orange: $2\n\n**Unknown Item:**\n1. Dog (not applicable for pricing)\n\n**Total Calculation:**\n- Price of 1 Apple = $1\n- Price of 1 Orange = $2\n\n**Total Price = $1 + $2 = $3**\n\nSo, the total price for the items is **$3**.", refusal=None, role='assistant', function_call=None, tool_calls=None))
<br>
<b>Total Calculation:**\n- Price of 1 Apple = $1\n- Price of 1 Orange = $2\n\n**Total Price = $1 + $2 = $3</b>

In real-world applications, user-provided information can be obtained through <a href="https://platform.openai.com/docs/guides/function-calling"> function calling</a> API  or by training custom models. We'll demonstrate both approaches in later examples.