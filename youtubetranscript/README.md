This example demonstrates how to use OpenAI to summarize a YouTube video transcript. The `youtube_transcript_api` is a third-party library that captures the video transcript, which can then be summarized using the Chat Completion API based on the transcript. To save costs, we use the `gpt-3.5-turbo` model, which is very effective for summarization.

The youtube video
https://youtu.be/CMsuDp_DER4?si=0xEnf4lsKLeKPOFt

Sample output of video youtube transcript
[{'text': '[Music]', 'start': 0.37, 'duration': 7.23}, {'text': 'ja agrip is a agricultural company and', 'start': 2.72, 'duration': 6.799}, {'text': 'this company is a subsidary company of', 'start': 7.6, 'duration': 4.8}, {'text': 'Japan Airline and then so this uh', 'start': 9.519, 'duration': 5.801}, {'text': 'company was established in', 'start': 12.4, 'duration': 6.639}, {'text': '2018 as a joint', 'start': 15.32, 'duration': 3.719}, {'text': 'Venter the company Wago is a very famous', 'start': 19.32, 'duration': 5.879}, {'text': 'agricultural company and then so they', 'start': 22.519, 'duration': 5.561}, {'text': 'have so experiences in the agriculture', 'start': 25.199, 'duration': 6.121},


Response from Chatgpt
choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="JA Agrip is an agricultural company established in 2018 as a joint venture with Wago, a well-known agricultural company. They have three main business points: farm business, restaurant business, and JA Agri products. They offer various types of fruits and vegetables, traditional Japanese dishes, and products made from their farm produce. The company aims to promote agriculture in Narita city and hopes to export their strawberries internationally with the help of Japan Airlines' transportation function. They invite international travelers to enjoy their strawberry picks, farm, and restaurant.", refusal=None, role='assistant', function_call=None, tool_calls=None))], model='gpt-3.5-turbo-0125', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=108, prompt_tokens=601, total_tokens=709))

