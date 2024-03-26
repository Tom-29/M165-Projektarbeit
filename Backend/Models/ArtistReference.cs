using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace Backend.Models;

public class ArtistReference
{
    [BsonRepresentation(BsonType.ObjectId)]
    [BsonElement("artistId")]
    public string ArtistId { get; set; }

    [BsonElement("day")]
    public DateTime Day { get; set; }
}