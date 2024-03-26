using Backend.Models;

namespace Backend.Services.Interfaces;

public interface IArtistService
{
    public Task<List<Artist>> GetAllArtistsByFestivalId(string festivalId);
}