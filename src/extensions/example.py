import arc

# For more info on plugins & extensions, see: https://arc.hypergonial.com/guides/plugins_extensions/

plugin = arc.RESTPlugin("example")


@plugin.include
@arc.slash_command("ping", "Pong!")
async def ping_slash(ctx: arc.RESTContext) -> None:
    await ctx.respond("Pong!")


@arc.loader
def load(client: arc.RESTClient) -> None:
    client.add_plugin(plugin)


@arc.unloader
def unload(client: arc.RESTClient) -> None:
    client.remove_plugin(plugin)
