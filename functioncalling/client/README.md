# README: `Function calling` in OpenAI API

This guide helps you use the `Function calling` feature in OpenAI API to call an external API based on user input.


## Code Overview

This script allows you to query item prices from external services using OpenAI's `Function calling` feature


### 1. External Function to Get Item Price
The server folder contains the service implementation in node.js

This function makes a GET request to an external API to retrieve the price of a given item:
```python
def get_item_price(item):
    response = requests.get(f'http://localhost:3000/price/{item}')
    return response.json()
```

### 2. Define Tools for OpenAI

The `tools` list defines the external functions that OpenAI can call:
```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_item_price",
            "description": "Get the item price",
            "parameters": {
                "type": "object",
                "properties": {
                    "item": {
                        "type": "string",
                        "description": "The item name",
                    },
                },
                "required": ["item"],
                "additionalProperties": False,
            },
        }
    }
]
```
function name: contatins the function name
parameters: define the parameters

### 3. Define User Messages

The script sets up the initial messages that will guide the user interaction:
```python
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Please enter the item name"
            },
            {
                "type": "text",
                "text": "Identify known/unknown items and sum the total."
            },            
        ]
    }
]
```

function name: contatins the function name
parameters: define the parameters


### 4. Function to Call OpenAI

This function sends the request to OpenAI, which will decide if an external function needs to be called:
```python
def callOpenAI(client):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        max_tokens=100
    ) 
    return response
```

### 6. Get User Input

This function captures user input and updates the message list:
```python
def getUserInput():
    item_name = input("Please enter the item name:")
    new_item = {
        "type": "text",
        "text": f"Item name: {item_name}"
    }   
    messages[0]["content"].append(new_item)  
```

### 6. Initialize the OpenAI Client

The script initializes the OpenAI client with your API key:
```python
client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")
```

### 8. Execute the Main Logic

OpenAI determines whether an external call is necessary. If an external call is required, the tool_calls variable will not be null:

tool_calls = response.choices[0].message.tool_calls

Example
Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content=None, refusal=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_ac9BfbR9mGgEseUjCNzDDaqF', function=Function(arguments='{"item":"apple"}', name='get_item_price'), type='function')]))


```python
# Get user input
getUserInput()

# Initiate the OpenAI call
response = callOpenAI(client)

# Check for external function call
tool_calls = response.choices[0].message.tool_calls
if tool_calls:
    tool_call = tool_calls[0]
    arguments = tool_call.function.arguments
    argumentsMap = json.loads(arguments)
    itemName = argumentsMap["item"]

    # Call the external function
    result = get_item_price(itemName)
    replyItem = result['item']
    replPrice = result['price']['price']

    # Prepare the function call result message
    function_call_result_message = {
        "role": "tool",
        "content": json.dumps({
            "item": replyItem,
            "price": result
        }),
        "tool_call_id": tool_call.id
    }

    # Send the completion payload to OpenAI
    completion_payload = {
        "model": "gpt-4o",
        "messages": [
            response.choices[0].message,
            function_call_result_message
        ]
    }
    completeResponse = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=completion_payload["messages"]
    )
    
    # Display the result
    print(completeResponse.choices[0])
```



## Example
Please enter the item name:apple
Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='The price of an apple is $0.99.', refusal=None, role='assistant', function_call=None, tool_calls=None))
