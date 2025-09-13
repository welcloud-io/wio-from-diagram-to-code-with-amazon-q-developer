When asked to use AWS Strands SDK here are the rules

- use lambda layer for strands packages
- install strands-agents python module in lambda layer folder
- install strands-agents-tools python module in lambda layer folder
- create rules with @tool decorator
- use "anthropic.claude-3-haiku-20240307-v1:0" model
- create a system prompt that describes the role of the agent
- for agent import Agent from strands
- for tool import tool from strands
- use response = agent(..) to invoke agent, convert the response to a string
- Allow lambda calling bedrock with stream response
- Strands Agent Class parameters are model, tools, system_prompt
- When you have to deal with dates (relative or absolute) use strands current_time tool from strand_tools