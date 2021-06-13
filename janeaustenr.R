library(tidyverse)
library(tidytext)
library(janeaustenr)
library(ggplot2)
austen <- austen_books()

#how many books
bnum <- austen %>% count(book, sort = TRUE) 
bnum[, "book"]

#bnum <- austen %>% distinct(book)

#plot book by line using austen
ggplot(austen, aes(x = book)) +
  geom_bar()

#plot book by line using bnum
ggplot(bnum, aes(x = book, y = n)) +
  geom_col()

#analyze only emma book
emma <- austen %>% filter(book == "Emma") %>%
  mutate(linenumber = row_number(), is_chapter = str_detect(text, pattern = regex("^CHAPTER [\\divxc]+", 
                                                                  ignore_case =  TRUE)),
         chapter = cumsum(is_chapter))

view(emma)

emmatrues <- emma %>% filter(is_chapter == "TRUE")
view(emmatrues)

#ungroup() 

austenbooks <- austen %>% 
              group_by(book) %>% 
  mutate(linenumber = row_number(), is_chapter = str_detect(text, pattern = regex("^CHAPTER [\\divxc]+", 
                                                                                  ignore_case =  TRUE)),
         chapter = cumsum(is_chapter))

austens_tokens <- austen %>% 
                  unnest_tokens(word, text)


