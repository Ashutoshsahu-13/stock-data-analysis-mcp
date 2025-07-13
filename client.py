from fastmcp import Client
import asyncio
import os
import json
import pandas as pd

 #server url
server_url="http://127.0.0.1:8000/mcp"

async def main():
    
    async with Client(server_url) as client:
        file_id=str(input("Enter file id:"))
        file_name=str(input("Enter file name:"))
        flag=True
        while True:
            user_input=input("Enter your query: ")
            if user_input.lower() in ["exit","quit"]:
                break
            try:
                param={"query":user_input}
                if flag:
                    param["file_id"]=file_id
                    param["file_name"]=file_name
                    flag=False

                data= await client.call_tool("analyze_stock_data",param)
                raw_text=data.text
                ans=json.loads(raw_text)
                print(ans.get("message","error"))
            except Exception as e:
                print(f"Error: {e}")
            
if __name__=="__main__":
    asyncio.run(main())


