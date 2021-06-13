library(gapminder)

Ex1 <- gapminder %>%
  filter(country == "Morocco")  %>%
  summarize(Avglife = mean(lifeExp))

Ex2 <- gapminder %>%
  filter(year == 1952) %>%
  group_by(country) %>%
  summarize(biggest = max(lifeExp))
  
Ex3 <- gapminder %>%
  filter(year == 2007, lifeExp>70)

  
Ex4 <- gapminder %>%
  filter(year == 2007, continent == "Africa") %>%
  arrange(lifeExp)

Ex5 <- gapminder %>%
  filter(year == 2007) %>%
  group_by(continent) %>%
  summarize(medianlifeExp = median(lifeExp))
  

#Ex6
  Gdpcontinent <- gapminder %>%
  group_by(continent, year) %>%
  summarize(medG = median(gdpPercap))
  

  ggplot(Gdpcontinent, aes(x = year, y = medG, color = continent)) +
  geom_line()

#Ex7
country_2007 <- gapminder %>%
filter(year == 2007)

ggplot(country_2007, aes(y = lifeExp, x = gdpPercap, size = lifeExp, color = continent)) +
  geom_point()



