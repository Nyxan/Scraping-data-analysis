# Scraping-data-analysis


This project scrapes job vacancies from various websites and analyzes the data to provide insights into technology trends and salary expectations. The analysis is performed using Python and the results are visualized using plots.

## Project Structure

- **scraper**: Contains the Scrapy spider to scrape job vacancies from `work.ua`.
- **data_analyzer.ipynb**: Jupyter Notebook for analyzing the scraped data.
- **vacancies.csv**: CSV file containing the scraped job vacancies data.

### Data example
[vacancies.csv](example/vacancies.csv)

### Graphic example
![img.png](example/img.png)

### Installation/getting started

1. Clone the repository:

```shell
git clone https://github.com/Nyxan/Scraping-data-analysis
```

2. Create and activate virtual environment:

```shell
# for Windows
python -m venv venv
venv\Scripts\activate
# for macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```shell
pip install -r requirements.txt
```

4. Run the scraper script:

```shell
scrapy crawl vacancies -o vacancies.csv
```

5. Open and run the `data_analyzer.ipynb` Jupyter notebook file to perform analytics and generate visualizations.

