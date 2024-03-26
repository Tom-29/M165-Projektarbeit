using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace Backend.Models;

public class Festival
{
    [BsonId]
    [BsonRepresentation(BsonType.ObjectId)]
    public string Id { get; set; }

    [BsonElement("name")]
    public string Name { get; set; }

    [BsonElement("country")]
    public string Country { get; set; }

    [BsonElement("genre")]
    public string Genre { get; set; }

    [BsonElement("date")]
    public Date Date { get; set; }

    [BsonElement("prices")]
    public List<Price> Prices { get; set; }

    [BsonElement("ratings")]
    public List<Rating> Ratings { get; set; }

    [BsonElement("artists")]
    public List<ArtistReference> Artists { get; set; }
}