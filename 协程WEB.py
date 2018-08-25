import asyncio
from aiohttp import web


fr = {}

async def index(request):

    name = request.match_info.get("name", "foo")

    print(name)
    #print(fr)
    await asyncio.sleep(3)
    
    if name in fr:
        
        return web.Response(body=fr[name])

    else:

        with open(name,'rb') as f:
            fr.update({name:f.read()})

        return web.Response(body=fr[name])


async def init(loop):

    app = web.Application(loop=loop) 

    app.router.add_route('GET','/{name}',index)

    srv = await loop.create_server(app.make_handler(),'0.0.0.0',2333)
    print('开启web服务')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()