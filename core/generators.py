import csv
import aiofiles

async def async_csv_generator(file_path, chunk_size=1000):
    async with aiofiles.open(file_path, mode='r') as f:
        reader = csv.DictReader(await f.readlines())
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) >= chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk