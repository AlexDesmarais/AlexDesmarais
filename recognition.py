# utils/recognize.py
from shazamio import Shazam
import asyncio

async def identify_chunk(path):
    shazam = Shazam()
    try:
        out = await shazam.recognize_song(path)
        track = out.get('track', {})
        return f"{track.get('title', 'Unknown')} - {track.get('subtitle', '')}" if track else None
    except:
        return None

def recognize_song_chunks(chunk_paths):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = [identify_chunk(chunk) for chunk in chunk_paths]
    results = loop.run_until_complete(asyncio.gather(*tasks))
    # Filter duplicates & Nones
    seen = set()
    return [song for song in results if song and not (song in seen or seen.add(song))]
