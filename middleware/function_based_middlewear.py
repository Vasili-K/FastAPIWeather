import json
import time

from fastapi import Request
from starlette.responses import StreamingResponse, Response


async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    response_body = b""
    async for chunk in response.body_iterator:
        response_body += chunk
    decoded_response_body = response_body.decode()
    if decoded_response_body.startswith('{"country"'):
        dt = json.loads(decoded_response_body)
        if dt.get('country') == 'PL' and dt.get('wind') > 5:
            dt['greetings'] = 'Hello from windy Poland'
        decoded_response_body = json.dumps(dt)

    response.headers["X-Process-Time"] = str(process_time)
    response.headers["Content-Length"] = str(len(decoded_response_body))

    return Response(content=decoded_response_body, status_code=response.status_code,
                    headers=dict(response.headers), media_type=response.media_type)
