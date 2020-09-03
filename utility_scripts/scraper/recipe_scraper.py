# Adopted from: https://github.com/rtlee9/recipe-scraper/tree/4f3d38c1b99acff43410f9d72118f4a4fc87eefa/recipe_scrapers/

from abstract_scraper import AbstractScraper
from utils import get_minutes, normalize_string


class AllRecipes(AbstractScraper):

    @classmethod
    def host(self):
        return 'allrecipes.com'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return get_minutes(self.soup.find('span', {'class': 'ready-in-time'}))

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'class': "checkList__line"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
            if ingredient.get_text(strip=True) not in ('Add all ingredients to list', '')
        ]

    def instructions(self):
        instructions_html = self.soup.findAll('span', {'class': 'recipe-directions__list--item'})

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])

    def picture(self):
        recipe_photo = self.soup.find('img', {'class': 'rec-photo'})
        return recipe_photo.attrs['src']
