import os
import requests
from openai import OpenAI
import json


# This function making api call to external api
def get_item_price(item):
    response = requests.get(f'http://localhost:3000/price/{item}')
    return response.json()


#Define the tools structure which contains the extenral function name OpenAPI may call
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_item_price",
            "description": "Get them item price",
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

# message
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



# Function to call OpenAPI
def callOpenAI(client):
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools,
    max_tokens=100
    ) 
    return response
       

#  Get user input
def getUserInput():
  item_name = input("Please enter the item name:")
  new_item = {
    "type": "text",
    "text": f"Item name: {item_name}"
  }   
  messages[0]["content"].append(new_item)  
  

# Initialize the API client
client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

# Get user input
getUserInput()

# Initiating the first OpenAI call; OpenAI will determine if it needs to leverage an external call.
response = callOpenAI(client)
print(response.choices[0])



#Check for non empty toll_calls object 
#ChatCompletionMessageToolCall(id='call_elYajbvEE1liIuONwxySNBdt', function=Function(arguments='{"item":"orange"}', 
#name='get_item_priceT'), type='function')
tool_calls = response.choices[0].message.tool_calls
if (tool_calls):
    #extracting the parameters
    tool_call = tool_calls[0]
    toolcallid = tool_call.id 
    functionName = tool_call.function
    arguments = tool_call.function.arguments
    argumentsMap = json.loads(arguments)
    itemName =  argumentsMap["item"]

    # Execute external function
    result = get_item_price(itemName)
    replyItem = result['item']
    replPrice = result['price']['price']

    # create a message contains the result from external function
    function_call_result_message = {
        "role": "tool",
        "content": json.dumps({
        "item": replyItem,
        "price": result
        }),
        "tool_call_id": tool_call.id
    }

    # create completion payload 
    completion_payload = {
    "model": "gpt-4o",
    "messages": [
        response.choices[0].message,
        function_call_result_message
    ]
}

    # send the completion payload to api
    completeResponse = client.chat.completions.create(
        model="gpt-4o-mini",messages=completion_payload["messages"])
    
    # display result
    print(completeResponse.choices[0])
