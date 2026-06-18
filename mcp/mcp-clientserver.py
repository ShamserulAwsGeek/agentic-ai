from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()
import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command": "python",
                "args": ["mcp/mcp-mathserver.py"],  #" mention correct absolute path to mcp-mathserver.py"
                "transport": "stdio",
            },
            
            "weather":{
                "url": "http://localhost:8000/mcp", #ensure server is running and accessible at this URL
                "transport": "streamable--http", 
            }  
        }          
    )
    
    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(model="qwen-qwq-32b")
    agent = create_agent(
        model, tools
    )

    math_response = await agent.ainvoke(
        {"message": [{"role": "user", "content": "What is 5 multiplied by 7?"}]}
    )

    print("Math Response:", math_response["message"][-1]["content"])


    weather_response = await agent.ainvoke(
        {"message": [{"role": "user", "content": "What is the weather in Bengaluru?"}]}
    )
    print("Weather Response:", weather_response["message"][-1]["content"])

asyncio.run(main())

