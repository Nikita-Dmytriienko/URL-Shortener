from httpx import AsyncClient


async def test_generate_slug(ac: AsyncClient):
    result = await ac.post("/short_url",json={"long_url":"https://my-site.com"})
    print(f"{result=}")