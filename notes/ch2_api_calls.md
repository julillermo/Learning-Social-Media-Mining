# Notes:
- "An API is like a middleman between the social media platform and the developers who wish to access information from it."
- "... an API is an interface that allows programmers to access other developer's code."
- As an example, use the API: `https://www.googleapis.com/youtube/v3/search?channelId=UCJFp8uSYCjXOMnkUyb3CQ3Q&part=snippet`
  - This doesn't work unless you specif credentials with google
  - Parts of the API
    - **base**: the endpoint you're hitting (ex. `https://www.googleapis.com/youtube/`)
    - **parameters**: the specific details you pass along (ex. `channelId=...`) separated by `&`
  - Note that APIs tend to change over time as a site evolves. Providers sometimes specify the version as part of the endpoint to hit. (Refer to available documentation for this scenario)
  - This API is set up such that only limited information is returned unless otherwise specified.

# Implementation notes:
- Skipped creation of YouTube API key, I assume I could generally follow along with what's supposed to happen.
