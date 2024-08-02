import scrapy
from scrapy.http import Response


class WorkUaJobsSpider(scrapy.Spider):
    name = "vacancies"
    allowed_domains = ["work.ua"]
    start_urls = ["https://www.work.ua/en/jobs-python/"]

    def parse(self, response: Response, **kwargs):
        vacancies = response.xpath("//div[contains(@class, 'job-link')]")

        for vacancy in vacancies:
            link = vacancy.xpath(".//h2/a/@href").get()
            if link:
                link = response.urljoin(link)
                yield response.follow(link, self.parse_job_details, meta={"link": link})

        page = response.xpath("//span[@class='text-default']/@title").get()
        if page:
            self.sum_pages = int(page.split("of ")[-1].strip())
            self.logger.info(f"Total pages: {self.sum_pages}")

            for page_number in range(2, self.sum_pages + 1):
                next_page = response.urljoin(f"?page={page_number}")
                yield response.follow(next_page, self.parse)

    def parse_job_details(self, response: Response):
        yield {
            "title": self.parse_title(response),
            "skills": self.parse_skills(response),
            "salary": self.parse_salary(response),
            "company": self.parse_company(response),
            "description": self.parse_description(response),
            "link": response.meta["link"],
        }

    def parse_title(self, response: Response) -> str:
        return response.xpath("//h1/text()").get(default="").strip()

    def parse_skills(self, response: Response) -> str:
        return response.xpath("//span[@class='ellipsis']/text()").getall()

    def parse_salary(self, response: Response) -> str:
        return (
            response.xpath(
                "//span[@title='Salary']/following-sibling::span[@class='strong-500']/text()"
            )
            .get(default="")
            .replace("\u2009", "")
            .replace("\u202f", "")
            .strip()
        )

    def parse_company(self, response: Response) -> str:
        return (
            response.xpath(
                "//span[@title='Company Information']/following-sibling::a/span[@class='strong-500']/text()"
            )
            .get(default="")
            .strip()
        )

    def parse_description(self, response: Response) -> str:
        job_description = response.xpath(
            "//div[@id='job-description']//text()"
        ).getall()
        return " ".join(job_description).replace("\r\n", "").strip()
