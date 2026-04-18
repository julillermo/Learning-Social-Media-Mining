# Notes:

- This is the most technincally relevant chapter in my opinion
- Actual live sites are messy to retrieve data from
- **Ethical Considerations for Data Scraping**:
  - "Scraping information from websites or republishing scraped data without permission may be against a company's terms of service, and you can get banned from the platform or, worse, result in legal action"
  - [“On the Ethics of Web Scraping”](https://robertorocha.info/on-the-ethics-of-web-scraping/)
    - _Can I take this data?_
    - _Can I republish this data?_
    - _Am I overloading the website's servers?_
    - _What can I use this data for?_
- `robots.txt`
  - Usually exists at the root of the website (ex. `http://facebook.com/robots.txt`)
  - Not something that can be enforced. Can be ignored by bad actors. Website owners may take measure when this trust is broken.
  - Usually found format:
    - `User-agent: [name-of-user-agent] or *` (who the allow/disallow rule applies to)
    - `Disallow/Allow: [directory from root]` (directory of the folder scrapers should skip over)
      - Can be more than 1 entry below a specified `User-agent`
- Terms of Service
  - A way to determine what the website owner allows access to besides those specified in `robots.txt`
- Technical Considerations for Data Scraping
  - Requests require compute from the server (costs the host money).
  - Swarming a server with requests can overwelm the system
  - We should take measures to slow down our scraper to not overwhelm the site we're extracting data from.
- Reasons for Scraping Data
  - You should do ethical research before you attempt to write code
  - Contexts on what's legal and ethical can vary dependeong on location, context, purpose, etc.
- Scraping from a Live Website
  - Try to plan & map out how you'll dig into the specific part of the rendered web page using the browser devzeloper tools.
  - Highly utilize the feature where hovering points to the equivalent UI / DOM location.
  - HTML tag `class`, `id`, and `name` attributes are very helpful to directly point to a specific part of the DOM.
- **Practice Polite Scraping**
  - Specify _headers_ as part of your request, so the site owner can contact you and communicte polite adjustment to your scraper.
    - The content within headers isn't struct, but the following are the common tags to use (followed by example values):
      - `user-agent:` `"Mozilla/5.0 (X11; Linux x86_64; rv:149.0) Gecko/20100101 Firefox/149.0",`
        - Information about the browser we're using. "While this information is not necessary for bots it may allow your scraper to open websites that normally can't be opened outside of a web browser."
        - "The user-agent header can communicate information about the browser capabilities our bot might use to opena page within a browser.
      - `from:` `https://github.com/julillermo`
  - Specify a delate between each request.
    - You `time` library include in python.
    - Use `time.sleep(2)` to delay two seconds at the end of every request.

# Implementation Notes:

- To further avoid overloading the website you're trying to scrape, it'd be better to download the raw HTML, save it as a file, and read from that instead constantly making requests to the website.
- Skipped the part were the booke was discussing reusability
