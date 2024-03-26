using Backend.Models;

namespace Backend.Services.Interfaces;

public interface IFestivalService
{
    public Task<List<Festival>> GetAllFestivalsAsync();

    public Task<Festival> GetFestivalByIdAsync(string id);
}