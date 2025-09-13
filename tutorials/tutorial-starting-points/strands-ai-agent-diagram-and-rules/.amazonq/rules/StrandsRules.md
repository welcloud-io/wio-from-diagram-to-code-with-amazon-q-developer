When asked to use AWS Strands SDK here are the rules

- install strands-agents python module in the 'strands_packages' target folder inside the lambda folder
- use strands_packages with import intructions
- import necessary python modules
- create rules with @tool decorator
- use "anthropic.claude-3-haiku-20240307-v1:0" model
- create a system prompt that describes the role of the agent
- for agent import Agent from strands
- for tool import tool from strands
- use response = agent(..) to invoke agent, convert the response to a string
- Allow lambda calling bedrock with stream response