import importlib
import jwt
import time

client = importlib.import_module("suno-api-client.suno_api_client.client")
api = importlib.import_module("suno-api-client.suno_api_client.api")
models = importlib.import_module("suno-api-client.suno_api_client.models")

class SunoRestClient(client.Client):
    _headers = {
        "user-agent": "SunoRestClient/1.0.0"
    }
    _clerk_version: str = "v1"
    _clerk_js_version: str = "4.73.2"
    _model_version = "chirp-v3-5"
    _studio_api_version = "v2"

    async def get_billing(self) -> models.BillingInfo:
        return await api.get_billing(client = await self._get_suno_studio_client())

    async def get_generated_lyrics(self, prompt: str) -> models.LyricsResult:
        lyrics_id = await self.generate_lyrics("beautiful song about new york subway")
        while getattr(lyrics, "status", None) != "complete":
            time.sleep(1)
            lyrics = await self.get_lyrics(lyrics_id.id)

    async def generate_lyrics(self, prompt: str) -> models.LyricsInfo:
        body = models.LyricsGenerationRequest(prompt)
        return await api.generate_lyrics(client = await self._get_suno_studio_client(), body = body)

    async def get_lyrics(self, lyrics_id: str) -> models.LyricsResult:
        return await api.get_lyrics(lyric_id = lyrics_id, client = await self._get_suno_studio_client())

    async def generate_audio(self, body: models.AudioGenerationRequest) -> models.AudioResult:
        body.mv = self._model_version
        return await api.generate_audio(client = await self._get_suno_studio_client(), version = self._studio_api_version, body = body)

    async def get_clip(self, clip_id: str) -> models.ClipInfo:
        return await api.get_clip(client = await self._get_suno_studio_client(), clip_id = clip_id)

    async def convert_wav(self, clip_id: str):
        await api.convert_wav(client = await self._get_suno_studio_client(), clip_id = clip_id)

    async def get_clip_wav(self, clip_id: str) -> models.WavInfo:
        return await api.get_clip_wav(client = await self._get_suno_studio_client(), clip_id = clip_id)
    
    async def concat_clip(self, clip_id: str) -> models.ClipInfo:
        return await api.generate_audio(client = await self._get_suno_studio_client(), version = self._studio_api_version, body = models.AudioConcatRequest(clip_id = clip_id))


    def __init__(self, cookie: str) -> None:
        self._sid: str = None
        self._auth_token: str = None
        self._clerk_client = client.Client(base_url="https://clerk.suno.com").with_headers({"cookie": cookie})

    async def _get_auth_token(self):
        if self._sid == None:
            await self._get_sid()
        token = await api.get_session_token(
            version = self._clerk_version, 
            session_id = self._sid,
            client = self._clerk_client,
            field_clerk_js_version = self._clerk_js_version)
        return token.jwt
        
    async def _get_sid(self):
        client_result = await api.get_client(
            version = self._clerk_version, 
            client = self._clerk_client,
            field_clerk_js_version = self._clerk_js_version)
        self._sid = client_result.response.last_active_session_id

    async def _get_suno_studio_client(self):
        if self._need_refresh(self._auth_token):
            self._auth_token = await self._get_auth_token()
        return client.AuthenticatedClient(base_url="https://studio-api.suno.ai", token= self._auth_token, follow_redirects = True).with_headers(self._headers)

    def _need_refresh(self, token: str) -> bool:
        if token == None:
            return True
        expired: int = jwt.decode(token, options={"verify_signature": False})['exp']
        return expired < time.time()
        