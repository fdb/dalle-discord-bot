# DALL-E Discord Bot

Very simple bot that generates images with DALL-E.

## To install

- Go to the [Discord developer portal](https://discord.com/developers/applications/)

- Permissions are set to 2048 (send messages)
- Scope is "bot" (not sure why)
- client_id comes from the bot configuration

In my case it looks like this:

<https://discord.com/oauth2/authorize?client_id=1284143138948251770&scope=bot&permissions=2048>

## To deploy

We're deploying to [fly.io](https://fly.io/).

```bash
flyctl launch
flyctl secrets set OPENAI_API_KEY=sk-your-key-here
flyctl secrets set DISCORD_BOT_TOKEN=your-bot-token
flyctl deploy
```
