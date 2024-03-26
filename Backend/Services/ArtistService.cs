using Backend.Models;
using Backend.Services.Interfaces;
using Microsoft.Extensions.Options;
using MongoDB.Driver;

namespace Backend.Services;

public class ArtistService : IArtistService
{
    private readonly IMongoCollection<Festival> _festivalCollection;
    
    private readonly IMongoCollection<Artist> _artistCollection;

    public ArtistService(IOptions<DatabaseContext> databaseContext)
    {
        var mongoClient = new MongoClient(databaseContext.Value.ConnectionString);
        var mongoDb = mongoClient.GetDatabase(databaseContext.Value.DatabaseName);
        _festivalCollection = mongoDb.GetCollection<Festival>("Festivals");
        _artistCollection = mongoDb.GetCollection<Artist>("Artists");
    }

    public async Task<List<Artist>> GetAllArtistsByFestivalId(string festivalId)
    {
        var artists = new List<Artist>();
        var festival = await _festivalCollection.Find(f => f.Id == festivalId).FirstOrDefaultAsync();
        if (festival != null && festival.Artists.Count != 0)
        {
            foreach (var artistRef in festival.Artists)
            {
                var artist = await _artistCollection.Find(a => a.Id == artistRef.ArtistId).FirstOrDefaultAsync();
                if (artist != null)
                {
                    artists.Add(artist);
                }
            }
        }

        return artists;
    }
}