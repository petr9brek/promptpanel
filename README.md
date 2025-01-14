<img src="https://promptpanel.com/images/logo.svg" alt="logo" style="width:64px;">

**Prompt Panel**\
The Universal AI Interface\
<a href="https://promptpanel.com/docs">Documentation</a> | <a href="https://hub.docker.com/r/promptpanel/promptpanel">DockerHub</a> | <a href="https://github.com/promptpanel/promptpanel">Prompt Panel App</a> | <a href="https://github.com/promptpanel/plugins">Agent Plugins</a>


## Installation

### Via Docker Compose:
```bash
curl -sSL https://promptpanel.com/manifest/docker-compose.yml | docker compose -f - up
```

which runs the following `docker-compose.yml`:

```yaml
version: "3.9"
services:
  promptpanel:
    image: promptpanel/promptpanel:latest
    container_name: promptpanel
    restart: always
    volumes:
      - ./database:/app/database
      - ./media:/app/media
    ports:
      - 4000:4000
    environment:
      PROMPT_OLLAMA_HOST: http://ollama:11434
  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    restart: always
```

Read more on <a href="https://promptpanel.com/installation/docker-compose-offline/" target="_new">running Prompt Panel</a>.

---

Your models, conversations, and logic are locked in walled-gardens.

Let's free your AI interface.

- <a target="_new" href="https://promptpanel.com/overview/packaged-plugins-models/">Run any large language model</a>, across any inference provider, any way you want. We're un-opinionated.
- <a target="_new" href="https://promptpanel.com/plugin-agent-authoring/building-plugin-agents/">Create custom plugin agents</a> and tailor the system to your unique needs.
- <a target="_new" href="https://promptpanel.com/overview/packaged-plugins-models/#llm-document">Bring your own data</a> - host and run models locally using any engine.
- <a target="_new" href="https://promptpanel.com/server-setup/accessing-your-data/">Move and use your data</a> - we're pro data accessibility and portability.

---

## Questions?
Feel free to get in contact with us at:\
info@promptpanel.com

---

![screenshot](https://github.com/promptpanel/promptpanel/assets/161855417/6e7a303d-0fbc-4896-870d-19700b579e71)
