namespace Backend.Models;

public class FestivalWithArtists
{
    public Festival Festival { get; set; }
    
    public ICollection<Artist> Artists { get; set; }= new List<Artist>();
}