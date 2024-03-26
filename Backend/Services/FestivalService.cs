using Backend.Models;
using Backend.Services.Interfaces;
using Microsoft.Extensions.Options;
using MongoDB.Driver;

namespace Backend.Services;

public class FestivalService : IFestivalService
{
    private readonly IMongoCollection<Festival> _festivalCollection;

    public FestivalService(IOptions<DatabaseContext> databaseContext)
    {
        var mongoClient = new MongoClient(databaseContext.Value.ConnectionString);
        var mongoDb = mongoClient.GetDatabase(databaseContext.Value.DatabaseName);
        _festivalCollection = mongoDb.GetCollection<Festival>("Festivals");
    }

    public async Task<List<Festival>> GetAllFestivalsAsync()
    {
        return await _festivalCollection.Find(_ => true).ToListAsync();
    }

    public async Task<Festival> GetFestivalByIdAsync(string id)
    {
        var festival = await _festivalCollection.Find(f => f.Id == id).FirstOrDefaultAsync();
        return festival;
    }
}