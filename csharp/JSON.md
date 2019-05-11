
# JSON in C#

In this example we will download JSON from API provided by [newsapi.org](newsapi.org) and the deserialize JSON using [Json.NET](https://www.newtonsoft.com/json) library.

```csharp
class Program
{
    static void Main()
    {
        WebClient wc = new WebClient();

        string apiKey = "ae5055d4deee4253bc5cbc39504b5cb3";
        string searchQuery = "tallinn";
        string url =
            $"https://newsapi.org/v2/everything?" +
            $"q={searchQuery}&" +
            $"from=2019-03-11&" +
            $"sortBy=publishedAt&" +
            $"apiKey={apiKey}";

        string content = wc.DownloadString(url);
        ApiResponse apiResponse = 
            JsonConvert.DeserializeObject<ApiResponse>(content);

        foreach (Article article in apiResponse.Articles)
        {
            Console.WriteLine(article.Title);
        }
      
    }
}

public class ApiResponse
{
    public Article[] Articles { get; set; }
}

public class Article
{
    public string Title { get; set; }
}
```
