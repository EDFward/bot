# Bot

Yes, we want to build a bot.

That's it.

## Architecture

- Microservice
    - Main bot service should be stateless
    - Different clients should have separate services (Telegram, Slack, etc)
- Data source fetched separately such as Celery jobs