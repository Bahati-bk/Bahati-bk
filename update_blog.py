import requests

USERNAME = "godfident-data"
API_URL = "https://api.hashnode.com/"

# GraphQL query
query = """
{
  user(username: "%s") {
    publication {
      posts(page: 0) {
        title
        brief
        slug
      }
    }
  }
}
""" % USERNAME

response = requests.post(API_URL, json={"query": query})
data = response.json()

# Extract latest posts
posts = data["data"]["user"]["publication"]["posts"][:3]  # get first 3 posts

# Generate Markdown for README
markdown = "## 📝 Latest Blog Posts ✨\n\n"
for post in posts:
    title = post["title"]
    slug = post["slug"]
    url = f"https://{USERNAME}.hashnode.dev/{slug}"
    markdown += f"- [{title}]({url})\n"

markdown += "\n🌸 More posts → [My Blog](https://godfident-data.hashnode.dev)\n"

print(markdown)
