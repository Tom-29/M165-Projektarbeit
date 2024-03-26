using MongoDB.Bson.Serialization.Attributes;

namespace Backend.Models;

public class Date
{
    [BsonElement("start")]
    public DateTime StartDate { get; set; }
    
    [BsonElement("end")]
    public DateTime EndDate { get; set; }
}