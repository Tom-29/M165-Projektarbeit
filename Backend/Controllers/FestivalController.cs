using Backend.Models;
using Backend.Services.Interfaces;
using Microsoft.AspNetCore.Mvc;

namespace Backend.Controllers;

[ApiController]
[Route("festival")]
public class FestivalController : ControllerBase
{
    private readonly IFestivalService _festivalService;

    public FestivalController(IFestivalService festivalService)
    {
        _festivalService = festivalService;
    }

    [HttpGet]
    public async Task<ActionResult<List<Festival>>> GetAll()
    {
        return await _festivalService.GetAllFestivalsAsync();
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<FestivalWithArtists>> GetFestivalById(string id)
    {
        return await _festivalService.GetFestivalByIdAsync(id);
    }
}