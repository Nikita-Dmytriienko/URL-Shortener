from database.crud import add_slug_to_database, get_long_url_by_slug_from_db
from exceptions import NoLongUrlFoundError, SlugAlreadyExistError
from shortener import generate_random_slug

#It's more convenient to do everything through a class
#That's the advantage of the OOP approach
async def generate_short_url(
    long_url: str,
    
) -> str:
#1 Generating this slug
#2 Adding to the database
#3 We give the client a link
    async def _generate_slug_and_add_to_db() -> str:
        slug = generate_random_slug()
        await add_slug_to_database(
            slug, long_url
        )
        return slug
    for attempt  in range(5):
        try:
            slug = await _generate_slug_and_add_to_db()
            return slug
        except SlugAlreadyExistError as ex:
            if attempt ==4:
                raise SlugAlreadyExistError from ex
    return slug
        
        


async def get_url_by_slug(slug: str) -> str:
    long_url = await get_long_url_by_slug_from_db(slug)
    if not long_url:
        raise NoLongUrlFoundError()
    return  long_url
