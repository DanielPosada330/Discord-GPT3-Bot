# Discord-GPT3-Bot
The purpose of this program was to create a Discord Bot that utilized the GPT Large Language Model (LLM) so that my friends and I could
mess with while gaming.

![image](https://github.com/DanielPosada330/Discord-GPT4-Bot/assets/104124602/f3e29b27-1909-4ce8-b625-5c67acd70684)


## Motivation
I wanted to practice my Python programming, while also incorporating a web server to keep the bot alive even if my main program was shut off.
I also wanted to learn more about using APIs and how to incorporate them into a program.
## Languages and Tools
For this program, I utilized Python for the main program, Flask for the web server to keep the bot alive,
Discord API to host and interact on Discord, and OpenAI API to access the GPT4 LLM.
## Build Status
This program is up and running. Feel free to check out the bot and the program to see how I set it up!
## Important variable descriptions
When creating the program, there are a couple of token's and secret keys that you must utilize. I'll clear up some possible misunderstandings:

![image](https://github.com/DanielPosada330/Discord-GPT4-Bot/assets/104124602/d0b003ff-2c24-44c3-bca0-d8ce8d9268f3)

For here you need to use your Discord Bot's secret token and your Open AI Secret Key respectively. I recommend saving all these securely, as
anyone who has the secret tokens can control the bot. BE CAREFUL!!!

![image](https://github.com/DanielPosada330/Discord-GPT4-Bot/assets/104124602/2032c894-fea2-4cff-9a1f-20a806d129bb)

It's iumportant that we also utilize async functions as there will be multiple calls to different servers, and we don't want the program to be
bogged down on one particular portion of the program when we can instead be efficient and jump around completing the requests that are fast
early, and wait for the last one.
