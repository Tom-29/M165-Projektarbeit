using Backend.Models;
using Backend.Services.Interfaces;
using Microsoft.AspNetCore.Mvc;

namespace Backend.Controllers;

[ApiController]
[Route("artist")]
public class ArtistController : ControllerBase
{
    private readonly IArtistService _artistService;

    public ArtistController(IArtistService artistService)
    {
        _artistService = artistService;
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<List<Artist>>> GetAllByFestivalId(string id)
    {
        return await _artistService.GetAllArtistsByFestivalId(id);
    }
}