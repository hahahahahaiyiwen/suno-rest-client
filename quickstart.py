import asyncio
import importlib
import time

suno = importlib.import_module("suno-rest-client")
models = importlib.import_module("suno-api-client.suno_api_client.models")

async def main():
    # Set cookie
    cookie = '<COOKIE>'
    
    # Initialize Suno rest client
    client = suno.SunoRestClient(cookie)

    # Generate clip
    context = models.AudioGenerationRequest(prompt = "", tags = "Pop rap about NYC.", title = "Metro Saga", make_instrumental = False)
    result = await client.generate_audio(body = context)
    clip = result.clips[0]

    # Poll status
    while clip.status != "complete" and clip.status != "streaming":
        print(f"Id: {clip.id}, Status: {clip.status}, wait 5s...")
        time.sleep(5)
        clip = await client.get_clip(clip_id = clip.id)
    
    # Get clip url
    print(clip.audio_url)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())