using Backend.Models;
using Backend.Services.Interfaces;
using Microsoft.Extensions.Options;
using MongoDB.Driver;

namespace Backend.Services;

public class FestivalService : IFestivalService
{
    private readonly IMongoCollection<Festival> _festivalCollection;

    private readonly IMongoCollection<Artist> _artistCollection;

    public FestivalService(IOptions<DatabaseContext> databaseContext)
    {
        var mongoClient = new MongoClient(databaseContext.Value.ConnectionString);
        var mongoDb = mongoClient.GetDatabase(databaseContext.Value.DatabaseName);
        _festivalCollection = mongoDb.GetCollection<Festival>("Festivals");
        _artistCollection = mongoDb.GetCollection<Artist>("Artists");
    }

    public async Task<List<Festival>> GetAllFestivalsAsync()
    {
        return await _festivalCollection.Find(_ => true).ToListAsync();
    }

    public async Task<FestivalWithArtists> GetFestivalByIdAsync(string id)
    {
        var festivalWithArtists = new FestivalWithArtists();
        festivalWithArtists.Festival = await _festivalCollection.Find(f => f.Id == id).FirstOrDefaultAsync();
        if (festivalWithArtists.Festival != null && festivalWithArtists.Festival.Artists.Count != 0)
        {
            foreach (var artistRef in festivalWithArtists.Festival.Artists)
            {
                var artist = await _artistCollection.Find(a => a.Id == artistRef.ArtistId).FirstOrDefaultAsync();
                if (artist != null)
                {
                    artist.Date = artistRef.Day;
                    festivalWithArtists.Artists.Add(artist);
                }
            }
        }

        festivalWithArtists.Festival.Artists = null;
        return festivalWithArtists;
    }

    public async Task PostRatingAsync(string festivalId, Rating rating)
    {
        var filter = Builders<Festival>.Filter.Eq("Id", festivalId);
        var update = Builders<Festival>.Update.AddToSet<Rating>("ratings", rating);
        await _festivalCollection.UpdateOneAsync(filter, update);
    }
}