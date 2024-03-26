using MongoDB.Bson.Serialization.Attributes;

namespace Backend.Models;

public class Price
{
    [BsonElement("name")]
    public string Name { get; set; }

    [BsonElement("price")]
    public decimal Amount { get; set; }
}