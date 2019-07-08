from aiohttp import web

routes = web.RouteTableDef()


@routes.route("*", "/")
async def handler(req):
    return web.Response(text="Hello!")

app = web.Application()
app.add_routes(routes)

web.run_app(app)
