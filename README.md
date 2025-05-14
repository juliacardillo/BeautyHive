# About the Project:
This project was for my Scalable Databases course, in which I demonstrated the need for a centralized beauty review platform. I created a conceptual framework for a scalable relational database for this platform, and implemented a technical mockup of the database by integrating Python and MySQL.

# Problem Statement:
Searching for credible makeup and skincare product reviews is often frustrating. In one
Google search, you get many different aggregated reviews, across many different sites. These
aggregated reviews can be misleading, even tricking users into buying fake products from
third-party sellers. On most sites, reviews are typically at the bottom of the page, forcing users to scroll past sometimes unnecessary information and advertisements; a feature that should
encourage users to purchase items can ultimately be discouraging, needlessly laborious, and
repetitive. It's fun to shop online until shopping online becomes an endless cycle of scrolling to
the bottom of pages, reading through unhelpful reviews, vetting fake products, cross-referencing
different platforms… and rinse and repeat. Figure 1 below demonstrates this prevalent issue.

![Review](https://github.com/user-attachments/assets/34ebff41-0f24-4149-8233-52e1f8d3faad)
![Review2](https://github.com/user-attachments/assets/b2d0b764-cdfc-438b-b908-93cf1219345f)

At first glance, the 5-star rating below the Walmart link looks glaringly positive. But after investigating this link further the reviews are, in actuality, very bad and even reveal that this product is fake and distributed by a third-party seller. This is just one of the many examples present online—Amazon especially has this issue with branded items sold by a third party. 

# Solution: 
Now introducing _BeautyHive_, the hub for all beauty product reviews! For real beauty enthusiasts, by real beauty enthusiasts; no advertisements, sponsorships, or bot reviews. BeautyHive centralizes and aggregates reviews for makeup and skincare products, cutting down time spent on searching for trustworthy reviews. Think LetterBoxd or Yelp, but for makeup and skincare! 

# About Each File:
* **ConnectionScript_Public.py** contains the code for the project. Using MySQL Connector for Python, I integrated a MySQL database with Python by initializing the database in MySQL, and then utilizing this Python script to interact with and edit the database.
* **Beautyhive_Presentation.pdf** contains the final slide deck I presented in class.
* **BeautyHive_UML.pdf, BeautyHive_RelationalSchema.pdf, BeautyHive_ERDiagram.pdf** contain the UML diagram, relational schema, and entity-relationship diagram respectively.
