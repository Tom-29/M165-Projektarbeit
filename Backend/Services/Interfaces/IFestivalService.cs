using Backend.Models;

namespace Backend.Services.Interfaces;

public interface IFestivalService
{
    public Task<List<Festival>> GetAllFestivalsAsync();

    public Task<FestivalWithArtists> GetFestivalByIdAsync(string id);

    public Task PostRatingAsync(string festivalId, Rating rating);
}