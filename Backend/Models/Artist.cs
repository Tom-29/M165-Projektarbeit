namespace Backend.Models;

using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

public class Artist
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

    [BsonElement("birthdate")]
    public DateTime? Birthdate { get; set; }
    
    public DateTime? Date { get; set; }
}