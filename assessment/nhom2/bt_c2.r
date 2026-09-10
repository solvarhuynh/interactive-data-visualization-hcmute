library(ggplot2)
library(plotly)

p <- ggplot(economics, aes(x = date, y = unemploy, color = uempmed, size = uempmed)) +
  geom_point() +           
  scale_color_gradient(              
    low = "yellow",
    high = "red"
  ) +
  theme_light() +
  labs(title = "Chart of unemployed people over the years",
       x = "Year",
       y = "Number of unemployed (in thousands)",
       color = "Median unemployment\nduration (in weeks)",
       size = "Median unemployment\nduration (in weeks)"
  )

ggplotly(p)
