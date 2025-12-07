from database.crud import add_slug_to_database
from shortener import generate_random_slug

#It's more convenient to do everything through a class
#That's the advantage of the OOP approach
async def generate_short_url(
    long_url: str,
    
)->str:
#1 Generating this slug
#2 Adding to the database
#3 We give the client a link
    slug = generate_random_slug()
    await add_slug_to_database(
        slug,
        long_url
    )
    return slug

await def get_url_by_slug(slug: str)->str:
        
    
