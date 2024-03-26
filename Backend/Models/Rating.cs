using MongoDB.Bson.Serialization.Attributes;

namespace Backend.Models;

public class Rating
{
    [BsonElement("stars")]
    public double Stars { get; set; }

    [BsonElement("username")]
    public string Username { get; set; }

    [BsonElement("comment")]
    public string? Comment { get; set; }
}
