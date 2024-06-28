# suno-rest-client

[![GitHub][github_badge]][github_link]

A python rest client for [Suno AI](https://www.suno.ai/) leveraging [openapi-python-client](https://github.com/openapi-generators/openapi-python-client)

## Quickstart

### Sign in [Suno AI](https://www.suno.ai/)

### Grab the cookie of your Suno AI account

- Open your browser and open 'Developer Tools' by press 'F12'
- Navigate to 'Network' tab
- Identity the request that includes the keyword `client?_clerk_js_version`
- Navigate to 'Header' tab
- Copy the Cookie header value

### Clone this project

### Run quickstart.py locally

- Replace `<COOKIE>` inside `cookie = '<COOKIE>'` with the cookie value copied
- Run `Python quickstart.py` to generate an audio clip, the url of the audio clip will be printed to the console
- Open your browser and paste the url
- Enjoy the audio generated

[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/hahahahahaiyiwen/suno-rest-client
