import arc

# For more info on plugins & extensions, see: https://arc.hypergonial.com/guides/plugins_extensions/

plugin = arc.GatewayPlugin("example")


@plugin.include
@arc.slash_command("ping", "Pong!")
async def ping_slash(ctx: arc.GatewayContext) -> None:
    await ctx.respond("Pong!")


@arc.loader
def load(client: arc.GatewayClient) -> None:
    client.add_plugin(plugin)


@arc.unloader
def unload(client: arc.GatewayClient) -> None:
    client.remove_plugin(plugin)
